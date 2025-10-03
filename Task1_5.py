marks_list = {}
totals = {}

# loop for 3 students
for i in range(1, 4):
    name = input(f"Enter the name of student {i}: ")
    marks = list(map(int, input(f"Enter the three marks of {name}: ").split()))
    
    # store marks in dictionary
    marks_list[name] = marks
    
    # calculate total and average
    total = sum(marks)
    average = total / len(marks)
    totals[name] = total
    
    print(f"{name}: Total={total}, Average={average:.2f}")

# print full marks list
print("\nAll students' marks:", marks_list)

# find topper
topper = max(totals, key=totals.get)
print(f"\nTopper: {topper} with {totals[topper]} marks")
