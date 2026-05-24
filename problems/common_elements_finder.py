def find_common(list1, list2):
    common=[]
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i]==list2[j]:
                if list1[i] not in common:
                    common.append(list1[i])
                break
    return common






print(find_common(list1 = [1,1,2,3],
list2 = [1,2,2,4]))