

"""             
==>>    UPDATES Created - DONE

1. Extract Unique GET Params.
2. If 2 forms have same 2 GET Params, then 4 GET URLs will be generated: DONE: later unique GET URLS are extracted
3. Payload = (uvw"xyz'yxz</zxy. DONE
4. Check encdoing separarately for each value of a context.     DONE
    Issue: one value has encoding and others may not have..!!


==>>    UPDATES REQUIRED 

1. Base Url for all websites. Resolve issues like ifu-institut.at and drudgereportarchives.com
2. Try the Vertical format of the EXCEL FILE 

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



"""

