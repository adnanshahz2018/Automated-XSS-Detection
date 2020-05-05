
# PLEASE CHECK ALL TYPES OF ENCODINGS. DONE 
# Addition of unicode inline javascript encoding...e.g: \u0022. " DONE 

import re
from WriteTextFile import write_text_file

class context_encoding:
    double_quotes = single_quotes = lessthan_sign = forwardslash = presence = False
    Text = None

    def __init__(self, Text):
        self.Text = Text
    def display(self,context):
        for value in context:   print(value)
    
# Function / Class Name can also be "Check_Mitigation()" 
    def set_write_text_object(self, Text):
        self.Text = Text

    def initialzie_context_encoding_variables(self):
        self.double_quotes = self.single_quotes = self.lessthan_sign = self.forwardslash = self.presence = False

    def encoding_analyzer(self, name, context):  # You Can ADD another Argument name to Specify the Context Name
        self.initialzie_context_encoding_variables()

        # for context in contexts:
        self.presence = True
        context = str(context)  # &#x27; for " ..??
        if( context.__contains__('&quot;') or context.__contains__('%22') or context.__contains__('\\'+'"') or
            context.__contains__('&#34;') or context.__contains__("\\" + "u0022") or context.__contains__('%2522')):
            self.double_quotes = True 
        else: 
            # print('check filter Double quotes')
            self.double_quotes = self.filtering_analyzer('double',name,context) 

        if( context.__contains__('%27') or context.__contains__('&#39;') or context.__contains__('&#039;') or
            context.__contains__("\\" + "'") or context.__contains__("\\" + "u0027") or context.__contains__('%2527') ):
            self.single_quotes = True  
        else: 
            # print('check filter Single quotes')
            self.single_quotes = self.filtering_analyzer('single',name,context)

        if( context.__contains__('&lt;') or context.__contains__('%3C') or 
            context.__contains__('%2'+'f') ):
            self.lessthan_sign = True 
        else: 
            self.lessthan_sign = self.filtering_analyzer('less_than',name,context)
        
        if( context.__contains__('%2'+'F') or context.__contains__("\\" + "/") or
            context.__contains__('&#47;')  ):
            self.forwardslash = True 
        else:
            self.forwardslash = self.filtering_analyzer('forwardslash', name, context)
        
        return self.presence, self.double_quotes, self.single_quotes, self.lessthan_sign, self.forwardslash


    def filtering_analyzer(self,special_char, name, context):
        if name == 'ATTR' and special_char == 'double' : 
            return self.double(context) or self.attr_single_quotes_outside(context,'xyz')
        if name == 'ATTR' and special_char == 'single' : 
            return self.single(context) or self.attr_double_quotes_outside(context,'yxz')
        if name == 'ATTR' and special_char == 'less_than' : 
            return self.less_than(context)
        
        if name == 'HTML' and special_char == 'double' : 
            return self.double(context)
        if name == 'HTML' and special_char == 'single' : 
            return self.single(context)
        if name == 'HTML' and special_char == 'less_than' :
            return self.less_than(context) 

        if name == 'SCRIPT' and special_char == 'double' : 
            return self.double(context) or self.script_single_quotes_outside(context,'xyz') 
        if name == 'SCRIPT' and special_char == 'single' : 
            return self.single(context) or self.script_double_quotes_outside(context,'yxz')
        if name == 'SCRIPT' and special_char == 'less_than': 
            return self.less_than(context)
        
        if name == 'URL' and special_char == 'double' : 
            return self.double(context)
        if name == 'URL' and special_char == 'single' : 
            return self.single(context)
        if name == 'URL' and special_char == 'less_than' : 
            return self.less_than(context)
        
        if special_char == 'forwardslash' :
            return self.check_forwardslash(context)
        
        return False
   

    def double(self,context): 
        pattern1 = re.compile(r'\"[\s]*xyz')
        value = pattern1.findall(context)
        if value:        
            # print('\nFiltering Value = ',value)
            return False    # No Filtering 

        return True     # Filtering is PRESENT

    def single(self, context):
        pattern1 = re.compile(r"\'[\s]*yxz")
        value = pattern1.findall(context)
        if value:        
            # print('\nFiltering Value = ',value)
            return False    # No Filtering 

        return True     # Filtering is PRESENT
    
    def less_than(self, context): 
        pattern1 = re.compile(r'\<[\s]*zxy')
        value = pattern1.findall(context)
        if value:        
            # print('\nhtml Filtering Value = ',value)
            return False    # No Filtering 
        
        return True     # Filtering is PRESENT
  
    def check_forwardslash(self, context):
        pattern1 = re.compile(r"\/\s*uvw")
        value = pattern1.findall(context)
        if value:        
            # print('\nFiltering Value = ',value)
            return False    # No Filtering 
        return True     # Filtering is PRESENT


    def attr_single_quotes_outside(self,context,attack):
        pattern = re.compile(r'[=]\s?\'[@\*!~|$_,}+*\\#*\"{*\s^*\'?\[\]*(*)*\/*.*\w*=:*&*;*\-*%*\d*]*'+ re.escape(attack))
        value = pattern.findall(str(context))
        if value:    
            self.Text.write_directly("\tAttr-Double\tEncapsulated With Single Quotes: Can't Break the Context\n")
            return True
        return False

    def attr_double_quotes_outside(self,context,attack):
        pattern = re.compile(r'[=]\s?\"[@\*!~|$_,}+\"*\\#*{*\s^*?\[\]\'*(*)*\/*.*\w*=*:&*;*\-*%*\d*]*'+ re.escape(attack))
        value = pattern.findall(str(context))
        if value:    
            self.Text.write_directly("\tAttr-Single\tEncapsulated With Double Quotes: Can't Break the Context\n")
            return True
        return False

    def script_single_quotes_outside(self,context,attack):
        pattern = re.compile(r'[=:]\s?\'[@\*!~|$_,}+:*\\#\'*{*\s^*?=\[\]*(*)*\/*.*\w*&*;*\-*%*\d*]*'+ re.escape(attack))
        value = pattern.findall(str(context))
        if value:    
            self.Text.write_directly("\tScript-Double\tEncapsulated With Single Quotes: Can't Break the Context\n")
            return True
        return False

    def script_double_quotes_outside(self,context,attack):
        pattern = re.compile(r'[=]\s?\"[@\*!~|$_,}+*\\#*\"{*\s^*?=\[\]\'*(*)*\/*.*\w*&*;*\-*%*\d*]*' + re.escape(attack))
        pattern1 = re.compile(r'[,]\s?\"[@\*!~|$_,}+*\\#*\"{*\s^*?=\[\]\'*(*)*\/*.*\w*&*;*\-*%*\d*]*'+ re.escape(attack))
        pattern2 = re.compile(r'[:]\s?\"[@\*!~|$_,}+*\\#*\"{*\s^*?=\[\]\'*(*)*\/*.*\w*&*;*\-*%*\d*]*'+ re.escape(attack))

        value = pattern.findall(str(context))
        if value:    
            self.Text.write_directly("\tScript-Single\tEncapsulated With Double Quotes: Can't Break the Context\n")
            return True
        value = pattern1.findall(str(context))
        if value:    
            self.Text.write_directly("\tScript-Single\tEncapsulated With Double Quotes: Can't Break the Context\n")
            return True
        value = pattern2.findall(str(context))
        if value:    
            self.Text.write_directly("\tScript-Single\tEncapsulated With Double Quotes: Can't Break the Context\n")
            return True

        return False


if __name__ == "__main__":
    CE = context_encoding()
    CE.html_less_than('input id="search" type="search" name="q" value="u"xyz< zxy')
    print( '{Context_Encoding}')
