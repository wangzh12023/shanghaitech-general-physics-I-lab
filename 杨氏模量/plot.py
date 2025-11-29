import matplotlib.pyplot as plt
import numpy as np
from measured_data import masses, x_up, x_down

# 设置绘图风格
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

def perform_linear_fit(x_data, y_data):
    """
    使用最小二乘法进行线性拟合 (y = kx + b)
    返回: 斜率 k, 截距 b, 拟合线 y值, 相关系数 R^2
    """
    x = np.array(x_data)
    y = np.array(y_data)
    
    # 1次多项式拟合 (线性)
    coeffs = np.polyfit(x, y, 1)
    k, b = coeffs
    
    # 生成拟合线数据
    fit_y = k * x + b
    
    # 计算 R^2
    y_mean = np.mean(y)
    ss_tot = np.sum((y - y_mean)**2)
    ss_res = np.sum((y - fit_y)**2)
    r_squared = 1 - (ss_res / ss_tot)
    
    return k, b, fit_y, r_squared

# --- 主绘图逻辑 ---

plt.figure(figsize=(10, 6))

# 1. 增重数据拟合 (Loading)
k_up, b_up, fit_y_up, r2_up = perform_linear_fit(masses, x_up)
plt.scatter(masses, x_up, color='blue', marker='o', label='增重测量值 (Loading)')
plt.plot(masses, fit_y_up, color='blue', linestyle='--', alpha=0.7, 
         label=f'增重拟合: x = {k_up:.5f}m + {b_up:.5f} ($R^2$={r2_up:.5f})')

# 2. 减重数据拟合 (Unloading)
k_down, b_down, fit_y_down, r2_down = perform_linear_fit(masses, x_down)
plt.scatter(masses, x_down, color='red', marker='x', label='减重测量值 (Unloading)')
plt.plot(masses, fit_y_down, color='red', linestyle='-.', alpha=0.7, 
         label=f'减重拟合: x = {k_down:.5f}m + {b_down:.5f} ($R^2$={r2_down:.5f})')

# 3. 图像装饰
plt.title('杨氏模量实验：拉力(质量)-标尺读数关系图', fontsize=14)
plt.xlabel('拉力质量 m (kg)', fontsize=12)
plt.ylabel('标尺读数 x (cm)', fontsize=12)
plt.legend(loc='upper left', frameon=True)
plt.grid(True, linestyle=':', alpha=0.6)

# 4. 显示整体斜率信息（物理意义分析用）
# 理论上 Δx/Δm = k
avg_k = (k_up + k_down) / 2
plt.text(0.75, 0.15, f'平均斜率 k_avg = {avg_k:.5f} cm/kg', 
         transform=plt.gca().transAxes, bbox=dict(facecolor='white', alpha=0.8))

# 保存并展示
output_filename = 'young_modulus_fitting.png'
plt.savefig(output_filename, dpi=300)
print(f"拟合图像已保存为: {output_filename}")
print(f"增重拟合斜率 k_up: {k_up:.5f}")
print(f"减重拟合斜率 k_down: {k_down:.5f}")
plt.show()