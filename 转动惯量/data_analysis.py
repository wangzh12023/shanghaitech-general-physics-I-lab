import math
from measured_data import *
from statistics import mean, stdev, variance, pstdev
 
# 处理零点误差
d_1 = [x - x_0 for x in x_1]
d_2 = [x - x_0 for x in x_2]
d_3 = [x - x_0 for x in x_3]

def process_data_method1(d,m):
    '''处理方法一的数据'''
    print("mass m =", m, "g")
    d = [round(x, 3) for x in d]
    print("raw data d:", d)
    print("mean of data:", mean(d))
    print("standard deviation of data:", stdev(d), "四舍五入后：", round(stdev(d), 4))
    # 依据拉依达定理剔除粗差：
    delta_data = [round(abs(x - round(mean(d), 4)), 4) for x in d]
    print("deviation from mean for each data point:", delta_data)
    d = [d[i] for i in range(len(d)) if delta_data[i] <= 3 * stdev(d)]
    print("3 sigma:", round(3 * stdev(d), 7))
    if len(d) < 6:
        print("after removing outliers,  data:", d)
        print("mean of data after removing outliers:", mean(d))
        print("standard deviation of data after removing outliers:", stdev(d), "四舍五入后：", round(stdev(d), 4))
    else:
        print("no outliers detected in data.")
    delta_a = 1.05 * stdev(d)
    print("delta_a =", delta_a, "四舍五入后：", round(delta_a, 4))
    delta_b = 0.95 * 0.004 # 0.004mm为螺旋测微仪的仪器误差
    print("delta_b =", delta_b, "四舍五入后：", round(delta_b, 4))
    uncertainty_u = round(math.sqrt(delta_a**2 + delta_b**2), 3)
    print("最终结果 d =", round(mean(d), 4), "±", uncertainty_u, "mm")
    
    rou = 6 * m / (3.141593 * (mean(d))**3) # g/mm^3, pi 取 6位有效数字
    print("密度 rou =", rou, "g/mm^3", "有效数字取测量值最小有效数字")
    
def process_data_method2(m_before, m_after, m):
    '''处理方法二的数据'''
    M_1_2 = [round(m_after[i] - m_before[i], 2) for i in range(len(m_before))]
    print("mass m of object:", m)
    print("raw data M_1_2 (m_after - m_before):", M_1_2)
    mean_M_1_2 = mean(M_1_2)
    print("mean of M_1_2:", mean_M_1_2)
    print("standard deviation of M_1_2:", stdev(M_1_2), "四舍五入后：", round(stdev(M_1_2), 4))
    # 依据拉依达定理剔除粗差：
    delta_M_1_2 = [round(abs(x - round(mean_M_1_2, 3)), 3) for x in M_1_2]
    print("deviation from mean for each data point:", delta_M_1_2)
    print("3 sigma:", round(3 * stdev(M_1_2), 7), "四舍五入后：", round(3 * stdev(M_1_2), 4))
    M_1_2 = [M_1_2[i] for i in range(len(M_1_2)) if delta_M_1_2[i] <= 3 * stdev(M_1_2)]
    if len(M_1_2) < 6:
        print("after removing outliers,  data:", M_1_2)
        print("mean of data after removing outliers:", mean(M_1_2))
        print("standard deviation of data after removing outliers:", stdev(M_1_2))
    else:
        print("no outliers detected in data.")
    delta_a_M = 1.05 * stdev(M_1_2)
    print("delta_a_M =", delta_a_M, "g")
    delta_b_M = 0.95 * 0.005
    print("delta_b_M =", delta_b_M, "g")
    uncertainty_u_M = round(math.sqrt(delta_a_M**2 + delta_b_M**2), 2)
    print("M_1_2的不确定度 U_M =", uncertainty_u_M, "g")
    print("最终结果 M_1_2 =", round(mean(M_1_2), 2), "±", uncertainty_u_M, "g") 
    rou = m / mean(M_1_2)
    print("密度 rou =", rou, "g/mm^3", "有效数字取测量值最小有效数字") 


print("方法一，物体1数据处理结果：")
process_data_method1(d_1, m_1)
print()
print("方法一，物体2数据处理结果：")
process_data_method1(d_2, m_2)
print()
print("方法一，物体3数据处理结果：")
process_data_method1(d_3, m_3)


print()
print("方法二，物体1数据处理结果：")
process_data_method2(m_before_1, m_after_1, m_1)
print()
print("方法二，物体2数据处理结果：")
process_data_method2(m_before_2, m_after_2, m_2)
print()
print("方法二，物体3数据处理结果：")
process_data_method2(m_before_3, m_after_3, m_3)