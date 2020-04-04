
import _osx_support

class BASEMENT:

    """ File: GenerateFormUrls , class: generate_form_urls_with_payloads """

    def combine_input_tags(self,input_tags):
        combined_get_params = ''
        for p in input_tags:   
            if p.get('name') != None: name = p.get('name') 
            else:   name = ''
            if p.get('value') != None: value = p.get('value')
            else:   value = ''
            combined_get_params = combined_get_params + name + '=' + value  + '&'

        # print( 'Complete Form & Input parameters \n', combined_get_params)
        return combined_get_params

    def get_response(self, url):
        headers = {}
        headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686)"
        # Using Requests Library to Send a Post Request
        send = requests.Session()
        resp = send.get(url, headers=headers)
        # if not str(resp.text).__contains__('xyz'): return
        # print('URL: ', url, '\t   Resp.length: ', len(str(resp.text)))
        return resp.text

    def get_form_urls(self,forms):
        return_link = []
        if forms:
            # print(forms)
            inputs = forms.find_all('input', attrs = {'type' : 'hidden'})       # All inputs of type hidden
            if inputs == None: inputs = ''
            # print('inputs = ' , inputs)
            query_name = ''
            query = forms.find('input', attrs = {'type' : 'text'})
            if query == None:   query = forms.find('input', attrs = {'type' : 'search'})
            if query == None:   query = forms.find('input', attrs = {'value' : ''}) 
            
            if query == None or query == '':   query_name = None  
            else: query_name = query.get('name')
            if query_name == None:  return False, ''
            combined_get_params = self.combine_input_tags(inputs) + query_name + '=' 
        else: 
            print( 'GET Form Not Found')
            return False, ''

        form_action = forms.get('action')
        if form_action == None: 
            print('Form action is NOT FOUND')
            return False, ''
        elif len(self.complete_link) > 0:   
            # print('form action: ' , form_action)
            self.make_link(form_action)
            
        mark = '?'
        if self.complete_link.__contains__('?'): mark = '&' 
        get_link = self.complete_link + mark + combined_get_params
        # print( 'form link: \n', self.complete_link + mark + combined_get_params )
        return_link.append( get_link )
        return True, return_link

#-------------------------------------------------------------------------------------------------------------
#  End of Class: BASEMENT
#-------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    print('{BASEMENT}')


"""             UPDATES REQUIRED

1. Extract Unique GET Params.
2. If 2 forms have same 2 GET Params, then 4 GET URLs will be generated: DONE: later unique GET URLS are extracted
3. Payload = u"xyz('yxz</zxy

"""


"""     ==>>    UPDATES SUGGESTED 

"""