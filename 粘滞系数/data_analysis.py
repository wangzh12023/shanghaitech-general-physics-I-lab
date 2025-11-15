import math
from measured_data import *
from statistics import mean, stdev, variance, pstdev


d = [round(i - x_0, 3) for i in d]  #去零差
print("d =", d)
mean_d = mean(d)
stdev_d = stdev(d)
print(f"平均值 = {mean_d} mm")
print(f"标准差 = {stdev_d} mm") 
print("肖维涅定理阈值：" , 1.65 * stdev_d)
#delta a
delta_a = 2.78 * stdev_d / math.sqrt(len(d))  # mm 读数误差

delta_b = 0.95 * 0.0005  # mm 读数误差
print(f"测量误差 delta_a = {delta_a} mm")
print(f"测量误差 delta_b = {delta_b} mm")
U  = math.sqrt(delta_a**2 + delta_b**2)
print(f"合成标准不确定度 U = {U} mm")

mean_t_23 = mean(t_23)
mean_t_25 = mean(t_25)
mean_t_27 = mean(t_27)
mean_t_29 = mean(t_29)
mean_t_31 = mean(t_31)
mean_t_32 = mean(t_32)

stdev_t_23 = stdev(t_23)
stdev_t_25 = stdev(t_25)
stdev_t_27 = stdev(t_27)
stdev_t_29 = stdev(t_29)
stdev_t_31 = stdev(t_31)
stdev_t_32 = stdev(t_32)

print(f"平均温度 t_23 = {mean_t_23} s, 标准差 = {stdev_t_23} s")
print("肖维涅定理阈值：" , 1.65 * stdev_t_23)
#验证是否有粗差
for i in t_23:
    if abs(i - mean_t_23) > 1.65 * stdev_t_23:
        print("t_23 有粗差：", i)
        break
print(f"平均温度 t_25 = {mean_t_25} s, 标准差 = {stdev_t_25} s")
print("肖维涅定理阈值：" , 1.65 * stdev_t_25)
for i in t_25:
    if abs(i - mean_t_25) > 1.65 * stdev_t_25:
        print("==========t_25 有粗差===============：", i)
        break
print(f"平均温度 t_27 = {mean_t_27} s, 标准差 = {stdev_t_27} s")
print("肖维涅定理阈值：" , 1.65 * stdev_t_27)
for i in t_27:
    if abs(i - mean_t_27) > 1.65 * stdev_t_27:
        print("==========t_27 有粗差===============：", i)
        break
print(f"平均温度 t_29 = {mean_t_29} s, 标准差 = {stdev_t_29} s")
print("肖维涅定理阈值：" , 1.65 * stdev_t_29)
for i in t_27:
    if abs(i - mean_t_27) > 1.65 * stdev_t_27:
        print("==========t_27 有粗差===============：", i)
        break
print(f"平均温度 t_29 = {mean_t_29} s, 标准差 = {stdev_t_29} s")
print("肖维涅定理阈值：" , 1.65 * stdev_t_29)
for i in t_29:
    if abs(i - mean_t_29) > 1.65 * stdev_t_29:
        print("==========t_29 有粗差===============：", i)
        break
print(f"平均温度 t_31 = {mean_t_31} s, 标准差 = {stdev_t_31} s")
print("肖维涅定理阈值：" , 1.65 * stdev_t_31)
for i in t_31:
    if abs(i - mean_t_31) > 1.65 * stdev_t_31:
        print("==========t_31 有粗差===============：", i)
        break
print(f"平均温度 t_32 = {mean_t_32} s, 标准差 = {stdev_t_32} s")
print("肖维涅定理阈值：" , 1.65 * stdev_t_32)
for i in t_32:
    if abs(i - mean_t_32) > 1.65 * stdev_t_32:
        print("==========t_32 有粗差===============：", i)
        break

delta_a_t_23 = 2.78 * stdev_t_23 / math.sqrt(len(t_23))
delta_a_t_25 = 2.78 * stdev_t_25 / math.sqrt(len(t_25))
delta_a_t_27 = 2.78 * stdev_t_27 / math.sqrt(len(t_27))
delta_a_t_29 = 2.78 * stdev_t_29 / math.sqrt(len(t_29))
delta_a_t_31 = 2.78 * stdev_t_31 / math.sqrt(len(t_31))
delta_a_t_32 = 2.78 * stdev_t_32 / math.sqrt(len(t_32))
print(f"delta_a_t_23 = {delta_a_t_23} s")
print(f"delta_a_t_25 = {delta_a_t_25} s")
print(f"delta_a_t_27 = {delta_a_t_27} s")
print(f"delta_a_t_29 = {delta_a_t_29} s")
print(f"delta_a_t_31 = {delta_a_t_31} s")
print(f"delta_a_t_32 = {delta_a_t_32} s")
delta_b_t = 0.95 * 0.005
print(f"delta_b_t = {delta_b_t} s")
U_23 = math.sqrt(delta_a_t_23**2 + delta_b_t**2)
U_25 = math.sqrt(delta_a_t_25**2 + delta_b_t**2)
U_27 = math.sqrt(delta_a_t_27**2 + delta_b_t**2)
U_29 = math.sqrt(delta_a_t_29**2 + delta_b_t**2)
U_31 = math.sqrt(delta_a_t_31**2 + delta_b_t**2)
U_32 = math.sqrt(delta_a_t_32**2 + delta_b_t**2)
print(f"温度测量合成标准不确定度 U_23 = {U_23} s")
print(f"温度测量合成标准不确定度 U_25 = {U_25} s")
print(f"温度测量合成标准不确定度 U_27 = {U_27} s")
print(f"温度测量合成标准不确定度 U_29 = {U_29} s")
print(f"温度测量合成标准不确定度 U_31 = {U_31} s")
print(f"温度测量合成标准不确定度 U_32 = {U_32} s")
v_0_23 = L / mean_t_23
v_0_25 = L / mean_t_25
v_0_27 = L / mean_t_27
v_0_29 = L / mean_t_29
v_0_31 = L / mean_t_31
v_0_32 = L / mean_t_32

print(f" v_0_23 = {v_0_23} m/s")
print(f" v_0_25 = {v_0_25} m/s")
print(f" v_0_27 = {v_0_27} m/s")
print(f" v_0_29 = {v_0_29} m/s")
print(f" v_0_31 = {v_0_31} m/s")
print(f" v_0_32 = {v_0_32} m/s")


# 计算eta
d = mean_d 
eta_1 = (((rho - rho_0) * 9.7940 * d**2) / (18 * v_0 * (1 + 2.4 * d / D))) - ((3/16) * v_0 * d * rho_0)