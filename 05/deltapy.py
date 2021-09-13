"""
異なるエネルギー順位をもつ波動関数の内積が0の証明
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

####################################
#物理定数
####################################
h = 6.6260896 * 10**(-34)#プランク定数
hbar = h/(2*np.pi)
me = 9.10938215 * 10**(-31)#電子の重さ
eV = 1.60217733 * 10**(-19)#電子ボルト

#####################################
#物理系の設定
#####################################
#ポテンシャル長
L = 10**(-9)

k0 = 1 * np.pi / L
k1 = 2 * np.pi / L
k2 = 3 * np.pi / L
k3 = 4 * np.pi / L
k4 = 5 * np.pi / L
k5 = 6 * np.pi / L 
omega0 = hbar * k0**2 / 2 /me
omega1 = hbar * k1**2 / 2 /me
omega2 = hbar * k2**2 / 2 /me
omega3 = hbar * k3**2 / 2 /me
omega4 = hbar * k4**2 / 2 /me
omega5 = hbar * k5**2 / 2 /me


######################################
#シュミレーション開始
#######################################
#空間、時間指定
x_num = 400
x = np.linspace(-L/2,L/2, x_num)


#波動関数計算
psi0 = np.sqrt(2/L) * np.sin(k0*(x+L/2))
psi1 = np.sqrt(2/L) * np.sin(k1*(x+L/2))
psi2 = np.sqrt(2/L) * np.sin(k2*(x+L/2))
psi3 = np.sqrt(2/L) * np.sin(k3*(x+L/2))
psi = [psi0, psi1, psi2, psi3]
a = psi0 * psi1

#積分計算
result = np.zeros((4,4))
for i in range(4):
    for j in range(4):
        result[i,j] = np.sum((L/x_num) * (psi[i] * psi[j]))
        

