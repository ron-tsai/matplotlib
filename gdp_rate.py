import matplotlib.pyplot as plt


plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False




import xlrd
data1=xlrd.open_workbook('C:\\Users\Administrator\Desktop\macroeconomics\\rategdp.xlsx')
print(data1)

table1=data1.sheets()[0]
x=table1.col_values(0)

y=table1.col_values(1)
print(x)
print(y)

plt.title('国内GDP增长率',color='r',fontsize='large')
plt.xlabel('年份',color='b')
plt.ylabel('增长率（%）',color='b')


plt.plot(x,y,color='g',linestyle='dashdot',linewidth=1,
        marker='o',markersize=5,label='GDP增长率')

plt.xticks(rotation=40)

for a,b in zip(x,y):
    plt.text(a,b,b,ha='right',va='center',fontsize=10,color='k')

#设置网格线
plt.grid(True,color='y')
plt.legend()
plt.show()