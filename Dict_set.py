#dictionary: dictionaries are used to store data values in key:values pairs
#they are unordered, mutable(changeable)& don't allow duplicate keys

# info = {
#     "key":"value",
#     "name":"Ram",
#     "age":21,
#     "is_adult":True,
#     "subjects":["python","Java","Javascript"],
#     "topics":("oops","data_types")
# }

#key can't be numbers
#immutable




# print(type(info))
# print(info)

#print particular values
# print(info["name"])
# print(info["topics"])
# print(info["subjects"])

#assigning new and updating existing
# info["name"]="Shyam"
# print(info["name"])

# info["surname"]="kumar"
# print(info)

#null dictionary

null_dict={}
# print(null_dict)

#nested_dictionary

student={
    "name":"Rahul",
    "subjects":{"physics":97,
                "chemistry":87,
                "maths":79
                }
}
# print(student)
#accessing nested data

# print(student["subjects"]["chemistry"])

#Dictionary Methods

#1.my_dict.keys()-> comes in list format

# print(student.keys())
# print(list(student.keys()))#typecasted to list form

#myDict.values()->gives the values

# print(student.values())
# print(list(student.values()))

#my_dict.items-> return in key-value pairs in tuples

# print(student.items())
# print(list(student.items()))

#my_dict.get()-> return the key according to the value

# print(student["name"])
# print(student.get("name"))


# print(student["name2"])#-> gives error
# print(student.get("name2"))#preferred because doesn't let program crash

# student.update({"city":"Delhi"})
# print(student)

#--->SETS:set is the collection of the unordered items
#sets are mutable but their elements are immutable
#Each element must be unique and immutable

collection={1,2,3,4}
# print(collection)
# print(len(collection))
# print(type(collection))

collection2={1,2,2,4,6,7,5}
print(collection2)

#empty set

collection_3=set()#creating empty set
# collection_3={}#users knows it is set but in program it is empty dict

#-->METHODS IN SETS

#1. set.add(element)-> adds elemet
collection_3.add(1)
collection_3.add(2)
collection_3.add(3)
# collection_3.add((1,2,3))
# collection_3.add([1,2,3])#error
# print(collection_3)


#2 set.remove(element)->removes the element
# collection_3.remove(2)
# print(collection_3)


#3. set.clear()#empties the set
# collection_3.clear()
# print(collection_3)


#4.set.pop()->removes a random value
# collection_3.pop()
# print(collection_3)


#set.union->combines both set and values and return new
set1={1,2,3}
set2={2,3,4}

print(set1.union(set2))#{1,2,3,4}


#set.intersection->combines common values and returns new
print(set1.intersection(set2))