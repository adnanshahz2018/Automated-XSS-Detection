

"""             
==>>    UPDATES Created - DONE

1. Extract Unique GET Params.
2. If 2 forms have same 2 GET Params, then 4 GET URLs will be generated: DONE: later unique GET URLS are extracted
3. Payload = (uvw"xyz'yxz</zxy. DONE
4. Check encdoing separarately for each value of a context.     DONE
    Issue: one value has encoding and others may not have..!!
5. Base Url for all websites. Resolved THE ISSUE of ifu-institut.at and drudgereportarchives.com

_____________________________________________________________________________________________________________________

==>>    UPDATES REQUIRED 

1. How to Create a Folder through program
2. Try the Vertical format of the EXCEL FILE.
3. we can at least store the SUCCESSFUL ATTACKS URL and Detection in the EXCEL FIle.. 

_____________________________________________________________________________________________________________________

==>>    Program Glitches

1. https://www.piceramic.com
2. OSError: [Errno 22] Invalid argument: "600WebsiteData/.ndt.net/\r\nhttps___www.linkedin.com_shareArticle_mini=true_
url=https_3A__www.ndt.net_title=NDT.net_summary=NDT.net_-_Web's_Largest_Portal_of_Nondestructive_Tes.txt"


_____________________________________________________________________________________________________________________
==>> RESOLVED ISSUES:
1. data-digital-data has been detected..
2. HTML missing due to Nested <span Tag inside a <span Tag:  SUCCESSFULLY Detected. 

_____________________________________________________________________________________________________________________
^^^ Remaining Issue:
1. Attack Payload Detection:
2. Return Only the Value where XSS is present or there is a Bypass. 
_____________________________________________________________________________________________________________________

==>>    FINDINGS:

ISSUE NO. 1:
1. https://www.burpee.com/search?q=(uvw"xyz'yxz</zxy
2. URL Context: Encoding is present and also absent for different attributes of the TAG e.g: <a> 
 <a class="b-breadcrumbs-keywords_link" href="/search?q=%28uvw%22xyz%27yxz%3C%2Fzxy" title="(uvw&quot;xyz'yxz&lt;/zxy">
3. Now, I think I have to break the tags in parts, in order to check this.
4. In my opinion, We shall give priority to the Non-Encoded and Non-Filtered attribute of the TAG.

ISSUE NO. 2:
1. https://www.burpee.com/search?q=(uvw"xyz'yxz</zxy
2. payload <img src=x onerror="alert(1)"> dones not work, it is in the <title> tag.
3. if we first close the </title> TAG , then it is XSSed
4. payload </title><img src=x onerror="alert(1)"> is SUCCESSFUL

ISSUE NO. 3:
1. Attack Methodology for URL: Does it need Encoding Analysis..?


ISSUE NO. 4:
1. On https://www.crane.com
i.  <a href="/stationery/featured-products">Featured Products</a> 
ii. <a href="/stationery/best-sellers">Best Sellers</a>

2. The href value is merged with base Url to produce a complete link. 
 https://www.crane.com + href
 
3. So what's the update, are we goin to do the same..
 


"""

