# pandas库的学习
import pandas as pd
import numpy as np

'''
pandas的数据类型
Series
dataframe
index

1.pd.Series(data,[index])
2.pd.Series(dict)
利用索引的方式寻值
Series['key'] --> values
'''

# Series对象可以有index值
data = pd.Series([0.25,0.5,0.75,1.0],index=['a','b','c','d'])
# print(data)
# print(data.values)
# print(data.index)

# Series 也是一个特殊的字典
population_dict = {                 # python字典
    'califarnia':38332521,
    'ny':26448193,
    'floride':19552860,
    'illinois':12882135,
}
population = pd.Series(population_dict) # 用字典去创建Series对象顺序是默认的
# print(population['ny'])
# print(population)
# 和字典不一样的是字典是没有索引操作的
# print(population['califarnia':'illinois'])

# 创建一个Series对象
# pd.Series(data,index=index)
# print(pd.Series([2,4,6]))
# 创建一个带有index值的Series对象
# print(pd.Series(5,index=[100,200,300]))
# 通过直接传一个字典来创建一个Series对象
# print(pd.Series({2:'a',1:'b',3:'c'}))

# dataframe 对象

population_dict = {                 # python字典
    '加利福尼亚':38332521,
    '纽约':26448193,
    '佛罗里达州':19552860,
    '伊利诺伊州':12882135,
}
population = pd.Series(population_dict) # 用字典去创建Series对象顺序是默认的

area_dict = {
    '加利福尼亚':423967,
    '纽约':141297,
    '佛罗里达州':170312,
    '伊利诺伊州':149995,
}
area = pd.Series(area_dict)

# 把两个Series对象传到DataFrame里面
states = pd.DataFrame({'人口总数':population,'州面积':area_dict})
# print(states.index) # 显示行索引
# print(states.columns) # 显示列索引
# print(states)
# print('~~~~~~~~通过键取它的值~~~~~~~~')
# 我们认为DataFrame对象是一个特殊的字典，它具有特殊的键值关系
# print(states['州面积']['纽约'])

# 针对DataFrame对象的建立进行阐述
# 通过单个 / 多个Series对象创建DataFrame对象
res1 = pd.DataFrame(population,columns=['人口数']) # 再添加额外的列时，接收的类型为列表数据类型
# print(population)
# print(res1)

# 通过字典列表的方式创建DataFrame对象
data = [{'a':i,'b':2*i} for i in range(3)] # 通过列表推导式生成的
# print(data)
# print(pd.DataFrame(data))
# print(pd.DataFrame(data,index=['num1','num2','num3']))

# # 列表推导式
# list_test = ['jack','mack','tom']
# # 我们要让列表中的值添加为：name:list_value(通过列表推导式实现)
# name = [{'name':i} for i in (list_test)]
# print(name)

# 通过numpy数组的方式创建DataFrame(不光能创建表格还能对numpy数组进行相应的调整与数据结构化)
res = np.random.rand(3,2)
# print(res)
# print(pd.DataFrame(res,columns=['foo','bar'],index=['a','b','c']))

# pandas的index对象(其实就是一个有序的集合)
# ind = pd.Index(2,3,5,7,11)
# print(ind[::2])
# print(ind[0])

# pandas数据类型的查询方式
# Series 数据类型进行索引操作
data = pd.Series([0.25,0.5,0.75,1.0],index=[['a','b','c','d']])
# print(data['b'])

# Series对象进行索引、值的成员检测
# print('e' in data)
# print(data.keys())
# print(data.items()) # 能利用items方法进行类似于字典的操作

# 索引器 loc为显式索引器
data = pd.Series(['a','b','c'],index==[1,3,5])
# print(data[1:3])
# print(data.loc[1:3])  # 显式索引器中引用的是index值

# 索引器 隐式索引器iloc
# print(data.iloc[1])  # 隐式索引器中引用的是角标

# DataFrame 对象的数据选择方法
population_dict = {                 # python字典
    '加利福尼亚':38332521,
    '纽约':26448193,
    '佛罗里达州':19552860,
    '伊利诺伊州':12882135,
}
population = pd.Series(population_dict) # 用字典去创建Series对象顺序是默认的
area_dict = {
    '加利福尼亚':423967,
    '纽约':141297,
    '佛罗里达州':170312,
    '伊利诺伊州':149995,
}
area = pd.Series(area_dict)

# 把两个Series对象传到DataFrame里面
data = pd.DataFrame({'number':population,'area':area_dict})
# print(data)
# print('~~~~~~~~~~~~~~~~~~~~~~~~~')
# 取出一列值 通过python字典的方式进行选择
# print(data['area'])
# print(data.area) # 通过属性方式进行数据选择
'''
1.如果列名不是纯字符串不可以使用属性操作
2.如果列名与DataFrame中的方法名重复也不可以
'''
# 临时增加列(如果从表格中导入数据不会对元数据产生伤害)
data['pa'] = data.number / data.area
# print(data)

# 将DataFrame对象数组化(有助于你的理解)
# print(data.values)

# DataFrame对象的转置操作(转置后数据会被结构化)
# print(data.T)

# 利用索引器进行DataFrame操作
# DataFrame对象隐式索引器(也同样支持索引器操作)
# print(data)
# print(data.iloc[:3,:2])

# DataFrame对象的显式索引器
# print(data.loc[:'佛罗里达州',:'p/a'])

'''
DataFrame对象中显式与隐式索引器的区别是
显式索引器可以直接利用二维数组的索引值进行切片操作
隐式索引器只能进行利用索引角标进行取片操作
'''

# DataFrame对象显式索引器的花哨索引(数组化之后-->二维数组)
# print(data.loc[data.pa > 100,['number','pa']])
# data.iloc[0,2] = 90
# print(data)

# 其它取值方式(与切片操作不同)
# print(data['加利福尼亚':'佛罗里达州']) # 不遵循常规的取值范围(start:end:step) start <= x < end
# 切片操作
# print(data[1:3])



