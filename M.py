import pandas as pd

import xlrd

data1=xlrd.open_workbook('C:\\Users\Administrator\Desktop\macroeconomics\\shangA.xlsx')
print(data1)
data2=xlrd.open_workbook('C:\\Users\Administrator\Desktop\macroeconomics\\gfx.xlsx')
table1=data1.sheets()[0]
x=table1.col_values(1)
table2=data2.sheets()[0]
y=table2.col_values(1)
print(x)
print(y)

from xg import correlation

print(correlation(x,y))






# import matplotlib.pyplot as plt
# import numpy as np
#
#
# fig=plt.figure()
# ax=fig.add_subplot(1,1,1)
#
# ax.plot(x,y)
#
# #x轴刻度自定义数字
# ticks=ax.set_xticks([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27])
#
# labels=ax.set_xticklabels(['1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019'],
#                           rotation=30,fontsize='small')
#
# ax.set_title(('My first matplotlib plot'))
# ax.set_xlabel('years')


#
# plt.plot(x,y)
# plt.xlabel('years')
# plt.ylabel(' Market value')

# plt.show()
