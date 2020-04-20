
import re
import os 


class write_text_file:
    url = ''
    # folder = 'drive/My Drive/650HomePages/'
    # folder = 'TuningData/'
    filename = ''
    payload = ''

    def __init__(self,base,url,payload):
        self.folder = base + '/'
        self.url = url
        # self.folder = self.core_url(url) + '/'
        self.payload = payload
        self.createfile()

    def core_url(self,link):
        exp = re.compile('\.?\-?[\w]+\.[\.\w]+')
        core = exp.findall(link)
        print('Core Url ', core)
        return core[0]

    def createfile(self):
        filename = self.get_filename()
        path = self.folder + filename + '.txt'
        textfile = open(path, "w")
        textfile.write(self.url + '\n')
        textfile.close()

    def get_filename(self):
        f = self.url
        f = f.replace("/", "_")
        f = f.replace("\\", "_")
        f = f.replace(":", "_")
        f = f.replace(" ", "")
        f = f.replace("\\n", "")
        f = f.replace('%', '_')
        
        f = f.replace("*", "_")
        f = f.replace("<", "_")
        f = f.replace(">", "_")
        f = f.replace("&", "_")
        
        f = f.replace("\"", "_")
        f = f.replace("|", "_")
        f = f.replace("?", "_")
        f = f.replace("+", "_")

        f = f.replace('\n','')
        f = f.replace('\r', '')
        f = f.replace('\t', '')
        
        f = f.rstrip("\t")
        f = f.rstrip("\n")
        f = f.rstrip("\r")
        f = f.rstrip("\r\n")

        if len(f) > 150: f = f[:150]
        # print('filename => ', f)
        return f

    def write_contexts(self, url, attrs, htmls, scripts, urls, same_attrs, same_htmls, same_scripts, same_urls):
        breakline = "\n----------------------------------------------------------------------------------\n"
        filename = self.get_filename()
        path = self.folder + filename + '.txt'
        textfile = open(path, "a", encoding='utf-8')

        print( "\nWriting Data in => ", filename + '.txt' , '\n' )
        textfile.write('_______________________________________________________________________________________________________\n')
        textfile.write(url + "\n")
        
        textfile.write(breakline + 'Attribute Context: [' + str( len(attrs) ) + ']\n')
        for a in attrs:
            textfile.write(str(a) + "\n")

        textfile.write(breakline + 'HTML Context: [' + str( len(htmls) ) + ']\n')
        for h in htmls:
            textfile.write(str(h) + "\n")

        textfile.write(breakline + 'Script Context: [' + str( len(scripts) ) + ']\n')
        for s in scripts:
            textfile.write(str(s) + "\n")

        textfile.write(breakline + 'URI Context: [' + str( len(urls) ) + ']\n')
        for u in urls:
            textfile.write(str(u) + "\n")

    # NOT WRITING SAME CONTEXT DATA
        # textfile.write(breakline + 'Same Attr : [' + str( len(same_attrs) ) + ']\n')
        # for s in same_attrs:
        #     textfile.write(str(s) + "\n")
        
        # textfile.write(breakline + 'Same HTML : [' + str( len(same_htmls) ) + ']\n')
        # for s in same_htmls:
        #     textfile.write(str(s) + "\n")

        # textfile.write(breakline + 'Same Script : [' + str( len(same_scripts) ) + ']\n')
        # for s in same_scripts:
        #     textfile.write(str(s) + "\n")
        
        # textfile.write(breakline + 'Same URI : [' + str( len(same_urls) ) + ']\n')
        # for s in same_urls:
        #     textfile.write(str(s) + "\n")
    #
        textfile.write(breakline + '\n')
        textfile.close()
#    
    def write_response(self, filename, data):
        path = '' +  filename + '.txt'
        textfile = open(path, "w+")
        # print(data)
        textfile.write(str(data))
        textfile.close()

    def write_links(self, filename, links):
        path = '' +  filename + '.txt'
        textfile = open(path, "w+")
        for data in links:  textfile.write(str(data) + '\n')
        textfile.close()
    
    def write_postforms(self, posturl, r, presence):
        breakline = "\n__________________________________________________________________________________"
        print('\n Writing Post Form Data to TEXT_FILE\n')
        filename = self.get_filename()
        path = self.folder + filename + '.txt'
        textfile = open(path, "a")
        textfile.write(breakline )
        textfile.write('\nPost Forms' + breakline + '\n')
        for i in range( len(posturl) ):
            textfile.write( str(posturl[i]) + '\t' + str(r[i]) + '\t' + str(presence[i]) + '\n')    
        textfile.close()

    def write_directly(self,data):
        filename = self.get_filename()
        path = self.folder + filename + '.txt'
        textfile = open(path, "a")
        try:
            textfile.write( data )
        except:
            textfile.write( str(data.encode(encoding='UTF-8',errors='strict')) )
        textfile.close()
        
    def write_encoding(self, Context, presence, double_quotes, single_quotes, lessthan_sign, forward_slash):
        filename = self.get_filename()
        path = self.folder + filename + '.txt'
        textfile = open(path, "a")
        if Context is None: 
            textfile.write('\n\n\t\t \t\tENCODING SUMMARY \n\t   \t  Presence\t\t"' + "\t\t'" + '\t\t<' + "\t\t( \n")
            return
        textfile.write('Mitigation        "' + "\t'" + '\t<' + "\t( \n")
        textfile.write(Context +':\t\t' + str(double_quotes) +'\t')
        textfile.write( str(single_quotes) +'\t'+ str(lessthan_sign) +'\t'+ str(forward_slash) + '\n' )
        textfile.close()


if __name__ == "__main__":
    print('{WriteTextFile}')

