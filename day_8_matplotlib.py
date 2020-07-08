# 在图例中显示不同尺寸的点

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# cities = pd.read_csv('Data\california_cities.csv')
# # print(cities.columns)
# lat,lon = cities['latd'],cities.longd
# population,area = cities.population_total,cities.area_total_km2
# # print(area)
# # 散点图的制作
# plt.scatter(lon,lat,
#             label = None,c = np.log(population),cmap='viridis',
#             s = area,linewidths=0,alpha=0.5
#             )
# plt.axis(aspect='equal')
# plt.xlabel('longitude')
# plt.ylabel('latiude')
# plt.colorbar(label='population')
# # 圆点图例制作
# for area in [100,300,500]:
#     plt.scatter([],[],c='k',alpha=0.3,s=area,label=str(area) + 'km$^2$')

# plt.legend(scatterpoints=1,frameon=False,labelspacing=1,title='city area')

# plt.show()

# ###################################################################

# 同时显示多个图例

from matplotlib.legend import Legend

# plt.style.use('seaborn-whitegrid') # 创建表格风格

# fig,ax = plt.subplots()
# lines = []
# styles = ['-','--','-.',':']

# x = np.linspace(0,10,1000)
# for i in range(4):
#     lines += ax.plot(x,np.sin(x - i * np.pi / 2),styles[i],color='black')
# ax.axis('equal')
# # 创建第一个图例
# ax.legend(lines[:2],['line a','line b'],loc='upper right',frameon=False)
# # 创建第二个图例
# leg = Legend(ax,lines[2:],['line c','line d'],loc='lower right',frameon=False)
# ax.add_artist(leg)

# plt.show()

# ##################################################################

# 配置颜色条

from matplotlib.colors import LinearSegmentedColormap

# plt.style.use('classic')

# x = np.linspace(0,10,1000)
# i = np.sin(x) * np.cos(x[:,np.newaxis])

# plt.imshow(i,cmap='gray')
# plt.colorbar()
# plt.show()

# def grayscale_cmap(cmap):
#     cmap = plt.cm.get_cmap(cmap)
#     colors = cmap(np.arange(cmap.N))
#     RGB_wight = [0.299,0.587,0.114]
#     luminace = np.sqrt(np.dot(colors[:,:3] ** 2,RGB_wight))
#     colors[:,:3] = luminace[:,np.newaxis]
#     return LinearSegmentedColormap.from_list(cmap.name + '_gray',colors,cmap.N)

# def view_colormap(cmap):
#     cmap = plt.cm.get_cmap(cmap)
#     colors = cmap(np.arange(cmap.N))
#     cmap = grayscale_cmap(cmap)
#     grayscale = cmap(np.arange(cmap.N))
#     fig,ax = plt.subplots(2,figsize=(6,2),
#                          subplot_kw=dict(xticks=[],yticks=[]),           
#                          )
#     ax[0].imshow([colors],extent=[0,10,0,1])
#     ax[1].imshow([grayscale],extent=[0,10,0,1])
#     plt.show()

# view_colormap('jet')
# view_colormap('viridis')
# view_colormap('cubehelix')
# view_colormap('RdBu')

# ##################################################################

# 多子图

plt.style.use('classic') # 创建表格风格

# ax1 = plt.axes() # 默认的主坐标轴
# ax2 = plt.axes([0.65,0.65,0.2,0.2])

# fig = plt.figure()
# ax1 = fig.add_axes([0.1,0.5,0.8,0.4],ylim=[-1.2,1.2])
# ax2 = fig.add_axes([0.1,0.1,0.8,0.4],ylim=[-1.2,1.2])
# x = np.linspace(0,10,1000)
# ax1.plot(x,np.sin(x))
# ax1.axis('equal')
# ax2.plot(x,np.cos(x))

for i in range(1,7):
    plt.subplot(2,3,i)
    plt.text(0.5,0.6,str((2,3,i)),fontsize=18,ha='center')

plt.show()

