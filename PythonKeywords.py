#Python keywords, identifiers and variables. These are the basic building blocks of Python programming.
import keyword
print(keyword.kwlist)
print(keyword.iskeyword)

print(keyword.iskeyword("techbeamers"))
print(keyword.iskeyword("try"))
print('ram'.isidentifier())
test='Ramvar'
intVar=100
print(intVar,test);