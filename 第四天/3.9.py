# 计科1914 0306224401 惠骁

import re

web = """<div id="line_u7_0" class="col-lg-3 col-md-3 col-sm-3 col-xs-9" style="margin: 10px;padding: 
0px;border: 1px solid #E4E4E4">
<a href="../info/1103/4582.htm" style="width: 100%;display: block;position: relative;textdecoration: none;outline: none">
<img 
src="/__local/6/F6/65/810526C24A2D78CA7980017F8AC_66F27B38_D79E4.jpg" 
style="width: 100%;height: 230px">
 <div style="position:absolute;right: 0px;bottom: 0px;width: 87px;height: 36px;textalign: center;line-break: 36px;background: rgba(247,147,30,0.5);color: #fff;font-size: 
21px">07-13</div>
</a>
<span style="padding: 15px 15px;height: 45px;display: block">《校园》冬日（2022 年
1 月 20 日晨）</span>
</div>
<div id="line_u7_1" class="col-lg-3 col-md-3 col-sm-3 col-xs-9" style="margin: 10px;padding: 
0px;border: 1px solid #E4E4E4">
<a href="../info/1103/4581.htm" style="width: 100%;display: block;position: relative;textdecoration: none;outline: none">
<img 
src="/__local/1/11/02/8DD8B78E1C645BB6AF2296C60B0_E51A8329_CE066.jpg" 
style="width: 100%;height: 230px">
 <div style="position:absolute;right: 0px;bottom: 0px;width: 87px;height: 36px;textalign: center;line-break: 36px;background: rgba(247,147,30,0.5);color: #fff;font-size: 
21px">07-13</div>
</a>
<span style="padding: 15px 15px;height: 45px;display: block">《校园》冬日（2022 年
1 月 20 日晨）</span>
</div>
<div id="line_u7_2" class="col-lg-3 col-md-3 col-sm-3 col-xs-9" style="margin: 10px;padding: 
0px;border: 1px solid #E4E4E4">
<a href="../info/1103/4299.htm" style="width: 100%;display: block;position: relative;textdecoration: none;outline: none">
<img 
src="/__local/C/C8/BA/99514BEA496D696A88F598A9773_383A9298_FC218.jpg" 
style="width: 100%;height: 230px">
 <div style="position:absolute;right: 0px;bottom: 0px;width: 87px;height: 36px;textalign: center;line-break: 36px;background: rgba(247,147,30,0.5);color: #fff;font-size: 
21px">05-27</div>
</a>
<span style="padding: 15px 15px;height: 45px;display: block">《校园》2022 之夏
</span>"""

# 定义正则表达式
pattern = r'src="([^"]*)"'

# 使用re.findall函数进行匹配
# 使用map为列表添加公共前缀
result = list(map(lambda x: 'https://www.tute.edu.cn/' +
              x,  re.findall(pattern, web)))
print(result)
