import math
from measured_data import *
from statistics import mean, stdev, variance, pstdev
T = [t / 10 for t in T_10]  # 单次振动周期，单位 s
T_mean = mean(T)
print("单次振动周期 T 平均值 =", round(T_mean, 4), "s")
sigma_T = stdev(T)
print("单次振动周期 T 标准差 =", round(sigma_T, 8), "s")
sigma_10T = stdev(T_10)
print("10次振动周期 10T 标准差 =", round(sigma_10T, 7), "s")
# 肖维涅定理剔除粗差
T_filtered = [t/10 for t in T_10 if abs(t/10 - T_mean) <= 1.96 * sigma_T]
if len(T_filtered) < len(T_10):
    print(f"剔除 {len(T_10) - len(T_filtered)} 个粗差")
    removed = [t/10 for t in T_10 if abs(t/10 - T_mean) > 1.96 * sigma_T]
    print("被剔除的数据:", removed)
    T_mean = mean(T_filtered)
    sigma_T = stdev(T_filtered)
    sigma_10T = stdev([t*10 for t in T_filtered])
    print("剔除后 T 平均值 =", round(T_mean, 7), "s")
    print("剔除后 T 标准差 =", round(sigma_T, 7), "s")
    print("剔除后 10T 标准差 =", round(sigma_10T, 7), "s")
T_mean = mean(T_filtered)
delta_b = 0.0005 * 0.95
# TODO: confirm the calculation of delta_a, I choose t_0.95 = 2.31 for n = 9
print(len(T_filtered))
delta_a = 2.31 * sigma_T / math.sqrt(len(T_filtered))  
u = math.sqrt(delta_a**2 + delta_b**2)
print("T 不确定度 u =", round(u, 8), "s")


delta_b_M = 0.05 * 0.95

U = math.sqrt((delta_b_M)**2)

print("M 不确定度 U =", round(U, 4), "g")


k = 4 * math.pi**2 * (1/3*mean(M)+mean(m_2)) * 1e-3 / T_mean**2
print("弹簧劲度系数 k =", round(k, 6), "N/m")