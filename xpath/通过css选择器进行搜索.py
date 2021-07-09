# -*-coding:  UTF-8
# @Time    :  2021/5/24 23:15
# @Author  :  Cooper
# @FileName:  通过css选择器进行搜索.py
# @Software:  PyCharm
from bs4 import BeautifulSoup
import re

#  准备数据
html = '''
<!DOCTYPE html>
<html lang="zh-cn">
<head>

<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-878633-1"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'UA-878633-1');
</script>

<meta charset="gbk" />
<meta name="robots" content="all" />
<meta name="author" content="w3school.com.cn" />
<link rel="stylesheet" type="text/css" href="/c5.css" />

<link rel="icon" type="image/png" sizes="16x16" href="/ui2019/logo-16-red.png">
<link rel="icon" type="image/png" sizes="32x32" href="/ui2019/logo-32-red.png">
<link rel="icon" type="image/png" sizes="48x48" href="/ui2019/logo-48-red.png">
<link rel="icon" type="image/png" sizes="96x96" href="/ui2019/logo-96-red.png">
<link rel="apple-touch-icon-precomposed" sizes="180x180" href="/ui2019/logo-180.png">


<title>Path 节点</title>
<title class='adsbygoogle'>Path 节点dfghksjdhfg</title>
<titl>Path 节点dfghk该开关花费的dhfg</titl>
<titl><!-- gfkhudfk富贵花开的积分工会看见的还是法国sdjrgdfjg --></titl>
</head>

<body class="xml">

<div id="wrapper">

<div id="header">
<a id="logo" href="/index.html" title="w3school 在线教程" style="float:left;">w3school 在线教程</a>
<div id="header_gg">
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- W3 椤电湁 -->
<ins class="adsbygoogle"
     style="display:inline-block;width:728px;height:90px"
     data-ad-client="ca-pub-3381531532877742"
     data-ad-slot="7423315034"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>
</div>
</div>

<div id="navfirst">
<ul id="menu">
<li id="h"><a href="/h.asp" title="HTML 系列教程">HTML 系列教程</a></li>
<li id="b"><a href="/b.asp" title="浏览器脚本教程">浏览器脚本</a></li>
<li id="s"><a href="/s.asp" title="服务器脚本教程">服务器脚本</a></li>
<li id="p"><a href="/p.asp" title="编程教程">编程教程</a></li>
<li id="x"><a href="/x.asp" title="XML 系列教程">XML 系列教程</a></li>
<li id="w"><a href="/w.asp" title="建站手册">建站手册</a></li>
<li id="r"><a href="/r.asp" title="参考手册">参考手册</a></li>
</ul>
</div>

<div id="navsecond">

<div id="course"><h2>XPath 教程</h2>
<ul>
<li><a href="/xpath/index.asp" title="XPath 教程">XPath 教程</a></li>
<li><a href="/xpath/xpath_intro.asp" title="XPath 简介">XPath 简介</a></li>
<li class="currentLink"><a href="/xpath/xpath_nodes.asp" title="XPath 节点">XPath 节点</a></li>
<li><a href="/xpath/xpath_syntax.asp" title="XPath 语法">XPath 语法</a></li>
<li><a href="/xpath/xpath_axes.asp" title="XPath Axes（轴）">XPath 轴</a></li>
<li><a href="/xpath/xpath_operators.asp" title="XPath 运算符">XPath 运算符</a></li>
<li><a href="/xpath/xpath_examples.asp" title="XPath 实例">XPath 实例</a></li>
<li><a href="/xpath/xpath_summary.asp" title="您已经学习了 XPath，下一步呢？">XPath 总结</a></li>
</ul>
<h2>XPath 参考手册</h2>
<ul>
<li><a href="/xpath/xpath_functions.asp" title="XPath、XQuery 以及 XSLT 函数">XPath 函数</a></li>
</ul>
</div><div id="selected">
<h2>建站手册</h2>
<ul>
<li><a href="/site/index.asp" title="网站构建">网站构建</a></li>
<li><a href="/w3c/index.asp" title="万维网联盟 (W3C)">万维网联盟 (W3C)</a></li>
<li><a href="/browsers/index.asp" title="浏览器信息">浏览器信息</a></li>
<li><a href="/quality/index.asp" title="网站品质">网站品质</a></li>
<li><a href="/semweb/index.asp" title="语义网">语义网</a></li>
<li><a href="/careers/index.asp" title="职业规划">职业规划</a></li>
<li><a href="/hosting/index.asp" title="网站主机">网站主机</a></li>
</ul>

<h2>编程</h2>
<ul>
<li><a href="/python/index.asp" title="Python 教程">Python 教程</a></li>
</ul>

<h2 id="link_about"><a href="/about/index.asp" title="关于 W3School" target="_blank">关于 W3School</a></h2>
<h2 id="link_help"><a href="/about/about_helping.asp" title="帮助 W3School" target="_blank">帮助 W3School</a></h2>


</div>

</div>

<div id="maincontent">

<h1>XPath 节点</h1>

<div id="tpn">
<ul class="prenext">
<li class="pre"><a href="/xpath/xpath_intro.asp" title="XPath 简介">XPath 简介</a></li>
<li class="next"><a href="/xpath/xpath_syntax.asp" title="XPath 语法">XPath 语法</a></li>
</ul>
</div>


<div id="intro">
<p><strong>在 XPath 中，有七种类型的节点：元素、属性、文本、命名空间、处理指令、注释以及文档节点（或称为根节点）。</strong></p>
</div>


<div>
<h2>XPath 术语</h2>

<h3>节点（Node）</h3>

<p>在 XPath 中，有七种类型的节点：元素、属性、文本、命名空间、处理指令、注释以及文档（根）节点。XML 文档是被作为节点树来对待的。树的根被称为文档节点或者根节点。</p>

<p>请看下面这个 XML 文档：</p>

<pre>&lt;?xml version=&quot;1.0&quot; encoding=&quot;ISO-8859-1&quot;?&gt;

&lt;bookstore&gt;

&lt;book&gt;
  &lt;title lang=&quot;en&quot;&gt;Harry Potter&lt;/title&gt;
  &lt;author&gt;J K. Rowling&lt;/author&gt; 
  &lt;year&gt;2005&lt;/year&gt;
  &lt;price&gt;29.99&lt;/price&gt;
&lt;/book&gt;

&lt;/bookstore&gt;</pre>

<p>上面的XML文档中的节点例子：</p>

<pre>
&lt;bookstore&gt; （文档节点）
&lt;author&gt;J K. Rowling&lt;/author&gt; （元素节点）
lang=&quot;en&quot; （属性节点） 
</pre>

<h3>基本值（或称原子值，Atomic value）</h3>

<p>基本值是无父或无子的节点。</p>

<p>基本值的例子：</p>

<pre>J K. Rowling
&quot;en&quot;</pre>

<h3>项目（Item）</h3>

<p>项目是基本值或者节点。</p>
</div>


<div>
<h2>节点关系</h2>

<h3>父（Parent）</h3>

<p>每个元素以及属性都有一个父。</p>

<p>在下面的例子中，book 元素是 title、author、year 以及 price 元素的父：</p>

<pre>&lt;book&gt;
  &lt;title&gt;Harry Potter&lt;/title&gt;
  &lt;author&gt;J K. Rowling&lt;/author&gt;
  &lt;year&gt;2005&lt;/year&gt;
  &lt;price&gt;29.99&lt;/price&gt;
&lt;/book&gt;</pre>

<h3>子（Children）</h3>

<p>元素节点可有零个、一个或多个子。</p>

<p>在下面的例子中，title、author、year 以及 price 元素都是 book 元素的子：</p>

<pre>&lt;book&gt;
  &lt;title&gt;Harry Potter&lt;/title&gt;
  &lt;author&gt;J K. Rowling&lt;/author&gt;
  &lt;year&gt;2005&lt;/year&gt;
  &lt;price&gt;29.99&lt;/price&gt;
&lt;/book&gt;</pre>

<h3>同胞（Sibling）</h3>

<p>拥有相同的父的节点</p>

<p>在下面的例子中，title、author、year 以及 price 元素都是同胞：</p>

<pre>&lt;book&gt;
  &lt;title&gt;Harry Potter&lt;/title&gt;
  &lt;author&gt;J K. Rowling&lt;/author&gt;
  &lt;year&gt;2005&lt;/year&gt;
  &lt;price&gt;29.99&lt;/price&gt;
&lt;/book&gt;</pre>

<h3>先辈（Ancestor）</h3>

<p>某节点的父、父的父，等等。</p>

<p>在下面的例子中，title 元素的先辈是 book 元素和 bookstore 元素：</p>

<pre>&lt;bookstore&gt;

&lt;book&gt;
  &lt;title&gt;Harry Potter&lt;/title&gt;
  &lt;author&gt;J K. Rowling&lt;/author&gt;
  &lt;year&gt;2005&lt;/year&gt;
  &lt;price&gt;29.99&lt;/price&gt;
&lt;/book&gt;

&lt;/bookstore&gt;</pre>

<h3>后代（Descendant）</h3>

<p>某个节点的子，子的子，等等。</p>

<p>在下面的例子中，bookstore 的后代是 book、title、author、year 以及 price 元素：</p>

<pre>&lt;bookstore&gt;

&lt;book&gt;
  &lt;title&gt;Harry Potter&lt;/title&gt;
  &lt;author&gt;J K. Rowling&lt;/author&gt;
  &lt;year&gt;2005&lt;/year&gt;
  &lt;price&gt;29.99&lt;/price&gt;
&lt;/book&gt;

&lt;/bookstore&gt;</pre>
</div>


<div id="bpn">
<ul class="prenext">
<li class="pre"><a href="/xpath/xpath_intro.asp" title="XPath 简介">XPath 简介</a></li>
<li class="next"><a href="/xpath/xpath_syntax.asp" title="XPath 语法">XPath 语法</a></li>
</ul>
</div>

</div>

<div id="sidebar">

<div id="tools">
<h5 id="tools_reference"><a href="/xpath/xpath_functions.asp">XPath, XQuery, 以及XSLT函数</a></h5>
</div>

<div id="sp_sidebar">
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- W3School 渚ф爮骞垮憡浣� -->
<ins class="adsbygoogle"
     style="display:inline-block;width:160px;height:600px"
     data-ad-client="ca-pub-3381531532877742"
     data-ad-slot="6744370501"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>
</div>

</div>

<div id="footer">
<p id="p1">
W3School 简体中文版提供的内容仅用于培训和测试，不保证内容的正确性。通过使用本站内容随之而来的风险与本站无关。版权所有，保留一切权利。
</p>

<p id="p2">

<a href="/about/about_use.asp" title="关于使用">使用条款</a>
<a href="/about/about_privacy.asp" title="关于隐私">隐私条款</a>
<a target="_blank" href="https://www.ykinvestment.com/">技术支持：赢科</a>
<a target="_blank" href="https://beian.miit.gov.cn">蒙ICP备06004630号</a>
</p>
</div>


</div>
</body>
</html>'''
bs = BeautifulSoup(html, 'lxml')

'''    
def find_all(self, name=None, attrs={}, recursive=True, text=None,
                 limit=None, **kwargs):
name参数：查找所有名字为name的标签，不过字符串会被自动忽略掉。可以传入标签名，正则，列表，字符串
soup.find_all('b')
for tag in soup.find_all(re.compile("^b")):
    print(tag.name)
soup.find_all(["a", "b"])

kwargs 根据属性进行查找，命名参数
attrs 根据属性进行查找，参数字典
text 根据文本进行查找,可以传入正则、字符串、列表
limit 用于限制最多查找几个
recursive 是否要递归查找 默认是true 如果为false只能查找直接子标签
'''
bs = BeautifulSoup(html.encode('utf-8'), 'lxml')
print(bs)

# BeautifulSoup类中提供了一个select()方法，该方法会将CSS选择器搜索到的结果放到列表中。
# 通过标签查找,直接传入标签名即可，不需要使用任何的修饰符

result = bs.select('title')
print(result)
# 通过类名查找,需要在class属性前面加  .
result = bs.select(".adsbygoogle")
print(result)
# 通过id名查找,需要在id面前加#
result = bs.select("#wrapper")
print(result)
# 通过组合查找,查找div下面的id="logo"的子标签
result = bs.select("div #logo")
print(result)
# 通过组合查找,查找div下面的a的子标签
result = bs.select("div > a")
print(result)
# 通过属性查找
# 查找sizes="48x48" 的link标签
result = bs.select('link[sizes="48x48"]')
print(result)
