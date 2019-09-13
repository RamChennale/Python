'''
Created on Jun 18, 2018

@author: ramchennale
'''
# This is module 

class MyModule:
    def __init__(self, moduleVar):
        self.moduleVar = moduleVar
        
    def myFunFromModule(self):
        print("module Var value ", self.moduleVar)
        print("I am  myFunFromModule() from MyModule() class")  
    
o1 = MyModule(100)
o1.myFunFromModule()



def greeting(name):
    print("Hello, " + name)
    
def I_am_From_MyModule():
    print("This is ' I_am_From_MyModule() ' function from MyModule MODULE ")

# module can contain functions, as already described, but also variables of all types 
#(arrays, dictionaries, objects etc)

person1 = {
    "name": "Ram",
    "age": "20",
    "num" : "101"
    }

print()
print()


import datetime

x = datetime.datetime.now()
print(x);

y = datetime.datetime(2017,9,12)
print(y)
print(y.year)
print(y.strftime("%A"))

'''
import camelcase

c = camelcase.CamelCase()

txt = "hello world  ram chennale"

print(c.hump(txt))
'''

