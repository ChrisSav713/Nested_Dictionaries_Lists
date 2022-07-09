# 3 Get Values From a List of Dictionaries
print("\n****** Get Values From a List of Dictionaries ****\n")

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary2(key_name, some_list):
    for list_item in some_list:
        print(list_item[key_name])

iterateDictionary2('first_name', students)
print("")
iterateDictionary2('last_name', students)