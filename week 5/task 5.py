total_sweets = int(input("enter amount of sweets: "))
total_students = int(input("how many students: "))
remaining = total_sweets%total_students
amount = total_sweets-remaining
groups = amount/total_students
print("there will be", groups,"sweets per student and", remaining,"left over")