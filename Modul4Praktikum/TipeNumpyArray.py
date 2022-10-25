import numpy

a = numpy.array([[1,3,5,7,9],[2,4,6,8,10]])
print(a)
print(a[1, 2:4])
print(type(a))

a = numpy.array([1,3,5,7,9])
b = numpy.array([3,5,6,7,9])
c = a+b
print(c)