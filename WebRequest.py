from urllib.request import urlopen
import urllib.response
import urllib.request
import urllib.parse
import requests 
import urllib3 
import re
from bs4 import BeautifulSoup

class web_request:  
    url = ''
    form_method = ''

    def __init__(self,url,method):
        self.url = url 
        self.form_method = method.lower()
        
    def get_source(self):    
        s1 = self.open_request()
        s2 = self.openurl()
        if len(s1) > len(s2): source = s1 
        else:   source = s2
        if not source: 
            source = requests.get(self.url)
            source = source.text
        return source
    
    def open_request(self):
        session = requests.Session()
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36  (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
        'Content-Type': 'text/html',}
        try:
            resp = requests.get(self.url, headers=headers, timeout=10)
            pagesource = resp.text
            # print('{WebRequest} =>  \n', pagesource)
            # self.write_response_textfile(str(pagesource))

            if pagesource:  return pagesource
            else: return requests.get(self.url)
        except:
            print('\n *[Requests Failed...]* ')
            return ''

    def openurl(self):  
        headers = {}
        # headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686)"
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36  (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
        'Content-Type': 'text/html',}
        # print('urllib => \n' , self.url)
        try:
            req  = urllib.request.Request(self.url)
            resp = urllib.request.urlopen(req, timeout=10)
            pagesource = resp.read().decode(encoding='utf-8', errors='strict') 
            # print(pagesource)
            return pagesource
        except:
            print('\n *[Urrlib Failure ]*') 
            return ''

if __name__ == "__main__":
    
    # link = 'https://www.raremaps.com/'
    # link = 'https://www.zentechnologies.com/search/search.php?query="><img src=x onerror="alert(1)"&search=1'
    # link = 'https://ifu-institut.at/search?text="><img src=x onerror="alert(1)"&cms_token=30f71d2dffb99d557a11bb04966d80a0'
    link = 'https://www.sweetwater.com/'
    link = 'http://db.etree.org/shnlist.php?artist=&artist_group_key=1&year=/uvw"xyz' + "'yxz<zxy"
    
    link = 'http://tw.gigacircle.com/category.html?group=abc/uvw"xyz' + "'yxz<zxy"
    Web = web_request(link, 'get')
    # resp = Web.get_source()
    pattern = re.compile(r'<(?!a)(?!z)(?!link)(?!frame)(?!script)\w{1,10}[~…*\s[@\*!\|$_,}+*\"*\\#*{*\s^*?\[\]\'\*(*)*\/*.*\w*:*=*&*;*\-*%*\d*\u00a1-\u0104\u4e00-\u9fff\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u4e00-\u9faf\u3400-\u4dbf]*[xX][yY][zZ][~…@\*!\|$_,}+*\"*\\#*{*\s^*?\[\]\'*(*)*<\/*.*\w*:*=*&*;*\-*%*\d*\u00a1-\u0104\u4e00-\u9fff\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u4e00-\u9faf\u3400-\u4dbf]*\/?>')

    resp = requests.get(link)
    resp = resp.text
    print(resp)

    value = pattern.findall(resp)
    # print('value: \n', value)
    
    print('{WebRequest}')