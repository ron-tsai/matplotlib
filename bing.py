# from pyecharts import options as opts
# from pyecharts.charts import Pie
#
# def create_pie(datas,title)-> Pie:
#     pie=Pie()
#     pie.add("",datas)
#     pie.set_global_opts(
#         title_opts=opts.TitleOpts(title=title),
#         legend_opts=opts.LegendOpts(pos_right='right')
#     )
#     pie.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{c}:{d}%"))
#     return pie

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False


# labels='农、林、牧、渔业','采矿业','制造业','电力、燃气及水的生产和供应业','建筑业','交通运输、仓储和邮政业','信息传输、计算机服务和软件业截至','批发和零售业','住宿和餐饮业','金融业','房地产业','租赁和商务服务业','科学研究、技术服务和地质勘查业','水利、环境和公共设施管理业','居民服务和其他服务业','教育','卫生、社会保障和社会福利业','文化、体育和娱乐业'
# sizes=

import xlrd
data1=xlrd.open_workbook('C:\\Users\Administrator\Desktop\macroeconomics\\oo.xlsx')

table1=data1.sheets()[0]
x=table1.col_values(0)
print(x)

y=table1.col_values(1)
print(y)
# datas=list(zip(x,y))
# print(datas)

# pie=create_pie(datas,'各行业对外直接投资份额')
# pie.render()

# figl,axl=plt.subplot()
# axl.pie(datas,autopct='%1.1f%%,shadow=True,startangle=90')
#
# plt.title('国内生产总值',color='r')
#
# for a,b in zip(x,y):
#     plt.text(a,b,b,ha='center',va='bottom',fontsize=12,rotation=90)

# plt.xlabel('年份',color='b')
# plt.ylabel('国内生产总值(亿元)',color='b')

# plt.xticks(rotation=40)
#
# plt.legend()

# plt.show()
labels=x
sizes=y
explode=(0.2,0,0.2,0,0.2,0,0.2,0,0.2,0,0.2,0,0.2,0,0.2,0,0.2,0)
plt.pie(sizes,explode=explode,labels=labels,shadow=False,autopct='%1.2f%%',
        pctdistance=0.6,labeldistance=0.8,rotatelabels=90,startangle=30,radius=1.1,counterclock=False,
        textprops={'fontsize':7,'color':'black'})
plt.title('对外投资各行业占比')
# plt.axis('equal')
plt.legend(loc='upper right',fontsize=8,bbox_to_anchor=(1.2,1.2),borderaxespad=0.1)
# plt.text()
plt.show()