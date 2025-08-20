# Student Roll Number Generator (Alphabetical Order)

# Step 1: Create empty list
students = []

# Step 2: Take number of students
n = int(input("Enter the number of students: "))

# Step 3: Input student names
for i in range(n):
    name = input(f"Enter name of student {i+1}: ")
    students.append(name)

# Step 4: Sort the list alphabetically
students.sort()

# Step 5: Display students with roll numbers
print("\n---Student List with Roll Numbers---:")
for index, student in enumerate(students, start=1):
    print(f"Roll No {index}: {student}")
