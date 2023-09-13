#IBM_pythonForDataScience
#Module1_stringOperations
#CarlosRamos

import re

#Declaration
name = "Michael Jackson"
print(name)

#Indexing
print(name[0])
print(name[6])
print(name[13])

#Negative Indexing
print(name[-1])
print(name[-15])

#Slicing
print(len("Michael Jackson"))
print(name[0:4])
print(name[8:12])
print(name[::2])
print(name[0:5:2])

#Concatenate

statement = name + " is the best"
print(statement)
print(name*3)

#Escape Secuences
print(name + "\n is the best")
print(name + "\t is the best")
print(name + " \\ is the best")
print(r" Michael Jackson \ is the best" )

#String Operations
a = "Thriller is the sixth studio album"
print("Before upper: ", a)
b = a.upper()
print("After upper: ", b)

a1 = "MICHAEL JACKSON IS THE BEST"
print("Before lower: ", a1)
b1 = a.lower()
print("After lower: ", b1)

a2 = "Michael Jackson is the best"
print(a2)
b2 = a2.replace("Michael", "Janet")
print(b2)

a3 = "Hello! Michael Jackson has: 12 characters."
print(a3)
b3 = a3.replace("!", ","). replace(":", ""). replace(".", "!")
print(b3)

print(name.find("el"))
print(name.find("Jack"))
print(name.find('Jasdfasdasdf'))

split_string = (name.split())
print(split_string)

#RegEx
s1 = "Freddie Mercury is the best"
pattern = r"Mercury"
result = re.search(pattern, s1)

if result:
    print("Match found!")
else:
    print("Match not found.")
    
patternX = r"\d\d\d\d\d\d\d\d\d\d"
textX = "My Phone number is 123467890"
matchX = re.search(patternX, textX)

if matchX:
    print("Phone number found: ", matchX.group())
else:
    print("No match")
    
patternY = r"\W"
textY = "Hello, world!"
matchY = re.findall(patternY,textY)
print("Matches: ", matchY)

s2 = "The real name of Freddie Mercury was Farrokch Bulsara"
result_s2 = re.findall("Farrokch", s2)
print(result_s2)

split_array = re.split("\s", s2)
print(split_array)

patternZ = r"Farrokch Bulsara"
replacement = "Pedro Pérez"
new_string = re.sub(patternZ, replacement, s2, flags=re.IGNORECASE)
print(new_string)