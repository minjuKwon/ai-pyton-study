import numpy as np
import matplotlib.pyplot as plt

x=np.arange(10)
fig,ax=plt.subplots()

ax.plot(
        x,x,label='y=x',
        linestyle='-',
        marker='.',
        color='blue'
        )

ax.plot(
        x,x**2,label='y=x^2',
        linestyle='-.',
        marker=',',
        color='red'
        )

ax.set_xlabel("x")
ax.set_ylabel("y")

ax.legend(
    loc='best',
    shadow=True,
    fancybox=True,
    borderpad=2
    )