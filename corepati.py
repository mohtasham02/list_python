money=[3000, 600000, 324990909, 90990900, 
30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
i=0
a=0
b=0
c=0
while i<len(money):
    if money[i]>=10000000:
        a+=1
    elif money[i]<10000000 and money[i]>=100000:
        b+=1
    else:
        c+=1
    i+=1
print("Corepati=",a)
print("lakhpati=",b)
print("dillwale=",c)