# p17.py
# Finds the highest and second-highest values in a list of numbers.
def second_highest(numbers):
    highest_number=numbers[0]
    second_highest_number=numbers[0]
    for i in numbers:
        if i > highest_number:
            second_highest_number=highest_number
            highest_number=i
   
           
    return highest_number,second_highest_number



print(second_highest([5, 8, 2, 10, 7]))