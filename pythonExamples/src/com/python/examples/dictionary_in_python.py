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
# dictionary in python
thisDictionary={
    "1":"A",
    "2":"B",
    "3":"C",
    "4":"D"
};

print(thisDictionary)

thisdict =	{
  "apple": "green",
  "banana": "yellow",
  "cherry": "red"
}
print(thisdict)

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