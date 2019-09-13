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
thisSet.add("ddd")
print(thisSet)


#set constructors
setConstructor=set(("1","A","3","2","c","B"));
print(setConstructor);