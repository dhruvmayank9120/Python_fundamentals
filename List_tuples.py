# #list-> a built in data type in python which is used to store multiple items in a single variable
# #syntax->
# # list_name = [item1, item2, item3, ...]
# #this is similar to arrays in other programming languages but lists are more flexible as they can store different types of data and can be modified after creation

# #->EXAMPLE
# marks = [85, 90, 78, 92, 88]
# print(marks) #output: [85, 90, 78, 92, 88]
# print(type(marks)) #output: <class 'list'>
# #type-> gives the type of the variable

# #accessing list items-> we can access list items using their index
# #syntax-> list_name[index]
# #similar as arrays accessing in other programming languages but in python index starts from 0
# print(marks[0]) #output: 85
# print(marks[3]) #output: 92

# #list can store different types of data
# my_list = [1, "Hello", 3.14, True]
# print(my_list) #output: [1, 'Hello', 3.14, True]
# #lists are mutable-> we can change the items in a list after it has been created
# my_list[1] = "World"
# print(my_list) #output: [1, 'World', 3.14, True]

# #-> LIST SLICING-> this is same as we do in strings but here we can slice the list to get a sublist
# #syntax-> list_name[start:stop:step]
# #synatx2-> list_name[start:stop] (step is by default 1)
# #start is inclusive and stop is exclusive

# print(marks[1:4]) #output: [90, 78, 92]
# print(marks[0:]) #output: [85, 90, 78, 92, 88]
# print(marks[:3]) #output: [85, 90, 78]

# #LIST METHODS
# #append-> adds an item to the end of the list
# marks.append(95)
# print(marks) #output: [85, 90, 78, 92, 88, 95]

# #len-> gives the number of items in the list
# print(len(marks)) #output: 6

# #sort-> sorts the items in the list in ascending order
# marks.sort()
# print(marks) #output: [85, 88, 90, 92, 95]

# #sorting in descending order
# marks.sort(reverse=True)
# print(marks) #output: [95, 92, 90, 88, 85]

# #reverse-> reverses the order of the items in the list
# marks.reverse()
# print(marks) #output: [85, 88, 90, 92, 95]

# #insert-> inserts an item at a specified index
# #syntax-> list_name.insert(index, item)
# marks.insert(2, 89)
# print(marks) #output: [85, 88, 89, 90, 92, 95]

# #remove-> removes the first occurrence of a specified item from the list
# #syntax-> list_name.remove(item)
# marks.remove(89)
# print(marks) #output: [85, 88, 90, 92, 95]

# #removes the last item from the list
# marks.pop()
# print(marks) #output: [85, 88, 90, 92, 95]

#->TUPLES-> a built in data type in python which is used to store multiple items in a single variable but unlike lists, tuples are immutable-> we cannot change the items in a tuple after it has been created
#syntax-> tuple_name = (item1, item2, item3, ...)
#example
#they are immutable-> cannot be changed
# marks_tuple = (85, 90, 78, 92, 88)
# print(marks_tuple) #output: (85, 90, 78, 92, 88)
# print(type(marks_tuple)) #output: <class 'tuple'>

tup = (1)#python will think that this is an integer not a tuple
# print(type(tup)) #output: <class 'int'>

# tup2 = (1,) #this is a tuple with one item
# print(type(tup2)) #output: <class 'tuple'>

#TUPLE METHODS

#index-> gives the index of the first occurrence of a specified item
#syntax-> tuple_name.index(item)
# print(marks_tuple.index(78)) #output: 2

#count-> gives the number of times a specified item appears in the tuple
#syntax-> tuple_name.count(item)
# print(marks_tuple.count(90)) #output: 1

#remove-> we cannot remove items from a tuple as they are immutable
#add-> we cannot add items to a tuple as they are immutable
#insert-> we cannot insert items into a tuple as they are immutable

#PRACTICE PROBLEMS

#Q1-> WAP to ask the user to enter names of their 3 favourite movies and store them in a  list

# movies=["John Wick", "The Dark Knight", "Inception"]
# print(movies) #output: ['John Wick', 'The Dark Knight', 'Inception']


#Q2-> WAP to check if a list contains a palindrome of elements or not(hint: use copy())

# list1 = [1,2,1]
# list2 = [1,2,3]

# copy_list1=list1.copy()
# copy_list1.reverse()

# if(copy_list1==list1):
#     print("palindrome")
# else:
#     print("not palindrome")

#Q-> WAP to count the number of students with grade A in the following tuple
#("C","D","A","A","B","B","A")

# grades=("C","D","A","A","B","B","A")

# print("no of A grades are: ",grades.count("A"))

grades=["C","D","A","A","B","B","A"]
grades.sort()
print(grades)
print(sorted(grades))