
# PLEASE CHECK ALL TYPES OF ENCODINGS. DONE 
# Addition of unicode inline javascript encoding...e.g: \u0022. " DONE 

import re

class context_encoding:
    double_quotes = single_quotes = lessthan_sign = parantheses = presence = False


    def display(self,context):
        for value in context:   print(value)
    
# Function / Class Name can also be "Check_Mitigation()" 

    def initialzie_context_encoding_variables(self):
        self.double_quotes = self.single_quotes = self.lessthan_sign = self.parantheses = self.presence = False


    def encoding_analyzer(self, name, context):  # You Can ADD another Argument name to Specify the Context Name
        self.initialzie_context_encoding_variables()

        # for context in contexts:
        self.presence = True
        context = str(context)  # &#x27; for " ..??
        if( context.__contains__('&quot;') or context.__contains__('%22') or context.__contains__('\\'+'"') or
            context.__contains__('&#34;') or context.__contains__("\\" + "u0022") ):
            self.double_quotes = True 
        else: 
            self.double_quotes = self.filtering_analyzer('double',name,context) 

        if( context.__contains__('%27') or context.__contains__('&#39;') or context.__contains__('&#039;') or
            context.__contains__("\\" + "'") or context.__contains__("\\" + "u0027") ):
            self.single_quotes = True  
        else: 
            self.single_quotes = self.filtering_analyzer('single',name,context)

        if( context.__contains__('&lt;') or context.__contains__('%3C') or 
            context.__contains__('%2'+'f') ):
            self.lessthan_sign = True 
        else: 
            self.lessthan_sign = self.filtering_analyzer('less_than',name,context)
        
        if( context.__contains__('%28') or context.__contains__('&#40') or
            context.__contains__('&#x28') or context.__contains__("\\" + "u0028") ):
            self.parantheses = True 
        else:
            self.parantheses = self.filtering_analyzer('parantheses', name, context)
        

        return self.presence, self.double_quotes, self.single_quotes, self.lessthan_sign, self.parantheses


    def filtering_analyzer(self,special_char, name, context):
        if name == 'ATTR' and special_char == 'double' : 
            return self.attr_double(context)
        if name == 'ATTR' and special_char == 'single' : 
            return self.attr_single(context)
        
        if name == 'HTML' and special_char == 'less_than' :
            print('HTML CONTEXT ==> ' , name ) 
            return self.html_less_than(context) 
        
        if name == 'SCRIPT' and special_char == 'double' : 
            return self.script_double(context)
        if name == 'SCRIPT' and special_char == 'single' : 
            return self.script_single(context)
        if name == 'SCRIPT' and special_char == 'less_than': 
            return self.script_less_than(context)
        if special_char == 'parantheses' :
            return self.script_parantheses(context)
        
        if name == 'URL' and special_char == 'double' : 
            return self.url_double(context)
        if name == 'URL' and special_char == 'single' : 
            return self.url_single(context)
        if name == 'URL' and special_char == 'less_than' : 
            return self.url_less_than(context)

        return False
    
    def attr_double(self,context): 
        pattern1 = re.compile(r'\"[\s]*xyz')
        # soup = ('<input id="search" type="search" name="q" value="u"xyz' + "'" + 'yxz</zxy" class="input-text required-entry" maxlength="128" placeholder="Search" />')
        value = pattern1.findall(context)
        if value:        
            # print('\nFiltering Value = ',value)
            return False    # No Filtering 

    # check for the attribute value starting from " or ' e.g: content=" or script tag value e.g: 'special_url' : ' u\"xyz'yxz
        return True     # Filtering is PRESENT

    def attr_single(self, context):
        pattern1 = re.compile(r"\'[\s]*yxz")
        value = pattern1.findall(context)
        if value:        
            # print('\nFiltering Value = ',value)
            return False    # No Filtering 

    # check for the attribute value starting from " or ' e.g: content=" or script tag value e.g: 'special_url' : ' u\"xyz'yxz
        return True     # Filtering is PRESENT

    def html_less_than(self, context): 
        pattern1 = re.compile(r'\<[\s]*\/?zxy')
        value = pattern1.findall(context)
        if value:        
            # print('\nhtml Filtering Value = ',value)
            return False    # No Filtering 
        
        return True     # Filtering is PRESENT

    def script_parantheses(self, context):
        pattern1 = re.compile(r"\(\s*uvw")
        value = pattern1.findall(context)
        if value:        
            # print('\nFiltering Value = ',value)
            return False    # No Filtering 

        return True     # Filtering is PRESENT

    def script_double(self, context): 
        pattern1 = re.compile(r'\"[\s]*xyz')
        value = pattern1.findall(context)
        if value:        
            # print('\nFiltering Value = ',value)
            return False    # No Filtering 

    # check for the attribute value starting from " or ' e.g: content=" or script tag value e.g:  'special_url' : ' u\"xyz'yxz
        return True     # Filtering is PRESENT

    def script_single(self, context):
        pattern1 = re.compile(r'\'[\s]*\/?zxy')
        value = pattern1.findall(context)
        if value:        
            # print('\nFiltering Value = ',value)
            return False    # No Filtering 
        
    # check for the attribute value starting from " or ' e.g: content=" or script tag value e.g:  'special_url' : ' u\"xyz'yxz
        return True     # Filtering is PRESENT

    def script_less_than(self, context): 
        pattern1 = re.compile(r'\<[\s]*\/?zxy')
        value = pattern1.findall(context)
        if value:        
            # print('\nFiltering Value = ',value)
            return False    # No Filtering 
        
        return True     # Filtering is PRESENT

    def url_filter_check(self, context): 
        pattern1 = re.compile(r'<[\s]*\/?zxy')
        value = pattern1.findall(context)
        if value:        
            print('\nFiltering Value = ',value)
            return False
        
        return True

    def url_double(self, context):
        pattern1 = re.compile(r'\"[\s]*\/?zxy')
        value = pattern1.findall(context)
        if value:        
            # print('\nFiltering Value = ',value)
            return False    # No Filtering 
        
        return True     # Filtering is PRESENT

    def url_single(self, context):
        pattern1 = re.compile(r'\'[\s]*\/?zxy')
        value = pattern1.findall(context)
        if value:        
            # print('\nFiltering Value = ',value)
            return False    # No Filtering 
        
        return True     # Filtering is PRESENT

    def url_less_than(self, context):
        pattern1 = re.compile(r'\<[\s]*\/?zxy')
        value = pattern1.findall(context)
        if value:        
            # print('\nFiltering Value = ',value)
            return False    # No Filtering 
        
        return True     # Filtering is PRESENT


if __name__ == "__main__":
    CE = context_encoding()
    CE.html_less_than('input id="search" type="search" name="q" value="u"xyz< zxy')
    print( '{Context_Encoding}')
