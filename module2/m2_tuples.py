#IBM_pythonForDataScience
#Module2_pythonDataStructures
#CarlosRamos

tuple1 = ("disco", 10, 1.2)
print(type(tuple1))
print(tuple1)

#Indexing
print(tuple1[0])
print(tuple1[1])
print(tuple1[2])

print(type(tuple1[0]))
print(type(tuple1[1]))
print(type(tuple1[2]))

print(tuple1[-1])
print(tuple1[-2])
print(tuple1[-3])

#Concatenate Tuples
tuple2 = tuple1 + ("hard rock", 10)
print(tuple2)

#Slicing
print(tuple2[0:3])
print(tuple2[3:5])
print(len(tuple2))

#Sorting
Ratings = (0, 9, 6, 5, 10, 8, 9, 6, 2)
RatingsSorted = sorted(Ratings)
print(RatingsSorted)

#Nested Tuple
NestedT = (1, 2, ("pop", "rock"), (3, 4), ("disco", (1, 2)))
print(NestedT)
print("Element 0 of Tuple: ", NestedT[0])
print("Element 1 of Tuple: ", NestedT[1])
print("Element 2 of Tuple: ", NestedT[2])
print("Element 3 of Tuple: ", NestedT[3])
print("Element 4 of Tuple: ", NestedT[4])

print("Element 2, 0 of Tuple: ",   NestedT[2][0])
print("Element 2, 1 of Tuple: ",   NestedT[2][1])
print("Element 3, 0 of Tuple: ",   NestedT[3][0])
print("Element 3, 1 of Tuple: ",   NestedT[3][1])
print("Element 4, 0 of Tuple: ",   NestedT[4][0])
print("Element 4, 1 of Tuple: ",   NestedT[4][1])

print(NestedT[2][1][0])
print(NestedT[2][1][1])
print(NestedT[4][1][0])
print(NestedT[4][1][1])

#Quiz on Tuples
genre_tuple = ("pop", "rock", "soul", "hard rock", "soft rock", "R&B", "progressive rock", "disco")
print(genre_tuple)
print(len(genre_tuple))
print(genre_tuple[3])
print(genre_tuple[3:6])
print(genre_tuple[0:2])

C_tuple = (-5, 1, -3)
C_list = sorted(C_tuple)
print(C_list)