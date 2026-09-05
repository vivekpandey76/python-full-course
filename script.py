
# for i in range(100):
#     print("hello")

# Print each character of the word "PYTHON" on a new line.

# name = "PYTHON"
# print(name[0])
# print(name[1])
# print(name[2])

# for char in name:
#     print(char)

# Take a number from the user and print its multiplication table.
# num = int(input("Enter your number:"))
# print(num * 1)
# print(num * 2)
# print(num * 3)
# print(num * 4)

# range default -> 0 -> 10 (exclude)
# (1,2..9)
# for i in range(1, 13):
#     print("Multiplication", num * i)

# Keep asking the user for a number and keep adding it to a total.
#  Stop when they enter 0, then print the total.

# 10
# num = int(input("enter your number:"))
# total = 7
# while num != 0:
#     total += num 
#     num = int(input("enter your number:"))

# print(total)

# Q → Print this pattern:
#          *
#          * *
#          * * *
#          * * * *

# Outer loop → controls the rows (lines)
# Inner loop → controls what gets printed in each row
# (1,2,3,4)
# outer loop -> 4 rows
# print("Vivek")

# for i in range(1, 5):
#     for j in range(i):
#         print("*", end=" ")
#     print()

# Print 1 to 10 but stop the loop as soon as the number 5 comes.
# for i in range(1, 11):
#     print(i)
#     if i == 5:
#         break

# print("End")

# Print 1 to 10 but skip all multiples of 3.
# 3 6 9 => don't print this
# i = 1 => 3 / 3 = 0 
# for i in range(1, 11):
#     if i % 3 == 0:
#         continue
#     print(i)

# print("End")

# for i in range(10):
#     pass

# print("hello")

# Search a number from 1 to 10. Print "Found" on break,
# "Not found" from the else.

# num = int(input("Enter your number from 1 to 10:"))
# (1,... 10)
# for i in range(1, 11):
#     if i == num:
#         print("Found")
#         break
# else:
#     print("Not Found")

# if 18 > 20:
#     pass

# Print the sum of the first n numbers.
# 10= 1 + 2 + 3 + 4 + 5 +6 .. + 10
# 1 + 2 + 3 + 4 = 10
# num = int(input("Enter number:")) 
# sum = 0
# for i in range(1, num + 1):
#     sum += i 

# print(sum)

# Reverse a number: 1234 → 4321.
# reverse * 10 + lastDigit
# reverse * 10 + lastDigit => 0 * 10 + 4 = 0 + 4 = 4 * 10 + 3 = 40 + 3 = 43 * 10 + 2 = 430 + 2 = 4321
# num = int(input("Enter your number"))
# reverse = 0
# while num > 0:
#     lastDigit = num % 10  
#     reverse = reverse * 10 + lastDigit 
#     num //= 10
# print(reverse)

# Count the vowels in a word entered by the user.
# "aeiou" 
# name = input("enter your name:").lower() 
# print(name)
# count = 0
# for char in name:
#     if char in "aeiou":
#         count += 1

# print("Number of vowels",count)







