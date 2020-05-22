import pandas as pd
import matplotlib.pyplot as plt


plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False


fig=plt.figure()
ax=fig.add_subplot(1,1,1)

data=pd.read_excel('C:\\Users\Administrator\Desktop\macroeconomics\\shenB1.xlsx',index_col=0)

ticks=ax.set_xticks([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27])

labels=ax.set_xticklabels(['1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019'],
                          rotation=40,fontsize='small')

ax.set_title(('深圳证券交易所B股市值变化趋势'))
ax.set_xlabel('年份')
ax.set_ylabel('市值（仟亿元人民币）')


plt.plot(data)
plt.show()