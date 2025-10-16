# 🎓 Student Performance Analysis (Basic Python Only)

print("=== Student Performance Analysis ===\n")

# Step 1: Sample Data (You can change the data)
students = [
    {"name": "Aisha", "gender": "Female", "math": 78, "reading": 85, "writing": 82},
    {"name": "Ravi", "gender": "Male", "math": 88, "reading": 75, "writing": 70},
    {"name": "Sara", "gender": "Female", "math": 92, "reading": 95, "writing": 94},
    {"name": "Karan", "gender": "Male", "math": 60, "reading": 65, "writing": 62},
    {"name": "Meena", "gender": "Female", "math": 72, "reading": 80, "writing": 78},
    {"name": "Aman", "gender": "Male", "math": 85, "reading": 79, "writing": 75}
]

# Step 2: Calculate Average Marks
total_math = total_reading = total_writing = 0

for s in students:
    total_math += s["math"]
    total_reading += s["reading"]
    total_writing += s["writing"]

n = len(students)
avg_math = total_math / n
avg_reading = total_reading / n
avg_writing = total_writing / n

print(f"Average Math Score: {avg_math:.2f}")
print(f"Average Reading Score: {avg_reading:.2f}")
print(f"Average Writing Score: {avg_writing:.2f}\n")

# Step 3: Find Highest and Lowest Performers
top_student = max(students, key=lambda s: (s["math"] + s["reading"] + s["writing"]))
lowest_student = min(students, key=lambda s: (s["math"] + s["reading"] + s["writing"]))

print(f"Top Performer: {top_student['name']} ({(top_student['math'] + top_student['reading'] + top_student['writing'])/3:.2f} avg)")
print(f"Lowest Performer: {lowest_student['name']} ({(lowest_student['math'] + lowest_student['reading'] + lowest_student['writing'])/3:.2f} avg)\n")

# Step 4: Compare Boys vs Girls Average
boys = [s for s in students if s["gender"] == "Male"]
girls = [s for s in students if s["gender"] == "Female"]

boys_avg = sum((s["math"] + s["reading"] + s["writing"]) / 3 for s in boys) / len(boys)
girls_avg = sum((s["math"] + s["reading"] + s["writing"]) / 3 for s in girls) / len(girls)

print(f"Average Score of Boys: {boys_avg:.2f}")
print(f"Average Score of Girls: {girls_avg:.2f}\n")

# Step 5: Simple Insights
print("=== Insights ===")
if girls_avg > boys_avg:
    print("• Girls performed better overall.")
else:
    print("• Boys performed better overall.")

if avg_math > avg_reading:
    print("• Students are stronger in Math than Reading.")
else:
    print("• Students are stronger in Reading than Math.")

print("•", top_student["name"], "is the top performer in the class!")
print("• Data shows clear performance patterns among genders and subjects.")
