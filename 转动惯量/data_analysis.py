import math
from measured_data import *
from statistics import mean, stdev, variance, pstdev
 
 
mean_m = mean(m)
print("物体质量 m 平均值 =", round(mean_m, 4), "g")

sigma_m = stdev(m)
print("物体质量 m 标准差 =", round(sigma_m, 4), "g")

delta_a_m = 1.05 * sigma_m
print("物体质量 m delta_a =", round(delta_a_m, 4), "g")
delta_b_m = 0.5 * 0.1 * 0.95
print("物体质量 m delta_b =", round(delta_b_m, 4), "g")
U = math.sqrt(delta_a_m**2 + delta_b_m**2)
print("物体质量 m 最终不确定度 U =", round(U, 4), "g")

mean_M_c = mean(M_c)
print("圆环质量 M_c 平均值 =", round(mean_M_c, 4), "g")
sigma_M_c = stdev(M_c)
print("圆环质量 M_c 标准差 =", round(sigma_M_c, 4), "g")
delta_a_M_c = 1.05 * sigma_M_c
print("圆环质量 M_c delta_a =", round(delta_a_M_c, 4), "g")
delta_b_M_c = 0.5 * 0.1 * 0.95
print("圆环质量 M_c delta_b =", round(delta_b_M_c, 4), "g")
U_M_c = math.sqrt(delta_a_M_c**2 + delta_b_M_c**2)
print("圆环质量 M_c 最终不确定度 U_M_c =", round(U_M_c, 4), "g")

mean_M_1 = mean(M_1)
print("圆柱1质量 M_1 平均值 =", round(mean_M_1, 4), "g")
sigma_M_1 = stdev(M_1)
print("圆柱1质量 M_1 标准差 =", round(sigma_M_1, 4), "g")
delta_a_M_1 = 1.05 * sigma_M_1
print("圆柱1质量 M_1 delta_a =", round(delta_a_M_1, 4), "g")
delta_b_M_1 = 0.5 * 0.1 * 0.95
print("圆柱1质量 M_1 delta_b =", round(delta_b_M_1, 4), "g")
U_M_1 = math.sqrt(delta_a_M_1**2 + delta_b_M_1**2)
print("圆柱1质量 M_1 最终不确定度 U_M_1 =", round(U_M_1, 4), "g")

mean_M_2 = mean(M_2)
print("圆柱2质量 M_2 平均值 =", round(mean_M_2, 4), "g")
sigma_M_2 = stdev(M_2)
print("圆柱2质量 M_2 标准差 =", round(sigma_M_2, 4), "g")
delta_a_M_2 = 1.05 * sigma_M_2
print("圆柱2质量 M_2 delta_a =", round(delta_a_M_2, 4), "g")
delta_b_M_2 = 0.5 * 0.1 * 0.95
print("圆柱2质量 M_2 delta_b =", round(delta_b_M_2, 4), "g")
U_M_2 = math.sqrt(delta_a_M_2**2 + delta_b_M_2**2)
print("圆柱2质量 M_2 最终不确定度 U_M_2 =", round(U_M_2, 4), "g")

mean_D_o = mean(D_o)
print("圆环外径 D_o 平均值 =", round(mean_D_o, 4), "mm")
sigma_D_o = stdev(D_o)
print("圆环外径 D_o 标准差 =", round(sigma_D_o, 4), "mm")
delta_a_D_o = 1.05 * sigma_D_o
print("圆环外径 D_o delta_a =", round(delta_a_D_o, 4), "mm")
delta_b_D_o = 0.02 * 0.95
print("圆环外径 D_o delta_b =", round(delta_b_D_o, 4), "mm")
U_D_o = math.sqrt(delta_a_D_o**2 + delta_b_D_o**2)
print("圆环外径 D_o 最终不确定度 U_D_o =", round(U_D_o, 4), "mm")

mean_D_i = mean(D_i)
print("圆环内径 D_i 平均值 =", round(mean_D_i, 4), "mm")
sigma_D_i = stdev(D_i)
print("圆环内径 D_i 标准差 =", round(sigma_D_i, 4), "mm")
delta_a_D_i = 1.05 * sigma_D_i
print("圆环内径 D_i delta_a =", round(delta_a_D_i, 4), "mm")
delta_b_D_i = 0.02 * 0.95
print("圆环内径 D_i delta_b =", round(delta_b_D_i, 4), "mm")
U_D_i = math.sqrt(delta_a_D_i**2 + delta_b_D_i**2)
print("圆环内径 D_i 最终不确定度 U_D_i =", round(U_D_i, 4), "mm")

mean_D_1 = mean(D_1)
print("圆柱1直径 D_1 平均值 =", round(mean_D_1, 4), "mm")
sigma_D_1 = stdev(D_1)
print("圆柱1直径 D_1 标准差 =", round(sigma_D_1, 4), "mm")
delta_a_D_1 = 1.05 * sigma_D_1
print("圆柱1直径 D_1 delta_a =", round(delta_a_D_1, 4), "mm")
delta_b_D_1 = 0.02 * 0.95
print("圆柱1直径 D_1 delta_b =", round(delta_b_D_1, 4), "mm")
U_D_1 = math.sqrt(delta_a_D_1**2 + delta_b_D_1**2)
print("圆柱1直径 D_1 最终不确定度 U_D_1 =", round(U_D_1, 4), "mm")

mean_D_2 = mean(D_2)
print("圆柱2直径 D_2 平均值 =", round(mean_D_2, 4), "mm")
sigma_D_2 = stdev(D_2)
print("圆柱2直径 D_2 标准差 =", round(sigma_D_2, 4), "mm")
delta_a_D_2 = 1.05 * sigma_D_2
print("圆柱2直径 D_2 delta_a =", round(delta_a_D_2, 4), "mm")
delta_b_D_2 = 0.02 * 0.95
print("圆柱2直径 D_2 delta_b =", round(delta_b_D_2, 4), "mm")
U_D_2 = math.sqrt(delta_a_D_2**2 + delta_b_D_2**2)
print("圆柱2直径 D_2 最终不确定度 U_D_2 =", round(U_D_2, 4), "mm")


def compute_beta(tk):
    k = [i+1 for i in range(10)]
    pairs = [(0,5), (1,6), (2,7), (3,8),(4,9)]
    betas = []
    for m, n in pairs:
        tm, tn = tk[m], tk[n]
        km, kn = k[m], k[n]
        beta = 2*math.pi*(kn*tm - km*tn)/(tn**2*tm - tm**2*tn)
        betas.append(beta)
    filtered = [round(b, 4) for b in betas if abs(b - mean(betas)) <= 3*stdev(betas)]
    if len(filtered) < len(betas):
        print("剔除异常值后各组β:", filtered)
    print("各组β:", filtered)
    print("标准差:", round(stdev(filtered),5))
    print("平均 =", mean(filtered))
    
    
    delta_a = 1.24 * stdev(filtered)
    print("delta_a =", round(delta_a,5))
    
    delta_b = 0.5 * 0.0001 * 0.95
    print("delta_b =", round(delta_b,6))
    U = math.sqrt(delta_a**2 + delta_b**2)
    print("不确定度 U=", round(U,6))
    
    return mean(filtered)

print("\n计算 tk_1 对应的 beta:")
compute_beta(tk_1)

print("\n计算 tk_2 对应的 beta:")
compute_beta(tk_2)
print("\n计算 tk_3 对应的 beta:")
compute_beta(tk_3)
print("\n计算 tk_4 对应的 beta:")
compute_beta(tk_4)
print("\n计算 tk_5 对应的 beta:")
compute_beta(tk_5)
print("\n计算 tk_6 对应的 beta:")
compute_beta(tk_6)




beta_1 = -0.065
beta_2 = compute_beta(tk_2)
beta_3 = -0.035
beta_4 = compute_beta(tk_4)
beta_5 = compute_beta(tk_5)
beta_6 = compute_beta(tk_6)



g = 9.80  # 重力加速度 m/s^2
R_exp = 15e-3  # 半径 R，单位 m
m_exp = mean_m * 1e-3  # 砝码平均质量，单位 kg

# 试样数据均值（单位转换为 kg 和 m）
M_c_kg, M_1_kg, M_2_kg = mean_M_c*1e-3, mean_M_1*1e-3, mean_M_2*1e-3
D_o_m, D_i_m, D_1_m, D_2_m = mean_D_o*1e-3, mean_D_i*1e-3, mean_D_1*1e-3, mean_D_2*1e-3

# 计算实验台转动惯量 J1
J1 = m_exp*R_exp*(g - R_exp*beta_2) / (beta_2 - beta_1)

# 计算实验台+试样转动惯量 J2
J2 = m_exp*R_exp*(g - R_exp*beta_4) / (beta_4 - beta_3)

# 计算待测试样转动惯量 J3
J3 = J2 - J1

J4 =  m_exp*R_exp*(g - R_exp*beta_6) / (beta_6 - beta_5)

J5 = J4-J1

J = 0.5 * mean(M_1) * 1e-3 * (D_1_m/2)**2 + 0.5 * mean(M_2) *1e-3 * (D_2_m/2)**2 + (mean(M_1)+mean(M_2))*1e-3 * (d*1e-3)**2
# 圆环理论值
R_out, R_in = D_o_m/2, D_i_m/2
J_ring_theory = 0.5*M_c_kg*(R_out**2 + R_in**2)
E_ring = (J3 - J_ring_theory)/J_ring_theory * 100

# 双圆柱理论值（备用）
M_cyl = M_1_kg + M_2_kg
R_cyl = D_1_m / 2
J_cyl_theory = 0.5*M_cyl*R_cyl**2
E_cyl = (J3 - J_cyl_theory)/J_cyl_theory * 100

print("\n" + "="*50)
print("转动惯量计算结果")
print("="*50)
print(f"J1 (实验台): {J1:.6e} kg·m²")
print(f"J2 (实验台+试样): {J2:.6e} kg·m²")
print(f"J3 (试样实验值): {J3:.6e} kg·m²")
print(f"\n圆环理论值: {J_ring_theory:.6e} kg·m²")
print(f"圆环相对误差: {E_ring:.2f}%")
# print(f"\n双圆柱理论值: {J_cyl_theory:.6e} kg·m²")
# print(f"双圆柱相对误差: {E_cyl:.2f}%")

print("J=", J)
print("J5=", J5)
print("J4=", J4)
print("相对误差=", abs(J5 - J)/J * 100, "%")

print((mean(M_1)+mean(M_2))*1e-3 * (d*1e-3)**2)
print(0.5 * mean(M_1) * 1e-3 * (D_1_m/2)**2 + 0.5 * mean(M_2) *1e-3 * (D_2_m/2)**2)