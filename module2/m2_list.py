#IBM_pythonForDataScience
#Module2_pythonDataStructures
#CarlosRamos

#list
Lista = ["Michael Jackson", 10.1, 1982]
print(Lista)

#Indexing
print('the same element using negative and positive indexing:\n Postive:',Lista[0],
'\n Negative:' , Lista[-3])
print('the same element using negative and positive indexing:\n Postive:',Lista[1],
'\n Negative:' , Lista[-2])
print('the same element using negative and positive indexing:\n Postive:',Lista[2],
'\n Negative:' , Lista[-1])

#List Concatenation
Lista1 = Lista + [[1,2], ("A", 1)]
print(Lista1)

#List Operations
print(Lista1[3:5])
Lista1.extend(["pop", 10])
print(Lista1)

Lista1.append(["pop", 10])
print(Lista1)

Lista_A = ["disco", 10, 1.2]
print("Before change: ", Lista_A)
Lista_A[0] = "hard rock"
print("After change: ", Lista_A)

print("hard rock".split())
print("A, B, C, D".split(","))

#Copy and CLone List
Lista_B = Lista_A
print("Lista A: ", Lista_A)
print("Lista B: ", Lista_B)

print("Lista_B[0]: ", Lista_B[0])
Lista_A[0] = "Afro Beat"
print("Lista_B[0]: ", Lista_B[0])

Lista_B = Lista_A[:]
print(Lista_B)

print("Lista_B[0]: ", Lista_B[0])
Lista_A = "Afro Beat"
print("Lista_B[0]: ", Lista_B[0])