
# PLEASE CHECK ALL TYPES OF ENCODINGS. DONE 
# Added unicode inline javascript encoding...e.g: \u0022. " DONE 

class context_encoding:
    double_quotes = single_quotes = lessthan_sign = forward_slash = presence = False

    def display(self,context):
        for value in context:   print(value)
    
# Function / Class Name can also be "Check_Mitigation()" 

    def initialzie_context_encoding_variables(self):
        self.double_quotes = self.single_quotes = self.lessthan_sign = self.forward_slash = self.presence = False


    def encoding_analyzer(self, contexts):  # You Can ADD another Argument name to Specify the Context Name
        self.initialzie_context_encoding_variables()
        
        for context in contexts:
            self.presence = True
            context = str(context)
            if( context.__contains__('&quot;') or context.__contains__('%22') or context.__contains__('\\'+'"') or
                context.__contains__('&#34;') or context.__contains__("\\" + "u0022") ):
                self.double_quotes = True  
           
            if( context.__contains__('%27') or context.__contains__('&#39;') or context.__contains__('&#039;') or
                context.__contains__("\\" + "'") or context.__contains__("\\" + "u0027") ):
                self.single_quotes = True  

            if( context.__contains__('&lt;') or context.__contains__('%3C') or 
                context.__contains__('%2'+'f') ):
                self.lessthan_sign = True 

        return self.presence, self.double_quotes, self.single_quotes, self.lessthan_sign, self.forward_slash


if __name__ == "__main__":
    print( '{Context_Encoding}')
    pass
