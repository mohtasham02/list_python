
li1 = [1,2,3,4,5]
li2 = [2,3,1,0,6,7]
 
temp3 = []
for element in li1:
    if element not in li2:
        temp3.append(element)
 
print(temp3)