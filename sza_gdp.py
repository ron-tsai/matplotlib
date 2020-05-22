import xlrd

data1=xlrd.open_workbook('C:\\Users\Administrator\Desktop\macroeconomics\\shenA.xlsx')
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