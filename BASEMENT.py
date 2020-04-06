

"""             
==>>    UPDATES Created - DONE

1. Extract Unique GET Params.
2. If 2 forms have same 2 GET Params, then 4 GET URLs will be generated: DONE: later unique GET URLS are extracted
3. Payload = (uvw"xyz'yxz</zxy. DONE


==>>    UPDATES REQUIRED 

1. Base Url for all websites. Resolve issues like ifu-institut.at
2. Check encdoing separarately for each value of a context. 
    Issue: one value has encoding and others may not have..!!
3. Try the Vertical format of the EXCEL FILE 

==>>    FINDINGS:

ISSUE NO. 1:
1. https://www.burpee.com/search?q=(uvw"xyz'yxz</zxy
2. URL Context: Encoding is present and also absent for different attributes of the TAG e.g: <a> 
 <a class="b-breadcrumbs-keywords_link" href="/search?q=%28uvw%22xyz%27yxz%3C%2Fzxy" title="(uvw&quot;xyz'yxz&lt;/zxy">
3. Now, I think I have to break the tags in parts, in order to check this.
4. In my opinion, We shall give priority to the Non-Encoded and Non-Filtered attribute of the TAG.

"""

