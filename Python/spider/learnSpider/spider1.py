# coding:utf-8
'''
    Created on 2016/6/18 0018 
    @Author:   HuShiwei
'''
import urllib
import urllib2

# response = urllib2.urlopen('http://www.baidu.com/')
# html = response.read()
# print html

# req = urllib2.Request('http://www.baidu.com')
# response = urllib2.urlopen(req)
# the_page = response.read()
# print the_page



# url = 'http://www.someserver.com/register.cgi'
#
# values = {'name' : 'WHY',
#           'location' : 'SDU',
#           'language' : 'Python' }
#
# data = urllib.urlencode(values) # 编码工作
# req = urllib2.Request(url, data)  # 发送请求同时传data表单
# response = urllib2.urlopen(req)  #接受反馈的信息
# the_page = response.read()  #读取反馈的内容

import re

strContent="""
<div class="article block untagged mb15" id='qiushi_tag_116725679'>

<div class="author clearfix">
<a href="/users/24667130/" target="_blank" rel="nofollow">
<img src="http://pic.qiushibaike.com/system/avtnew/2466/24667130/medium/20160525163529.jpg" alt="饮最烈的酒、艹最爱的人"/>
</a>
<a href="/users/24667130/" target="_blank" title="饮最烈的酒、艹最爱的人">
<h2>饮最烈的酒、艹最爱的人</h2>
</a>
</div>


<div class="content">

傍晚在楼下陪女儿玩……<br/>有只小狗狗不停的叫，女儿听得有点不高兴了，怒气冲冲的跑到小狗狗身边，指着小狗狗威胁道：叫，叫，叫……再叫明天就送你去上学！

</div>



<div class="stats">
<span class="stats-vote"><i class="number">5786</i> 好笑</span>
<span class="stats-comments">


<span class="dash"> · </span>
<a href="/article/116725679" data-share="/article/116725679" id="c-116725679" class="qiushi_comments" target="_blank">
<i class="number">68</i> 评论
</a>



</span>
</div>
<div id="qiushi_counts_116725679" class="stats-buttons bar clearfix">
<ul class="clearfix">
<li id="vote-up-116725679" class="up">
<a href="javascript:voting(116725679,1)" class="voting" data-article="116725679" id="up-116725679" rel="nofollow">
<i class="iconfont" data-icon-actived="&#xf0061;" data-icon-original="&#xf001f;">&#xf001f;</i>
<span class="number hidden">5918</span>
</a>
</li>
<li id="vote-dn-116725679" class="down">
<a href="javascript:voting(116725679,-1)" class="voting" data-article="116725679" id="dn-116725679" rel="nofollow">
<i class="iconfont" data-icon-actived="&#xf0020;" data-icon-original="&#xf0020;">&#xf0020;</i>
<span class="number hidden">-132</span>
</a>
</li>

<li class="comments">
<a href="/article/116725679" id="c-116725679" class="qiushi_comments" target="_blank">
<i class="iconfont" data-icon-actived="&#xf0062;" data-icon-original="&#xf001d;">&#xf001d;</i>
</a>
</li>

</ul>
</div>
<div class="single-share">
<a class="share-wechat" data-type="wechat" title="分享到微信" rel="nofollow">微信</a>
<a class="share-qq" data-type="qq" title="分享到QQ" rel="nofollow">QQ</a>
<a class="share-qzone" data-type="qzone" title="分享到QQ空间" rel="nofollow">QQ空间</a>
<a class="share-weibo" data-type="weibo" title="分享到微博" rel="nofollow">微博</a>
</div>
<div class="single-clear"></div>

</div>
"""


strs='''
<div class="content">

傍晚在楼下陪女儿玩……<br/>有只小狗狗不停的叫，女儿听得有点不高兴了，怒气冲冲的跑到小狗狗身边，指着小狗狗威胁道：叫，叫，叫……再叫明天就送你去上学！

</div>
'''

pattern=re.compile(r'strs')
