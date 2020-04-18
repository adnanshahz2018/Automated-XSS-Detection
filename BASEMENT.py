

"""             
_____________________________________________________________________________________________________________________
==>>    UPDATES Created - DONE

1. Extract Unique GET Params.
2. If 2 forms have same 2 GET Params, then 4 GET URLs will be generated: DONE: later unique GET URLS are extracted
3. Payload = (uvw"xyz'yxz</zxy. DONE
4. Check encdoing separarately for each value of a context.     DONE
    Issue: one value has encoding and others may not have..!!
5. Base Url for all websites. Resolved THE ISSUE of ifu-institut.at and drudgereportarchives.com
6. Now We Store the SUCCESSFUL ATTACK_URL, Context_name and Detection in the EXCEL FIle.. 

_____________________________________________________________________________________________________________________
==>>    UPDATES REQUIRED 

1. How to Create a Folder through program
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

ISSUE NO. 3:
1. Attack Methodology for URL: Does it need Encoding Analysis..?

ISSUE NO. 4:
1. On https://www.crane.com
i.  <a href="/stationery/featured-products">Featured Products</a> 
ii. <a href="/stationery/best-sellers">Best Sellers</a>
2. The href value is merged with base Url to produce a complete link. 
 https://www.crane.com + href
3. So what's the update, are we going to do the same..
        YEAH I THINK WE SHOULD.. ====>> CommoN SensE :)
 
ISSUE NO. 5:
1. https://www.moosejaw.com/content/ann-arbor-shop
2. could not detect all the get params, though webpage has One GET Form with 14 get params..!!

ISSUE 6:
https://www.rei.com/
GET Input NOT captured . 
has one get param 'q'

ISSUE 7:
Check https://www.stevespanglerscience.com
 Look for 2 or more script contexts... with updated RegExp

"""

