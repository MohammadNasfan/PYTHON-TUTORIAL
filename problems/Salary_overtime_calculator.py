# p4.py
# Calculates total salary with overtime pay for a list of worked hours.
def calculate_salary(hours,hourly_rate):    
    total_salary=0
    for i in hours:
        if i<0:
            continue
        if i<=8:
           total_salary +=i*hourly_rate
        else:
           total_salary += 8 * hourly_rate + (i - 8) * hourly_rate * 1.5
    return total_salary

    

print(calculate_salary([8, 9, 7], 100))     
     
     
       

