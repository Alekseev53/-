lst = [0]*1_000
ans = []
for i in range(2,len(lst)):
    if lst[i] == 0:
        ans.append(i)
    for j in range(2*i,len(lst),i):
        lst[j]+=1
print(*ans)