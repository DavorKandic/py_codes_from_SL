""" Given problem: For a given number k find two elements of array so that their sum is equal to k."""
# A.K.A Twosum problem
# ... like it's a problem TO SOME people ;)
def sumOfTwo(arr,k):
    l=len(arr)
    i=0
    j=l-1
    while i<=j:
        a=arr[i]
        b=arr[j]
        if a+b==k:
            return (a,b)
        elif a+b<k:
            i+=1
        elif a+b>k:
            j-=1

lst = [0,1,3,5,6,7]

res_tuple = sumOfTwo(lst,11)
print(res_tuple)