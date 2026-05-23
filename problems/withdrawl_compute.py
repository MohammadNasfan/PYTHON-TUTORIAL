# p1.py
# Implements a withdrawal validation function and prints the result.
def withdraw(balance,amount):
    if(amount>balance or amount<=0 or amount%100!=0):
     return "Invalid transaction"
    
    updated_balance=(balance-amount)
    return updated_balance
print(withdraw(5000,50000))
    
    
    
    
    
        