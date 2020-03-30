
import re 
from bs4 import BeautifulSoup

''' These Functions contain the Python Regex which will help us Extract the Data From the response source code of the Page '''

class regular_expression:
    pagesource = ''
    payload = '"' + "xyz'yxz</zxy"
    soup = None

    def __init__(self,data):
        self.pagesource = data
        self.soup = BeautifulSoup(data,features="lxml")

    def set_payload(self,payload):
        self.payload = payload

    def RegExpAttribute(self):
        pattern = re.compile(r'<(?!a)(?!link)(?!meta)(?!frame)(?!iframe)(?!script)\w{1,10}\s[@\*!|$_,}+*"*\\#*{*\s^*?\[\]\'\*(*)*\/*.*\w*:*=*&*;*\-*%*\d*]*[xX][yY][zZ][@\*!|$_,}+*"*\\#*{*\s^*?\[\]\'*(*)*<\/*.*\w*:*=*&*;*\-*%*\d*]*\/?>')
        values = pattern.findall(self.pagesource)
        # print(values)
        return values

    def RegExpHtml(self):
        pattern = re.compile(r'<(?!script)\w{1,10}[\*\|\_\<\!"\#\\,\(\)\s\'\/\›\$\.\w\+\?\:\=\&\;\-\%\d]*>[\*\|\_\<\!"\#\\,\(\)\s\'\/\›\$\.\w\+\?\:\=\&\;\-\%\d]*[xX][yY][zZ][\*\|\_\<\!"\#\\,\(\)\s\'\/\›\$\.\w\+\?\:\=\&\;\-\%\d]*<\/?\w{1,10}?>')
        values = pattern.findall(self.pagesource)
        return values

    def RegExpScript(self):
        pattern = re.compile(r'<script[\*|_!@\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*[xX][yY][zZ][\*|$@_›"\(\)\s|\/\.\w\+\?:=&;\-*%\d\',!#]*\/?>')
        # pattern1 = re.compile(r'<script[@\*!~|$_,}+*"*\\#*{*\s^*?\[\]\'*(*)*\/*.*\w*:*=*&*;*\-*%*\d*]*>[\*!|@$_,}+*"~*\\#*{*\s^*?\[\]\'*(*)*\/*.*\w*:*=*>&*;*\-*%*\d*]*[xX][yY][zZ][@!\\$_#*"~*}\[\]+{*\s^*?(*)*\/*\.*\w*:*=*&*;*\-*%*,|*\d*\'\>*]*\<?[@!\\$_#*"*}\[\]~+{*\s^*?(*)*\/*\.*\w*:*=*&*;*\-*%*,|*\d*\'\>*]*<\/script>')
        values = pattern.findall(self.pagesource) +  self.soup.find_all('script', text=re.compile('xyz'))
        return values

    def RegExpURI(self):
        value = list()
        p  =  re.compile(r'<img[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*src=[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*[xX][yY][zZ][|$_›"\(\)\s|\/\.\w\+\?:=&;\-*%\d\',!#]*\/*>') 
        p1 =  re.compile(r'<a[\*\|\_\<\!\"\#\\,\(\)\s\'\/\›\$\.\w\+\?\:\=\&\;\-\%\d]*href=[\*\|\_\<\!\"\#\\,\(\)\s\'\/\›\$\.\w\+\?\:\=\&\;\-\%\d]*[xX][yY][zZ][\*\|\_\<\!\"\#\\,\(\)\s\'\/\›\$\.\w\+\?\:\=\&\;\-\%\d]*>') 
        p2 =  re.compile(r'<link[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*href=[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*[xX][yY][zZ][|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*>') 
        p3 =  re.compile(r'<form[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*action=[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*[xX][yY][zZ][|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*>') 
        p4 =  re.compile(r'<source[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*src=[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*[xX][yY][zZ][|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*>') 
        p5 =  re.compile(r'<input[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*src=[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*[xX][yY][zZ][|$_›"\(\)\s|\/\.\w\+\?:=&;\-*%\d\',!#]*\/*>') 
        p6 =  re.compile(r'<frame[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*src=[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*[xX][yY][zZ][|$_›"\(\)\s|\/\.\w\+\?:=&;\-*%\d\',!#]*\/*>') 
        p7 =  re.compile(r'<iframe[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*src=[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*[xX][yY][zZ][|$_›"\(\)\s|\/\.\w\+\?:=&;\-*%\d\',!#]*\/*>') 
        # p8 =  re.compile(r'<script[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*src=[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*[xX][yY][zZ][|$_›"\(\)\s|\/\.\w\+\?:=&;\-*%\d\',!#]*\/*>') 
        p9 = re.compile(r'<meta[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*content=[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*[xX][yY][zZ][|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*>') 
        p10 = re.compile(r'<svg><image[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*href=[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*[xX][yY][zZ][|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*>') 
        p11 = re.compile(r'<meta[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*http-equiv=[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*[xX][yY][zZ][|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*>') 
        p12 =  re.compile(r'<input[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*formaction=[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*[xX][yY][zZ][|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*>') 

        value = value + p.findall(self.pagesource) + p1.findall(self.pagesource) + p2.findall(self.pagesource) + p3.findall(self.pagesource) + p4.findall(self.pagesource)  + p5.findall(self.pagesource) + p6.findall(self.pagesource) 
        value = value + p7.findall(self.pagesource) + p9.findall(self.pagesource) + p10.findall(self.pagesource) + p11.findall(self.pagesource) + p12.findall(self.pagesource) 
        return value 

# >>>>>>>>>>>>>>>>  Looking for the EXACT and SAME Appearance of the Payload >>>>>>>>>>>>>>>>>>>

    def RegExpSameAttribute(self):
        p = re.compile(r'<(?!a)(?!link)(?!meta)(?!frame)(?!iframe)(?!script)\w{2,10}[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*' + re.escape(self.payload) +  r'[|$_›"\(\)\s|\/\.\w\+\?:=&;\-*%\d\',!#]*\/?>')
        return p.findall(self.pagesource) 

    def RegExpSameHtml(self):
        p = re.compile(r'<(?!script)\w{1,10}[_,*"*#*{*\s*\'*(*)*\/*.*\w*:*=*&*;*\-*%*\d*]*>[!|$_,}+*"*\\#*{*\s^*>?\[\]\'*(*)*\/*.*\w*:*=*&*;*\-*%*\d*]*' + re.escape(self.payload) +  r'[!|$_,}+*"*\\#*{*\s^*>?\[\]\'*(*)*\/*.*\w*:*=*&*;*\-*%*\d*]*<\/\w{1,10}>')
        return p.findall(self.pagesource)

    def RegExpSameScript(self):
        p = re.compile(r'<script[_!\"*#\\*,*\(*\)\s\'*\/*›\.*\w*\+*\?*:*=*&*;*\-*%*\d*]*\w{2,10}\-?\w{2,10}[_!\\*,*#\(*\)›\s\'*\/*\.*\w*\+*\?*:*=*&*;*\-*%*\d*"]*' + re.escape(self.payload) +  r'[_›"\(*\)*\s\/*\.*\w*\+*\?*:*=*&*;*\-*%*\d*\'*,*!#]*>')
        p1 = re.compile(r'<script[_,*"*#*{*\s*\'*(*)*\/*.*\w*:*=*&*;*\-*%*\d*]*>[!|$_,}+*"*\\#*{*\s^*>?\[\]\'*(*)*\/*.*\w*:*=*&*;*\-*%*\d*]*' + re.escape(self.payload) +  r'[!|$_,}+*"*\\#*{*\s^*>?\[\]\'*(*)*\/*.*\w*:*=*&*;*\-*%*\d*]*<\/script>')
        return p.findall(self.pagesource) +  self.soup.find_all( 'script', text=re.escape(self.payload) ) # + p1.findall(self.pagesource)
    
    def attack_script(self):
        p = re.compile(r'<script.*' + re.escape(self.payload) +  r'.*<\/script>')
        return p.findall(self.pagesource) +  self.soup.find_all( 'script', text=re.escape(self.payload) ) # + p1.findall(self.pagesource)


    def RegExpSameURI(self):
        value = list()
        p =  re.compile(r'<img[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*src=[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*' + re.escape(self.payload) +  r'[|$_›"\(\)\s|\/\.\w\+\?:=&;\-*%\d\',!#]*\/*>') 
        p1 = re.compile(r'<a[\*\|\_\<\!\"\#\\,\(\)\s\'\/\›\$\.\w\+\?\:\=\&\;\-\%\d]*href=[\*\|\_\<\!\"\#\\,\(\)\s\'\/\›\$\.\w\+\?\:\=\&\;\-\%\d]*' + re.escape(self.payload) +  r'[\*\|\_\<\!\"\#\\,\(\)\s\'\/\›\$\.\w\+\?\:\=\&\;\-\%\d]*>') 
        p2 = re.compile(r'<link[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*href=[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*' + re.escape(self.payload) +  r'[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*>') 
        p3 = re.compile(r'<form[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*action=[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*' + re.escape(self.payload) +  r'[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*>') 
        p5 = re.compile(r'<input[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*src=[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*' + re.escape(self.payload) +  r'[|$_›"\(\)\s|\/\.\w\+\?:=&;\-*%\d\',!#]*\/*>') 
        p6 = re.compile(r'<frame[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*src=[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*' + re.escape(self.payload) +  r'[|$_›"\(\)\s|\/\.\w\+\?:=&;\-*%\d\',!#]*\/*>') 
        p7 = re.compile(r'<iframe[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*src=[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*' + re.escape(self.payload) +  r'[|$_›"\(\)\s|\/\.\w\+\?:=&;\-*%\d\',!#]*\/*>') 
        # p8 = re.compile(r'<script[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*src=[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*' + re.escape(self.payload) +  r'[|$_›"\(\)\s|\/\.\w\+\?:=&;\-*%\d\',!#]*\/*>') 
        p9 = re.compile(r'<meta[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*content=[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*' + re.escape(self.payload) +  r'[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*>') 
        p10 = re.compile(r'<svg><image[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*href=[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*' + re.escape(self.payload) +  r'[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*>') 
        p11 = re.compile(r'<meta[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*http-equiv=[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*' + re.escape(self.payload) +  r'[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*>') 
        p12 = re.compile(r'<input[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*formaction=[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*' + re.escape(self.payload) +  r'[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*>') 
        p13 = re.compile(r'<source[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*src=[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*' + re.escape(self.payload) +  r'[|_!\"#\\,\(\)\s\'\/›$\.\w\+\?:=&;\-%\d]*>') 

        value = value + p.findall(self.pagesource) + p1.findall(self.pagesource) + p2.findall(self.pagesource) + p3.findall(self.pagesource) + p5.findall(self.pagesource) + p6.findall(self.pagesource) 
        value = value + p7.findall(self.pagesource) + p9.findall(self.pagesource) + p10.findall(self.pagesource) + p11.findall(self.pagesource) + p12.findall(self.pagesource) + p13.findall(self.pagesource) 
        return value


    def cotext_attack(self, Context):
        if Context == 'ATTR'    : return self.RegExpSameAttribute()
        if Context == 'HTML'    : return self.RegExpSameHtml()
        if Context == 'SCRIPT'  : return self.RegExpSameScript()
        if Context == 'URL'     : return self.RegExpSameURI()


# Looking for the Appearance of the payload in response against a post form submission.

    def RegExp_postforms(self):
        value = list()
        attr = re.compile(r',.*[xX][yY][zZ].*,')
        # html = re.compile(r',.*[xX][yY][zZ].*,')
        value = attr.findall(self.pagesource) # + html.findall(self.pagesource)
        return value

if __name__ == "__main__":
    print('{RegularExpression}')
