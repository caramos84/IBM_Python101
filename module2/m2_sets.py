#IBM_pythonForDataScience
#Module2_pythonDataStructures
#CarlosRamos

#Sets
set1 = {"pop", "rock", "soul", "hard rock", "rock", "disco"}
print(set1)

album_list = ["Michael Jackson", "Thriller", 1982, "00:42:19", "Pop, Rock, R&B", 46.0, "30-Nov-82", None, 10]
album_set = set(album_list)
print(album_set)

music_genres = set(["pop", "pop", "rock", "folk rock", "hard rock", "soul", "progressive rock", "sof rock", "R&B", "disco"])
print(music_genres)

#Set Operations
A = set(["Thriller", "Back in Black", "AC/DC"])
print(A)
A.add("NSYNC")
print(A)
A.remove("NSYNC")
print(A)
print("AC/DC" in A)

#Sets Logic Operations
album_set01 = set(["Thriller", "AC/DC", "Back in Black", ])
album_set02 = set(["AC/DC", "Back in Black", "The Dark Side of the Moon"])
print(album_set01, album_set02)

intersection = album_set01 & album_set02
print(intersection)
print(album_set01.difference(album_set02))
print(album_set02.difference(album_set01))
print(album_set01.intersection(album_set02))
print(album_set01.union(album_set02))
print(album_set01.issuperset(album_set02))
print(album_set02.issubset(album_set01))
print(set({"Back in Black", "AC/DC"}).issubset(album_set01))
print(album_set01.issuperset({"Back in Black", "AC/DC"}))