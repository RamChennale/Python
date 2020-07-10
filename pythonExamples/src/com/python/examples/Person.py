'''
Created on Jun 18, 2018

@author: ramchennale
'''
'''import unittest


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testName(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

'''
class Person():
    def __init__(self, name, age, num, attendance, location):
        self.name = name;
        self.age = age;
        self.num = num;
        self.attendance = attendance;
        self.location = location;


o = Person("Ram", 27, 8989, "Present", "Bengaluru");
print("")
#print(o.name,o.age,o.num,        o.attendance, "    ", o.location); # Space in " " will considered
    

class PersonFunc():
    def __init__(self,name,age,num):
        self.name=name;
        self.age=age;
        self.num=num;
        
    def myDetails(self):
        print("My name is :",self.name)
        print("My age is",self.age);
        print ("My number is : ",self.num);

o1 = PersonFunc("Ram",27,2488);
o1.myDetails();
print("")


class Person1:
    def __init__(self, name1, age1):
        self.name1 = name1
        self.age1 = age1

    def myfunc1(self):
        print("Hello my name is ",self.name1);
        print("And my age is " ,self.age1);

p1 = Person1("John", 36)
p1.myfunc1()
print("")
p1.age1=1000
p1.myfunc1();
print("")
del p1.age1
p1.myfunc1;
del p1;
print("")
p1.myfunc1;
'''
Traceback (most recent call last):
  File "C:\Users\ramchennale\workspace\pythonDemo\examples\Person.py", line 79, in <module>
    p1.myfunc1;
NameError: name 'p1' is not defined
'''

class Restaurant(object):
    bankrupt = False
    def open_branch(self):
        if not self.bankrupt:
            print("branch opened")



'''
class Restaurant(object):
    bankrupt = False
    def open_branch(self):
        if not self.bankrupt:
            print("branch opened")
            
            
x = Restaurant()
x.bankrupt
OR 
The above command is same as:
Restaurant().bankrupt


The first argument of every class method, including init, is always a reference to the current instance 
of the class. By convention, this argument is always named self. In the init method, self refers to the 
newly created object; in other class methods, it refers to the instance whose method was called. For example 
the below code is the same as the above code.

class Restaurant(object):
    bankrupt = False
    def open_branch(this):
        if not this.bankrupt:
            print("branch opened")
'''




x=10
y=20
for i in range(10,20):
    print(x)
    x=y
    y=x+y













