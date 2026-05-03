# strings and conditions

str1 = "This is a string."
str2 = "apna college"

#can be in triple quotes
str3 = '''This is also a string'''

#ESSCAPE SEQUENCES

#/n-> new line
str4 = "This is a string\nwith a new line"
print(str4)

#/t-> tab
str5 = "This is a string\twith a tab"
print(str5)

#OPERATIONS ON STRINGS
#concatenation
str6 = str1 + " " + str2
print(str6)

final_str = str1 + " " + str2 + " " + str3
print(final_str)

#length of string
#len() also counts spaces and special characters
print(len(str1))
print(len(final_str))

#indexing-> positioning of characters in a string
#starts from 0
#A P N A _ C O L L E G E
#0 1 2 3 4 5 6 7 8 9 10 11
print(str2[0]) #A
print(str2[1]) #P
print(str2[2]) #N
print(str2[3]) #A
print(str2[4]) #_
print(str2[5]) #C
print(str2[6]) #O
print(str2[7]) #L
print(str2[8]) #L
print(str2[9]) #E
print(str2[10]) #G
print(str2[11]) #E

#they are immutable-> cannot be changed
#str2[0] = "a" #error

#slicing-> extracting a portion of a string
#syntax-> string[start:end:step]
#syntax2-> string[start:end] (step is by default 1)
#start is inclusive and end is exclusive
str7="Apna College"
print(str7[0:4]) #apna
print(str7[4:12]) # college