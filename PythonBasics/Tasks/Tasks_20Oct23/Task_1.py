
# PALINDROME CHECKER
#Create a function that checks if a given string is a palindrome (reads the same forwards and backward) 121.
def palindrome(string):
  print('Plain string :', string)
  print(type(string))
  print("-------")
  print('Reverse string : ', string[::-1])
  if string == string[::-1]:
      print(f'{string} is a Palindrome string')
  else:
      print(f'{string} is not Palindrome string')

palindrome('malayalam') #madam, #swapnali, #Madam, case sensitive.

#Approach --> i/p --> 'madam' , o/p --> This is palindrome, i/p -> 'swapnali', o/p --> this is not palindrome
#rough work --> check string given & check if it is same when reversed, if both same, it is palindrome, else not




