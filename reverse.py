#places reverse
# places=["delhi", "gujrat", "rajasthan", "punjab", "kerala"]
# i=0
# while i<len(places):
#     b=places[::-1]
#     i+=1
# print(b)

#palindrome name 
name=list(input("enter name:"))
i=0
while i<len(name):
    b=name[::-1]
    i+=1
if name==b:
    print("its a palindrome:",name,b)
else:
    print("its not a palindrome:",name,b)