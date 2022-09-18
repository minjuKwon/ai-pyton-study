import matplotlib.pyplot as plt

labels=['A','B','C','D','E']
ratio=[4,3,2,2,1]

fig,ax=plt.subplots()

plt.bar(labels,ratio)
plt.show()