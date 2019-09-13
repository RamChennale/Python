#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ramchennale
#
# Created:     23/07/2018
# Copyright:   (c) ramchennale 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
j = 10
while j <= 20:
    print(j)
    j=j+1

# remember to increment i, or else the loop will continue forever.
i=1
while i<=10:
    print(i)
    if i >= 5:
        break;
    i =i+1

a=20
while a >= 10:
    print("a ",a)
    a -=1


b = 0
while b < 6:
  b += 1 #  b=b+1
  if b == 3:
    continue
  print(b)


num=0
for letters in 'Ram chennale':
    if(letters=='a'):
        num=num+1
print(num,'a '+'letters found')

count=0
while count<20:
    count+=1
    if count % 3 ==0:
        continue
    if count == 17:
        break
    print(count)











