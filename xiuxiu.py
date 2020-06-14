import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
plt.subplot(1,1,1)

import xlrd
data1=xlrd.open_workbook('C:\\Users\Administrator\Desktop\macroeconomics\\nation.xlsx')
print(data1)

table1=data1.sheets()[0]
x=table1.col_values(0)

y=table1.col_values(1)

plt.bar(x,y,width=0.5,align='center',label='中国对外直接投资国家及地区',color='g')

plt.title('中国对外直接投资存量',color='r')

for a,b in zip(x,y):
    plt.text(a,b,b,ha='center',va='bottom',fontsize=8,rotation=90)

plt.xlabel('国家',color='b')
plt.ylabel('直接投资存量(万美元)',color='b')

plt.xticks(rotation=90,fontsize=6)

plt.legend()

plt.show()