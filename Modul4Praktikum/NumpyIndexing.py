import numpy as np

l = [[1,2,3],[3,6,9],[2,4,6]]
a = np.array(l)

print("Matriks")
print(a)
print("\nBaris ke-0")
print(a[0])

print("\nNilai pada indeks 0,2")
print(a[0,2])

print("Semua nilai pada kolom ke-2")
print(a[:,2])