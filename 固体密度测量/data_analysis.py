import math
from decimal import Decimal, ROUND_HALF_UP
from measured_data import *
import statistics as stats
from statistics import mean, stdev, variance, pstdev
import numpy as np
 
# 处理零点误差
d_1 = [x - x_0 for x in x_1]
d_2 = [x - x_0 for x in x_2]
d_3 = [x - x_0 for x in x_3]

def process_data_methodata(d,m):
    '''处理方法一的数据'''
    print("mean of data:", mean(d))
    print("standard deviation of data:", stdev(d), "四舍五入后：", round(stdev(d), 4))
    # 依据拉依达定理剔除粗差：
    delta_data = [abs(x - mean(d)) for x in d]
    d = [d[i] for i in range(len(d)) if delta_data[i] <= 3 * stdev(d)]
    if len(d) < 6:
        print("after removing outliers,  data:", d)
        print("mean of data after removing outliers:", mean(d))
        print("standard deviation of data after removing outliers:", stdev(d), "四舍五入后：", round(stdev(d), 4))
    else:
        print("no outliers detected in data.")
    delta_a = 1.05 * stdev(d)
    print("delta_a =", delta_a, "mm")
    delta_b = 0.95 * 0.004 # 0.004mm为螺旋测微仪的仪器误差
    print("delta_b =", delta_b, "mm")
    uncertainty_u = round(math.sqrt(delta_a**2 + delta_b**2), 3)
    print("d的不确定度 U =", uncertainty_u, "mm")
    print("最终结果 d =", round(mean(d), 4), "±", uncertainty_u, "mm")
    
    rou = 6 * m / (math.pi * (mean(d)/2)**3) # g/mm^3
    print("密度 rou =", rou, "g/mm^3")
    


print("方法一，物体1数据处理结果：")
process_data_methodata(d_1, m_1)
print()
print("方法一，物体2数据处理结果：")
process_data_methodata(d_2, m_2)
print()
print("方法一，物体3数据处理结果：")
process_data_methodata(d_3, m_3)