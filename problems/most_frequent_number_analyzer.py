# p16.py
# Finds the most frequent element in a list of visits.
def  most_frequent(visits):
    best_count=0
    most_frequent_number=[0]
    for i in range(len(visits)):
       current_count=0
       for j in range(len(visits)):
           if visits[i]==visits[j]:
               current_count+=1
               if current_count>best_count:
                best_count=current_count
                most_frequent_number=visits[i]
           
               
               



       return most_frequent_number,current_count
print(most_frequent([3,1,3,3,2,3,4,3,1,2,1,1,1]))

