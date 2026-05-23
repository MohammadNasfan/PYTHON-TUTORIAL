# p14.py
# Analyzes student attendance records for risk, perfect attendance, and averages.
# total students
# absent-risk students
# perfect attendance students
# average attendance
# student with highest attendance
def analyze_attendance(attendance):
    total_students=0
    absent_risk_students=[]
    perfect_attendane_student=[]
    sum=0
    avg=0
    highest_attendence=0
    highest_attendence_student=0
    for i in attendance:
        student=i[0]
        days_present=i[1]
        total_students+=1
        sum+=days_present
        if days_present<18:
            absent_risk_students.append(student)
        if days_present==30:
            perfect_attendane_student.append(student)
        avg=sum/total_students
        if days_present>highest_attendence:
            highest_attendence=days_present
            highest_attendence_student=student

        

      







    return total_students,absent_risk_students,perfect_attendane_student,avg,highest_attendence_student










print(analyze_attendance([
 ["Ali",28],
 ["Sara",15],
 ["John",30],
 ["Emma",22],
 ["Mike",10]
]))