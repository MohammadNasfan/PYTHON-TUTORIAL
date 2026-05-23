# p11.py
# Counts even and odd numbers in a list and prints the result.

def count_even_odd(nums):
    even_count=0
    odd_count=0
    for i in nums:
        if i%2==0:
            even_count+=1
        else:
            odd_count+=1
    return even_count,odd_count










print(count_even_odd([1, 2, 3, 4, 5, 6]))