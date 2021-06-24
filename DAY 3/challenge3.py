import numpy as np
# X = np.array([1, 7, 13, 105])
x = []
x_length = 5

for i in range(int(x_length)):
    num = input("num :")
    x.append(int(num))

print("Original array:")
print(x)
x = np.array(x)
size = (x.size * x.itemsize)
print("Size of the memory occupied by the said array:")
print("{} bytes".format(size) )

