# 加强对分组的练习
import pandas as pd
import numpy as np
import math

# 数据导入
def info():
    columns = ['place','names','pattern','totalprice','price','direc','s','number','renovation','jg']
    ng_info =  pd.read_csv('Data\ng.csv',names=columns)
    return ng_info

# 价格
def price(ng_info):
    print('###########数据样本抽样展示##########')
    print(ng_info.head())
    # 房产销售总价
    print('###########房源价格展示##########')
    totail_price = ng_info.totalprice.sum()  # -->['price']
    print('数据内南岗区的房地产销售总额为：',totail_price*10000,'元人民币')
    total_price_dict = dict(ng_info.totalprice.describe())
    print('数据内南岗区的房地产销售单价最小值为：',total_price_dict['min'],'万元人民币')
    print('数据内南岗区的房地产销售单价最大值为：', total_price_dict['max'], '万元人民币')
    print('数据内南岗区的房地产销售单价1/4价格为：', math.floor(total_price_dict['25%']), '万元人民币')
    print('数据内南岗区的房地产销售单价1/2价格为：', math.floor(total_price_dict['50%']), '万元人民币')
    # 计算房产平均价格
    print('###########房源每平米价格展示##########')
    mean_price_m = ng_info.price.mean()
    mean_std = ng_info.price.std()
    m_dict = ng_info.price.describe()
    print('数据内南岗区的房地产每平米平均值额为：', mean_price_m , '元人民币')
    print('数据内南岗区的房地产每平米方差额为：', math.floor(mean_std), '元人民币')
    print('数据内南岗区的房地产每平米单价最大值为：', m_dict['max'], '万元人民币')
    print('数据内南岗区的房地产每平米单价1/4价格为：', math.floor(m_dict['25%']), '元人民币')
    print('数据内南岗区的房地产每平米单价1/2价格为：', math.floor(m_dict['50%']), '元人民币')
#地段分析
def place(ng_info):
    place_count = ng_info.groupby('place').price.count()
    print('最多房源区域:',place_count.idxmax(),'共计：',place_count.max(),'套房源')
    print('最少房源区域:', place_count.idxmin(), '共计：', place_count.min(), '套房源')
    names_count = ng_info.groupby('names').price.count()
    print('最多房源小区:', names_count.idxmax(), '共计：', names_count.max(), '套房源')
    print('最少房源小区:', names_count.idxmin(), '共计：', names_count.min(), '套房源')
# 房屋格局
def house_pattern(ng_info):
    pattern_count = ng_info.groupby('pattern').s.mean()
    descri_dict = dict(ng_info.pattern.describe())
    print(pattern_count)
    print('户型共计：',descri_dict['unique'],'种')
    print('户型最多为：', descri_dict['top'], '类量：',descri_dict['freq'],'套')
# 装修情况
def renovation(ng_info):
    renovation_count = ng_info.groupby('renovation').count()
    num2 = renovation_count.names['精装']
    renovation_dict = dict(ng_info.renovation.describe())
    print('装修种类一共：',renovation_dict['unique'],'种')
    print('最多的装修形式：',renovation_dict['top'],'有',renovation_dict['freq'],'个')
    print('排行第二的装修形式：精装' , '有',num2, '个')

if __name__ == '__main__':
    nangang_house_info = info()
    price(nangang_house_info)         # 价格分析
    print('########地段分析########')
    place(nangang_house_info)         # 地段分析
    print('########格局与面积分析########')
    house_pattern(nangang_house_info)   # 格局分析
    print('########装修风格########')
    renovation(nangang_house_info)
    