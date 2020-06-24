import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn;seaborn.set()

a = np.array([0,1,2])
b = np.array([5,5,5])
#print(a + b)

#如果两个数组的维度不一样可以进行计算操作吗
#print(a + 5)
M = np.ones(3)
#print(M)
#print(M + a)

a = np.arange(3)
b = np.arange(3)[:,np.newaxis]
# print(a)
# print(b)

'''
numpy的广播规则
规则一：如果两个数组的维度数不同，那么小维度数组的形状将会在最左边补1
规则二：如果两个数组的形状在任何一个维度上都不匹配，那么数组的形状会沿着维度为1的维度扩展以匹配另外一个数组的形状
规则三：如果两个数组的形状在任何一个维度上都不匹配并且没有任何一个维度等于1，那么就会引发异常
'''

#规则一
M = np.ones((2,3))
a = np.arange(3)
# print(M,'<-->',a)
# print(a + M)

#规则三
M = np.ones((3,2))
a = np.arange(3)
# print(M,a)
# print(M + a)

#广播规则的应用
#数组的归一化
X = np.random.random((10,3))
# print(X.mean(0))
Xmean = X.mean(0)
#print(Xmean)
X_contered = X - Xmean # 广播机制
# print(X,X_contered)
# print(X_contered.mean(0))

# numpy 比较，掩码和布尔逻辑
rainfall = pd.read_csv('Python\data\Seattle2014.csv')['PRCP'].values
# print(rainfall)
inches = rainfall / 254 # 将毫米转换为英寸
# print(inches)
# plt.hist(inches,40)
# plt.show()

# numpy 的比较运算(核心结果：bool值的一种展现)
x = np.array([1,2,3,4,5])
# print(x < 3)
'''
== 全等于 (=赋值：变量赋值，变量的重定向，==等于，等同，一样，相同)
!= 不等于 (不一样，不同，异常)
>< 大于小于 (比较运算：x<y,x>y)
<= >= 小于等于，大于等于 (比较运算)
返回的结果：bool值 布尔值
计算机语言的功能：
1.稳定的计算结果
2.循环
3.判断
4.高速的运算结果
'''
rng = np.random.RandomState(0) # 随机数种子(固定随机状态)
x = rng.randint(10,size=(3,4))
# print(x)
# print(x < 6)

# 小于6的数字有多少
# print(np.count_nonzero(x < 6)) # 比较运算之后的统计
# print(np.sum(x < 6)) # 聚合方法
# print(np.sum(x < 6,axis=1)) # 比较行(axis=1)
# print(np.sum(x < 6,axis=0)) # 比较列(axis=0)
# print(np.any(x > 0)) # 比较任意值 

# 花哨索引 (花哨：与其他不同比较有个性。索引：利用索引的方式取值或改变值)
rand = np.random.RandomState(0)
x = rand.randint(100,size=10)
ind = [3,7,4] # 花哨索引方式
# print(x[ind])
# print(x[3],x[7],x[4])

ind = np.array([[3,7],
                [4,5]]) # 花哨索引的方式：利用数组结构与形状当作角标取出索引值
# print(x[ind])

X = np.arange(12).reshape((3,4)) # 花哨索引方式：利用两个数组当作索引，然后通过索引获取周围数组的当中的值
# print(X)
row = np.array([0,1,2])
col = np.array([2,1,3])
# print(X[row,col])

# 组合索引
# print(X[1:,[2,0,1]]) # 组合花哨索引：切片+花哨的方式

# 示例：
mean = [0,0]
cov = [[1,2],
       [2,5]]
X = rand.multivariate_normal(mean,cov,100)
# plt.scatter(X[:,0],X[:,1])
# plt.show()
# print(X.shape) # 数组的结构

# indices = np.random.choice(a.shape[0], 20,replace=False)
# a[indices]

# 利用花哨索引修改数组当中的值
x = np.arange(10)
i = np.array([2,1,8,4])
x[i] = 99
# print(x)

# 数组的排序
# 选择排序
# def test(x):
#        print(len(x))
#        for i in range(len(x)):
#               swap = i + np.argmin(x[i:])
#               print(i,'<-->',swap)
#               # print(x[i],'<-++->','index:%s'%swap,x[swap])
#               x[i],x[swap] = x[swap],x[i]
#        return x

# if __name__ == "__main__":
#     x = np.array([2,1,4,3,5])
#     print(test(x))

# 利用numpy函数进行快速排序
x = np.array([2,1,4,3,5])
# print(np.sort(x))
# print(np.argsort(x))

# 沿着行或者列进行排序
rand = np.random.RandomState(0) # 随机种子数
X = rand.randint(0,10,(4,6))
# print(X)
# print(np.sort(X,axis=0))
# print(np.sort(X,axis=1))

# 部分排序(部分无规则排序)
x = np.array([7,2,3,1,6,5,4])
# print(np.partition(x,3))
# print(np.partition(x,3,axis=1))

# 排序综合示例
X = rand.randint(0,10,(4,6))
print(X)
plt.scatter(X[:,0],X[:,1])
plt.show()
