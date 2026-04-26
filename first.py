# print("Hello Yaseen")
# print("Welcome to Python")
# numbers = [1, 2, 3, 4, 5]
# count = len(numbers)
# if count>3 :
#     print("length of list is " , count)

# x = 3
# try:
#   if x > 3 :
#     print("x is greater than 3")
#   elif x < 3 :
#     print("X is less than 3")
#   else :
#     print("x is equal 3")

# except:
#     print("Something went wrong")

# mylist = ["apple", "banana", "cherry" , "apple"]
# #print(mylist)
# print(len(mylist))
# print(mylist[2:3])

# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#   print(x)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "e" in x]

print(newlist)