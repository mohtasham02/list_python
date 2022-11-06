list=[6,1,3,5,6,3,1]
i=0
a=[]
sum=0
while i<len(list):
	if list[i] not in a:
		a.append(list[i])
		sum=sum+(a[i]+a[i])*2
	i+=1
print(sum)