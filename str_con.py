# # strings and conditions

# str1 = "This is a string."
# str2 = "apna college"

# #can be in triple quotes
# str3 = '''This is also a string'''

# #ESSCAPE SEQUENCES

# #/n-> new line
# str4 = "This is a string\nwith a new line"
# print(str4)

# #/t-> tab
# str5 = "This is a string\twith a tab"
# print(str5)

# #OPERATIONS ON STRINGS
# #concatenation
# str6 = str1 + " " + str2
# print(str6)

# final_str = str1 + " " + str2 + " " + str3
# print(final_str)

# #length of string
# #len() also counts spaces and special characters
# print(len(str1))
# print(len(final_str))

# #indexing-> positioning of characters in a string
# #starts from 0
# #A P N A _ C O L L E G E
# #0 1 2 3 4 5 6 7 8 9 10 11
# print(str2[0]) #A
# print(str2[1]) #P
# print(str2[2]) #N
# print(str2[3]) #A
# print(str2[4]) #_
# print(str2[5]) #C
# print(str2[6]) #O
# print(str2[7]) #L
# print(str2[8]) #L
# print(str2[9]) #E
# print(str2[10]) #G
# print(str2[11]) #E

# #they are immutable-> cannot be changed
# #str2[0] = "a" #error

# #slicing-> extracting a portion of a string
# #syntax-> string[start:end:step]
# #syntax2-> string[start:end] (step is by default 1)
# #start is inclusive and end is exclusive
# str7="Apna College"
# print(str7[0:4]) #apna
# print(str7[4:12]) # college

# #slicing-> this means start from index 0 to the end of the string
# print(str7[0:]) #Apna College
# #can be -ve indexing-> starts from the end of the string
# print(str7[-1]) #e
# print(str7[-2]) #g

# str8 = "apple"
# print(str8[-5:-1])

# #endswith-> checks if a string ends with a specific substring
# #gives a boolean output
# print(str8.endswith("le")) #True
# print(str8.endswith("p")) #False

# #capitalize-> converts the first character of a string to uppercase and the rest to lowercase
# print(str8.capitalize()) #Apple

# #replace-> replaces a specified substring with another substring
# print(str8.replace("p", "b")) #abble

# #find-> returns the index of the first occurrence of a specified substring, or -1 if not found
# #returns the index of the first occurrence of "p"
# print(str8.find("p")) #1

# #count-> counts the number of occurrences of a specified substring in a string
# print("count of 'p': ", str8.count("p")) #2

# #PRACTICE PROBLEMS
# #WAP to input user's first name and laste name & print the length

# name = input_str = input("Enter your first name and last name: ")
# print("Length of your full name:", len(name))

#WAP to find the occurrence of a specific character in a string and print the index

# str = "Hi, $I am a $ symbol $99.89"
# print(str.count("$")) #3


##--> CONDITIONAL STATEMENTS
##->syntax
#if(condition):
    #code to be executed if condition is true
#elif(condition):
    #code to be executed if the condition is true
#else:
    #code to be executed if none of the conditions are true

#--EXAMPLE
# age = 21

# if(age >= 18):
#     print("You are an adult.")

#->EXAMPLE
# light = "green"
# if(light == "green"):
#     print("Go")
# elif(light == "yellow"):
#     print("Slow down")
# else:
#     print("Stop")

#->EXAMPLE
#indentation-> this means spaces or tabs at the beginning of a line of code
# age = 24
# if(age >24):
#     print("You are eligible to vote.")

#-->EXAMPLE

# marks = int(input("Enter your marks: "))

# if marks >= 90:
#     print("Grade: A")
# elif marks >= 80 and marks < 90:
#     print("Grade: B")
# elif marks >= 70 and marks < 80:
#     print("Grade: C")
# elif marks >= 60 and marks < 70:
#     print("Grade: D")
# else:
#     print("Grade: F")

#->nested if-else statements-> this means an if-else statement inside another if-else statement
#syntax
#if(condition):
    #code to be executed if condition is true
    #if(condition):
        #code to be executed if condition is true
    #else:
        #code to be executed if condition is false

#PRACTICE PROBLEMS

#Q1 WAP to check if number is even or odd

# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print("The number is even.")
# else:
#     print("The number is odd.")

# #Q2 WAP to find the greatest of 3 numbers entered by the user
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# num3 = int(input("Enter the third number: "))

# if num1 >= num2 and num1 >= num3:
#     print("The greatest number is:", num1)
# elif num2 >= num1 and num2 >= num3:
#     print("The greatest number is:", num2)
# else:
#     print("The greatest number is:", num3)

# #Q3 WAP to check if a number is multiple of 7 or not
# num = int(input("Enter a number: "))
# if num % 7 == 0:
#     print("The number is a multiple of 7.")
# else:
#     print("The number is not a multiple of 7.")

