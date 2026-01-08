# Student Performance Analyzer

def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "Fail"


def performance_feedback(percentage):
    if percentage >= 85:
        return "Excellent performance 👏"
    elif percentage >= 70:
        return "Good performance 🙂"
    elif percentage >= 50:
        return "Average performance 😐"
    else:
        return "Needs improvement ⚠️"


# Main Program
print("===== Student Performance Analyzer =====")

name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

subjects = int(input("Enter number of subjects: "))

marks = []
total_marks = 0

for i in range(subjects):
    score = float(input(f"Enter marks for subject {i + 1}: "))
    marks.append(score)
    total_marks += score

max_marks = subjects * 100
percentage = (total_marks / max_marks) * 100

grade = calculate_grade(percentage)
feedback = performance_feedback(percentage)

# Result Display
print("\n===== Result =====")
print("Name:", name)
print("Roll Number:", roll_no)
print("Total Marks:", total_marks, "/", max_marks)
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)
print("Feedback:", feedback)
print("==============================")
