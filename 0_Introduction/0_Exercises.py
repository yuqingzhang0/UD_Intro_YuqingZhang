#!/usr/bin/env python
# coding: utf-8

# # Exercise 00
# Write a bit of code that prints _Introduction to Programming_ to the console and execute the cell

# In[16]:


print('Introduction to Programming')


# -----------------------------------------------------------------------------
# # Exercise 01
# Hello World is traditionally the first program anyone writes. It is
# very simple and the only thing it should do is print Hello World! to the
# terminal window.
# Create a file called HelloWorld.py and edit the contents so it prints Hello World! to the terminal and execute it using the command line.

# -----------------------------------------------------------------------------
# # Exercise 02
# Write some code to print your name, email, and age on separate lines. For each element first assign it to a variable and use the variable to print. 
# 
# Bonus: try to create the print statement for all variable in one line of code. (hint: '\n' is the character for a new line)

# In[15]:


myname = 'Yuqing Zhang'
email = 'ucbvy23@ucl.ac.uk'
age = '22'
print (myname)
print (email)
print (age)


# In[14]:


myname = 'Yuqing Zhang'
email = 'ucbvy23@ucl.ac.uk'
age = '22'
print(f"{myname}\n{email}\n{age}")


# -----------------------------------------------------------------------------
# # Exercise 03
# Print the numbers 0, 178, -21, 2938 divided by 49, 436 multiplied with 9948 and 12 to the power of 20
# 
# (Hint: Look up the documentation of basic arithmetic operators)

# In[12]:


n1 = 0
n2 = 178
n3 = -21
n4 = 2938
N1 = n1/49
N2 = n2/49
N3 = n3/49
N4 = n4/49
N5 = 436*9948
N6 = 12**20
print (f"{N1}\n{N2}\n{N3}\n{N4}\n{N5}\n{N6}")


# -----------------------------------------------------------------------------
# # Exercise 04
# Print sin(200), cos(100), tan($\pi$/4)
# 
# (Hint: Look up for how to use trigonometric function, and how to get the value of $\pi$.)

# In[13]:


import math
math.pi
N1 = math.sin(200)
N2 = math.cos(100)
N3 = math.tan(math.pi/4)
print (f"{N1}\n{N2}\n{N3}")


# -----------------------------------------------------------------------------
# # Exercise 05
# Write a program to read your first and last names from the console seperately, and then print them on the console together, separated by a space.

# In[10]:


firstname = input ('my first name: ')
lastname = input ('my last name: ')
fullname = str(firstname)+' '+str(lastname)
print (fullname)


# -----------------------------------------------------------------------------
# # Exercise 06
# Write a program that determines whether a number given as user input is positive or negative
#  
# You will need to convert the console input from a string to a number first!

# In[9]:


user_input = input ('enter a number: ')
number = float(user_input)
if (number > 0):
    print ('the number is positive')
elif (number < 0):
    print ('the number is negative')
else:
    print ('the number is zero')


# -----------------------------------------------------------------------------
# # Exercise 07
# Write a program that picks a random number between 1-20 and makes the user guess until they get the number right. Then print a congratulations message
# - (Find out yourself how to generate a random integer)
# - Bonus: make the user choose the range within which they have to guess
# - Bonus: keep track of how many guesses were made and print this at the end

# In[5]:


import random
min_number = int(input("Enter the minimum range number: "))
max_number = int(input("Enter the maximum range number: "))
random_numbers = int(random.randint(int(min_number),int(max_number)))
user_input = None
num_guess = 0
while (user_input) != (random_numbers):
    try:
        user_input = int(input("Guess the number between"+ " "+ str(min_number)+ " and " + str(max_number) +': '))
        num_guess +=1
        if (user_input) < (random_numbers):
            print ("The number is greater than you have input.")
        elif (user_input) > (random_numbers):
            print("The number is less than you have input. ")
        elif (user_input) == (random_numbers):
            print("Congratulations." + "The number is" +" "+ str(random_numbers) + ".")
            print("You guessed the number for" + " " + str(num_guess) + " times.")
    except Valueerrors:
        print("Invalid values. Enter a valid number: ")


# -----------------------------------------------------------------------------
# # Exercise 08
# Ask a sentence as input, then print the words in alphabetical order.
# Hint: look up how to split up a string

# In[6]:


sentence = str(input ('Enter a sentence: '))
sentence_lower = sentence.lower( )
word1 = sentence_lower.split( )
ordered_words = sorted(word1)
print ("Words in alphabetical order:" + str(ordered_words))


# -----------------------------------------------------------------------------
# # Exercise 09
# Write a program using for loops to print a christmas tree of x lines high
# specified by the user.
# (use for loops)
# so for instance, a chrismas tree of 4 high should looks like this:
# 
# ```
# 
#     *
#    ***
#   *****
#  *******
#     |
# 
# ```
# 
# hint: first combine strings into a variable before printing

# In[7]:


lines = input ("Enter the height of the christmas tree that you want: ")
for x in range(1,int(lines)+1):
    print ((int(lines)-x)*' ' + (2*x-1)*'*'+ (int(lines)-x)*' ')
print ((int(lines)-1)*" " + "|" + (int(lines)-1)*" ")


# -----------------------------------------------------------------------------
# # Exercise 10
# Write a piece of code that prints the first $n$ numbers of the padovan sequence

# In[8]:


N = int(input ('Enter the numbers of the padoven sequence: '))
n1 = 1
n2 = 1
n3 = 1
if N in range (4):
    if N == 1:
        print ("1")
    elif N == 2:
        print (f'{n1}\n{n2}')
else:
    print (f'{n1}\n{n2}\n{n3}')
for i in range(3,N):
    i = n1 + n2
    n1 = n2
    n2 = n3
    n3 = i
    print (i)


# In[ ]:




