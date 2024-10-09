

for i in range(n):      #копирую a в f
    for j in range(n):
        f[i][j] = a[i][j]
print("F")
for i in f:
    print(i)

size = len(f)
sum0=0
sumnum=0
d=[]
k=[]
for i in range(n):
    for j in range(n):
        if j % 2 != 0 :
            if i > j and i+j>size-1:
                if f[i][j] == 0:
                    sum0+=1
        elif j % 2 != 0 or j == 0:
            if i > j and i + j < size-1:
                sumnum+=f[i][j]

#print(sumnum)
#print(sum0)
t=0
y=0

if sum0 > sumnum :
    for i in range(n): #2
        for j in range(n):
            if i<j and i+j < size-1:
                d.append(f[i][j])
    for j in range(n): #1
        for i in range(n-1,-1,-1):
            if i > j and i + j < size - 1:
                 k.append(f[i][j])
    for i in range(n):
        for j in range(n):
            if i < j and i + j < size - 1:
                f[i][j]=k[t]
                t+=1
    for j in range(n) :
        for i in range(n-1,-1,-1):
            if i > j and i + j < size - 1 :
                f[i][j]=d[y]
                y+=1
    print("F1 then sum0 > sumnum")
    for i in f:
        print(i)

else:
    for i in range(n): #2
        for j in range(n):
            if i<j and i+j < size-1:
                d.append(f[i][j])
    for j in range(n-1,-1,-1): #3
        for i in range(n):
             if i < j and i + j >size - 1:
                 k.append(f[i][j])
    for i in range(n):
        for j in range(n-1,-1,-1):
            if i < j and i + j < size - 1:
                f[i][j]=k[t]
                t+=1
    for j in range(n-1,-1,-1):
        for i in range(n-1,-1,-1):
            if i < j and i + j > size - 1:
                f[i][j]=d[y]
                y+=1

    print("F2 then sum0 < sumnum")
    for i in f:
        print(i)

p=0
#print("D")
#print(d)
#print("K")
#print(k)
c = [[0]*n for _ in range(n)]
for i in range(n): #a*f
    for j in range(n):
        s=0
        for p in range(n):
            s+=a[i][p]*f[p][j]
        c[i][j]=s
print("c")
for i in c:
    print(i)

x= [[0]*n for _ in range(n)]

for i in range(n):            #k*c
    for j in range(n):
        c[i][j]*=l

print("c")
for i in c:
    print(i)

at = [[0]*n for _ in range(n)]
for i in range(n): #at
    for j in range(n):
        at[i][j]=a[j][i]
print("at")
for i in at:
    print(i)

atk=[[0]*n for _ in range(n)]
for i in range(n): #at*k
    for j in range(n):
        atk[i][j]=at[i][j]*l
print("atk")
for i in atk:
    print(i)

m=[[0]*n for _ in range(n)]
for i in range(n): #c-atk
    for j in range(n):
        m[i][j]=c[i][j]-atk[i][j]
print("result")
for i in m:
    print(i)
