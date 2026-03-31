age = int(input("Enter your age: "))

if age < 13:
    print("You are child")
elif 13 <= age <=19:
    print("You are Teen")
elif 20 <= age <=59:
    print("You are Adult")
else: 
    print("You are Senior")
