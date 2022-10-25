import numpy as np

l = [[1,2,3],[3,6,9],[2,4,6]]
a = np.array(l)

print("Matriks")
print(a)

print("\nManipulasi satu nilai:")
a[0,2] = 7
print(a)

print("\nManipulasi satu kolom")
a[:,0] = [0,8,9]
print(a)

# a[0,0] = "a"
# print("\nKetika menghilangkan tanda pagar")
# print(a)
