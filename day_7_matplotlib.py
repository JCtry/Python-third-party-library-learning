import matplotlib.pyplot as plt
import numpy as np

# x = np.linspace(0,10,100)
# y = np.sin(x)
# fig = plt.figure() # 建立好一个画图板
# plt.plot(x,y,'-')
# plt.plot(x,np.cos(x),'--')
# plt.show()

# 保存绘制好的图片
# fig.savefig('photo\sin_cos.png')

# 查看能保存的图片格式
# dict_file_type = fig.canvas.get_supported_filetypes()
# for file_type in dict_file_type:
#     print(file_type)

# 创建图形
# plt.figure()
# 在图形中创建子图
# plt.subplot(2,1,1) # (行，列，子图编号)
# plt.plot(x,np.sin(x))
# plt.subplot(2,1,2)
# plt.plot(x,np.cos(x))
# plt.show()
# 面向对象的风格接口
# fig,ax = plt.subplots(2)
# ax[0].plot(x,np.sin(x))
# ax[1].plot(x,np.cos(x))
# plt.show()

# #########################################################

# 简易线性图的画法

# plt.style.use('seaborn-whitegrid') # 创建表格风格

# fig = plt.figure() # 创建图形
# ax = plt.axes() # 创建坐标轴
# x = np.linspace(0,10,100)
# ax.plot(x,np.sin(x))

# 控制线条颜色的表达方式
# plt.plot(x,np.sin(x-0),color='blue') # 标准的颜色名称
# plt.plot(x,np.sin(x-1),color='g') # 缩写颜色代码
# plt.plot(x,np.sin(x-2),color='0.75') # 范围在0-1的灰度值
# plt.plot(x,np.sin(x-3),color='#FFDD44') # 十六进制的rgb编码
# plt.plot(x,np.sin(x-4),color=(1.0,0.2,0.3)) # rgb元组
# plt.plot(x,np.sin(x-5),color='chartreuse') # html颜色名称

# 控制线条风格
# plt.plot(x,x+0,linestyle='solid')
# plt.plot(x,x+1,linestyle='dashed')
# plt.plot(x,x+2,linestyle='dashdot')
# plt.plot(x,x+3,linestyle='dotted')

# 符号简写
# plt.plot(x,x+4,linestyle='-') # 实线
# plt.plot(x,x+5,linestyle='--') # 虚线
# plt.plot(x,x+6,linestyle='-.') # 点划线
# plt.plot(x,x+7,linestyle=':') # 实心点

# 非关键字参数控制线条风格
# plt.plot(x,x+8,'-g') # 实线颜色为绿色 linestyle , color
# plt.plot(x,x+9,'--c')
# plt.plot(x,x+10,'-.k')
# plt.plot(x,x+11,':r')

# plt.show()

# ##########################################################

# 调整图形，坐标轴的上下线

# plt.style.use('seaborn-whitegrid') # 创建表格风格

# x = np.linspace(0,10,100)
# plt.plot(x,np.sin(x))
# plt.plot(x,np.cos(x))
# plt.xlim(-1,11) # x轴坐标调整
# plt.ylim(-1.5,1.5) # y轴坐标调整

# 坐标翻转(逆序显示)
# plt.xlim(11,-1) # x轴坐标调整
# plt.ylim(1.5,-1.5) # y轴坐标调整

# 利用axis方法调整上下限并且进行绘图收紧
# plt.axis([-1,11,-1.5,1.5])
# plt.axis('tight') # 压缩收紧

# 设置图形标签
# plt.title('a sine/cosine cure') # 图形标题

# plt.plot(x,np.sin(x),'-g',label='sin(x)')
# plt.plot(x,np.cos(x),':b',label='cos(x)')
# plt.xlabel('x')
# plt.ylabel('sin(x')

# plt.axis('equal') # 1:1 绘制
# plt.legend()

# plt.show()

# ###########################################################

# 简易散点图的画法

# plt.style.use('seaborn-whitegrid') # 创建表格风格

# rng = np.random.RandomState(0)
# fig = plt.figure()
# x = np.linspace(0,10,30)
# y = np.sin(x)
# 利用plt.plot方法绘制散点图
# plt.plot(x,y,'o',color='black')

# 散点图的标记
# for maker in ['o','.',',','x','+','v','^','<','>','s','d']:
#     plt.plot(rng.rand(5),rng.rand(5),maker,label="maker={0}".format(maker))
#     # print(rng.rand(5))
#     plt.legend()
#     plt.xlim(0,1.8)

# 非关键字的复合传参
# plt.plot(x,y,'-ok',label='x')
# plt.plot(x,y,'-p',color='gray',markersize=10,linewidth=2,markerfacecolor='red',
#         markeredgecolor='green',markeredgewidth=1,label='test'
#         )

# 利用plt.catter()画散点图
# plt.scatter(x,y,marker='o')
# plt.xlim(-1,11) # x轴的坐标调整
# plt.ylim(-1.5,1.5)
# x = rng.rand(100)
# y = rng.rand(100)
# color = rng.rand(100)
# sizes = 100 * rng.rand(100)
# plt.scatter(x,y,c=color,s=sizes,alpha=0.5,cmap='viridis')

# 鸾尾花数据散点图展示

from sklearn.datasets import load_iris

# iris = load_iris()
# features = iris.data.T
# plt.scatter(features[0],features[1],c=iris.target,s=100*features[3],cmap='viridis',alpha=0.5)

# plt.legend()

# plt.show()

# ############################################################

# 等高线与密度图

# plt.style.use('seaborn-whitegrid') # 创建表格风格

# def f(x,y):
#     return np.sin(x) ** 10 + np.cos(10 + y + x) * np.cos(x)

# if __name__ == "__main__":
#     x = np.linspace(0,5,50)
#     y = np.linspace(0,5,40)
#     X,Y = np.meshgrid(x,y)
#     Z = f(X,Y)
#     # plt.contour(X,Y,Z,color='RdGy')
#     plt.contour(X,Y,Z,color='RdGy')
#     plt.show()


# #############################################################

# 频次图，直方图区间划分和分布密度

# plt.style.use('seaborn-whitegrid') # 创建表格风格
# rng = np.random.RandomState(0)
# data = np.random.randn(1000)
# print(data)
# 频次图
# plt.hist(data,bins=30,alpha=0.5,histtype='stepfilled',color='steelbule',
#         edgecolor='none'
#         )

# x1 = np.random.normal(0,0.8,1000)
# x2 = np.random.normal(-2,1,1000)
# x3 = np.random.normal(3,2,1000)
# kwargs = dict(histtype='stepfilled',alpha=0.3,bins=40)
# plt.hist(x1,**kwargs)
# plt.hist(x2,**kwargs)
# plt.hist(x3,**kwargs)

# mean = [0,0]
# cov = [[1,1],[1,2]]
# x,y = np.random.multivariate_normal(mean,cov,10000).T

# plt.hist2d(x,y,bins=30,cmap='Blues')
# plt.hexbin(x,y,bins=30,cmap='Blues')
# cb = plt.colorbar()
# cb.set_label('counts in bin')

# plt.show()

# #############################################################

#配置图例

# plt.style.use('classic')

# x = np.linspace(0,10,1000)
# fig,ax = plt.subplots()
# ax.plot(x,np.sin(x),'-b',label='sine')
# ax.plot(x,np.cos(x),'--r',label='cosine')
# ax.axis('equal')
# #ax.legend(loc='upper lef',frameon=False)
# ax.legend(fancybox=True,framealpha=1,loc='lower center',frameon=True,ncol=2,shadow=True)
# plt.show()



