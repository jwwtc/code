#%% packages

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from smt.sampling_methods import LHS

#%% sampling --- Temperature // Duration

xlimits=np.array([[700, 1000], [300, 600]])
sampling=LHS(xlimits=xlimits)

num = 20
x = sampling(num)

print(x)
print(x.shape)

#%% figure

plt.plot(x[:, 0], x[:, 1], ".")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

#%%

