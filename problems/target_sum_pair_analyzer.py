# p5.py
# Finds and prints pairs of numbers whose sum matches the target.
def find_pairs(numbers,target):
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
           if numbers[i]+numbers[j]==target:
            print (numbers[i],numbers[j])
                
               
find_pairs([10,20,30,40], 50)                    
                    
           
                



