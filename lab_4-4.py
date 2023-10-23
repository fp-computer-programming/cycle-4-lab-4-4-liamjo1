"""

*** You must write a comment for every chunk of code you write from now on along with your author tag***

Create a Python file named lab_4-4.py

Use the find method to return the index of the first occurrence of the letter "t" in the word "flibbertigibbet".

Using this value, print the letter immediately following the first "t". hint: you may need to store the index value as a variable!

Create a variable storing you first name written in lowercase. Using a string method, print this variable in uppercase.

Use the split method to split the following sentence at each comma: "I wish, I wish, I was a fish."

"""
my_word = "flibbertigibbet"
# input word as variable - O'Hara

my_index = my_word.find("t")
# find where t is in the word - O'Hara

print(my_word[my_index + 1])
# print letter after t in the index - O'Hara

first_name = "liam"
# store first name in lowercase - O'Hara

print (first_name.upper())
# make variable uppercase - O'Hara

my_string ="I wish, I wish, I was a fish."
# declare string - O'Hara

print(my_string.split(sep=','))
# split string at commas - O'Hara