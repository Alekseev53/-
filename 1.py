a = [9,5,8,1,2]

for j in range(len(a)-1):
    for i in range(1,len(a)-j):
        if a[i]<a[i-1]:
            a[i],a[i-1] = a[i-1],a[i]
print(a)
