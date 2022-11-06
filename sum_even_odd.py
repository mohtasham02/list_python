elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]

odd_sum = 0
even_sum = 0

for sub in elements:
    for item in str(sub):
        if int(item) % 2 == 0:
            even_sum += int(item)
        else:
            odd_sum += int(item)
print("Odd digit sum : " + str(odd_sum))
print("Even digit sum : " + str(even_sum))