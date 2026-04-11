# =========================
# Exercise 1: Sets
# =========================

my_fav_numbers = {2, 4, 6, 8}

my_fav_numbers.add(8)   
my_fav_numbers.add(10)

my_fav_numbers.discard(10)

friend_fav_numbers = {2, 4}

our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

print(our_fav_numbers)


# =========================
# Exercise 2: Basket (Lists)
# =========================

basket = ["Banana", "Apples", "Oranges", "Blueberries"]

basket.remove("Banana")
basket.remove("Blueberries")

basket.append("Kiwi")
basket.insert(0, "Apples")

print(basket.count("Apples"))

basket.clear()
print(basket)


# =========================
# Exercise 3: Floats List
# =========================

numbers = []
num = 1.5

for i in range(8):
    numbers.append(num)
    num = num + 0.5

print(numbers)


# =========================
# Exercise 4: Even Numbers (For Loop)
# =========================

for i in range(1, 21):
    if i % 2 == 0:
        print(i)


# =========================
# Exercise 5: While Loop (Name Check)
# =========================

while True:
    name = input("Enter your name: ")

    if name.isdigit() or len(name) < 3:
        print("give the correct name")
    else:
        print("thank you")
        break


# =========================
# Exercise 6: Favorite Fruits
# =========================

fruits = input("Enter your favorite fruits (separated by spaces): ")
fruits_list = fruits.split()

new_fruit = input("Enter a fruit: ")

if new_fruit in fruits_list:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")
    
    # =========================
# Exercise 8: Pizza Toppings
# =========================

toppings = []

while True:
    topping = input("Enter a topping (or 'quit' to stop): ")

    if topping == "quit":
        break

    toppings.append(topping)
    print(f"Adding {topping} to your pizza.")

# calculate total price
total_price = 10 + len(toppings) * 2.5

# print results
print("Your toppings:", toppings)
print("Total price:", total_price)

# =========================
# Exercise 9:  Tickets
# =========================

total_cost = 0

while True:
    age = input("Enter age (or 'quit' to stop): ")

    if age == "quit":
        break

    age = int(age)

    if age < 3:
        cost = 0
    elif age <= 12:
        cost = 10
    else:
        cost = 15

    total_cost += cost

print("Total cost:", total_cost)

# =========================
# Bonus: Restricted Movie
# =========================

allowed = []

while True:
    age = input("Enter age (or 'quit' to stop): ")

    if age == "quit":
        break

    age = int(age)

    if 16 <= age <= 21:
        allowed.append(age)

print("Allowed people:", allowed)