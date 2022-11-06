num=[50,40,23,70,56,12,5,10,7]
max=num[0]
i=1
while i<len(num):
    if max<num[i]:
        max=num[i]
    i+=1
print(max)