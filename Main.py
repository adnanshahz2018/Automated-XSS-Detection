
import os 
import re
import requests
import pandas as pd 
from bs4 import BeautifulSoup

from WebRequest import web_request
# from WriteExcelFile import write_excel_file
from Analyze_Attack import analyze_attack

class main_class:
    url = ''
    web = None
    # folder = 'drive/My Drive/SQL_Vulnerable'
    # folder = '600WebsiteData'
    folder = 'TuningData'
    dirName = ''
    base = ''
    links = [] 
    website = []
    source = None

    def __init__(self,url):
        base_url = self.find_base_url(url)
        print(' BASE URL [', base_url, ']\n')
        self.base = self.folder + '/' + base_url
        self.create_directory(self.folder)
        self.dirName = self.folder + '/' + self.dirName

        self.create_directory( self.base )


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
        tags = tags + soup.find_all('link', href=True)
        for tag in tags:    
            if self.valid_link(tag['href'],links):    links.append(tag['href'])
        # print(links)
        return links

    def set_base_url(self,url):
        self.base = url 

    # Validata link
    def valid_link(self,link,links):
        link = str(link)
        # here we are checking if the first or Very inital part of url/link contains our <base-url>. 
        # bcoz sometimes links like : www.linkedIn.com/base-url can also have <base-url> but we don't need it.
        if link[:len(self.base*2)].__contains__(self.base) and link[:4] == 'http':  
            if link not in links:  return True
        else:   return False
    
    def find_base_url(self,link):
        link = link.replace('http://www','')
        link = link.replace('https://www','')
        link = link.replace('http://','')
        link = link.replace('https://','')

        if link.__contains__('/'): 
            parts = link.split('/')
            link = parts[0]
        
        self.dirName =  link
        return link
    
    def create_directory(self, directory):
        # Create target Directory if it does not Exist
        if not os.path.exists(directory):
            os.mkdir(directory)
            print("Directory " , directory ,  " Created ")
        # else:    print("Directory " , directory ,  " already exists")

    def bfs_crawling(self,index, web_links):
        count = index
        self.links = web_links.copy()
        # print('\n\t\t WE ARE FETCHING LINKS \n\n')
        for i in range(index, len(web_links) ):
            count+=1
            self.url = web_links[i]

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


def main_operation(links):
    bfs_levels = 0
    M = main_class(links[0])
    base = M.dirName
    index = 0 
    for bfs in range(bfs_levels):
        index, links = M.bfs_crawling(index,links)
        if (index > 21): break      

    # print('Index = ', index)
    new_links = []
    if len(links) > 19 :    
        for i in range(20): new_links.append(links[i]) 
    else:   new_links = links

    for link in new_links: print(link)

    """ Now the Tool Anaylyzes the website, Attacks it (if possible) and Generates Reports (Text Files) """
    Analyzer = analyze_attack(base, M.folder)
    Analyzer.collect_data(new_links)



# The website links are stored in Excel file and we read the file to get the links 
def read_excel(excel_filename):
    df = pd.read_excel(excel_filename)
    links = df['websites']
    return links

if __name__ == "__main__":
    print('\n=> This Automated Tool assists in finding XSS Vulnerablilities.\n=> It assumes that there is a potential XSS Present in the Website\n')

    links = []
# -----------------------  Links for Testing -------------------------------
    # links += ['https://www.moma.org/']      # 376 Unique Links in this website with 2 level bfs...  
    # links += ['https://www.britannica.com/']
    # links += ['https://www.roomandboard.com/']    # Check for the problem: where you find the get parama: 'query' but further the *Requests Fails*
    # links += ['https://www.africanews.com/']
    # links += ['https://www.iita.org/']
    # links += ['https://www.agricultureinformation.com/forums/']
    # links += ['https://www.acehardware.com'] #  Has 1 Get form but No GET Params are present  
    # links += ['http://drudgereportarchives.com/']
    # links += ['https://ifu-institut.at/']
    # links += ['https://www.sweetwater.com/']
    # links += ['https://www.drdelphinium.com/']
    # links += ['https://www.harbourbayflorist.com/']
    # links += ['https://www.nearlynatural.com']

    # links += ['https://www.deere.com/en/']   # Done well and stored
    # links += ['https://www.1000bulbs.com/'] #Done & stored
    # links += ['https://www.cat.com/en_US'] #DOne stored
    # links += ['https://www.kirklands.com/']   # Done  stored
    # links += ['https://www.discountpartysupplies.com/'] # Done stored 
    # links += ['https://www.burpee.com/']      # Done stored
    # links += ['https://www.bangalla.com/'] # done stored
    # links += ['https://www.vanhalenstore.com/']   #Done Well Stored
    # links += ['https://madeinoregon.com/']        # Done Well 
    # links += ['https://www.gsmarena.com/']            # Done well// has only 2-3 pages while finding links through 'href'
    # links += ['https://www.theverge.com/']            # This site Can't be reached
    # links += ['https://www.crazycrow.com/site/']       #Done Well stored
    # links += ['https://www.keh.com/']     #done stored
    # links += ['https://www.ces.ncsu.edu/'] # Done  stored
    # links += ['https://www.abcstores.com/']             #Done Well stored
    # links += ['https://www.rods.com/']                      # Done well stored
    # links += ['https://www.tenthousandvillages.com/']       # Access denied
    # links += ['https://www.ruralking.com/']               # Done well stored
    # links += ['https://www.ars.usda.gov/']      #Done well stored
    # links += ['https://www.harryanddavid.com/'] # Done Nothing in it
    # links += ['https://www.asapawards.com/']    # Nothing Found
    # links += ['http://www.lllreptile.com/']  #Done well & Stored
    # links += ['https://www.geappliances.com/'] # No Forms
    # links += ['https://www.wayfair.com']    # DONE WELL & STORED

    # links += ['https://www.lowes.com/']   # Done well , stored
    # links += ['https://www.husqvarna.com/']   #Nothing found
    # links += ['http://www.beistle.com']   #nothing found
    # links += ['https://www.nobleworkscards.com']  #nothing found
    # links += ['https://elegantbaby.com']
    # links += ['http://cigi.sourceforge.net/']
   
    # links += ['https://www.zentechnologies.com/']     # done stored

# New Links <==>

    # links += ['https://atasteofkentucky.com/kentucky-derby-2020']
    # links += ['https://www.timberland.co.uk/homepage.html']
    # links += ['https://www.aquacave.com/']
    # links += ['https://www.armysurplusworld.com']
    # links += ['https://www.faz.net/aktuell/']
    # links += ['https://www.stevespanglerscience.com']
    # links += ['https://celticbydesign.com']
    # links += ['https://www.rei.com/']
    # links += ['https://wanderingbull.com/']
    # links += ['https://www.borsheims.com/']
    
    # links += ['https://www.stevespanglerscience.com']
    # links += ['https://www.scientificamerican.com/']
    # links += ['https://takeoverflow.com/']
    # links += ['https://www.redrivercatalog.com/']
    # links += ['https://www.airbnb.com.br']  # 1 match, script, 1,29,942 steps (~796ms) | regex101.com 
    links += ['https://www.zdf.de/']
    # READING LINKS FROM EXCEL FILE
    # links =  read_excel('sample_data/data.xlsx')


    count = 0
    for link in links: 
        count+=1
        one_link = []
        one_link.append(link)
        print(' WEBSITE  [' , count ,'/', len(links), ']  =>  ' ,link)
        main_operation(one_link)

    print('\n----------------------   PROGRAM  ENDED   -----------------------------\n')

