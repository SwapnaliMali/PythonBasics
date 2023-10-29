#5. Write a Python program to count the number of strings in a list where
# the string length is 2 or more and the first and last character are the same.

new_list = ['abca','erere','w','a', 'swapnali', 'madam','naman','qu','pqr']
print(new_list)
print('Total length of list is : ',len(new_list))

abc_list = []
for i in new_list:
    if len(i) >= 2 and i[0] == i[-1]:
        abc_list.append(i)
print(abc_list)
print('The total count of number of strings in a list where string length is 2 or more & first '
      '& last chars are same are :', len(abc_list))


