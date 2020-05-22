import pandas as pd
import matplotlib.pyplot as plt


plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False


fig=plt.figure()
ax=fig.add_subplot(1,1,1)

data=pd.read_excel('C:\\Users\Administrator\Desktop\macroeconomics\\GDP.xlsx',index_col=0)

import xlrd
data1=xlrd.open_workbook('C:\\Users\Administrator\Desktop\macroeconomics\\shangA.xlsx')
print(data1)

table1=data1.sheets()[0]
x=table1.col_values(0)

y=table1.col_values(1)
print(x)
print(y)

ax.set_title(('上海证券交易所A股市值变化趋势'))
ax.set_xlabel('年份')
ax.set_ylabel('市值（十万亿元人民币）')


plt.plot(x,y,color='k',linestyle='dashdot',linewidth=1,
        marker='o',markersize=5,label='GDP')

plt.xticks(rotation=40)

for a,b in zip(x,y):
    plt.text(a,b,b,ha='center',va='bottom',fontsize=8,rotation=40)

#设置网格线
plt.grid(True)
plt.legend()
plt.show()