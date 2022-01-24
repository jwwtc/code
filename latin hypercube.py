import numpy as np
import matplotlib.pyplot as plt

from smt.sampling_methods import LHS

xlimits=np.array([[300, 400], [2, 10]])
sampling=LHS(xlimits=xlimits)

num = 10
x = sampling(num)

plt.plot(x[:, 0], x[:, 1], ".")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

print(x)
print(x.shape)