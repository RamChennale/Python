'''
Created on Jun 7, 2018

@author: ramchennale
'''

print ('Hello well  come to Python  world');
print()
#This is python comment
"""
Multi line commenting 
way in  
Python
"""

x=10;
y='Ram'
z=y+"Chennale";
print (x);
print (y);
print (z);
print()
#Variable declaration and case sensitive
_a=10;
A=20
a=30
print (_a,a,A)
print( _a+a+A);
print()

c=50;
d="Ram";
e=4.3
#print(d+c)


# int float and complex 

f =-5j
print (type(a));
print (type(d));
print (type(e));
print(type(f))
print()

'''
OUTPUT
<class 'int'>
<class 'str'>
<class 'float'>
<class 'complex'>
'''

#Variable Type

f = int(1); #
g = int(1.2); #
h = int("1") #
#i = int('1.4') #
print(f, g, h);
print()

i = float(2);
j = float(2.2);
k =float("2");
l= float("2.3");   
print(i,j,k)
print()
m=str("s1");
n=str("3");
o=str("3.1")
p=str("Rama");
print(m,n,o,p)

#strings
a="Hello world"
print(a);
print();
print("Second position : at 'Hello world' is    "+a[2]);
print();
print ("White spaces removed : "+a.strip())
print();

#Enter input from command prompt
print("Ente your name : ");
q= input();
print("Hello "+q);

tl= ["a","b","c"];
print(tl);

tl[1]="bda";
print(tl)

#list constructor
plist=list(("1","2","3"));
print(plist);

plist.append("4");
print(plist);

plist.remove("3");
print(plist);
print(len(plist));


# this is tuples
thistuple=["1","2"];
print(thistuple)

print(len(thistuple));
#this tuple constructor
ttuple=tuple(("1","constructor","3"));
print(ttuple);


# set in python 
thisSet={"1","2","3","ram"};
print(thisSet);
thisSet.add("4");
print(thisSet);
thisSet.add("ram");#Duplicates not allowed
print(thisSet)
thisSet.add("Ram");
print(thisSet);
print(len(thisSet));


#set constructors
setConstructor=set(("1","A","3","2","c","B"));
print(setConstructor);
'''
Output  # characters at left side and numbers at right side in same inserted order
set(['1', '3', '2', 'ram'])
set(['1', '3', '2', 'ram'])
set(['1', '3', '2', 'ram', '4'])
set(['1', '3', '2', 'ram', '4'])
set(['Ram', 'ram', '1', '3', '2', '4'])
('Set length is : ', 6)
set(['A', 'c', 'B', '1', '3', '2'])
'''


# dictionary in python 
thisDictionary={
    "1":"A",
    "2":"B",
    "3":"C",
    "4":"D"
};
print(thisDictionary);
thisDictionary["1"]=("a");
thisDictionary["2"]="b";
print(thisDictionary);
#dictionary constructors
dictConstru=dict(apple="green", banana="yellow", cherry="red");
print(dictConstru);
dictConstru["sweet"]="mango";
print(dictConstru);
del(dictConstru["sweet"]);
print(dictConstru);
'''
{'1': 'A', '3': 'C', '2': 'B', '4': 'D'}
{'1': 'a', '3': 'C', '2': 'b', '4': 'D'}
{'cherry': 'red', 'banana': 'yellow', 'apple': 'green'}
{'cherry': 'red', 'sweet': 'mango', 'banana': 'yellow', 'apple': 'green'}
{'cherry': 'red', 'banana': 'yellow', 'apple': 'green'}
'''


#Python Conditions and If statements
a = 33
b = 200
if b > a:
  print("b is greater than a")
  
print();
c=10
if a > b: print("a is greater than b");
elif b>c: print("b is greater than c");


i = 1
while i < 6:
  print(i)
  i += 1
  
  
# Defining functions in python
    
def fun1(ram):
    print (ram);
fun1("ram");
fun1("Chennale")
fun1("Kal")

#Default value in function

def funDefaultValue(country="India"):
    print("My country  is : "+country)
funDefaultValue("Japan");
funDefaultValue();
funDefaultValue("israel");


# Defining functions in python
    
def fun2(ram):
    print (ram);
fun1("ram");
fun1("Chennale")
fun1("Kal")

#Default value in function

def funDefaultValue1(country="India"):
    print("My country  is : "+country)
funDefaultValue1("Japan");
funDefaultValue1();
funDefaultValue1("israel");


def my_function(x):
  return x
def my_function1(x):
  return 5*x
print("")
print(my_function(3))
print(my_function(5))
print(my_function(9))
print(my_function1(5))
print(my_function1(9))
print("")

#lambada function
myfun= lambda i:i*2
print(myfun(2))

myfun1 = lambda x,y : x+y
print(myfun1(2,3))

myfun2 = lambda x,y : x*y;
print(myfun2(10,10))
print("")

def myfunc(n):
  return lambda i: i*n
doubler = myfunc(2)
tripler = myfunc(3)
val = 11
print("Doubled: " + str(doubler(val)) + ". Tripled: " + str(tripler(val)))


#Arrays in python

#Arrays are not built-in functions in python
car=["Maruti","ford","skoda","TaTa"];
print(car);
print(car[1]); 
del(car[0]);
print(car)
print("")

x=car[1];
print(x)
print(car)
car[0]="NANO"
print(car);
print(len(car))
print("")
for x in car:
    print("")
    print(x);
    
car.pop(0);
print(car);


## Creating a class
class Person():
    def __init__(self,name,age):
        self.name=name;
        self.age=age;
    
p1= Person("Ram", 27)
print(p1.name,"   ",p1.age);
#print(p1.age);






