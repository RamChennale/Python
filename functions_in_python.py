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
# Defining functions in python

#syntax

def my_function():
  print("Hello from a function")

my_function();

def fun_name():
    print("Entered inside the function")
    print("Eneter value  a")
    #a=input()
    print("Eneter value  b")
   # b=input()
    a=10
    b=20
    if a==b:
        print("a and b are a==b")
    else:
        print("a and b are a!=b")

fun_name();

def my_Name_Is(fname):
    print(fname+" Lotus")

my_Name_Is("Ram")
my_Name_Is("Navneet")


#Default value in function

def funDefaultValue(country="India"):
    print("My country  is : "+country)
funDefaultValue("Japan");
funDefaultValue();
funDefaultValue("israel");

def set_Fun_Def_Val(company="Lotus Tech"):
    print("I am working at : "+company)

set_Fun_Def_Val();
set_Fun_Def_Val("Ram channale");
set_Fun_Def_Val();
set_Fun_Def_Val("N N");

def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))
