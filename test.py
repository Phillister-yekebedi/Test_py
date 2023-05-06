# Write a Python function that takes two arguments (a and b) and returns their sum.
def addition ( a, b):
    sum = a + b
    return sum

print(addition(100,100))

# Write a Python function that takes a string as input and returns the string reversed  
def str(word):
   w=word[::-1]
   return w
print(str('Wonderful'))
    
   
# Write a Python function that takes a list of integers as input and returns the sum of 
# all the integers in the list.
def numb(lists):
     return sum(list)

sum= [1,3,4,5,6,8]
print(sum)

def number(numbers):
   sum=0
   for n in numbers:
      sum+=n
      return sum
print(number([1,2,3,4,5]))
      



# Write a Python function that takes a list of integers as input and returns a new list 
# with all the even numbers removed.
def even():
   numbers = []
   x= range(0,10)
   for i in x:
      if i % 2 == 0:
        numbers.append(i)
        return numbers

print(even())


# Write a Python function that takes a list of integers as input and returns the 
# highest value in the list.
def many(nums):
    highest_value= 0
    for num in nums:
        if num > highest_value:
         return highest_value
    
print(many([45,89,34,89,9]))

def highest(nums):
   for n in nums:
         n=max(nums)
         return n
print(highest([1,3,5]))
   


# Write a Python function that takes a list of strings as input and returns a new
# list with all the strings capitalized.

def capitalizes(word):
    capitalize =  word.capitalize()
    return capitalizes

print(capitalizes(['world','Well','better']))




