#%% packages

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from smt.sampling_methods import LHS

#%% sampling

xlimits=np.array([[700, 1000], [300, 50000], [0.5, 2.5]])
sampling=LHS(xlimits=xlimits)

num = 20
x = sampling(num)

print(x)
print(x.shape)

#%% figure

fig = plt.figure()


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

plt.xlabel("x")
plt.ylabel("y")
plt.ylabel("z")

ax = plt.axes(projection='3d')
ax.scatter3D(x[:, 0], x[:, 1], x[:,2], c=x[:,2], cmap='Greens');

plt.show()

#%%