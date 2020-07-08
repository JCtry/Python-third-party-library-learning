#网格绘制图片的方法
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt

#绘图风格
# plt.style.use('classic')

#创建   利用share 与 sharey 可以共享x,y坐标
# fig,ax = plt.subplots(2,3,sharex='col',sharey='row')

# ax[0,0].plot(np.arange(0,5),np.arange(0,5))

# for i in range(2):
#     for j in range(3):
        #  ax[i,j].text(0.5,0.5,str((i,j)),fontsize=18,ha='center')

# plt.show()

# ###################################################################

from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
from sklearn.manifold import Isomap

digits = load_digits(n_class=6)
# fig,ax = plt.subplots(8,8,figsize=(6,6))
# for i,axi in enumerate(ax.flat):
#     axi.imshow(digits.images[i],cmap='binary')
    # axi.set(xticks[],yticks[])

iso = Isomap(n_components=2)
projection = iso.fit_transform(digits.data)
plt.scatter(projection[:,0],projection[:,1],lw=0.1,c=digits.target,
            cmap=plt.cm.get_cmap('cubehelix',6))
plt.colorbar(ticks=range(6),label='digit value')
plt.clim(-0.5,5.5)


plt.show()
