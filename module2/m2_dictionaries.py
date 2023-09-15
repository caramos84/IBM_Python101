#IBM_pythonForDataScience
#Module2_pythonDataStructures
#CarlosRamos

#Dictionaries
Dict = {"key1": 1, "key2": "2", "key3": [3, 3, 3], "key4": (4, 4, 4), ("key5"): 5, (0, 1): 6}
print(Dict)

print(Dict["key1"])
print(Dict[(0, 1)])

release_year_dict = {"Thriller": "1982", "Back in Black": "1980", "The Dark Side of the Moon": "1973", "The Bodyguard": "1992", "Bat Out of Hell": "1977", "Their Greatest Hits (1971-1975)": "1976", "Saturday Night Fever": "1977", "Rumours": "1977"}
print(release_year_dict)

#Keys
print(release_year_dict["Thriller"])
print(release_year_dict["The Bodyguard"])
print(release_year_dict.keys())
print(release_year_dict.values())

release_year_dict["Graduation"]="2007"
print(release_year_dict)
del(release_year_dict["Thriller"])
del(release_year_dict["Graduation"])
print(release_year_dict)
print("The Bodyguard" in release_year_dict)

soundtrack_dic = {"The Bodyguard": "1992", "Saturday Night Fever": "1977"}
print(soundtrack_dic)
print(soundtrack_dic.keys())
print(soundtrack_dic.values())

album_sales_dict = {"The Bodyguard": 50, "Back in Black": 50, "Thriller": 65}
print(album_sales_dict)
print(album_sales_dict.keys())
print(album_sales_dict.values())