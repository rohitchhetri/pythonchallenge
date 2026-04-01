#  Q1: Print numbers 1 to 10

# for i in range(1,11):
#     print(i)


# # Q2 Even number  from 1 to 20 
# for i in range(1,21):
#     if i % 2 == 0:
#         print(i)

# # Q3 Multiplication Table 
# print("Welcome to Multiplication Table")

# while True:
#     number = int(input("Enter your number: "))

#     for i in range(1, 11):
#         print(number, "x", i, "=", number * i)

#     choice = input("Do you want another? (yes/no): ")

#     if choice.lower() != "yes":
#         print("Thank you!")
#         break

# #Q4 Take input n → print numbers from 1 to n
# n = int(input("Enter number: "))
# for i in range (1, n+1):
#  print(i, end=" ")

#Q5 
total = 0 
n = 5
for i in range(1, n+1):
    total += i 

print("Sum: ", total)