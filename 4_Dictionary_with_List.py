# 4 Iterate Through a Dictionary with List Values
print("\n****** Iterate Through a Dictionary with List Values ****\n")

dojo = {
'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for key, value in some_dict.items():
        print(f'''\n{len(value)} {key}''')
        for item in value:
            print(item)

printInfo(dojo)