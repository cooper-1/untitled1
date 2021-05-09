from pyecharts import options as opts
from pyecharts.charts import Bar
l1=['星期一','星期二','星期三','星期四','星期五','星期七','星期日']
l2=[100,200,300,400,500,400,300]
bar = (
    Bar()
    .add_xaxis(l1)
    .add_yaxis("基本柱状图", l2)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="B站番剧排行榜"),
        yaxis_opts=opts.AxisOpts(name="均集播放/万"),
        xaxis_opts=opts.AxisOpts(name="番剧名称"),)
)

bar.render("B站番剧排行榜数据.html") #这里我指定了我的存放路径和文件名
