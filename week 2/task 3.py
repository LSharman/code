total = int(input("enter amount of students: "))
remaining = total%24
amount = total-remaining
groups = amount/24
print("there will be", groups+1,"groups with", remaining,"in the small group")