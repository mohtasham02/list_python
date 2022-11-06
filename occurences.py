a= ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
i=0
l1=[]
c=0
while i<len(a):
    if a[i] not in l1:
        l1.append(a[i])
        j=0
        count=0
        while j<len(a):
            if l1[c]==a[j]:
                count+=1
            j=j+1
        print(a[i],count,"time")
        c=c+1
    i=i+1