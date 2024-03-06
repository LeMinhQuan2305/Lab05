list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
listghep = [list1[i] + list2[j] for i in range(len(list1)) for j in range(len(list2))]
print(listghep)