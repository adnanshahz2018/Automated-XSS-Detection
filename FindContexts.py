
import os 
from RegularExpression import regular_expression
from WriteTextFile import write_text_file
# from WriteExcelFile import write_excel_file

class find_contexts:
    R = None 
    url = ''
    payload = ''

    def find_context(self, url, payload, pagesource):    
        R = regular_expression(pagesource)

        attrs   = R.RegExpAttribute()
        htmls   = R.RegExpHtml()
        scripts = R.RegExpScript()
        urls    = R.RegExpURI()

        same_attrs    = R.RegExpSameAttribute()
        same_htmls    = R.RegExpSameHtml()
        same_scripts  = R.RegExpSameScript()
        same_urls     = R.RegExpSameURI()
        
        # Display the Context Values on the Console 
        self.display(attrs, htmls, scripts, urls, same_attrs, same_htmls, same_scripts, same_urls)

        # W = write_text_file(url, payload)
        # W.write_contexts(attrs, htmls, scripts, urls, same_attrs, same_htmls, same_scripts, same_urls)

        # E = write_excel_file(self.url,'XssDataSheet.xlsx', self.payload)
        # E.write_contexts(attrs, htmls, scripts, urls, same_attrs , same_htmls, same_scripts, same_urls)
        return attrs, htmls, scripts, urls, same_attrs, same_htmls, same_scripts, same_urls
    

    def display(self, attrs, htmls, scripts, urls, same_attrs, same_htmls, same_scripts, same_urls):
        print('-------------------------------------------------------------------------------------------------------\n')
        
        print('Attribute Context [' , len(attrs)        ,  ']\n' , attrs)
        print('HTML Context ['      , len(htmls)        ,  ']\n' , htmls)
        print('Script Context ['    , len(scripts)      ,  ']\n' , scripts)
        print('URI Context ['       , len(urls)         ,  ']\n' , urls)
        
        print('SAME Attribute ['    , len(same_attrs)   ,  ']\n' , same_attrs)
        print('SAME HTML ['         , len(same_htmls)   ,  ']\n' , same_htmls)
        print('SAME Script ['       , len(same_scripts) ,  ']\n' , same_scripts)
        print('SAME URI ['          , len(same_urls)    ,  ']\n' , same_urls)
        
        print('--------------------------------------------------------------------------------------------------------\n')
        

if __name__ == "__main__":
    print('{FindContext}')


