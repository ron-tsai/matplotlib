import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
# plt.subplot(1,1,1)
fig,ax=plt.subplots()

import xlrd
data1=xlrd.open_workbook('C:\\Users\Administrator\Desktop\macroeconomics\\tu.xlsx')
print(data1)

table1=data1.sheets()[0]
x=table1.col_values(0)

y=table1.col_values(1)

# plt.bar(x,y,width=0.5,align='center',label='中国对外直接投资国家及地区',color='g')
plt.barh(x,y,height=0.5,align='center',label='投资额（亿美元）',color='g')

plt.title('图1.1  2018年世界各国外国直接投资总额',color='r',y=-0.14)



plt.ylabel('国家',color='b')
# plt.xlabel('直接投资存量(万美元)',color='b')

plt.yticks(rotation=0,fontsize=7)

for x,y in enumerate(y):
    plt.text(y,x,'%s'% y)

plt.legend()

plt.show()