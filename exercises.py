import numpy as np

#a
x = np.zeros(10)
x[4] = 1
print(x)

#b
y = np.arange(10, 50)
print("Orignal array")
print(y)

#c
y = y[::-1]
print("Reverse array")
print(y)

#d
x = np.arange(0,9).reshape(3,3)
print(x)

#e
x = [1,2,0,0,4,0]
print(np.nonzero(x))

#f
x = np.random.random(30)
print("Orignal array")
print(x)
print(np.mean(x))

#g
x = np.ones((5,5))
print("Orignal array")
print(x)
print("1 on the border and 0 inside in the array")
x[1:-1,1:-1] = 0
print(x)

#h
print("Checkboard pattern:")
x = np.zeros((8,8),dtype=int)
x[1::2,::2] = 1
x[::2,1::2] = 1
print(x)

#i
print("Checkboard pattern:")
x = np.array([0,1])
x = np.tile(x, (8,4))
print(x)

#j
z = np.arange(11)
z[3:9] = np.negative(z[3:9])
print(z)

#k
z = np.random.random(10)
z = np.sort(z)
print(z)

#l
A = np.random.randint(0,2,5)
B = np.random.randint(0,2,5)
print(A)
print(B)
equal = (A == B)
print(equal)

#m
z = np.arange(10, dtype=np.int32)
print(z)
print(z.dtype)
z = z.astype(np.float32)
print(z)
print(z.dtype)

#n
A = np.arange(9).reshape(3,3)
B = A + 1
C = np.dot(A,B)
D = np.diag(C)
print(A)
print(B)
print(C)
print(D)
