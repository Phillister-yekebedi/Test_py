# 1. Write a Python program to get a single string from two given strings, 
# separated by a space, and swap the first two characters of each string
# def get_single_string( ):
def single_string(string, string2):
    new_str1 = string2[:2] + string[2:]
    new_str2 = string[:2] + string2[2:]
    return new_string + " " + new_string2

print(single_string("Hello", "World"))


# 2.Write a Python function that takes a list of words and returns the 
# longest word and the length of the longest one

def longest_string(words):
    longest_word = ""
    max_length = 0
    for word in word_list:
        if len(word) > max_length:
            longest_word = word
            max_length = len(word)
    return (longest_word, max_length)

print(longest_string("Tanzania","Juba","Nairobi"))


# 3. Write a Python program that accepts a comma-separated sequence of
#  words as input and prints the distinct words in sorted form (alphanumerically).

def comma_sequence_of_words(sequence_of_words):
    sequence = sequence_of_words.split()

# 4. Write a Python function that takes two lists and returns True if 
# they have at least one common member.
def common_member(list1, list2):
   for l in list1:
      for t in list2:
         if l == t:
            return True
print (common_member([1,2,3,5,8,9],[1,2,3,4,6,7,10]))         

# 5. Write a Python program to convert a list to a list of dictionaries.
# Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
colors = ["Black", "Red", "Maroon", "Yellow"]
rgb = ["#000000", "#FF0000", "#800000", "#FFFF00"]

color_dicts = []

for i in range(len(colors)):
    color_dict = {"color": colors[i], "rgb": codes[i]}
    color_dicts.append(color_dict)

print(color_dicts)


# 6. Write a Python program to check whether all dictionaries in a list are empty or not

def check_dict_in_list(dict_in_list ):
    for check in dict_in_list:
        if bool(check):
            return False
        
print(check_dict_in_list= [{},{},{}])     


# 7. Given a list of numbers, use list comprehension to remove all odd numbers from the list:
# numbers = [3,5,45,97,32,22,10,19,39,43]


def remove_odd_number(odd):
    empty = []
    for d in odd:
        if d % 2 == 0:
            empty.append(d)
        
numbers = [3,5,45,97,32,22,10,19,39,43]        
        
print(numbers)        


# 8. Find the common numbers in two lists (without using a tuple or set) 
# list_a = 1, 2, 3, 4, 
# list_b = 2, 3, 4, 5

list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]

common_nums = []

for num in list_a:
    if num in list_b and num not in common_nums:
        common_nums.append(num)

print(common_nums)

# 9. Use a nested list comprehension to find all of the numbers from 
# 1-1000 that are divisible by any single digit besides 1 (2-9)
def divisible(number):
    num = range (1, 10001)
    for num in number:
        if (num % divide ==0 ):


# 10. Write a Python function to remove all vowels in a string
def remove_vowels(name):
   vowels = ["a","e","1","o","u"]
   result = []
   for r in name:
        if r not in name:
            result+=vowels
    return result 


print (remove_vowels("Yekebedi"))
    
   