"""
無限に深い井戸型ポテンシャルに対する固有状態
"""

import numpy as np
import matplotlib.pyplot as plt

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
psi4 = np.sqrt(2/L) * np.sin(k4*(x+L/2))
psi5 = np.sqrt(2/L) * np.sin(k5*(x+L/2))


plt.plot(x, psi0, color='blue')
plt.plot(x, psi1, color='orange')
plt.plot(x, psi2, color='green')
plt.plot(x, psi3, color='red')
plt.show()

