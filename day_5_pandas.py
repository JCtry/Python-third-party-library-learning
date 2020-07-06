# 多级索引的取值与取片

import numpy as np
import pandas as pd

# 层级索引
index = [('california',2000),('california',2010),
         ('new york',2000),('new york',2010),
         ('texas',2000),('texas',2010)
         ]
population = [33871648,37253956,
              18976457,19378102,
              20851820,25145561
              ]
pop = pd.Series(population,index=index)
# print(pop)
index = pd.MultiIndex.from_tuples(index) # 制作多级索引
pop = pop.reindex(index) # 利用多级索引替换现有索引形成新的df对象
pop.index.names = ['state','year']
# 精确查找，单个取值
# print(pop['texas'],2010)
# 局部取值
# print(pop['texas'])
# 切片(开始结束的索引都要)
# print(pop['california':'new york'])
# 切二级索引
# print(pop[:,2000])
# 花哨索引
# print(pop[['california':'new york']])

# ##########################################################

# df对象的多级索引
# 多级的列索引
index = pd.MultiIndex.from_product([[2013,2014],[1,2]]
                                    names=['year','visit']
                                    )

columns = pd.MultiIndex.from_product([['bob','guido','sue'],['hr','temp']],
                                    names=['subject','type']
                                    )

data = np.round(np.random.randn(4,6),1)
# print(data)
data[:,::2] *= 10
data += 37
health_data = pd.DataFrame(DATA,index=index,columns=columns)
# print(health_data)
# 精确索引
# print(health_data['bob','hr'])
# 通过索引值的方式查询(iloc索引器负责找索引值)
# print(health_data.iloc[:2,:2])
# loc索引器的用法
# print(health_data.loc[:,('bob','hr')])

# #########################################################
# 多级索引的行列转换
index = pd.MultiIndex.from_product([['a','b','c'],[1,2]])
data = pd.Series(np.random.rand(6),index=index)
data.index.names = ['char','int']
# print(data['a':'b'])
# print(data.unstack()) # 行列转换

# print(data)
# print(pop)
# print(pop.unstack())
# print(pop.unstack(level=0))

# 索引的设置与重置
pop_flat = pop.reset_index(name='populations') # 重新添加索引
pop_flat = pop_flat.set_index(['state','year'])
print(pop_flat.index)


