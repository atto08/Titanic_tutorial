import numpy as np
import matplotlib.pyplot as plt

# Fixing random state for reproducibility
np.random.seed(19680801)


N = 100
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = (30 * np.random.rand(N))**2  # 0 to 15 point radii
xv = [65,37,48,29,54,84,19]
yc = [1,2,3,4,5,6,7]


plt.scatter(xv, yc, s=500, c='r', alpha=0.5)
plt.show()