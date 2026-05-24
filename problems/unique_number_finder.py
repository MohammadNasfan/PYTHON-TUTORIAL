def unique_patterns(numbers):
    unique_list=[]
    for i in range(len(numbers)):
        count=0
        for j in range(len(numbers)):
            if numbers[i]==numbers[j]:
                count+=1
        if count==1:
                unique_list.append(numbers[i])
    return unique_list

print(unique_patterns([1,2,2,3,4,4,5]))