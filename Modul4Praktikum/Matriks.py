from traceback import print_tb
import numpy as np

# numpy array sebagai matriks dari list
l = [[1,2,3],[3,6,9],[2,4,6]]
a = np.array(l)

print("Matriks")
print(a)
print("\nTipe Data")
print(a.dtype)
print("\nDimensi")
print(a.shape)