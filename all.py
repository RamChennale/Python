#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ramchennale
#
# Created:     25/07/2018
# Copyright:   (c) ramchennale 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
# Program to check if a string
#  is palindrome or not

# change this value for a different output
my_str = 'aIbohPhoBiA'

# make it suitable for caseless comparison
my_str = my_str.casefold()

# reverse the string
rev_str = reversed(my_str)

# check if the string is equal to its reverse
if list(my_str) == list(rev_str):
   print("It is palindrome")
else:
   print("It is not palindrome")






# Program to sort alphabetically the words form a string provided by the user

# change this value for a different result
my_str = "Hello this Is an Example With cased letters"

# uncomment to take input from the user
#my_str = input("Enter a string: ")

# breakdown the string into a list of words
words = my_str.split()

# sort the list
words.sort()

# display the sorted words

print("The sorted words are:")
for word in words:
   print(word)




# Program to sort alphabetically the words form a string provided by the user

# change this value for a different result
my_str = "Hello this Is an Example With cased letters"

# uncomment to take input from the user
#my_str = input("Enter a string: ")

# breakdown the string into a list of words
words = my_str.split()

# sort the list
words.sort()

# display the sorted words

print("The sorted words are:")
for word in words:
   print(word)






# define punctuation
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

my_str = "Hello!!!, he said ---and went."

# To take input from the user
# my_str = input("Enter a string: ")

# remove punctuation from the string
no_punct = ""
for char in my_str:
   if char not in punctuations:
       no_punct = no_punct + char

# display the unpunctuated string
print(no_punct)





# Program to count the number of each vowel in a string

# string of vowels
vowels = 'aeiou'

# change this value for a different result
ip_str = 'Hello, have you tried our turorial section yet?'

# uncomment to take input from the user
#ip_str = input("Enter a string: ")

# make it suitable for caseless comparisions
ip_str = ip_str.casefold()

# make a dictionary with each vowel a key and value 0
count = {}.fromkeys(vowels,0)

# count the vowels
for char in ip_str:
   if char in count:
       count[char] += 1

print(count)




def convertToBinary(n):
   """Function to print binary number
   for the input decimal using recursion"""
   if n > 1:
       convertToBinary(n//2)
   print(n % 2,end = '')

# decimal number
dec = 34

convertToBinary(dec)




# Python program to check if the number provided by the user is an Armstrong number or not

# take input from the user
# num = int(input("Enter a number: "))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")






# Python program to check if the input number is prime or not

num = 407

# take input from the user
# num = int(input("Enter a number: "))

# prime numbers are greater than 1
if num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")

# if input number is less than
# or equal to 1, it is not prime
else:
   print(num,"is not a prime number")







# Python Program to display the powers of 2 using anonymous function

# Change this value for a different result
terms = 10

# Uncomment to take number of terms from user
#terms = int(input("How many terms? "))

# use anonymous function
result = list(map(lambda x: 2 ** x, range(terms)))

# display the result

print("The total terms is:",terms)
for i in range(terms):
   print("2 raised to power",i,"is",result[i])






# Program to display the Fibonacci sequence up to n-th term where n is provided by the user

# change this value for a different result
nterms = 10

# uncomment to take input from the user
#nterms = int(input("How many terms? "))

# first two terms
n1 = 0
n2 = 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence upto",nterms,":")
   while count < nterms:
       print(n1,end=' , ')
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1


