
import os 
import re
import requests
import pandas as pd 
from bs4 import BeautifulSoup

from WebRequest import web_request
from DirectGetParams import direct_get_params
# from WriteExcelFile import write_excel_file
from Analyze_Attack import analyze_attack

class main_class:
    url = ''
    web = None

    folder = 'ChineseLanguage'
    # folder = 'solvingissues'
    # folder = 'Business_E-Commerce_Customer_Relationship_Management'

    dirName = ''
    base = ''
    domain_url = ''
    links = [] 
    website = []
    source = None

    def __init__(self,url):
        base_url = self.find_base_url(url)
        self.domain_url = self.find_domain_url(url)
        print(' BASE URL [', base_url, ']\n')
        self.base = self.folder + '/' + base_url
        self.create_directory(self.folder)
        self.dirName = self.folder + '/' + self.dirName

        self.create_directory( self.base )

    def find_domain_url(self,url):
        if '/' not in url: return url

        url = str(url)
        char = '/'
        k = 3
        if url.__contains__('http'):
            temp = url.split(char)
            domain = char.join(temp[:k]), char.join(temp[k:])
            domain = domain[0]
        else:
            domain = url.split(char)[0]
        print(' Domain = ', domain)
        return domain

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
            elif tag['href'][0] == '/': links.append(self.domain_url + tag['href'])
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
            if link not in links:  
                return True
        return False

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
        # print('\n Inside-links = ', len(web_links) ,'\n')
        # print('\n\t\t WE ARE FETCHING LINKS \n\n')
        for i in range(index, len(web_links) ):
            count+=1
            print(count, end=' - ')
            self.url = web_links[i]

            self.web = web_request(self.url,'GET')
            self.base = self.find_base_url(self.url)
            self.source = self.get_source(self.url)
            bfs_links = self.get_links()
            # print('\n\n', bfs_links, '\n\n')
            
            # Removing Duplicates
            for new_link in bfs_links: 
                if new_link not in self.links:
                    self.links.append(new_link)

        return count , self.links.copy()


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
        # print('\n INDEX = ', index ,'\n')
        for link in links: print(link)
        print( ' Total Links = ', len(links))

        # if (index > 21): break      

    # print('Index = ', index)
    # new_links = []
    # if len(links) > 19 :    
    #     for i in range(20): new_links.append(links[i]) 
    # else:   new_links = links
    # for link in links: print(link)


    # print('\n Crawler Links:', len(links), '\n')


    """ Now the Tool Anaylyzes the website, Attacks it (if possible) and Generates Reports (Text Files) """
    Analyzer = analyze_attack(base, M.folder)
    Analyzer.collect_data(links)



# The website links are stored in Excel file and we read the file to get the links 
def read_excel(excel_filename):
    df = pd.read_excel(excel_filename)
    links = df['websites']
    return links

if __name__ == "__main__":
    print('\n=> This Automated Tool assists in finding XSS Vulnerablilities.\n=> It assumes that there is a potential XSS Present in the Website\n')

    direct_param = direct_get_params()

    links = []
# -----------------------  Links for Tuning & Testing -------------------------------


    # links += ['http://www.webhostingsearch.com//reviews.php?searchString=']
    # links += ['http://nbasavant.com/leaderboard.php?ddlMin=500&ddlPos&ddlTeam&ddlYear=2014&sort=aaaaaaa']
    # links += ['http://db.etree.org/shnlist.php?artist&artist_group_key=1&year=']
    # links += ['https://www.nejm.org/search?pageType=search&q=/uvw"xyzyxz<zxy&asug=']
    # links += ['https://jobs.berlin.de/?stf=freeText&ns=1&qs=[]&companyID=0&cityID=0&sourceOfTheSearchField=resultlistpage:general&searchOrigin=Resultlist_top-search&ke=&ws=Berlin']
    # links += ['https://www.datasheet4u.com/search.php?sWord=']
    # links += ['https://www.scientificamerican.com/search/?q=']


# Demo with Ashar Javed 
    # links += ['https://www.bild.de/suche.bild.html?query=XXXXXXXX&type=video&resultsStart=0&resultsPerPage=12&sortBy=date']

    # links += ['http://tw.gigacircle.com/category.html?group=XXXXXXXX']  # The Jibrish Characters NOT Detected /\/\/\/\//\/\/\

    # links += ['http://jnarmer.sdabocconi.it/events/login.php?id=']
    # links += ['http://pinterface.tianjimedia.com/front/wap/searchresult.jsp?keyword=XXXXXXX']




    # links += ['https://list.tmall.com/search_product.htm?q=%22xyz&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton']
    # links += ['https://www.sogou.com/tx?hdq=sogou-wsse-3f7bcd0b3ea82268&ie=utf-8&query=newzone']
    # links += ['https://mp.weixin.qq.com/s?src=3&timestamp=1589628993&ver=1&signature=az-e2gCzl1q7yCzsvOkRCJypGTZhF80phDfqBZCInQAFeqMVc4wQ2VbFLFtZqB6CdjdYa1KF9di5sbWViELTx6fJ4GVWqS45y*gEVRWR7Vu5U2HuxwUvWlX7tnEKr-uEbl0V95FqoV0vruxGirCnKzPgxcxji0xfz49r0fVkKrc=']
    # links += ['http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=xyz&fenlei=256&rsv_pq=fa06ddd00004840d&rsv_t=fbdd9WNuUOiqIQKKkBcR6lfGDpYV1JPYybSIEeS7Kqh3GNVgXsNzrFRfGtI&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_sug3=4&rsv_sug2=0&rsv_btype=i&inputT=535&rsv_sug4=1204']

    # links += ['https://www.sohu.com/']
    # links += ['https://pages.tmall.com/wow/a/act/tmall/tmc/26646/wupr?spm=a2240.7829288.0.0.44c34fe50dbvxn&pos=1&wh_pid=main-192807&acm=lb-zebra-153802-761482.1003.2.7829925&scm=1003.2.lb-zebra-153802-761482.ITEM_1590379293744_7829925']
    # links += ['https://list.tmall.com/search_product.htm?q=xtz&type=p&vmarket=&spm=a211oj.0.a2227oh.d100&from=..pc_1_searchbutton']
    # links += ['https://so.com/s?q=xtz&src=360portal&_re=0']
    # links += ['https://world.taobao.com/']

    # links += ['https://search.jd.com/Search?keyword=xzt&enc=utf-8&gp=2&wq=xzt&pvid=c774e1cdcd23496e8e185ab578e800c6']
    # links += ['http://www.sina.com.cn/mid/search.shtml?range=all&c=news&q=xzy&from=home&ie=utf-8']
    # links += ['https://www.zhanqi.tv/search?q=x']
    # links += ['https://so.csdn.net/so/search/s.do?q=x&t=&u=']
    # links += ['https://s.weibo.com/weibo/xz?topnav=1&wvr=6&b=1']

    # links += ['http://17ok.com/']
    # links += ['https://search.bilibili.com/all?keyword=new&from_source=nav_search_new']
    # links += ['http://so.jrj.com.cn/cse/search?q=&s=5981575158355482147&nsid=1']
    # links += ['https://www.google.com.hk/webhp?hl=hi&sourceid=cnhp&gws_rd=ssl']
    # links += ['https://s.1688.com/imall/offer_search.htm?keywords=&n=y&netType=1%2C11&encode=utf-8&spm=a260k.dacugeneral.search.0']
    # links += ['https://www.yy.com/93479716/93479716?tempId=16777299999']

    links += ['https://search.gome.com.cn/search?question=new&searchType=goods&search_mode=normal&reWrite=true&instock=1']
    # links += ['https://www.6.cn/search.php?type=use&key=new']
    # links += ['https://zzk.cnblogs.com/s?t=b&w=nerw']
    # links += ['http://www.chinaso.com/search/pagesearch.htm?q=&site=eastday.com&search_scope=insite']
    # links += ['https://so.iqiyi.com/so/q_new?source=input&sr=161302371559']

    # links += ['http://s.rednet.cn/?scope=1&title=0&q=new']
    # links += ['https://www.alibabacloud.com/s?k=new']
          
    # for link in links:
    #     direct_param.start(link)

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

'''       ^^^^^   TASKS REMAINING

1. Revert Payload : uvw"xyz'</zxy


'''