import matplotlib.pyplot as plt


plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False




import xlrd
data1=xlrd.open_workbook('C:\\Users\Administrator\Desktop\macroeconomics\\shenB.xlsx')
print(data1)

table1=data1.sheets()[0]
x=table1.col_values(0)

y=table1.col_values(1)
print(x)
print(y)

plt.title('深圳证券交易所A股市值变化趋势',color='r',fontsize='large')
plt.xlabel('年份',color='b')
plt.ylabel('市值（十万亿元人民币）',color='b')


plt.plot(x,y,color='k',linestyle='dashdot',linewidth=1,
        marker='o',markersize=5,label='市值')

plt.xticks(rotation=40)

for a,b in zip(x,y):
    plt.text(a,b,b,ha='right',va='center',fontsize=7,rotation=90,color='g')

#设置网格线
plt.grid(True,color='y')
plt.legend()
plt.show()