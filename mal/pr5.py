import numpy as np

# 1
Z = np.zeros(10)
Z[4] = 1
print(Z)

# 2
Z = np.arange(10, 50)
print(Z)

# 3
Z = np.arange(50)
Z = Z[::-1]
print(Z)

# 4
Z = np.arange(9).reshape(3, 3)
print(Z)

# 5
Z = np.random.random((10, 10))
Zmin, Zmax = Z.min(), Z.max()
print(Zmin, Zmax)

# 6
Z = np.random.random(30)
m = Z.mean()
print(m)

# 7
Z = np.zeros((8, 8), dtype=int)
Z[1::2, ::2] = 1
Z[::2, 1::2] = 1
print(Z)

# 8
Z = np.random.random((10, 2))
X, Y = Z[:, 0], Z[:, 1]
R = np.hypot(X, Y)
T = np.arctan2(Y, X)
print(R)
print(T)

# 9
Z = np.random.random(10)
Z[Z.argmax()] = 0
print(Z)

# 10
Z = np.arange(100)
v = np.random.uniform(0, 100)
index = (np.abs(Z - v)).argmin()
print(Z[index])
