print("Inisialisasi Dictionary")
# dictionary dengan key integer
myDict1 = {1:"apple",2:"ball"}
print(myDict1)

# dictionary dengan key campurt
myDict2 = {"name":"John",1:[2,3,4]}
print(myDict2)

# dictionary dengan menggunakan fungsi dict
myDict3 = dict([(1,"apple"),(2,"ball")])
print(myDict3)

print("===Mengakses element===")
print(myDict1[1])
print(myDict2["name"])
print(myDict3.get(1))
