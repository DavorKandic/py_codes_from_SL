"""Simple sorting algorithm"""
def find_next(arr):
    lst = []
    tgt = min(arr)
    i=0
    lst.append(tgt)
    while i < len(arr):
        tgt += 1
        for el in arr:
            if el == tgt:
                lst.append(el)
        i+=1
    return lst

print(find_next([3,1,4,2,6,11,5]))