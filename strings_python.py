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
str1='Ram'
str2="Ram chennale"
str3='''Ram chennale lotus'''
str4="""ram
chennale
lotus
bengaluru"""

print(str1)
print()
print(str2)
print()
print(str3)
print()
print(str4)
print()

print(str1[1])
#If we try to access index out of the range or use decimal number, we will get errors.
#print(str1[100]) ERROR IndexError: string index out of range
print(str2[2])
print(str2[-1])


#We cannot delete or remove characters from a string. But deleting the string entirely is possible using the keyword del.
#str1[1]='Z'  #TypeError: 'str' object does not support item assignment
print(str1)
del str1        # Str1 is deleted can not access
#print(str1) ERROR  NameError: name 'str1' is not defined

print('All string : ',str2+str3+str4)

str4="""ram
chennale
lotus
bengaluru"""


count = 0
for letter in 'Hello World':
    if(letter == 'l'):
        count += 1
print(count,'l '+' letters found')

num=0
for letters in 'Ram chennale':
    if(letters=='a'):
        num=num+1
print(num,'a '+'letters found')



# We can test if a sub string exists within a string or not, using the keyword in.
'ram' in 'ram chennale'  # True
'ram' not in 'ram chennale'  #False

"PrOgRaMiZ".lower() #'programiz'
"PrOgRaMiZ".upper()         #'PROGRAMIZ'
"This will split all words into a list".split()  #['This', 'will', 'split', 'all', 'words', 'into', 'a', 'list']

' '.join(['This', 'will', 'join', 'all', 'words', 'into', 'a', 'string'])#'This will join all words into a string'
'Happy New Year'.find('ew') #7
'Happy New Year'.replace('Happy','Brilliant')  #'Brilliant New Year'



