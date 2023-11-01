#Program 3:

#Remove duplicate elements from a list.

my_list = [1, 2, 2, 3, 4, 4, 5]
print('origial list is : ',my_list)

unique_list = set(my_list)
print('Duplicates removed / unique elements only in : ',unique_list)

print("-------------------")
#Program 4:
#Remove a key-value pair from the dictionary.

my_dict = {'a':1,'b':3,'pqr':45,'xyz':789,'Fruit': 'Apple'}
print('Before removing key value pair from dictionary, original dictionary is : ',my_dict)

my_dict.pop('xyz')
print('After removing key value paair from dictionary : ',my_dict)

