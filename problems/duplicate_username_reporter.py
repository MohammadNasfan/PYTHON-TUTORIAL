# p12.py
# Finds duplicate usernames and reports duplicate entries.
def find_duplicates(usernames):
    duplicate=0
    duplicates=[]
    for i in range(len(usernames)):
        for j in range(i+1,len(usernames)):
            if usernames[i]==usernames[j]:
               
               if usernames[i] not in duplicates:
                   duplicates.append(usernames[i])
    duplicate=len(duplicates)
    return {"duplicate usernames":duplicates,
            "number of duplicates":duplicate}
    
               






print(find_duplicates(["alex", "john", "alex", "mike","mike", "john"]))