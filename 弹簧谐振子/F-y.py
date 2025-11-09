'''
Original code:
    Copyright (c) 2024 XiongWenye
Modified code:
    Copyright (c) 2025 Zihan Wang
'''
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

from measured_data import *
from statistics import mean, stdev, variance, pstdev
 

x1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
x2 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

#draw  F = k * delta_y1 and F = k * delta_y2 respectively, where delta_y1 = y1 - y1[0], delta_y2 = y2 - y2[0]
g = 9.794

delta_y1 = np.array(l_1) - l_1[0]
delta_y2 = np.array(l_2) - l_2[0]

slope1, intercept1, r_value1, p_value1, std_err1 = linregress(delta_y1, x1)
line1 = slope1 * delta_y1 + intercept1
k1 = slope1
f1 = k1 * delta_y1

slope2, intercept2, r_value2, p_value2, std_err2 = linregress(delta_y2, x2)
line2 = slope2 * delta_y2 + intercept2
k2 = slope2
f2 = k2 * delta_y2

plt.figure()
plt.plot(delta_y1, x1, 'o', label='data point')
plt.plot(delta_y1, line1, 'r', label=f'x1 = {slope1:.5f}delta_y1 + {intercept1:.2f}')
plt.xlabel('Δy₁ (mm)')
plt.ylabel('x₁')
plt.title('x1-delta_y1 ')
plt.legend()
plt.grid(True)

plt.figure()
plt.plot(delta_y2, x2, 'o', label='data point')
plt.plot(delta_y2, line2, 'r', label=f'x2 = {slope2:.5f}delta_y2 + {intercept2:.2f}')
plt.xlabel('Δy₂ (mm)')
plt.ylabel('x₂')
plt.title('x2-delta_y2 ')
plt.legend()
plt.grid(True)

plt.show()

print(f"k1 = {k1}")
print(f"k2 = {k2}")

K1 = k1 * g
K2 = k2 * g

print(f"K1 = {K1}")
print(f"K2 = {K2}")