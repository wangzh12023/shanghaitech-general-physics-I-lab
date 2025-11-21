import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from measured_data import *

# 配置字体以支持中文显示
plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# --- 查找表 ---

# 肖维涅准则系数表
# 键为 n, 值为系数 c
chauvenet_coeffs = {
    3: 1.38, 4: 1.53, 5: 1.65, 6: 1.75, 
    7: 1.80, 8: 1.86, 9: 1.92, 10: 1.96, 11: 2.00
}

# t因子表 (t_0.95, 根据您提供的图片)
# 键为 n, 值为 t_0.95
student_t_095 = {
    3: 4.30, 4: 3.18, 5: 2.78, 6: 2.57, 
    7: 2.45, 8: 2.36, 9: 2.31, 10: 2.26, 11: 2.23
}

def analyze_dataset_verbose(name, data, resolution, unit="s"):
    """
    对一组数据进行详细分析，打印每一步计算结果，支持肖维涅准则剔除粗差。
    """
    n_original = len(data)
    print("-" * 60)
    print(f"正在分析: {name}")
    print(f"原始数据 (n={n_original}): {data}")
    
    # 1. 原始统计
    mean_val = np.mean(data)
    print(f"{name} 原始平均值 = {round(mean_val, 5)} {unit}")
    
    if n_original < 2:
        print("数据量太少，无法计算标准差。")
        return mean_val, 0
        
    sigma_val = np.std(data, ddof=1) # 贝塞尔公式，样本标准差
    print(f"{name} 原始标准差 (sigma) = {round(sigma_val, 5)} {unit}")
    
    # 2. 肖维涅准则剔除粗差
    c_val = chauvenet_coeffs.get(n_original)
    if c_val:
        limit = c_val * sigma_val
        # print(f"肖维涅判据系数 c(n={n_original}) = {c_val}")
        # print(f"剔除阈值 |Xi - mean| > {round(limit, 5)}")
        
        filtered_data = []
        outliers = []
        for x in data:
            if abs(x - mean_val) > limit:
                outliers.append(x)
            else:
                filtered_data.append(x)
        
        if outliers:
            print(f"发现粗差并剔除: {outliers}")
            data = filtered_data
            # 剔除后重新计算
            mean_val = np.mean(data)
            sigma_val = np.std(data, ddof=1)
            print(f"{name} 剔除后平均值 = {round(mean_val, 5)} {unit}")
            print(f"{name} 剔除后标准差 = {round(sigma_val, 5)} {unit}")
        else:
            print("未发现粗差，保留所有数据。")
    else:
        print(f"警告: 未找到 n={n_original} 的肖维涅系数，跳过粗差剔除。")

    n_final = len(data)
    
    # 3. 计算不确定度
    # A类不确定度: delta_a = t * sigma / sqrt(n)
    t_factor = student_t_095.get(n_final)
    if t_factor:
        delta_a = t_factor * sigma_val / math.sqrt(n_final)
        print(f"{name} delta_a = {t_factor} * {round(sigma_val,5)} / sqrt({n_final}) = {round(delta_a, 5)} {unit}")
    else:
        # 如果查不到表，默认使用 k=1 或者报错，这里做一个简单的 fallback
        delta_a = sigma_val / math.sqrt(n_final)
        print(f"警告: 未找到 n={n_final} 的 t_0.95，仅计算 sigma/sqrt(n)。delta_a = {round(delta_a, 5)} {unit}")
        
    # B类不确定度: delta_b = 0.5 * 分度值 * 0.95
    # 电子计时器分度值通常为 0.001s
    delta_b = 0.5 * resolution * 0.95
    print(f"{name} delta_b = 0.5 * {resolution} * 0.95 = {round(delta_b, 5)} {unit}")
    
    # 合成不确定度
    U = math.sqrt(delta_a**2 + delta_b**2)
    print(f"{name} 最终不确定度 U = {round(U, 4)} {unit}")
    
    return mean_val, U

# =========================
# 主程序
# =========================

sin_squared_theta_2 = []
two_T_means_angle = []
two_T_uncertainties_angle = []

print("\n" + "="*30)
print("实验一：固定摆长，改变摆角")
print("="*30)

for item in theta_T:
    angle = item["theta_value"]
    vals = item["2T_values"]
    name_str = f"摆角{angle}° 2T"
    
    # 计时器分度值 0.001s
    mean_res, u_res = analyze_dataset_verbose(name_str, vals, resolution=0.001)
    
    rad = math.radians(angle)
    x_val = math.sin(rad/2)**2
    
    sin_squared_theta_2.append(x_val)
    two_T_means_angle.append(mean_res)
    two_T_uncertainties_angle.append(u_res)

# 拟合 2T vs sin^2(theta/2)
slope_1, intercept_1, r_value_1, p_value_1, std_err_1 = stats.linregress(sin_squared_theta_2, two_T_means_angle)

print("\n" + "-" * 20)
print("拟合结果 (改变摆角):")
print(f"线性方程: 2T = {slope_1:.4f} * sin^2(theta/2) + {intercept_1:.4f}")
print(f"相关系数 R^2: {r_value_1**2:.4f}")

# 计算 g
T_zero = intercept_1 / 2
L_m = L / 100.0 
g_1 = 4 * math.pi**2 * L_m / (T_zero**2)
print(f"计算得到的重力加速度 g = {g_1:.4f} m/s^2")


print("\n" + "="*30)
print("实验二：改变摆长")
print("="*30)

L_values = []
T_squared_values = []
two_T_means_length = []

for item in L_T:
    L_val = item["L"]
    vals = item["2T_values"]
    name_str = f"摆长{L_val}cm 2T"
    
    mean_res, u_res = analyze_dataset_verbose(name_str, vals, resolution=0.001)
    
    T_val = mean_res / 2
    T_sq = T_val**2
    
    L_values.append(L_val)
    T_squared_values.append(T_sq)
    two_T_means_length.append(mean_res)

# 拟合 T^2 vs L (cm)
slope_2, intercept_2, r_value_2, p_value_2, std_err_2 = stats.linregress(L_values, T_squared_values)

print("\n" + "-" * 20)
print("拟合结果 (改变摆长):")
print(f"线性方程: T^2 = {slope_2:.4f} * L(cm) + {intercept_2:.4f}")
print(f"相关系数 R^2: {r_value_2**2:.4f}")

g_2_cm = 4 * math.pi**2 / slope_2
g_2 = g_2_cm / 100.0
print(f"计算得到的重力加速度 g = {g_2:.4f} m/s^2")


# =========================
# 绘图
# =========================
plt.figure(figsize=(12, 5))

# 图1
plt.subplot(1, 2, 1)
plt.errorbar(sin_squared_theta_2, two_T_means_angle, yerr=two_T_uncertainties_angle, fmt='o', color='blue', label='Data', capsize=3)
x_fit_1 = np.linspace(min(sin_squared_theta_2), max(sin_squared_theta_2), 100)
y_fit_1 = slope_1 * x_fit_1 + intercept_1
plt.plot(x_fit_1, y_fit_1, 'r--', label=f'Fit: $y={slope_1:.2f}x+{intercept_1:.2f}$, $R^2={r_value_1**2:.4f}$')
plt.xlabel(r'$sin^2(\theta/2)$')
plt.ylabel(r'$2T (s)$')
plt.title(r'Relationship between $2T$ and $sin^2(\theta/2)$')
plt.legend()
plt.grid(True)

# 图2
plt.subplot(1, 2, 2)
plt.scatter(L_values, T_squared_values, color='green', label='Data')
x_fit_2 = np.linspace(min(L_values), max(L_values), 100)
y_fit_2 = slope_2 * x_fit_2 + intercept_2
plt.plot(x_fit_2, y_fit_2, 'r--', label=f'Fit: $y={slope_2:.4f}x+{intercept_2:.3f}$, $R^2={r_value_2**2:.4f}$')
plt.xlabel(r'$L (cm)$')
plt.ylabel(r'$T^2 (s^2)$')
plt.title(r'Relationship between $T^2$ and $L$')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
print("\n[Info] 绘图代码已执行 (Preview mode)")