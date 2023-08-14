a = [7,1,3,2,8]
n = len(a)

def find_place(x,a):
    for i,y in enumerate(a):
        if x < y:
            return i
    return len(a)

for part_1 in range(1,n):
    first_part = a[:part_1 - 1]
    second_part = a[part_1 - 1:]
    first_element = second_part[0]
    place = find_place(first_element,first_part)

    first_part.insert(place,first_element)
    a = first_part + second_part[1:]
print(a)

