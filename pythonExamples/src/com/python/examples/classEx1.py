## Creating a class
class Person():
    def __init__(self,name,age):
        self.name=name;
        self.age=age;

p1= Person("Ram", 27)
print(p1.name,"   ",p1.age);