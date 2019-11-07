""" Analyzes frequency of characters in a string"""
# Made it in city bus for about 20 minutes ;)

lower = 'abcdefghijklmnopqrstuvxyz'

str = 'Quick brown fox jumps over lazy dog.'

lst = []

for ltr in lower:
    x = str.count(ltr)
    lst.append(x)

res = []

i = 0

while i<len(lst):
    s="{} : {}".format(lower[i],lst[i])
    res.append(s)
    i+=1
    
for an in res:
    print(an)
