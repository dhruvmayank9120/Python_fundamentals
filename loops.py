#loops-> they are used in python to repeat instructions

#while loop
# count = 0

# while count<5:
#     print("hello")
#     count = count + 1

# i = 5
# while i>0:
#     print(i)
#     i = i - 1

#BREAK AND CONTINUE

#below code prints till 3
# i=1
# while i<=5:
#     print(i)
#     if(i==3):
#         break
#     i+=1

#below code print except 3
# i = 0
# while i<=5:
#     if(i==3):
#         i = i + 1
#         continue
#     print(i)
#     i = i + 1
        
#for loop

# list = [1,2,3,4,5]

# for num in list:
#     print(num)

# str = "ApnaCollege"

# for char in str:
#     print(char)

#we can use else inside for loop

#PRACTICE PROBLEMS ON FOR LOOP

#q1-> print the elements of the following using a loop:
#[1,4,9,16,25,36,49,64,81,100]

# nums=[1,4,9,16,25,36,49,64,81,100]

# for num in nums:
#     print(num)



#q2-> Search for a number x in this tuple using loop:
#nums=[1,4,9,16,25,36,49,64,81,100]

# user_in=int(input("give any number"))

# nums=[1,4,9,16,25,36,49,64,81,100]
# target = 64
# for num in nums:
#     if(target == user_in):
#         print("found")
#         break
    
#range()-> returns a sequence of numbers, starting from 0 by default and increments by 1 by default and stops before a specified number.
#range(start?(optional), stop(mandatory), step?(optional))

# seq = range(10)

# for i in seq:
#     print(i)

#can be written like this also
# for i in range(10):
#     print(i)

# for i in range(2,10):
#     print(i)

# for i in range(1,10,2):
#     print(i)
#in range(inclusive, exclusive)
# for i in range(1,101):
#     print(i)

# for i in range(100, 0, -1):
#     print(i, end=", ")

# for i in range(1,11):
#     print(5 * i)

#PASS statement-> null statement that does nothing. It is used as a placeholder for the future code

for i in range(5):
    pass

print("some useful work")