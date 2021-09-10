"""
ディラックのデルタの近似
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


######################################
#シュミレーション開始
#######################################
#空間、時間指定
x_num = 100
x = np.linspace(-5.0, 5.0, x_num)

#アニメーションの作成
fig = plt.figure(figsize = (10,6))
ims = []    
#波動関数計算
for n in range(5):
    y = np.sin(n*x)/(np.pi*x)
    img = plt.plot(x, y, color='blue', linewidth=3.0, linestyle='solid')
    ims.append(img)
    

#描画
plt.title("animation")
plt.xlabel("x")
plt.ylabel("y")
anime = animation.ArtistAnimation(fig, ims, interval=10)
anime.save("pulse.html", writer=animation.HTMLWriter())
plt.show()