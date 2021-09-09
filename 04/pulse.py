"""
ガウス分布a(k)で重みづけをした電子波束
a(k)はどのような分布でも構わない
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
E0 = 10.0 * eV
sigma = np.sqrt(np.log(2)) * 10**9
k0 = np.sqrt(2 * me * E0 /hbar**2) 
#波数
k = np.linspace(k0 - 5*sigma, k0 + 5*sigma, 400)


######################################
#シュミレーション開始
#######################################
#空間、時間指定
x_num = 400
x = np.linspace(-5.0 * 10**(-9),5.0 * 10**(-9), x_num)

#行列表記
x_matrix,k_matrix = np.meshgrid(x, k)


#波動関数計算
psi = np.exp(-((k_matrix-k0)/(2*sigma))**2) * np.exp(1j * k_matrix * x_matrix)
psi = psi.sum(axis=0)

plt.plot(x,psi.real)
plt.plot(x,psi.imag)
plt.show()


