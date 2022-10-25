from ctypes import Union


A = {1,2,3,4,5}
B = {4,5,6,7,8}

# Operasi Union
print("Operasi Union")
Union1 = A|B
print(Union1)

Union2 = A.union(B)
print(Union2)

# Operasi Intersection
print("Operasi Intersection")
intersec1 = A&B
print(intersec1)

intersec2 = A.intersection(B)
print(intersec2)
