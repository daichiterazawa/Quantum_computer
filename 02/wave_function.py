"""
自由空間中の電子の運動（実軸）を求めるプログラム
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
E1 = 0.25 * eV
E2 = 1.0 * eV
E3 = 4.0 * eV

#波数
k1 = np.sqrt((2 * me * E1)/hbar**2)
k2 = np.sqrt((2 * me * E2)/hbar**2)
k3 = np.sqrt((2 * me * E3)/hbar**2)

#角振動数
omega1 = E1/hbar
omega2 = E2/hbar
omega3 = E3/hbar

######################################
#シュミレーション開始
#######################################
#空間、時間指定
dx,x_num = 10**(-11),400
x = np.linspace(0, dx*x_num, x_num)
dt,t_num = 1.0 * 10**(-16),100
t = np.linspace(0, dt*t_num, t_num)
#行列表記
x_matrix,t_matrix = np.meshgrid(x, t)


#波動関数計算
psi1 = np.cos(k1 * x_matrix - omega1 * t_matrix)
psi2 = np.cos(k2 * x_matrix - omega2 * t_matrix)
psi3 = np.cos(k3 * x_matrix - omega3 * t_matrix)

#グラフプロット
fig = plt.figure(figsize=(10,6))
ims = []
for i in range(t_num):
    img = plt.plot(x, psi1[i,:], color='blue')
    img += plt.plot(x, psi2[i,:], color='blue')
    img += plt.plot(x, psi3[i,:], color='blue')
    
    ims.append(img)

#アニメーション
plt.title("wave_function")
plt.xlabel("x")
plt.ylabel("psi(x,t)")
anime = animation.ArtistAnimation(fig, ims, interval=10)
anime.save("output.html", writer=animation.HTMLWriter())
plt.show()

    
    






















