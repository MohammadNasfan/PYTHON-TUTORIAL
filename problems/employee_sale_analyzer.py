# p10.py
# Analyzes employee sales records to determine totals, best performer, and zero-sale days.
def analyze_sales(sales):

    total_sales = 0
    highest_sale = sales[0][0]

    best_employee = 0
    best_employee_total = 0

    zero_sales_days = 0

    employee_number = 0

    for employee in sales:

        employee_number += 1

        employee_total = 0

        for sale in employee:

            total_sales += sale

            employee_total += sale

            if sale > highest_sale:
                highest_sale = sale

            if sale == 0:
                zero_sales_days += 1

        if employee_total > best_employee_total:

            best_employee_total = employee_total
            best_employee = employee_number

    return {
        "total_sales": total_sales,
        "highest_sale": highest_sale,
        "best_employee": best_employee,
        "zero_sales_days": zero_sales_days
    }


sales = [
    [100, 200, 300],
    [400, 100, 50],
    [250, 250, 250],
    
]

print(analyze_sales(sales))