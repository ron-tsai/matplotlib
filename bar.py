


import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
plt.subplot(1,1,1)

import xlrd
data1=xlrd.open_workbook('C:\\Users\Administrator\Desktop\macroeconomics\\gfx.xlsx')
print(data1)

table1=data1.sheets()[0]
x=table1.col_values(0)

y=table1.col_values(1)

plt.bar(x,y,width=0.5,align='center',label='GDP',color='g')

plt.title('国内生产总值',color='r')

for a,b in zip(x,y):
    plt.text(a,b,b,ha='center',va='bottom',fontsize=12,rotation=90)

plt.xlabel('年份',color='b')
plt.ylabel('国内生产总值(亿元)',color='b')

plt.xticks(rotation=40)

plt.legend()

plt.show()
