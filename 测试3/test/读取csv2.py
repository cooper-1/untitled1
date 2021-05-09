# -*-coding:  utf-8 -*-
# @Time    :  2021/3/6 13:21
# @Author  :  Cooper
# @FileName:  读取csv2.py
# @Software:  PyCharm
import pandas as pd                         #导入pandas包
import numpy as np
from pyecharts import options as opts
from pyecharts.charts import Bar
al=[]
bl=[]
cl=[]
dl=[]
data = pd.read_csv("text2.csv")
a=data.loc[:, ['番剧名称','均集播放/万','播放量/万','均集活跃/万']]
data = np.array(a)
for da in data:
        al.append(da[0])
        bl.append(da[1])
        cl.append(da[2])
        dl.append(da[3])
        print(da[0],'   ',end='')
        print(da[1],'   ',end='')
        print(da[2],'   ',end='')
        print(da[3])
print(al)
print(bl)
print(cl)
print(dl)
bar = (
    Bar()
    .add_xaxis(al)
    .add_yaxis("均集播放/万", bl)
    .add_yaxis("总播放量/万", cl)
    .add_yaxis("均集活跃/万", dl)

    .set_global_opts(
        # xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15)),
        title_opts=opts.TitleOpts(title="B站番剧排行榜"),
        yaxis_opts=opts.AxisOpts(name="播放量"),
        xaxis_opts=opts.AxisOpts(name="番剧名称",axislabel_opts=opts.LabelOpts(rotate=-45),),
        datazoom_opts=opts.DataZoomOpts(type_="slider")
    )
        # xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15),)
)   .set_series_opts(
        label_opts=opts.LabelOpts(is_show=False),
        markline_opts=opts.MarkLineOpts(
            data=[
                # opts.MarkLineItem(type_="min", name="最小值"),
                opts.MarkLineItem(type_="max", name="最大值"),
                opts.MarkLineItem(type_="average", name="平均值"),
                 ]
        ),
    )


bar.render("B站番剧排行榜数据3.html") #这里我指定了我的存放路径和文件名