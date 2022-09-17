import numpy as np
import matplotlib.pyplot as plt

x=np.array(["soccer","baseball","basketball","badminton","PingPong"])
y=np.array([13,10,17,8,7])
z=np.random.randn(1000)

fig,axes=plt.subplots(1,2,figsize=(12,4))

axes[0].bar(x,y)

axes[1].hist(z,bins=150)