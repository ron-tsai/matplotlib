import matplotlib.pyplot as plt

y1=[100280,110863,121717,137422,161840,187319,219439,270092,319245,348518,
412119,487940,538580,592963,643563,688858,746395,832036,919281,990865]
y2=[70.90505031,78.38797212,86.06272202,97.16697354,114.4323502,132.4475746,155.1583802,190.9741626,225.7282793,
246.4264101,291.3971935,345.0078772,380.8137606,419.2664898,455.0441611,487.0709675,527.7535834,588.3076238,649.9960874,700610.9863]

x=['2000','2001','2002','2003','2004','2005','2006','2007','2008','2009',
   '2010','2011','2012','2013','2014','2015','2016','2017','2018','2019']
fig=plt.figure(figsize=(10,8),dpi=80)

barwidth=0.4
x1=list(range(len(x)))
x2=[i-barwidth/2 for i in x1]
x3=[i+barwidth/2 for i in x1]

plt.bar(x2,y1,width=barwidth,color='orange')
plt.bar(x3,y2,width=barwidth,color='b')

plt.xticks(x1,x)
plt.show()

# a=[12,55]
# b=['1','2']
# fig=plt.figure(figsize=(20,10),dpi=80)
# plt.bar(range(len(b)),a)
# # plt.bar(range(len(x)),y2)
# plt.show()
