
import re 
from bs4 import BeautifulSoup

''' These Functions contain the Python Regex which will help us Extract the Data From the response source code of the Page '''

class regular_expression:
    pagesource = ''
    payload = '(uvw"' + "xyz('yxz</zxy"
    soup = None

    #   Regex for the Detection of All Context reflections 
    a = r'[çè¦½éæ¼çåé¡¼æé¸æ¨ææçå§å®¹~…*\s[@\*!|$_,}+*\"*\\#*{*\s\^*?\[\]\'\*(*)*\/*.*\w*:*=*&*;*\-*%*\d*\u00a1-\u0104\u4e00-\u9fff\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u4e00-\u9faf\u3400-\u4dbf]*'
    h = r'[çè¦½éæ¼çåé¡¼æé¸æ¨ææçå§å®¹\u00a1-\u0104\u4e00-\u9fff\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u4e00-\u9faf\u3400-\u4dbf\*\|\_\<\!\"\#\\,\(\)\s\'\/\›\$\.\w\+\?\:\=\&\;\-\%\d]*'
    su = r'[çè¦½éæ¼çåé¡¼æé¸æ¨ææçå§å®¹\u00a1-\u0104\u4e00-\u9fff\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u4e00-\u9faf\u3400-\u4dbf\*|_!@\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*'
    regex = r''


    def __init__(self,data):
        self.pagesource = data
        self.pagesource = re.sub(u"[\u00a1-\u0104]", "", self.pagesource,  flags=re.UNICODE)
        self.soup = BeautifulSoup(self.pagesource,features="lxml")
        # print("\n*****************************After Replacing ***************************\n",self.pagesource)

    def set_payload(self,payload):
        self.payload = payload 

    def unify_values(self,values):
        new_value = []
        for value in values:
            if value not in new_value: new_value.append(value)
        return new_value

    def RegExpAttribute(self):
        # pattern = re.compile(r'<(?!a)(?!z)(?!link)(?!frame)(?!script)\w{1,10}[~…*\s[@\*!\|$_,}+*\"*\\#*{*\s^*?\[\]\'\*(*)*\/*.*\w*:*=*&*;*\-*%*\d*\u00a1-\u0104\u4e00-\u9fff\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u4e00-\u9faf\u3400-\u4dbf]*[xX][yY][zZ][~…@\*!\|$_,}+*\"*\\#*{*\s^*?\[\]\'*(*)*<\/*.*\w*:*=*&*;*\-*%*\d*\u00a1-\u0104\u4e00-\u9fff\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u4e00-\u9faf\u3400-\u4dbf]*\/?>')

        pattern = re.compile(r'<(?!a)(?!z)(?!meta)(?!link)(?!frame)(?!script)\w{1,10}' + self.a + r'[xX][yY][zZ]' + self.a + r'\/?>' , re.I | re.S | re.M)
        values = pattern.findall(self.pagesource)
        # print("\n*****************************Attribute Context ***************************\n",self.pagesource)
        # print('values:\n', values)
        return values

    def RegExpHtml(self):
        # pattern = re.compile(r'<\/?(?!script)(?!z)\w{1,10}[\u00a1-\u0104\u4e00-\u9fff\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u4e00-\u9faf\u3400-\u4dbf\*\|\_\<\!\"\#\\,\(\)\s\'\/\›\$\.\w\+\?\:\=\&\;\-\%\d]*>[\u00a1-\u0104\u4e00-\u9fff\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u4e00-\u9faf\u3400-\u4dbf\*\|\_\<\!\"\#\\,\(\)\s\'\/\›\$\.\w\+\?\:\=\&\;\-\%\d]*[xX][yY][zZ][\u00a1-\u0104\u4e00-\u9fff\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u4e00-\u9faf\u3400-\u4dbf\*\|\_\<\!\"\#\\,\(\)\s\'\/\›\$\.\w\+\?\:\=\&\;\-\%\d“”]*<\/?(?!z)\w{1,10}\>?')

        pattern = re.compile(r'<\/?(?!script)(?!z)\w{1,10}' + self.h + r'>' +  self.h + r'[xX][yY][zZ]' + self.h + r'<\/?(?!z)\w{1,10}\>?')
        values = pattern.findall(self.pagesource)
        return values

    def RegExpScript(self):
        # pattern = re.compile(r'<script[\u4e00-\u9fff\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u4e00-\u9faf\u3400-\u4dbf\*|_!@\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*[xX][yY][zZ][\u4e00-\u9fff\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u4e00-\u9faf\u3400-\u4dbf\*|$@_›"\(\)\s|\/\.\w\+\?:=&;\-*%\d\',!#]*\/?>')
        # pattern1 = re.compile(r'<script[\u4e00-\u9fff\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u4e00-\u9faf\u3400-\u4dbf@\*!~|$_,}+*"*\\#*{*\s^*?\[\]\'*(*)*\/*.*\w*:*=*&*;*\-*%*\d*]*>[\u4e00-\u9fff\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u4e00-\u9faf\u3400-\u4dbf\*!|@$_,}+*"~*\\#*{*\s^*?\[\]\'*(*)*\/*.*\w*:*=*>&*;*\-*%*\d*]*[xX][yY][zZ][\u4e00-\u9fff\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u4e00-\u9faf\u3400-\u4dbf@!\\$_#*"~*}\[\]+{*\s^*?(*)*\/*\.*\w*:*=*&*;*\-*%*,|*\d*\'\>*]*\<?[\u4e00-\u9fff\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u4e00-\u9faf\u3400-\u4dbf@!\\$_#*"*}\[\]~+{*\s^*?(*)*\/*\.*\w*:*=*&*;*\-*%*,|*\d*\'\>*]*<\/script>')
        
        pattern = re.compile(r'<script' + self.su + r'[xX][yY][zZ]' + self.su + r'\/?>')
        values = pattern.findall(self.pagesource)  +  self.soup.find_all('script', text=re.compile(r'[xX][yY][zZ]'))
        return self.unify_values(values)

    def RegExpURI_old(self):
        value = list()
        p  =  re.compile(r'<img[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*src=[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*[xX][yY][zZ][\u4e00-\u9fff\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u4e00-\u9faf\u3400-\u4dbf|$_›"\(\)\s|\/\.\w\+\?:=&;\-*%\d\',!#]*\/*>') 
        p1 =  re.compile(r'<a[\u4e00-\u9fff\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u4e00-\u9faf\u3400-\u4dbf\*\|\_\<\!\"\#\\,\(\)\s\'\/\›\$\.\w\+\?\:\=\&\;\-\%\d]*href=[\u4e00-\u9fff\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u4e00-\u9faf\u3400-\u4dbf\*\|\_\<\!\"\#\\,\(\)\s\'\/\›\$\.\w\+\?\:\=\&\;\-\%\d]*[xX][yY][zZ][\u4e00-\u9fff\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u4e00-\u9faf\u3400-\u4dbf\*\|\_\<\!\"\#\\,\(\)\s\'\/\›\$\.\w\+\?\:\=\&\;\-\%\d]*>') 
        p2 =  re.compile(r'<link[\u4e00-\u9fff\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u4e00-\u9faf\u3400-\u4dbf|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*href=[\u4e00-\u9fff\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u4e00-\u9faf\u3400-\u4dbf|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*[xX][yY][zZ][\u4e00-\u9fff\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u4e00-\u9faf\u3400-\u4dbf|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*>') 
        # p3 =  re.compile(r'<form[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*action=[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*[xX][yY][zZ][|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*>') 
        p4 =  re.compile(r'<source[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*src=[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*[xX][yY][zZ][|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*>') 
        p5 =  re.compile(r'<input[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*src=[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*[xX][yY][zZ][|$_›"\(\)\s|\/\.\w\+\?:=&;\-*%\d\',!#]*\/*>') 
        p6 =  re.compile(r'<frame[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*src=[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*[xX][yY][zZ][|$_›"\(\)\s|\/\.\w\+\?:=&;\-*%\d\',!#]*\/*>') 
        p7 =  re.compile(r'<iframe[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*src=[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*[xX][yY][zZ][|$_›"\(\)\s|\/\.\w\+\?:=&;\-*%\d\',!#]*\/*>') 
        # p8 =  re.compile(r'<script[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*src=[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*[xX][yY][zZ][|$_›"\(\)\s|\/\.\w\+\?:=&;\-*%\d\',!#]*\/*>') 
        p9 = re.compile(r'<meta[\u4e00-\u9fff\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u4e00-\u9faf\u3400-\u4dbf|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*content=[\u4e00-\u9fff\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u4e00-\u9faf\u3400-\u4dbf|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*[xX][yY][zZ][\u4e00-\u9fff\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u4e00-\u9faf\u3400-\u4dbf|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*>') 
        p10 = re.compile(r'<svg><image[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*href=[\u4e00-\u9fff|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*[xX][yY][zZ][\u4e00-\u9fff\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u4e00-\u9faf\u3400-\u4dbf|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*>') 
        p11 = re.compile(r'<meta[\u4e00-\u9fff\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u4e00-\u9faf\u3400-\u4dbf|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*http-equiv=[\u4e00-\u9fff\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u4e00-\u9faf\u3400-\u4dbf|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*[xX][yY][zZ][\u4e00-\u9fff\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u4e00-\u9faf\u3400-\u4dbf|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*>') 
        p12 =  re.compile(r'<input[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*formaction=[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*[xX][yY][zZ][|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*>') 

        value = value + p.findall(self.pagesource) + p1.findall(self.pagesource) + p2.findall(self.pagesource) + p4.findall(self.pagesource)  + p5.findall(self.pagesource) + p6.findall(self.pagesource) 
        value = value + p7.findall(self.pagesource) + p9.findall(self.pagesource) + p10.findall(self.pagesource) + p11.findall(self.pagesource) + p12.findall(self.pagesource) 
        # + p3.findall(self.pagesource) + p8.findall(self.pagesource) 
        return value 

    def RegExpURI(self):
        value = list()
        p  = re.compile( r'<img' + self.su + r'src=' + self.su + r'[xX][yY][zZ]' + self.su + r'\/*>') 
        p1 = re.compile( r'<img' + self.su + r'href=' + self.su + r'[xX][yY][zZ]' + self.su + r'\/*>') 
        p2 =  re.compile(r'<a' + self.su + r'href=' + self.su + r'[xX][yY][zZ]' + self.su + r'\/*>') 
        p3 = re.compile( r'<link' + self.su + r'href=' + self.su + r'[xX][yY][zZ]' + self.su + r'\/*>') 
        p4 = re.compile( r'<source' + self.su + r'src=' + self.su + r'[xX][yY][zZ]' + self.su + r'\/*>') 
        p5 = re.compile( r'<frame' + self.su + r'src=' + self.su + r'[xX][yY][zZ]' + self.su + r'\/*>') 
        p6 = re.compile( r'<iframe' + self.su + r'src=' + self.su + r'[xX][yY][zZ]' + self.su + r'\/*>') 
        p7 = re.compile( r'<meta' + self.su + r'content=' + self.su + r'[xX][yY][zZ]' + self.su + r'\/*>') 
        p8 = re.compile( r'<meta' + self.su + r'http-equiv=' + self.su + r'[xX][yY][zZ]' + self.su + r'\/*>') 
        
        value += p.findall(self.pagesource) + p1.findall(self.pagesource) + p2.findall(self.pagesource) + p3.findall(self.pagesource) + p4.findall(self.pagesource)
        value += p5.findall(self.pagesource) + p6.findall(self.pagesource) + p7.findall(self.pagesource)+ p8.findall(self.pagesource)
        return value 

# >>>>>>>>>>>>>>>>  These functions Find the Exact payload reflection after attacking the websites >>>>>>>>>>>>>>>>>>>

    def RegExpSameAttribute(self):
        p = re.compile(r'<\w{1,10}' + self.a + r'\s?' + self.a + re.escape(self.payload) + self.a + r'\/?>')
        return p.findall(self.pagesource) 

    def RegExpSameHtml(self):
        p = re.compile(r'<\/?(?!script)\w{1,10}' + self.h + r'>' + self.h + re.escape(self.payload) + self.h + r'<\/\w{1,10}>')
        return p.findall(self.pagesource)

    def RegExpSameScript(self):
        p = re.compile(r'<script' + self.su + r'\w{2,10}\-?\w{2,10}' + self.su + re.escape(self.payload) + self.su + r'>')
        p1 = re.compile(r'<script' + self.su + r'>' + self.su + re.escape(self.payload) + self.su + r'<\/script>')
        return p.findall(self.pagesource) + p1.findall(self.pagesource) + self.soup.find_all( 'script', text=re.escape(self.payload) ) 
 
    def RegExpSameURI_old(self):
        value = list()
        p =  re.compile(r'<img[`|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*src=[`|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*' + re.escape(self.payload) +  r'[`|$_›"\(\)\s|\/\.\w\+\?:=&;\-*%\d\',!#]*\/*>') 
        p1 = re.compile(r'<a[\u4e00-\u9fff\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u4e00-\u9faf\u3400-\u4dbf`\*\|\_\<\!\"\#\\,\(\)\s\'\/\›\$\.\w\+\?\:\=\&\;\-\%\d]*href=[\u4e00-\u9fff\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u4e00-\u9faf\u3400-\u4dbf`\*\|\_\<\!\"\#\\,\(\)\s\'\/\›\$\.\w\+\?\:\=\&\;\-\%\d]*' + re.escape(self.payload) +  r'[\u4e00-\u9fff\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u4e00-\u9faf\u3400-\u4dbf`\*\|\_\<\!\"\#\\,\(\)\s\'\/\›\$\.\w\+\?\:\=\&\;\-\%\d]*>') 
        p2 = re.compile(r'<link[\u4e00-\u9fff\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u4e00-\u9faf\u3400-\u4dbf`|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*href=[\u4e00-\u9fff\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u4e00-\u9faf\u3400-\u4dbf`|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*' + re.escape(self.payload) +  r'[\u4e00-\u9fff\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u4e00-\u9faf\u3400-\u4dbf`|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*>') 
        p3 = re.compile(r'<form[`|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*action=[`|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*' + re.escape(self.payload) +  r'[`|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*>') 
        p5 = re.compile(r'<input[`|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*src=[`|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*' + re.escape(self.payload) +  r'[`|$_›"\(\)\s|\/\.\w\+\?:=&;\-*%\d\',!#]*\/*>') 
        p6 = re.compile(r'<frame[`|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*src=[`|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*' + re.escape(self.payload) +  r'[`|$_›"\(\)\s|\/\.\w\+\?:=&;\-*%\d\',!#]*\/*>') 
        p7 = re.compile(r'<iframe[`|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*src=[`|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*' + re.escape(self.payload) +  r'[`|$_›"\(\)\s|\/\.\w\+\?:=&;\-*%\d\',!#]*\/*>') 
        # p8 = re.compile(r'<script[`|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*src=[`|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*' + re.escape(self.payload) +  r'[`|$_›"\(\)\s|\/\.\w\+\?:=&;\-*%\d\',!#]*\/*>') 
        p9 = re.compile(r'<meta[\u4e00-\u9fff\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u4e00-\u9faf\u3400-\u4dbf`|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*content=[\u4e00-\u9fff\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u4e00-\u9faf\u3400-\u4dbf`|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*' + re.escape(self.payload) +  r'[\u4e00-\u9fff\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u4e00-\u9faf\u3400-\u4dbf`|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*>') 
        p10 = re.compile(r'<svg><image[`|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*href=[`|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*' + re.escape(self.payload) +  r'[`|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*>') 
        p11 = re.compile(r'<meta[\u4e00-\u9fff\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u4e00-\u9faf\u3400-\u4dbf`|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*http-equiv=[\u4e00-\u9fff\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u4e00-\u9faf\u3400-\u4dbf`|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*' + re.escape(self.payload) +  r'[\u4e00-\u9fff\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u4e00-\u9faf\u3400-\u4dbf`|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*>') 
        p12 = re.compile(r'<input[`|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*formaction=[`|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*' + re.escape(self.payload) +  r'[`|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*>') 
        p13 = re.compile(r'<source[`|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*src=[`|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*' + re.escape(self.payload) +  r'[`|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*>') 

        value = value + p.findall(self.pagesource) + p1.findall(self.pagesource) + p2.findall(self.pagesource) + p3.findall(self.pagesource) + p5.findall(self.pagesource) + p6.findall(self.pagesource) 
        value = value + p7.findall(self.pagesource) + p9.findall(self.pagesource) + p10.findall(self.pagesource) + p11.findall(self.pagesource) + p12.findall(self.pagesource) + p13.findall(self.pagesource) 
        return value

    def RegExpSameURI(self):
        value = list()
        p  = re.compile( r'<img' + self.su + r'src=' + self.su + re.escape(self.payload) + self.su + r'\/*>') 
        p1 = re.compile( r'<img' + self.su + r'href=' + self.su + re.escape(self.payload) + self.su + r'\/*>') 
        p2 =  re.compile(r'<a' + self.su + r'href=' + self.su + re.escape(self.payload) + self.su + r'\/*>') 
        p3 = re.compile( r'<link' + self.su + r'href=' + self.su + re.escape(self.payload) + self.su + r'\/*>') 
        p4 = re.compile( r'<source' + self.su + r'src=' + self.su + re.escape(self.payload) + self.su + r'\/*>') 
        p5 = re.compile( r'<frame' + self.su + r'src=' + self.su + re.escape(self.payload) + self.su + r'\/*>') 
        p6 = re.compile( r'<iframe' + self.su + r'src=' + self.su + re.escape(self.payload) + self.su + r'\/*>') 
        p7 = re.compile( r'<meta' + self.su + r'content=' + self.su + re.escape(self.payload) + self.su + r'\/*>') 
        p8 = re.compile( r'<meta' + self.su + r'http-equiv=' + self.su + re.escape(self.payload) + self.su + r'\/*>') 
        
        value += p.findall(self.pagesource) + p1.findall(self.pagesource) + p2.findall(self.pagesource) + p3.findall(self.pagesource) + p4.findall(self.pagesource)
        value += p5.findall(self.pagesource) + p6.findall(self.pagesource) + p7.findall(self.pagesource)+ p8.findall(self.pagesource)
        return value 


    def context_attack(self, Context):
        if Context == 'ATTR'    : return self.RegExpSameAttribute()
        if Context == 'HTML'    : return self.RegExpSameHtml()
        if Context == 'SCRIPT'  : return self.RegExpSameScript()
        if Context == 'URL'     : return self.RegExpSameURI()
    
    def attack_script(self):
        values = list()
        p = re.compile(r'<script.*' + re.escape(self.payload) +  r'.*<\/script>')
        values = p.findall(self.pagesource) +  self.soup.find_all( 'script', text=re.escape(self.payload) )
        return self.unify_values(values)

# Looking for the Appearance of the payload in response against a post form submission.
    def RegExp_postforms(self):
        value = list()
        attr = re.compile(r'.*[xX][yY][zZ].*')
        # html = re.compile(r',.*[xX][yY][zZ].*,')
        value = attr.findall(self.pagesource) # + html.findall(self.pagesource)
        return value

if __name__ == "__main__":
    
    data = "<div class='col-md-12 searchresults'>Displaying results for <span style='color:red;'><q><img src=x onerror='alert`1`'></q></span></div>	"
    RegExp = regular_expression(data)
    RegExp.set_payload("<img src=x onerror='alert`1`'>")
    value = RegExp.context_attack("HTML")
    print(value)
    print('{RegularExpression}')
