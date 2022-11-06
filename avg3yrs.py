marks = [[78, 76, 94, 86, 88],[91, 71, 98, 65],[95, 45, 78],[87, 67, 49, 68, 88]]
for i in range(1):
    total_marks1=0
    for j in range(5):
        total_marks1=  total_marks1+marks[i][j]
        avg1=int(total_marks1/5)
    print("avg for 1st year",avg1)
    for i in range(2):
        total_marks2=0
        for j in range(4):
            total_marks2=  total_marks2+marks[i][j]
            avg2=int(total_marks2/4)
    print("avg for 2nd year=",avg2)
    for i in range(3):
        total_marks3=0
        for j in range(3):
            total_marks3=  total_marks3+marks[i][j]
            avg3=int(total_marks3/3)
    print("avg for 3rd year=",avg3)
    for i in range(4):
        total_marks4=0
        for j in range(5):
            total_marks4=  total_marks4+marks[i][j]
            avg4=int(total_marks4/3)
    print("avg for 4th year=",avg4)6