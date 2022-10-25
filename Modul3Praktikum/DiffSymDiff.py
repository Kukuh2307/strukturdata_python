A = {1,2,3,4,5}
B = {4,5,6,7,8}

# Operasi Difference
print("Operasi Difference")
diff1 = A-B
print(diff1)
diff2 = A.difference(B)
print(diff2)

diff21 = B-A
print(diff21)
diff22 = B.difference(A)
print(diff22)

# Operasi Symetric Difference
print("Operasi Symetric Difference")
symdiff1 = A^B
print(symdiff1)

symdiff21 = A.symmetric_difference(B)
print(symdiff21)

symdiff22 = B.symmetric_difference(A)
print(symdiff22)
