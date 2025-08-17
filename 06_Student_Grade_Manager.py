#Student Grade Manager

#Step-1: Get students score
student_scores = input("Enter student scores seperated by commas:")
score = [int(score) for score in student_scores.split(",")]

#Step-2: Assign grades using list comprehension
grades = [
    "A" if score >= 90 else
    "B" if score >= 80 else
    "C" if score >= 70 else
    "D" if score >= 60 else
    "F"
    for score in score
]

#Step-3: Filter passing and failing students
passing_students = [score for score in score if score >= 60]
failing_students = [score for score in score if score < 60]

#Step-4: Print Results
print("\n---Student Grades---")
for i, (score,grades) in enumerate(zip(score,grades),start=1):
    print(f"Student {i}: Score = {score},Grade = {grades}")
print("\n---Passing and Failing studnets---")    
print("Passing Students:", passing_students)
print("Failing Students:",failing_students)
