a = [1,2,9,5,7,8]

for i in range(len(a)):
    mx = a[0]
    mx_idx = 0
    for j in range(len(a)-i):
        if a[j] > mx:
            mx = a[j]
            mx_idx = j
    a[mx_idx],a[-i-1] = a[-i-1],a[mx_idx]
print(a)