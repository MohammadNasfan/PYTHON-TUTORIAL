# p2.py
# Checks password strength based on length, uppercase, lowercase, and digit requirements.
def check_password(password):
    if(len(n)>=8 and any(q.isupper() for q in n) and any(d.islower() for d in n) and any(g.isdigit() for g in n)):
      return "Strong password"
     
    return "Weak password"
n=input("Enter the password:")
    
     

print(check_password(n))