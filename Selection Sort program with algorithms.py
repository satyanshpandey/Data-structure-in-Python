'''
list1 = [11,23,45,65,1,2]

print(list1)

#Find the minimum value of the list

min_val = min(list1)
print("This is minimum value of the list",min_val)

#Find the minimum value's Index number.

min_ind = list1.index(min_val)
print("This is the minimum value's index number ",min_ind)

#Step1:- first swap one element of the list and after that remainig elements...
list1[0],list1[min_ind] = list1[min_ind],list1[0]
print(list1)

'''

list1 = [11,23,45,65,1,2]

print(list1)


for i in range(len(list1)):
    min_val = min(list1[i:])
    min_ind = list1.index(min_val)
    list1[i],list1[min_ind] = list1[min_ind],list1[i]
    

print(list1)



