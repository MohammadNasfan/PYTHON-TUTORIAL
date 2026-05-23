# p3.py
# Analyzes a list of numbers for even/odd counts and min/max values.
def analyze_numbers(numbers):
    count = 0
    largest = numbers[0]
    smallest = numbers[0]
    for i in numbers:
        if i % 2 == 0:
            count += 1
        if i>largest:
            largest=i
        if i<smallest:
            smallest=i
    return{"even": count,
    "odd": len(numbers) - count,
    "smallest": smallest,
    "largest": largest}
    
    
        
print(analyze_numbers([1,2,3,4,5,6,7,8,9,10]))
    
        
            
    
    

# print(analyze_numbers([4, 7, 2, 9, 10]))
    
# def new(numbers):
#     largest = numbers[0]
#     smallest = numbers[0]
#     for i in numbers:
#       if i>largest:
#          largest = i
#       if i<smallest:
#         smallest = i 
#     return largest,smallest

    
   
    
# print(new([1,3,5,6,4,5,3]))











    
