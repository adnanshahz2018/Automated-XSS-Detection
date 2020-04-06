
import os 
import re
import requests 
from bs4 import BeautifulSoup

from WebRequest import web_request
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

    def set_base_url(self,url):
        self.base = url 

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
        print('\nBase Url = [', base , ']')
        return base # 'madeinoregon.com'

    

    def bfs_crawling(self,index, web_links):
        count = index
        self.links = web_links.copy()
        print('\n\t\t WE ARE FETCHING LINKS \n\n')
        for i in range(index, len(web_links) ):
            count+=1
            self.url = web_links[i]
            print(' LINK  [' , count ,']  =>  ' ,self.url)

            self.web = web_request(self.url,'GET')
            self.base = self.find_base_url(self.url)
            self.source = self.get_source(self.url)
            bfs_links = self.get_links()
            
            # Removing Duplicates
            for new_link in bfs_links: 
                if new_link not in self.links:
                    self.links.append(new_link)

        return len(self.links) , self.links

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
    print('\n=> This Automated Tool assists in finding XSS Vulnerablilities.\n=> It assumes that there is a potential XSS Present in the Website\n')

    Analyzer = analyze_attack()
    links = []
# -----------------------  Links for Testing -------------------------------
    # links += ['https://www.moma.org/']      # 376 Unique Links in this website with 2 level bfs...  
    # links += ['https://www.britannica.com/explore/yearinreview/']
    # links += ['https://www.roomandboard.com/']    # Check for the problem: where you find the get parama: 'query' but further the *Requests Fails*
    # links += ['https://www.harryanddavid.com/']
    # links += ['https://www.1000bulbs.com/']
    # links += ['https://www.africanews.com/']
    # links += ['https://www.ars.usda.gov/']      #200
    # links += ['https://www.iita.org/']
    # links += ['https://www.agricultureinformation.com/forums/']
    # links += ['https://www.acehardware.com'] # NOt GET URLs has 1 Get form 
    # links += ['https://www.vanhalenstore.com/']
    # links += ['http://www.lllreptile.com/']
    # links += ['http://www.drudgereportarchives.com/']
    # links += ['https://www.ifu-institut.at/']
    # links += ['https://www.sweetwater.com/']
    # links += ['https://www.drdelphinium.com/']
    # links += ['https://www.harbourbayflorist.com/']
    # links += ['https://www.nearlynatural.com']

    # links += ['https://www.cat.com/en_US'] #DOne
    # links += ['https://www.kirklands.com/']   # Done  
    # links += ['https://www.discountpartysupplies.com/'] # Done 
    # links += ['https://www.burpee.com/']      # Done
    # links += ['https://www.bangalla.com/'] # done
    # links += ['https://www.zentechnologies.com/']     # done
    # links += ['https://www.madeinoregon.com/']        # Done Well 
    # links += ['https://www.gsmarena.com/']            # Done well// Request Failure
    # links += ['https://www.theverge.com/']            # Done well // Request Failue
    # links += ['https://www.crazycrow.com/site/']                #Done Well
    # links += ['https://www.keh.com/']     #done
    # links += ['https://www.ces.ncsu.edu/'] # Done 
    # links += ['https://www.abcstores.com/']             #Done Well
    # links += ['https://www.rods.com/']                      # Done well
    # links += ['https://www.tenthousandvillages.com/']       # Done well
    links += ['https://www.ruralking.com/']               # Done well 



    # links += ['']
    # links += ['']
    # links += ['']
    # links += ['']
    # links += ['']
    # links += ['']
    # links += ['']
    # links += ['']
    # links += ['']
    # links += ['']



    M = main_class(links[0])

    # Collecting all the links of a web page (these are the references of webpages)
    index = 0 
    for bfs in range(3):
        index, links = M.bfs_crawling(index,links)
        if (index > 21): break      

    # print('Index = ', index)
    new_links = []
    if len(links) > 19 :
        for i in range(20): new_links.append(links[i]) 
    else:
        new_links = links
    # print(len(new_links), '\n')
    for link in new_links: print(link)

    """ Now the Tool Anaylyzes the website, Attacks it (if possible) and Generates Reports (Text Files) """
    Analyzer.collect_data(new_links)
    
    print('\n----------------------   PROGRAM  ENDED   -----------------------------\n')

