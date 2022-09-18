from statistics import stdev
import numpy as np
import matplotlib.pyplot as plt

coffee=np.array([202,177,121,148,89,121,137,158])

cf_mean=coffee.mean()
cf_std=stdev(coffee)

print("Mean : ",round(cf_mean,2))
print("Sample std.Dev : ",round(cf_std,2))

fig, ax=plt.subplots()

plt.hist(coffee)
plt.show()