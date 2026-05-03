#list-> a built in data type in python which is used to store multiple items in a single variable
#syntax->
# list_name = [item1, item2, item3, ...]
#this is similar to arrays in other programming languages but lists are more flexible as they can store different types of data and can be modified after creation

#->EXAMPLE
marks = [85, 90, 78, 92, 88]
print(marks) #output: [85, 90, 78, 92, 88]
print(type(marks)) #output: <class 'list'>
#type-> gives the type of the variable

#accessing list items-> we can access list items using their index
#syntax-> list_name[index]
#similar as arrays accessing in other programming languages but in python index starts from 0
print(marks[0]) #output: 85
print(marks[3]) #output: 92

#list can store different types of data
my_list = [1, "Hello", 3.14, True]
print(my_list) #output: [1, 'Hello', 3.14, True]
#lists are mutable-> we can change the items in a list after it has been created
my_list[1] = "World"
print(my_list) #output: [1, 'World', 3.14, True]

#-> LIST SLICING-> this is same as we do in strings but here we can slice the list to get a sublist
#syntax-> list_name[start:stop:step]
#synatx2-> list_name[start:stop] (step is by default 1)
#start is inclusive and stop is exclusive

print(marks[1:4]) #output: [90, 78, 92]
print(marks[0:]) #output: [85, 90, 78, 92, 88]
print(marks[:3]) #output: [85, 90, 78]

#LIST METHODS
#append-> adds an item to the end of the list
marks.append(95)
print(marks) #output: [85, 90, 78, 92, 88, 95]

#len-> gives the number of items in the list
print(len(marks)) #output: 6

#sort-> sorts the items in the list in ascending order
marks.sort()
print(marks) #output: [85, 88, 90, 92, 95]

#sorting in descending order
marks.sort(reverse=True)
print(marks) #output: [95, 92, 90, 88, 85]

#reverse-> reverses the order of the items in the list
marks.reverse()
print(marks) #output: [85, 88, 90, 92, 95]

#insert-> inserts an item at a specified index
#syntax-> list_name.insert(index, item)
marks.insert(2, 89)
print(marks) #output: [85, 88, 89, 90, 92, 95]

#remove-> removes the first occurrence of a specified item from the list
#syntax-> list_name.remove(item)
marks.remove(89)
print(marks) #output: [85, 88, 90, 92, 95]

#removes the last item from the list
marks.pop()
print(marks) #output: [85, 88, 90, 92, 95]