
import re
import os
import requests
from requests import Request, Session
from bs4 import BeautifulSoup
from WebRequest import web_request
from FindContexts import find_contexts


class generate_form_urls_with_payloads:
    payload = '(uvw"' + "xyz'yxz</zxy"
    complete_link = original_url = ''
    formvalues = {}
    get_params = []

    def start_search(self,link):
        complete_links = []
        self.core_url(link)
        web = web_request(link,'get')
        s1 = web.open_request()
        s2 = web.openurl()
        if len(s1) > len(s2): source = s1
        else: source = s2

        # print(link)
        self.get_params = []
        complete_links = self.analyse_forms(source, 'get') 
        # print('\nForm Links [', len(complete_links), '] \n',  complete_links)

        params = []
        # Removing Duplicates
        for x in self.get_params:   
            if x not in params: params.append(x) 

        return params, complete_links
    
    def core_url(self,link):
        exp = re.compile('https?:\/\/[\w]+?\.?\-?[\w]+\.[\.\w]+')
        core = exp.findall(link)
        # print('Core Url ', core)
        self.complete_link = core[0]
        self.original_url = core[0]
        return core

    def analyse_forms(self, source, method):
        inputs = query = ''
        forms = []
        links = []
        soup = BeautifulSoup(source, features="lxml")

        forms = soup.find_all('form', attrs = {'method' : method.upper() })
        forms = forms + soup.find_all('form', attrs = {'method' : method.lower() })
        # print('\n Forms \n', forms)
        for form in forms:
            flag, form_links = self.check_get_urls(form)
            if flag:    links += form_links  
        return links
        

    def check_get_urls(self, form):
        if not form: return False, ['']
        fields = form.find_all('input')
        if not fields: return False, ['No InputFields']

        find = find_contexts()
        links = []
        formdata = {}
        
        for field in fields:
            if(field.get('type') == 'hidden' or field.get('type') == 'text' or field.get('type') == 'Text' or 
            field.get('type') == 'TEXT' or field.get('type') == 'search' or field.get('type') == 'Search' or 
            field.get('type') == 'SEARCH' ):    
                self.get_params.append(field.get('name'))
                formdata[field.get('name')] = field.get('value')
        
        if not form.get('action'): return False, ['No FormAction']
        # print('form-action: ' , form.get('action'))
        url = self.make_link(form.get('action'))
        self.formvalues = formdata.copy()
        num_inputs = len(formdata)
        # print('\t\t' + 'Form-Inputs:', num_inputs)

        for f in formdata:
            formdata[f] = self.payload
            data = self.merge(form.get('action'), formdata)
            # print('URL: ', url)
            get_url = url + data
            links.append(get_url)
            formdata = self.formvalues.copy()
        return True, links

    def merge(self, action, formdata):
        data = '?'
        # print(formdata)
        if action.__contains__('?'):    data = '&'
        for f in formdata:  
            if formdata[f]: data += f + '=' + formdata[f] + '&' 
            else:   data += f + '=' + '' + '&'
        # print('form_data = ', data[:-1])
        form_data = data[:-1]
        return form_data
    
    def make_link(self,form_action):
        if not len(form_action) > 0 : return 
        self.complete_link = self.original_url 
        if not len(self.complete_link) > 0: return

        if      self.if_complete_link(form_action):  self.complete_link = form_action
        elif    self.complete_link[-1] == '/' and form_action[0] == '/': self.complete_link = self.complete_link[:-1] + form_action
        elif   self.complete_link[-1] != '/' and form_action[0] == '/': self.complete_link = self.complete_link + form_action
        elif   self.complete_link[-1] != '/' and form_action[0] != '/': self.complete_link = self.complete_link + '/' + form_action
        else:   self.complete_link = self.complete_link + form_action
        
        if self.complete_link[0] == '/' and self.complete_link[1] == '/': self.complete_link = 'https:' + self.complete_link
        return self.complete_link
    
    def if_complete_link(self,action):
        if(action.__contains__('https') or action.__contains__('www') ):
            return True
        return False 


if __name__ == '__main__':
    links = list()

    # link = 'https://www.wayfair.com'
    # link = 'https://www.lowes.com/'
    # link = 'https://www.husqvarna.com/'
    # link = 'http://www.beistle.com'
    # link = 'https://www.geappliances.com/'
    # link = 'https://www.nobleworkscards.com'
    # link = 'https://alicescottage.com'

#   ---------------------------- Successfully Done -------------------------------- 

    # link = 'https://www.discountpartysupplies.com/'
    # link = 'https://www.asapawards.com/'
    # link = 'https://www.earthsunmoon.com/'
    # link = 'https://www.ethanallen.com/'
    # link = 'https://www.frigidaire.com'
    # link = 'https://www.swarovski.com'
    # link = 'https://www.oscardo.com'
    # link = 'https://elegantbaby.com'
    # link = 'https://www.graphics3inc.com/'
    # link = 'https://www.bdiusa.com'
    # link = 'https://www.frigidaire.com'
    # link = 'https://calspas.com'                                                                                                  

    # link = 'https://www.britannica.com/search?query='
    # link = 'https://www.ediblearrangements.com/fruit-arrangements?SearchText="xyz%27yxz&lt;/zxy'
    # link = 'https://huel.com/pages/search-results?q=%22xyz'
    link = 'https://www.britannica.com/'                #Done Well
    # link = 'https://www.harryanddavid.com/'           # Done well 
    # link = 'https://www.nearlynatural.com/'           # Done well
    # # link = 'https://www.cat.com/en_US'              # Done well
    # link = 'https://www.deere.com/en/'                # Done well
    link = 'https://leica-geosystems.com/'            # No <form with method='get'
    # link = 'https://www.ruralking.com/'               # Done well 
    # link = 'https://www.burpee.com/'                    # Done Well
    # link = 'https://www.equinenow.com/'                 # Failure: action="#"
    # link = 'https://everythingaustralian.com.au/'       # Done well
    # link = 'https://www.rods.com/'                      # Done well
    # link = 'https://www.tenthousandvillages.com/'       # Done well
    # link = 'https://www.dollsofindia.com/'              # Done well
    # link = 'https://africaimports.com/'                 # Done well
    link = 'https://www.serrv.org/'                     # No <form with method='get'
    # link = 'https://madeinoregon.com/'                  # Done Well 
    # link = 'https://www.crazycrow.com/site/'                #Done Well
    # link = 'https://www.shamansmarket.com/'                 # No <form with method='get'
    # link = 'https://www.scotweb.co.uk/'                 # No <form with method='get'
    # link = 'https://www.countrystorecatalog.com/'       # No <form with method='get', 228 hidden inputs in post form. Failed to detect form in source 
    # link = 'https://www.bangalla.com/'                  # Done well
    # link = 'https://tulumba.com/'               # No <form with method='get', blocks payloads and goes back to default page 
    # link = 'https://www.abcstores.com/'             #Done Well
    # link = 'https://www.yelp.com/'               # A sencond Input Field was to be selected by user, so it was Not defined Already {Location}
    # link = 'https://www.gsmarena.com/'              #Done well
    # link = 'https://www.theverge.com/'               #Done well
    # link = 'https://www.digitaltrends.com/'         # Does Not work with payload having special chars { ', ", <, /}, No post forms
    # link = 'https://www.engadget.com/'              # No <form with method='get', has post and adding payload works, gives results

    # links.append( 'https://www.yelp.com/')                # A sencond Input Field was to be selected by user, so it was Not defined Already {Location}
    # links.append( 'https://www.gsmarena.com/'  )             #Done well
    # links.append( 'https://www.theverge.com/'   )            #Done well
    # links.append( 'https://www.digitaltrends.com/')         # Does Not work with payload having special chars { ', ", <, /}
    # links.append( 'https://www.engadget.com/'      )        # No <form with method='get'

    # links.append( '' )
    # links.append( '' )
    # links.append( '' )
    # links.append( '' )
    # links.append( '' )   

    # links.append( 'https://www.wayfair.com/' )            # Fails to capture the GET Form
    # links.append( 'https://www.lowes.com/' )              # Request Times Out / Fails
    # links.append( 'https://www.uncommongoods.com/' )           # No <form with method='get' 
    # links.append( 'https://www.potterybarn.com/' )        # Fails to Detect get Form
    # links.append( 'https://www.williams-sonoma.com/' )    # Failed with "urllib" and Source Code of "Requests" doesn't have GET Form [failed]
    # link = 'https://www.williams-sonoma.com/'               # Failure

    # link = 'https://www.westelm.com/'           # Source Code downloaded doesn't have GET Form
    # link = 'https://www.dyson.com/en.html'      # Request Times Out
    # link = 'http://acehardware.com/'            # Detects <form with method='get', but there is no input field in it
    # link = 'https://www.surlatable.com/'        # Program worked fine, but website doesn't tolerates special chars {', ", <, /}
    # link = 'https://www.lampsplus.com/'           # No <form with method='get' , has post and we can use isformtrue = true => payload

    # link = 'https://www.containerstore.com/welcome.htm'     # Source Code downloaded doesn't have GET Form

    # link = 'https://www.moma.org/'              # Done Well
    # link = 'https://casper.com/home/'           # No <form with method='get'
    # link = 'https://www.pbteen.com/'            # Failed with "urllib" and Source Code of "Requests" doesn't have GET Form [failed]
    # link = 'https://www.yankeecandle.com/'      # No <form with method='get', No post
    # link = 'https://www.kirklands.com/'         # Done Well
    # link = 'https://www.1000bulbs.com/'         
    # link = 'https://www.ajmadison.com/'         # No <form with method='get' no post
    # link = 'https://www.repairclinic.com/'      # No <form with method='get' No post
    # link = 'https://www.architecturaldepot.com/' # There is a Robot Check , Failed with "urllib" and Source Code of "Requests" doesn't have GET Form  
    # link = 'https://www.roomandboard.com/'       # There is No Atrribute action="" in <form 
    # link = 'https://www.potterybarn.com/' 
    # link = 'https://www.wayfair.com/'            # Failure
    # link = 'https://www.partygameideas.com/'    # Done Well
    # link = 'https://readymadepubquiz.com/'
    # link = 'https://cardsagainsthumanity.com/'
    # link = 'https://www.keh.com/'
    # link = 'https://developers.google.com/chart/infographics/docs/post_requests'
    # link = ''

    print('\n------------------------STARTED---------------------\n')

    # -------------------------Creating the Object-------------------------------
    G = generate_form_urls_with_payloads()
    G.start_search(link)
    

""" 
------------------------------ Any Ideas or Algorithm, Post'em Here -----------

_________________________________________________________________________________

Failures:
1. https://www.yesasia.com/global/search/xyz/0-0-0-q.xyz_bpt.48-en/list.html
2. https://www.novica.com/xyz/s/
3. https://www.fragonard.com/en/search/xyz

_________________________________________________________________________________

"""

