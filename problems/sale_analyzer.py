# p9.py
# Analyzes sales data for totals, highest sales, best employee, and zero-sale days.
# total sales
# highest single sale
# employee with highest total sales
# number of days where sales were zero
def analyze_sales(sales):
    total_sales=0
    highest_sale=0
    employee=0
    best_employeetotal=0
    zero_saleday=0
    for i in sales:
        employee+=1
        total_employeesale=0
        for j in i:
            total_sales += j
            total_employeesale+=j
            if j>highest_sale:
                highest_sale=j
            if j==0:
                zero_saleday+=1
            if total_employeesale>best_employeetotal:
                best_employeetotal=total_employeesale
                best_employeetotal=employee
    
            
    return {"total sales":total_sales,
            "highest sale":highest_sale,
            "best emplyee":employee,
            "zero sales day":zero_saleday}

                 
           








print(analyze_sales([
    [100,200,300],
    [400,100,50],
    [250,250,250]
]))