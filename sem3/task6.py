X=list()
Y=list()
a=list(map(int,input().split()))
for i in range(len(a)):
    if i%2==0:
        X.append(a[i])
    else: Y.append(a[i])
medX = 0
medY = 0
medX2 = 0
medXY = 0
for i in X:
    medX += i
    medX2 += i ** 2
for i in Y:
    medY += i
for i in range(len(X)):
    medXY += X[i] * Y[i]
medX /= len(X)
medY /= len(Y)
medX2 /= len(X)
medXY /= len(X)
b = (medXY - medX * medY) / (medX2 - medX ** 2)
c = medY - b * medX
print(medX, medY, medX2, medXY)
print(b, c)
