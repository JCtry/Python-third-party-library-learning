import numpy as np
import pandas as pd

# 随机数对象
rng = np.random.RandomState(42)
print(rng)

# 通用函数 : dataframe数据类型与series数据类型的运算
area = pd.Series({'alaska':172337,'texas':695662,'california':423967},name='area')
population = pd.Series({'newyork':19651127,'texas':26448193,'california':38332521},name='population')

# population / area 人口除以面积 == 比值
# print(population/area)
# 索引值的并集操作
# print(area.index | population.index)
# NaN值的产生环境
A = pd.Series([2,4,6],index=[0,1,2])
B = pd.Series([1,3,5],index=[1,2,3])
# print(A+B)
# 做等价相加可以避免缺失值的情况
# print(A.add(B,fill_value=0))

# dataframe数据类型的索引对齐
a = pd.DataFrame(rng.randint(0,20,(2,2)),columns=['A','B'])
# print(a)
b = pd.DataFrame(rng.randint(0,10,(3,3)),columns=['B','A','C'])
# print(b)
# print(a+b)
# 缺失值的处理
fill = a.stack().mean() # 将平均值取代nan值
# print(a.add(b,fill_value=fill))

# 运算
a1 = rng.randint(10,size=(3,4))
# print(a1)
# print(a1[0])
# print(a1-a1[0])

df = pd.DataFrame(a1,columns=list('qrst'))
# print(df)
# print(df['r'])
# print(df.subtract(df['r'],axis=0))

# 缺失值的数据类型以及区别 null , NaN , NA


# 缺失值的处理
vals1 = np.array([1,None,3,4])
# print(vals1)
vals2 = np.array([1,np.nan,3,4])
# print(vals2)

# nan值可以进行运算么?
# print(1 / np.nan)
# print(vals2.mean())
# print(vals2.sum())
# print(vals2.std())
# print(vals2.max())
# print(vals2.min())
# pandas中的缺失值 与 python自带的None值还是有区别的 nan <--> none
# print(pd.Series([1,np.nan,2,None]))
x = pd.Series(range(2),dtype=int)
x[0] = None
# print(x)

# 处理缺失值
# 第一种处理缺失值的方法 bool dataframe与series对象通用此方法
data = pd.Series([1,np.nan,'hello','None'])
# print(data) # 元数据
# print(data.isnull()) # 缺失值返回True
# print(data.notnull()) # 非缺失值返回True
# print('~~~~~~~~~~~~~~~~~~~~~~~~~')
# 剔除缺失值
# print(data.dropna()) # series对象的剔除缺失值
df = pd.DataFrame([[1,no.nan,2]
                   [2,3,5]
                   [np.nan,4,6]
                   ])
# print(df)
# print(df.dropna()) # 默认情况下dropna剔除的是nan值的行
# print(df.dropna(axis='columns'))  # 如果参数axis给了columns那么删除列
df[3] = np.nan
# print(df)
# print(df.dropna(axis='columns',how='all')) # how 参数为all删除整行或整列都必须为nan的行列
# print(df.dropna(axis='columns',how='any')) # how 参数为any只要是nan值都删除
# thresh参数的使用
# print(df.dropna(axis='rows',thresh=3)) # thresh 参数为保留非空的最小值

# 填充缺失值
data = pd.Series([1,np.nan,2,None,3],index=list('abcde'))
# print(data)
# print(data.fillna(0)) # fillna 函数可以将nan值替代某些参数

# 将有效值从前往后的填充到缺失值中
# print(data.fillna(method='ffill'))
# 从后往前传
# print(data.fillna(method='bfill'))

# dataframe 对象的填充方法
print(df)
print(df.fillna(method='bfill',axis=1)) # df对象的缺失值填充与series顺序一样但是分行与列 (axis)


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
# print(pop[('california',2000):('texas',2000)]) # 利用多级索引进行切片
# print(pop.index)
# for i in pop.index:
#     # print(i)
#     if i[1] == 2010:
#         print(i)
res = [for i in pop.index if i[1] == 2010] # 通过列表推导式或者for...in...遍历的方法虽然能实现但是操作复杂
# print(pop[res])

# 利用pandas多级索引 (简便方法)
index = pd.MultiIndex.from_tuples(index) # 制作多级索引
pop = pop.reindex(index) # 利用多级索引替换现有索引形成新的df对象
# print(pop)
# print(pop[: 'california'])

# 高维数据的多级索引
# unstack()函数 将复杂的多维series 转换为容易离家的df
pop_df = pop.unstack()
# print(pop_df)
# 逆操作
# print(pop_df.stack())
pop_df = pd.DataFrame({'total':pop,
                      'under18':[9267089,9284094,
                                 4687374,4318033,
                                 5906301,6879014
                                ]
                      })
# print(pop_df)
f_u18 = pop_df['under18'] / pop_df['total']
# print(f_u18.unstack())

# 多级索引的创建方法
df = pd.DataFrame(np.random.rand(4,2),
                  index=['a','b','c','d']
                  columns=['data1','data2']
                 )
#print(df)

#多级索引的等级名称
pop.index.names = ['state','year']
#print(pop)

#多级的列索引
index = pd.MultiIndex.from_product([[2013,2014],[1,2]],
                                    names = ['year','visit']
                                        )
columns =pd.MultiIndex.from_product([['bob','guido','sue'],['hr','temp']],
                                   names=['subject','type'])
data = np.round(np.random.randn(4,6),1)
#print(data)
data[:,::2] *= 10
data += 37
health_data = pd.DataFrame(data,index=index,columns=columns)
print(health_data['guido'])
