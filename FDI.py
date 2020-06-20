import matplotlib.pyplot as plt
import matplotlib
# matplotlib.rc
# font = {'family' : 'MicroSoft YaHei',
#               'weight' : 'bold',
#               'size'   : 'larger'}
# matplotlib.rc('font',**font)
from matplotlib import font_manager

# my_font=font_manager.FontProperties(fnames='C:\Windows\Fonts\SimHei.ttc')
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
# x=['中国','印尼','马来西亚','泰国','越南','印度','巴西','阿根廷','墨西哥']
x=['1996','1997','1998','1999','2000','2001','2002','2017']
y1=[41725.5,45257.0,45462.8,40318.7,40714.8,46877.6,52742.9,136320.0]
y2=[6245.0,4729.0,-207.0,-1838.0,-4550.4,-2977.4,145.1,23063.1]
y3=[7297.0,6323.0,2714.0,3895.3,3787.6,553.9,3203.4,9543.4]
y4=[2338.0,3882.0,7492.0,6106.4,3410.1,5073.2,3355.4,7635.2]
y5=[2395.0,2220.0,1671.0,1412.0,1289.0,1300.0,1400.0,14100.0]
y6=[2525.0,3619.0,2633.0,2168.0,3588.0,5477.6,5629.7,9916.1]
y7=[16.6,11.9,19.0,53.6,23.3,61.2,25.5,77.0]
y8=[76.8,84.5,672.8,154.6,229.6,498.5,205.3,1146.7]
y9=[ 9185.5,12829.6,12756.8,13943.6,18247.1,30041.8,24055.3,29695.0]
fig=plt.figure(figsize=(10,8),dpi=80)
plt.plot(x,y1)
plt.plot(x,y2)
plt.plot(x,y3)
plt.plot(x,y4)
plt.plot(x,y5)
plt.plot(x,y6)
plt.plot(x,y7)
plt.plot(x,y8)
plt.plot(x,y9)

plt.ylabel('百万美元')
plt.legend(['中国','印尼','马来西亚','泰国','越南','印度','巴西','阿根廷','墨西哥'])
plt.grid(alpha=0.3)
plt.title('图1.1  部分发展中国家FDI流入量趋势',y=-0.1)
plt.show()