
# Exercise 1
print("Hello world\n" * 4)

# Exercise 2
print((99 ** 3) * 8)

# Exercise 3
print(5 < 3)              # False
print(3 == 3)             # True
print(3 == "3")           # False
print("Hello" == "hello") # False

# Exercise 4
computer_brand = "mac"
print("I have a " + computer_brand + " computer.")

# Exercise 5
name = "amit"
age = 25
shoe_size = 38
info = "my name is " + name + " i am " + str(age) + " years old and my shoe size is " + str(shoe_size)
print(info)

# Exercise 6
a = 10
b = 5
if a > b:
    print("Hello World")

# Exercise 7
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# Exercise 8
user_name = input("What is your name? ")
if user_name == "amit":
    print("We have the same name! 🎉")
else:
    print("Nice to meet you! 😊")

# Exercise 9
height = int(input("What is your height in cm? "))
if height > 145:
    print("You are tall enough to ride! 🎢")
else:
    print("You need to grow more to ride! 📏")