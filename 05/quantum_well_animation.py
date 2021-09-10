"""
無限に深い井戸型ポテンシャルに対する固有状態
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
t_num = 100
t = np.linspace(-2*np.pi/omega0, 2*np.pi/omega0, t_num)
x_mesh, t_mesh = np.meshgrid(x, t)


#波動関数計算
psi0 = np.sqrt(2/L) * np.sin(k0*(x_mesh+L/2)) * np.exp(-1j * omega0 * t_mesh)
psi1 = np.sqrt(2/L) * np.sin(k1*(x_mesh+L/2)) * np.exp(-1j * omega1 * t_mesh)
psi2 = np.sqrt(2/L) * np.sin(k2*(x_mesh+L/2)) * np.exp(-1j * omega2 * t_mesh)
psi3 = np.sqrt(2/L) * np.sin(k3*(x_mesh+L/2)) * np.exp(-1j * omega3 * t_mesh)
"""
psi4 = np.sqrt(2/L) * np.sin(k4*(x+L/2))
psi5 = np.sqrt(2/L) * np.sin(k5*(x+L/2))
"""

fig = plt.figure(figsize =(10,6))
ims = []
for i in range(t_num):  
    img = plt.plot(x, psi0[i,:].real, color='blue')
    img += plt.plot(x, psi1[i,:].real, color='orange')
    img += plt.plot(x, psi2[i,:].real, color='green')
    img += plt.plot(x, psi3[i,:].real, color='red')
    ims.append(img)
    
#描画
anime = animation.ArtistAnimation(fig, ims, interval = 10)
anime.save("pulse.html", writer=animation.HTMLWriter())



