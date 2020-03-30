
from WebRequest import web_request
from WriteTextFile import write_text_file
from RegularExpression import regular_expression
from FindContexts import find_contexts
from GenerateFormUrls import generate_form_urls_with_payloads
from ContextEncoding import context_encoding
from AttackMethodology import attack_methodology

class analyze_attack:
    payload = '"' + "xyz'yxz</zxy"

    def get_source(self,url):
        Web = web_request(url,'GET')
        source = Web.get_source()
        return source

    def remove_duplicate_get_urls(self,get_urls):
        unique_get_urls = [] 
        # print('Removing Duplicates...')
        for x in get_urls:
            # Removing Duplicates
            if x not in unique_get_urls: unique_get_urls.append(x)  
        return unique_get_urls

    def collect_data(self,links):
        Search = generate_form_urls_with_payloads()
        get_urls = []    # it is the list in which GET <form> links are added / concatenated
        links_count = 0
        
        # we have 2 links
        for link in links:  #links contains all the references/links
            links_count += 1
            print( '\n[', links_count , '/',  len(links), '] => ', link, end="")
            if not link == [] and link.__contains__('http'):   
                # generates links/urls from every <form ... method="get">. 
                # We receive a list of links/urls. 
                get_urls = Search.start_search(link) 
            else: continue
            unique_get_urls = self.remove_duplicate_get_urls(get_urls)
            print('\nUnique GET URLs:[',len(unique_get_urls), ']\n', unique_get_urls)
            self.collect_response_data(link, unique_get_urls)

    def collect_response_data(self,link, unique_get_urls): # adds payload in GET params..?
        attack_urls = []
        count = 0

        # Single Text File Containing Both GET and POST Form Response.
        Text = write_text_file(link, self.payload)
        # print( 'Unique GET URLs [', len(unique_get_urls) , ']\n', unique_get_urls ,'\n' )

        # Collecting Context Data of  <GET Forms>
        for u in unique_get_urls:
            count+=1
            if u: url = u   # if url is not Empty then Attach the Payload
            else: continue
            if url.__contains__('http'):    # Checking for a Valid Url
                print('[', count , '/', len(unique_get_urls), ']', 'Checking Encoding =>',  url )
                source = self.get_source(url) # Retrieving source code of the webpage
                # Fucntion Call
                self.record_data(url,source,Text)

    # ----- Finding Contexts, selecting attack-Methodology and attack-payloads
    def record_data(self,url,source,Text):
        Find = find_contexts()
        # Finding All Contexts
        attrs, htmls, scripts, urls, same_attrs, same_htmls, same_scripts, same_urls = Find.find_context(url, self.payload, str(source) )
        # Writing Contexts to Text File
        Text.write_contexts(url, attrs, htmls, scripts, urls, same_attrs, same_htmls, same_scripts, same_urls)
        # The function { encoding_analyzer() } returns True for the encoding or escaping of special chars and False otherwise.
        Text.write_encoding( None, '','','','','')
        # Cotext Encoding and Attack Methodology for each Context
        self.check_encoding_and_attack( url, Text, 'ATTR', attrs)
        self.check_encoding_and_attack( url, Text, 'HTML', htmls)
        self.check_encoding_and_attack( url, Text, 'SCRIPT', scripts)
        self.check_encoding_and_attack( url, Text, 'URL', urls)

    def check_encoding_and_attack(self, url,Text, context_name, context_data):
        CE = context_encoding()
        presence, double_quotes, single_quotes, lessthan_sign, forward_slash = CE.encoding_analyzer(context_data)
        if context_name == 'URL' or context_name == 'HTML' or context_name == 'ATTR':
            print_presence = str(presence) + '  '
        else:   
            print_presence = str(presence)
        
        print('Special Chars = Context Presence   \"\t \'\t<\t/')
        print(context_name,'Encoding=\t', print_presence, '\t   ', double_quotes, single_quotes, lessthan_sign, forward_slash )
        
        Text.write_encoding(context_name, presence, double_quotes, single_quotes, lessthan_sign, forward_slash)
        self.try_attacks(url, context_name, presence, double_quotes, single_quotes, lessthan_sign, forward_slash)

    def try_attacks(self, url, Context, presence, double_quotes, single_quotes, lessthan_sign, forward_slash):
        AM = attack_methodology()
        pay = self.payload
        attack_payloads = []
        tag, attack_payloads = AM.get_attack_payload(Context, presence, double_quotes, single_quotes, lessthan_sign, forward_slash )
        print('Attack Payloads: ', attack_payloads)
        
        if tag:
            for attack in attack_payloads:
                url = url.replace(pay, attack)
                pay = attack
                print('\n', Context, 'Attack Url: ', url)
                data = self.get_source(url)
                if( str(data).__contains__(attack)):
                    print('\n\n=> ATTACK SUCCESSFUL with Payload: ', attack)
                    # print('=>The Automated Tool Assumes that there is a potential XSS Present in the Website\n')
                    RegExp = regular_expression(data)
                    RegExp.set_payload(attack)
                    print('Detection of Payload:\n', RegExp.cotext_attack(Context) , '\n\n')
                    # input('Press Enter To Proceed.. ')
                else:
                    print('\n\n ______ UnSuccessful with payload: ', attack, '\n\n')
        