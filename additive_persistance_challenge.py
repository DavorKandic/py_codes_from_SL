"""Calculates the number of all-digit additions of multidigit number till it becomes a single digit number. E.g:

   1234 => 1 + 2 + 3 + 4 = 10 (1. iteration)
   
   10 => 1 + 0 = 1<single digit!>(2. iteration)
   
   Returns number of iterations: 2
"""

def adder(num_str):
    res = 0
    for dg in num_str:
        res += int(dg)
    return res
    
def counter(num_str):
    ln = len(num_str)
    count = 0
    while ln > 1:
        num_str = str(adder(num_str))
        ln = len(num_str)
        count += 1
    return count


n = input('Enter multidigit number:\n')


print(f'Number of addition is: {counter(n)}')