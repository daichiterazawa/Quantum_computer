import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#範囲
x_min = -1.0 * np.pi
x_max = 1.0 * np.pi

#サンプル数
N = 100
#アニメ分割数
AN = 30

#計算
#xの範囲
x = np.linspace(x_min, x_max, N)
#ファイの範囲
phi = np.linspace(0,2*np.pi,AN)
#行列表記
x_matrix,phi_matrix = np.meshgrid(x,phi)
#yの範囲
y = np.sin(x_matrix + phi_matrix)

#アニメーションの作成
fig = plt.figure(figsize = (10,6))
ims = []
for i in range(AN):
    img = plt.plot(x,y[i,:], color='blue', linewidth=3.0, linestyle='solid')
    ims.append(img)
    

#描画
plt.title("sin animation")
plt.xlabel("x")
plt.ylabel("y")
anime = animation.ArtistAnimation(fig, ims, interval=50)
anime.save("output.html", writer=animation.HTMLWriter())
plt.show()
