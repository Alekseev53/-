#    0,1,2,3,4 ,5 ,6
a = [1,2,3,4,10,15,20]

def find_bin(x,a):
    l = -1
    r = len(a)
    while(r-l>1):
        m = (r-l)//2+l #Так без переполнений
        if a[m]>x:
            r = m
        else:
            l = m
    return l

print(find_bin(1,a))
print(find_bin(-1,a))
print(find_bin(21,a))
print(find_bin(5,a))
print(find_bin(4,a))