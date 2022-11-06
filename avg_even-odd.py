l=[23,14,56,12,19,9,15,25,31,42,43]
sumodd=0
sumeven=0
odd=[]
even=[]
allnumbersum=0
l2=len(l)
for i in l:
    allnumbersum+=i
    if(i%2==0):
        sumeven+=i
        even.append(i)
        length=len(even)
    else:
        sumodd+=i
        odd.append(i)
        l1=len(odd)
print("Count of odd numbers=",l1)
print("Count of even numbers=",length)
print("Count of all the numbers=",len(l))
print("Sum of odd numbers=",sumodd)
print("Sum of even numbers=",sumeven)
print("Sum of all the numbers=",allnumbersum)
print("Average of odd numbers=",int(sumodd/l1))
print("Average of even numbers=",int(sumeven/length))
print("Average of all numbers=",int(allnumbersum/l2))