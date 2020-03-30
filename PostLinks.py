
import re, os, json
import requests
from requests import Request, Session
import urllib.parse as parse
from bs4 import BeautifulSoup
from WebRequest import web_request
from RegularExpression import regular_expression

import pandas as pd

class post_links:
    url = ''
    write_flag = False
    source = ''
    base_link = ''
    complete_link = ''
    filename = 'sample_data/data.xlsx'
    username = 'newxyzmodifieduser2020'
    email = 'a@xyz.com'
    password = 'newxyzmodifieduser2020'

    # At the start of the program this function collects the source code of the web page and the base url.
    def start_search(self,link):
        web = web_request(link,'get')
        s1 = web.open_request()
        s2 = web.openurl()
        self.base_link = link
        # collecting source code in 'source'
        if len(s1) >= len(s2): self.source = s1
        else: self.source = s2
    
    # this method extracts the Post Forms from a web page
    def get_forms(self):
        forms = []
        soup = BeautifulSoup(self.source, features="lxml")
        forms += soup.find_all('form', attrs = {'method' : 'POST' })
        forms += soup.find_all('form', attrs = {'method' : 'post' })
        # print(forms)
        return forms
        

    # This function is responsible for Extracting input fields and adding payloads ( username,email,passwords)
    # Also responsible for submitting forms and caturing responses against post requests
    def find_inputs(self):
        posturls = []
        presence = []
        responses = []
        r = ''
        forms = self.get_forms()
        print('Number of POST Forms [', len(forms), ']')

        if len(forms) == 0: 
            self.write_flag = False
            return ['None'], ['NO POST FORMS'] , ['No Presence']
        else: 
            self.write_flag = True

        for form in forms: 
            # retrieviing all the input fields of a form
            fields = form.find_all('input')
            # formdata = dict( (field.get('name'), field.get('value')) for field in fields)
            
            # Defining a dictionary to store the name, value pairs of our form-fields. 
            formdata = {}
            for field in fields:
                # print('\ninside Form--Fields; ', form)

                if not field.get('type') == 'submit' and not field.get('type') == 'checkbox' and not field.get('type') == 'radiobox':
                    formdata[field.get('name')] = field.get('value')
            try:
                if 'email' in formdata:         formdata['email'] = self.email
                if 'user' in formdata:          formdata['user']  = self.username
                if 'username' in formdata:      formdata['username']  = self.username
                if 'user_name' in formdata:     formdata['user_name']  = self.username
                if 'pass' in formdata:          formdata['pass'] = self.password
                if 'passw' in formdata:         formdata['passw'] = self.password
                if 'password' in formdata:      formdata['password'] = self.password
            except Exception :
                print(end='')

            for f in formdata:
                if f:   
                    if f.__contains__('name'):      formdata[f] = self.username 
                    if f.__contains__('email'):     formdata[f] = self.email
                    if f.__contains__('Email'):     formdata[f] = self.email
                    if f.__contains__('password'):  formdata[f] = self.password

            # print('formdata\n',formdata)
            # return '', '', ''
            
            # Further operation is done Only if our <form> has a 'form-action'
            if form.get('action'):  
                # print(form)

                # Creating Complete link (posturl) from the "form-action"
                url_link = self.make_link(form.get('action'))
                posturl = parse.urljoin(url_link, form['action'])
                posturls.append( posturl )
                # print('Post-Url: ', posturl)
            
                headers = {}
                headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686)"

                # Using Requests Library to Send a Post Request
                s = requests.Session()
                r = s.post(posturl, data=formdata, headers=headers)
                # Reg = regular_expression(str(r.text))
                
                # Saving Response of the request sent to the server e.g; <Response 200>
                if r.text.__contains__('xyz'):
                    responses.append(r)
                    presence.append('Present')
                    # print('Payload = ', Reg.RegExp_postforms())
                else:
                    responses.append(r) 
                    presence.append('NOT FOUND') 
                # print(r.text)
            else:
                posturls.append('None')
                responses.append('FormAction Not Found')
                presence.append('None')
        print('-------------------------------------------______________________---------------------------------------------------------------')
        return posturls, responses, presence

    # Takes Input a "form-action" and returns a valid complete link,
    # Example: form-acion = /search/data.php => retrun value = https://www.example.com/search/data.php 
    def make_link(self,form_action):
        self.complete_link = self.base_link
        if not len(form_action) > 0 : return 
        if not len(self.complete_link) > 0: return

        if      self.if_complete_link(form_action):  self.complete_link = form_action
        elif    self.complete_link[-1] == '/' and form_action[0] == '/': self.complete_link = self.complete_link[:-1] + form_action
        elif   self.complete_link[-1] != '/' and form_action[0] == '/': self.complete_link = self.complete_link + form_action
        elif   self.complete_link[-1] != '/' and form_action[0] != '/': self.complete_link = self.complete_link + '/' + form_action
        else:   self.complete_link = self.complete_link + form_action

        # print('\t', self.complete_link)
        if self.complete_link[0] == '/' and self.complete_link[1] == '/': self.complete_link = 'https:' + self.complete_link
        return self.complete_link
    
    # This functions checks if the form-action is complete link or Not e.g: https://www.example.com/ is complete link
    def if_complete_link(self,action):
        if(action.__contains__('https') or action.__contains__('www') ):
            return True
        return False

    # The website links are stored in Excel file and we read the file to get the links 
    def read_excel(self):
        df = pd.read_excel(self.filename)
        links = df['websites']
        return links
    
    # Writing the Response data along with the urls of the that page/form of the website
    def write_text(self,link, posturl, R, presence):
        if self.write_flag :
            with open('PostForm_Data.txt','a') as f:
                f.write(str(link) + '\t' + str(posturl) + '\t' + str(R) + '\t' + str(presence) + '\n')

    # This function is responsible to complete all the operations on a list of links
    def collect_data(self, links):
        p = post_links()
        index = 0
        posturl = r = presence = 'None'

        for link in links:
            if type(link) == str:
                if link.__contains__('http'):
                    index += 1
                    print('\n'+ str(index) , '. ', link ) # this will create numbering e.g; 1. https://www.google.com   2. https://www.facebook.com 
                    
                    try:
                        p.start_search(link)
                        posturl, r, presence = p.find_inputs() 
                        print( link, '\t', posturl, '\t', r, '\t', presence)
                        p.write_text(link, posturl, r, presence)
                    except Exception:
                        pass
        return link, posturl, r, presence

        
def get_urls():
    df = pd.read_excel('xssdata.xlsx')
    links = df['web']
    urls = []
    for link in links:   
        with open('links.txt','a') as f:
            f.write(core_url(link) + '\n')

# This function extracts the base of a link e.g. http://www.fao.org/home/en/ has core url: ".fao.org"
def core_url(link):
        exp = re.compile(r'https?:\/\/[\w]+?\.?\-?[\w]+\.[\.\w]+')
        core = exp.findall(link)
        # print('Core Url ', core)
        # self.complete_link = core[0]
        print(core[0])
        return core[0]


if __name__ == "__main__":
    p = post_links()
    #           website Link               Response,  Meaning,         Terms: NP = no post forms,  NFA = no form action
    # link = 'https://www.engadget.com/'    # 403, forbidden by server
    # link = 'https://www.lampsplus.com/'   # 411 , content length not given
    # link = 'https://www.husqvarna.com/'   #  200
    # link = 'http://www.beistle.com'       # 200
    # link = 'https://www.geappliances.com/'  # NP
    # link = 'https://www.nobleworkscards.com' # 200
    # link = 'https://alicescottage.com'     # NP
    
    link = 'https://www.discountpartysupplies.com/' # 200
    link = 'https://www.asapawards.com/'            # NP
    link = 'https://www.earthsunmoon.com/'  # 200
    link = 'https://www.ethanallen.com/'    # NP
    link = 'https://www.frigidaire.com'     # NP
    link = 'https://www.swarovski.com'      # NP
    link = 'https://www.graphics3inc.com/'  # NP
    link = 'https://www.frigidaire.com'     # NP
    link = 'https://calspas.com'            # NP
    
    link = 'http://www.fao.org/home/en/'    # NP
    link = 'https://www.usda.gov/'  
    link = 'https://scau.edu.cn/'           # 200
    link = 'https://cgiar.org/'
    link = 'https://www.cirad.fr/'
    link = 'http://uaf.edu.pk/'             # 200
    link = 'https://ucanr.edu/'     
    link = 'https://www.cabdirect.org/'     # 200
    link = 'https://www.nrcs.usda.gov/wps/portal/nrcs/site/national/home/'  #200
    link = 'https://www.cabi.org/'
    link = 'https://cce.cornell.edu/'       #200
    link = 'https://www.arborday.org/'
    link = 'https://extension.psu.edu/'
    link = 'https://www.honey.com/'
    link = 'https://www.ars.usda.gov/'      #200
    link = 'https://www.iita.org/'
    link = 'https://www.bdiusa.com'            # 411, Content Length Not Provided
    # link = 'https://www.oscardo.com'      # 400, Need to evaluate it 
    # link = 'https://elegantbaby.com'      # 400, Nedd more knowledge
    # Email login, of course I can't login bcoz I have to be registerd.
    # link = 'https://login.createsend.com/l/9A8E73400EDACAB4/5C5FF3BBE2CD94CE?ReturnUrl=%2F' 
    link = 'https://www.rustyzipper.com/'
    # link = 'https://www.raremaps.com/'

    # print(link)
    # p.start_search(link)
    # posturl, r, presence = p.find_inputs()
    # print( link, '\t', posturl, '\t', r, '\t', presence)
    # p.write_text(link, posturl, r, presence)

    with open('data.txt', 'w') as f:    f.write('')

    links = p.read_excel()
    p.collect_data(links)

#...