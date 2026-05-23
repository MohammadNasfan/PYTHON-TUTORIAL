# p8.py
# Evaluates exam marks to count pass/fail, distinctions, and summary statistics.
def analyze_results(marks):
    passed=0
    distinction=0
    failed=0
    highest=0
    lowest=marks[0]
    avg=0
    total=0
    for i in marks:
        if i>=40:
            passed+=1
        else:
            failed+=1
        if i>=75:
            distinction+=1
        if i>highest:
            highest=i
        if i<lowest:
            lowest=i
        total+=i
        avg=total/len(marks)
        
    return{"passed": passed,
           "failed":failed,
           "highest":highest,
           "lowest":lowest,
           "average":avg,
           "distinction":distinction}


            
            
        







print(analyze_results([78, 45, 90, 32, 67, 88, 45, 91]))