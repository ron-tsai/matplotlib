# #coding=utf-8
from pyecharts.charts import Pie
import random

attr=['啊','哦','额','以','无','与']
v1=[11,22,33,43,12,3]
pie=Pie('1')
pie.add("",attr,v1,is_label_show=True)
pie.render()


