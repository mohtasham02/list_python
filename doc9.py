a1 = [50, 40, 23, 70, 56, 12, 5, 10, 7]
i=0
max=0
max1=0
max2=0
while i <len(a1):
    if max<a1[i]:
        max=a1[i]
    elif max1<a1[i]:
        max1=a1[i]
    elif max1<max and max2<a1[i]:
        max2=max
    i+=1
print("1st maximum=",max)
print("second maximum =",max1)
print("third maximum=",max2) 
