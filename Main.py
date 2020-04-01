
import os 
import re
import requests 
from bs4 import BeautifulSoup

from WebRequest import web_request
from PostLinks import post_links 
# from WriteExcelFile import write_excel_file
from Analyze_Attack import analyze_attack

class main_class:
    url = ''
    web = None
    base = ''
    links = [] 
    website = []
    source = None

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
        web = web_request(url,'GET')
        source = web.get_source()
        return source

    # Extract links from the source     
    def get_links(self):
        links = []
        soup = BeautifulSoup(self.source,features="lxml")
        tags = soup.find_all('a', href=True)
        for tag in tags:    
            if self.valid_link(tag['href'],links):    links.append(tag['href'])
        # print(links)
        return links
    
    # Validata link
    def valid_link(self,link,links):
        if str(link).__contains__(self.base):  
            if link not in links:  return True
        else:   return False
    
    def find_base_url(self,link):
        exp = re.compile(r'(?!\w)\.?[\.\w]+')
        # print(link)
        part = exp.findall(link)
        # print(part)
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
#  End of Class: main_class
#-------------------------------------------------------------------------------------------------------------
       

# _____________________________________________________________________________________________________________

    """ We Have To Deal with Post Forms Yet:     Below Code  """
# _____________________________________________________________________________________________________________

    # Collecting Response Data of  <Post Forms>
    # postlink = []
    # postlink.append(link)
    # link, posturl, r, presence = post.collect_data(postlink)
    # Writing Response of Post Forms
    # Text.write_postforms( posturl, r, presence)

    # Excel = write_excel_file(url,'NewDataSheet.xlsx', payload)
    # Excel.write_contexts(attrs, htmls, scripts, urls, same_attrs , same_htmls, same_scripts, same_urls)


if __name__ == "__main__":
    print('\n=> The Automated Tool Assumes that there is a potential XSS Present in the Website\n')

    Post = post_links()
    A = analyze_attack()
    links = []
# -----------------------  Links for Testing -------------------------------
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
    # links += ['https://www.acehardware.com']
    # links += ['https://www.vanhalenstore.com/']
    # links += ['http://www.lllreptile.com/']

    # links += ['https://www.ces.ncsu.edu/']
    # links += ['http://drudgereportarchives.com/']
    links += ['https://www.zentechnologies.com/']
    # links += ['https://ifu-institut.at/']
    # links += ['https://www.sweetwater.com/']
    # links += ['https://www.drdelphinium.com/']
    # links += ['https://www.harbourbayflorist.com/']
    # links += ['https://www.nearlynatural.com']

    # links = Post.read_excel()
    M = main_class(links[0])

    # Collecting all the links of a web page (these are the references of webpages)
    index = 0
    for bfs_levels in range(0):
        index, links = M.bfs_crawling(index,links)      

    # collecting links from an Excel File ('data.xlsx') 
    A.collect_data(links)  

    # Check Post links here
    # Post.collect_data(links)
    
print('\n----------------------   PROGRAM  ENDED   -----------------------------\n')

"""   <--   Suggested WORK / Algorithms -->

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