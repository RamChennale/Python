'''
Created on Jun 19, 2018

@author: ramchennale
'''
import os
## Reading file 

f = open("ram.txt", "r")
#print(f.read())
print(f.read(2))
print(f.readline())
print("")
print(f.readline())
print(f.readline())

print(" ")
g = open("ram.txt","tr")
for i in g:
    print(i)

## Writing to a file     
print("")
h = open("ram.txt","a")
h.write("Now the file have ore line of text")
print(f.read())

i = open("ram1.txt","w")
i.write("New created file")
j = open("ram1.txt","r")
print(j.read())

##deleting a file 
#os.remove("D:\\ram1.txt")


## Checking whether file exits or not to delete
if os.path.exists("D:\\ram1.txt"):
    os.remove("D:\\ram1.txt")
    print("file deleted")
else:
    print("file dose not exists")


