

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

2. Try the Vertical format of the EXCEL FILE.

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
[ So Tool-Created URL was SAME as Manual Finding fo the URL]

ISSUE 11:   [ Resolved ]
Unique GET URLs:
    a. If [2] forms have same [2] GET Params, then [4] GET URLs will be generated and then [2] unique GET URLS are extracted
    b. BUT if they have DIFFERENT FORM ACTIONS, then there will be 4 UNIQUE GET URLS.



"""

