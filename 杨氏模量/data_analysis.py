import math
import statistics
import numpy as np
from scipy import stats
from measured_data import *

# ================= 工具函数 =================

def get_chauvenet_coeff(n):
    table = {
        5: 1.65, 6: 1.75, 7: 1.80, 8: 1.86,
        9: 1.92, 10: 1.96, 11: 2.00
    }
    return table.get(n, 2.00)

def get_t_factor(n):
    table = {
        3: 4.30, 4: 3.18, 5: 2.78, 6: 2.57,
        7: 2.45, 8: 2.36, 9: 2.31, 10: 2.26,
        11: 2.23
    }
    return table.get(n, 1.96)

def remove_outliers_chauvenet(data, name="Data"):
    clean_data = list(data)
    print(f"--- 开始对 [{name}] 进行肖维涅准则检验 ---")
    while True:
        n = len(clean_data)
        if n < 3: break
        
        mean_val = statistics.mean(clean_data)
        stdev_val = statistics.stdev(clean_data)
        chauvenet_c = get_chauvenet_coeff(n)
        limit = chauvenet_c * stdev_val
        
        outliers = [x for x in clean_data if abs(x - mean_val) > limit]
        
        if outliers:
            print(f"    -> 发现粗差: {outliers}，已剔除。")
            for out in outliers:
                clean_data.remove(out)
        else:
            print(f"    -> 未发现粗差，检验通过 (n={n})。")
            break
    print(f"--- [{name}] 检验结束 ---\n")        
    return clean_data

# ================= 主处理流程 =================

print("=== 杨氏模量实验数据处理 (最小二乘法拟合版) ===\n")

# --- 1. 处理金属丝直径 d ---
print("[1] 金属丝直径 d 处理:")
d_corrected = [x - d_zero for x in d_readings]
d_final = remove_outliers_chauvenet(d_corrected, "直径d")
n_d = len(d_final)
d_mean = statistics.mean(d_final)
d_std = statistics.stdev(d_final)

# 不确定度
t_d = get_t_factor(n_d)
ua_d = t_d * d_std / math.sqrt(n_d)
ub_d = 0.95 * delta_inst_d
U_d = math.sqrt(ua_d**2 + ub_d**2)

print(f"  平均直径 d = {d_mean:.5f} cm")
print(f"  不确定度 U_d = {U_d:.5f} cm\n")

# --- 2. 处理光杠杆标尺读数 x (线性拟合) ---
print("[2] 标尺读数 x 处理 (线性拟合):")

# 准备数据 (质量m为x轴, 读数x为y轴)
# 注意：masses 单位 kg, x_up/down 单位 cm
m_array = np.array(masses)
x_up_array = np.array(x_up)
x_down_array = np.array(x_down)

# 2.1 增重过程拟合
slope_up, intercept_up, r_value_up, p_value_up, std_err_up = stats.linregress(m_array, x_up_array)
print(f"  增重拟合: k_up = {slope_up:.5f} cm/kg, R^2 = {r_value_up**2:.5f}")

# 2.2 减重过程拟合
slope_down, intercept_down, r_value_down, p_value_down, std_err_down = stats.linregress(m_array, x_down_array)
print(f"  减重拟合: k_down = {slope_down:.5f} cm/kg, R^2 = {r_value_down**2:.5f}")

# 2.3 计算平均斜率 k_avg
k_avg_cm_kg = (slope_up + slope_down) / 2
print(f"  平均斜率 k = {k_avg_cm_kg:.5f} cm/kg")

# 2.4 斜率的不确定度 (A类)
# 取两次拟合标准误差的合成，或者平均标准误差。这里取平均作为估计。
# 也可以对合并数据进行拟合。为简单起见，取平均标准误差并扩大置信度。
# 自由度 n-2 = 11-2 = 9。t0.95(9) ≈ 2.26
n_fit = len(masses)
t_fit = get_t_factor(n_fit - 2) # 自由度 n-2
u_k_a = t_fit * ((std_err_up + std_err_down) / 2)

# 斜率的B类不确定度通常忽略，或归入拟合残差。
# 这里主要由拟合的统计误差决定。
U_k_cm_kg = u_k_a 

print(f"  斜率不确定度 U_k = {U_k_cm_kg:.5f} cm/kg (由拟合标准误计算)")

# --- 3. 计算杨氏模量 E ---
print("\n[3] 杨氏模量 E 计算:")

# 转换单位为国际单位制
d_m = d_mean * 1e-2      # m
D_m = D_raw * 1e-2       # m
L_m = L_raw * 1e-2       # m
H_m = H_raw * 1e-2       # m
k_SI = k_avg_cm_kg * 1e-2 # cm/kg -> m/kg (每公斤对应的位移米数)

# 公式推导:
# E = (8 * F * L * H) / (pi * d^2 * D * delta_x)
# F = m * g,  delta_x / m = k
# E = (8 * g * L * H) / (pi * d^2 * D * k)

numerator = 8 * g * L_m * H_m
denominator = math.pi * (d_m**2) * D_m * k_SI
E = numerator / denominator

print(f"  计算结果 E = {E:.4e} Pa")


def format_sci(val, unc):
    exponent = int(math.floor(math.log10(abs(val))))
    coeff = val / (10**exponent)
    unc_coeff = unc / (10**exponent)
    return f"({coeff:.2f} ± {unc_coeff:.2f}) × 10^{exponent}"

print(f"  最终结果: E = {E} Pa (P=0.95)")