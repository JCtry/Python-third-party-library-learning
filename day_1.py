# numpy 入门
# pip install numpy  pip install pandas

import numpy as np  # 导入numpy库并且重新命名为np
from scipy import special
import pandas as pd
import matplotlib.pyplot as plt


# 创建一个长度为10 数组当中值都为0
np.zeros(10, dtype='float')
'''
bool_  布尔值（真假），用一个字节存储
int_   默认类型（通常情况下int64或者int32）
int8   字节（byte ，范围-128到127）
int16  整型（范围从-32768-32767）
int64  整型（范围-9223372036854775808 - 9223372036854775807）
float_ float64类型的简化形式
float16 半精度浮点型 
'''
# 创建一个3X5的浮点型数组，并且数组当中的内容都为3.14
np.full((3, 5), 3.14)
# 创建一个3*5的数组，数组的值一个线性序列
np.arange(0, 20, 2)
# 创建一个5各元素的数组，这5各数均匀的分配到0-1
np.linspace(0, 1, 5)
# 创建一个3*3的，在0-1均匀分布的随机数组成的数组
np.random.random((3, 3))
# 创建一个3*3的，均值为0，方差为1的正态分布的随机数数组
np.random.normal(0, 1, (3, 3))
# 创建一个3*3的，【0-10】区间的随机整型数组
np.random.randint(0, 10, (3, 3))

# numpy 数组的属性
# np.random.seed(0) # 设置随机数种子

x1 = np.random.randint(10, size=6)
x2 = np.random.randint(10, size=(3, 4))
x3 = np.random.randint(10, size=(3, 4, 5))
# 常见的数组属性介绍
# print('x3的维度为:',x3.ndim)
# print('x3的形状：',x3.shape)
# print('x3的整体大小',x3.size)

# 数组的索引
# print(x1)
# print(x1[-1])

# 数组的取值范围（X，Y）
# x2[1,2] = 12
# print(x2)
# print(x2[1,2])

# 数组的切片
# 一维数组的切片操作
x = np.arange(10)
# print(x[5:1:-1])  # 如果从-1开始所有元素去逆序

# 多维数组的取片操作
# print(x2)
# print(x2[:2,:2])

# 数组的变形
grid = np.arange(1, 10).reshape((3, 3))  # 将1-9放入一个3*3的矩阵当中
# print(grid)

x = np.array([1, 2, 3])
# print(x)
# print(x.reshape((1,3)))
# print(x.reshape((3,1)))
# print(x[:,np.newaxis])

# 数组的拼接
x = np.array([1, 2, 3])
y = np.array([3, 2, 1])
z = np.array([99, 99, 99])
# print(np.concatenate([x,y,z]))
grid = np.array([[1, 2, 3],
                 [4, 5, 6]
])
# np.concatenate([grid,grid],axis=1)

# 按固定维度拼接
x = np.array([1, 2, 3])
grid = np.array([[9, 8, 7], [6, 5, 4]])
y = np.array([[99],
              [99]
              ])
# print(np.hstack([grid,y]))
# print(np.vstack([x,grid]))

# 数组的分裂
x = [1, 2, 3, 99, 99, 3, 2, 1]
x1, x2, x3 = np.split(x, [3, 5])
# print(x1)
# print(x2)
# print(x3)
# 垂直分裂
grid = np.arange(16).reshape((4, 4))
upper, lower = np.vsplit(grid, [2])
# print(upper)
# print(lower)

# 水平分裂
left, right = np.hsplit(grid, [2])
# print(left)
# print(right)

# numpy 的函数操作
# numpy的运算
x = np.arange(4)
# print('原数组为：',x)
# print('加法操作为：',x + 5)
# print('减法操作为：',x - 5)
# print('乘法操作为：',x * 5)
# print('除法操作为：',x / 2)
# print('地板法操作为：',x // 2)  # 取商运算
# print('取反：',-x)
# print('幂运算：',x ** 2)
# print('取余运算：',x % 2)      # 取余数
#
# # 函数式数组运算
# # 加法
# print('~~~~函数式的数组运算~~~~')
# print(np.add(x,5))             # 加法
# print(np.subtract(x,5))        # 减法
# print(np.negative(x))          # 负数运算
# print(np.multiply(x,3))        # 乘法运算
# print(np.divide(x,2))          # 除法操作
# print(np.floor_divide(x,2))    # 地板除
# print(np.power(x,2))           # 指数运算
# print(np.mod(x,2))             # 取余运算

# 绝对值运算
x = np.array([-2, -1, 0, 1, 2])
# print(abs(x))
# print(np.absolute(x))

# 三角函数
theta = np.linspace(0, np.pi, 3)
# print(theta)
# print(np.sin(theta))
# print(np.cos(theta))
# print(np.tan(theta))

# 逆三角函数
x = [-1, 0, 1]
# print('~~~~~~逆三角函数~~~~~~')
# print(np.arcsin(x))
# print(np.arccos(x))
# print(np.arctan(x))

# 指数和对数的相关函数
x = [1, 2, 3]
# print(x)
# print('e^x:',np.exp(x))
# print('2^x:',np.exp2(x))
# print('3^x',np.power(3,x))

# 对数运算
x = [1, 2, 4, 10]
# print(x)
# print('ln(x):',np.log(x))
# print('log2(x)',np.log2(x))

# gamma函数伽马
x = [1, 5, 10]
# print('gama:',special.gamma(x))
# print('ln|gama(x)|:',special.gammaln(x))
# print('beta(x,2):',special.beta(x,2))

# 误差函数（高斯积分）
x = np.array([0, 0.3, 0.7, 1.0])
# print('erf(x):',special.erf(x))
# print('erfc(x):',special.erfc(x))
# print('erfinv(x)',special.erfcinv(x))

# numpy的高级通用函数特性
# 指定输出
x = np.arange(5)
y = np.empty(5)
np.multiply(x, 10, out=y)
y = np.zeros(10)
np.power(2, x, out=y[::2])
# print(y)

# numpy 的聚合
x = np.arange(1, 6)
# print(np.add.reduce(x))        # 求和
# print(np.multiply.reduce(x))   # 阶乘

# numpy 每一步计算结果都能看到
# print(np.add.accumulate(x))
# print(np.multiply.accumulate(x))

# numpy的更多聚合操作
L = np.random.random(100)
# print(L)
# print(sum(L))     # 解释器-->编译器-->结果
# print(np.sum(L))  # 编译 ---------> 结果

# 最大值，最小值
big_array = np.random.rand(1000000)
# print(np.min(big_array))
# print(np.max(big_array))

# 多维度聚合操作
M = np.random.random((3, 4))
# print(M)
# print(M.sum())
# print(M.min())
# print(M.max())
# print(M.min(axis=0)) # axis=0就是按列查找最小值
# print(M.min(axis=1)) # 按行查找

'''
np.sum              求和 
np.prod             求和
np.mean             均值
np.std              方差
np.var              方差
np.min              最小值
np.max              最大值
np.argmin           最小值索引
np.argmax           最大值索引
np.median           中位数
np.percentile       排序统计值
np.any              验证任何一个元素是否为真
np.all              验证所有元素是否为真
'''
data = pd.read_csv('Data\president_heights.csv')
heights = np.array(data['height(cm)'])
print(heights)
print('总统身高的平均值：', heights.mean())
print('总统身高的方差：', heights.std())
print('总统身高的最小值：', heights.min())
print('总统身高的最大值：', heights.max())
print('总统身高1/4：', np.percentile(heights, 25))
print('总统身高的中间值：', np.median(heights))
print('总统占比值75%：', np.percentile(heights, 75))
plt.hist(heights)
plt.title('zt-heights')
plt.xlabel('cm')
plt.ylabel('numbers')
plt.show()
