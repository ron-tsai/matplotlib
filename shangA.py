import pandas as pd
import matplotlib.pyplot as plt


plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False


fig=plt.figure()
ax=fig.add_subplot(1,1,1)

data=pd.read_excel('C:\\Users\Administrator\Desktop\macroeconomics\\shangA1.xlsx',index_col=0)
# print(data.head())

# value=data['Market value']

# data.plot(ax=ax,style='k-')
# ax.set_xlim('1992年','2019年')
# ax.set_ylim(40000000000,40000000000000)
#x轴刻度自定义数字
ticks=ax.set_xticks([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27])

labels=ax.set_xticklabels(['1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019'],
                          rotation=40,fontsize='small')

ax.set_title(('上海证券交易所A股市值变化趋势'))
ax.set_xlabel('年份')
ax.set_ylabel('市值（十万亿元人民币）')


plt.plot(data)
plt.show()





# fig=plt.figure()
# ax=fig.add_subplot(1,1,1)
# ax.plot(np.random.rand(1000).cumsum())
#
# #x轴刻度自定义数字
# ticks=ax.set_xticks([0,250,500,750,1000])
#
# labels=ax.set_xticklabels(['one','two','three','four','five'],
#                           rotation=30,fontsize='small')
#
# ax.set_title(('My first matplotlib plot'))
# ax.set_xlabel('Stages')
#
# #或使用
# # props={'title':'My first matplotlib plot',
# #        'xlabel':'Stages'}
# # ax.set(**props)
#
#
#
#
#
# import pandas as pd
# import csv
#
# data=pd.read_csv('C:\\Users\Administrator\Desktop\macroeconomics\\shangA.csv',
#                  index_col=0)
#
# a4=data.head()
# print(a4)
#
# year=data['A']
# year.plot(ax=ax,style='k-')
#
# ax.set_xlim(['1992年','2019年'])
# ax.set_ylim([600,1800])
#
# plt.show()