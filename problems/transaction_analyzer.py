# p6.py
# Analyzes transaction amounts for income, expenses, balance, and largest values.
    # total income,total expense,largest income,largest expense
def analyze_transactions(transactions):
    largest_income=0
    largest_expense=0
    total_income=0
    expense=0
    balance=0
    for i in transactions:
         if i>0 and i>largest_income:
          largest_income=i
         if i<0 and i<largest_expense:
          largest_expense=i
         if i>0:
          total_income+=i
         if i<0:
          expense+=abs(i)
         balance+=i
    return{"income":total_income,
           "expense":expense,
           "largest income":largest_income,
           "largest expense":largest_expense,
           "balance":balance}
     
print(analyze_transactions([500,-200, 1000, -300, -100]))
     
        








