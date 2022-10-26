import numpy as np
import time

def trad_version():
    t1 = time.time()
    X = range(10000000)
    Y = range(10000000)
    X = []
    for i in range(len(X)):
        Z.append(X[i]) + Y([i])
    return time.time() - t1

def numpy_version():
    t1 = time.time()
    X = range(10000000)
    Y = range(10000000)
    X = []
    for i in range(len(X)):
        Z.append(X[i]) + Y([i])
    return time.time() - t1

# run fungsi
speed_trad = trad_version()
print("Waktu eksekusi Looping List:")
print(speed_trad)

speed_np = numpy_version()
print("\nWaktu eksekusi Numpy Array")
print(speed_np)