# challenge 1

age = int(input("How old are you? "))

if age > 0 and age <= 12:
    print("You're a kid! Go play outside")
elif age >= 13 and age <= 17:
    print("Teen vibes! Focus on school")
elif age >= 18 and age <= 24:
    print("Young adult! Explore & build")
elif age >= 25 and age <= 40:
    print("Prime years! Grind mode")
elif age >= 41:
    print("You're seasoned! Enjoy the wisdom")
else:
    print("Hmm... that doesn't look like a real age")


# challenge 2

menu = 'MENU\n 1. Burger\n 2. Pizza\n 3. Salad\n 4. Exit\n'
print(menu)

user_choice = int(input("Pick a number from the menu: "))

if user_choice == 1:
    print("Burger")
elif user_choice == 2:
    print("Pizza")
elif user_choice == 3:
    print("Salad")
elif user_choice == 4:
    print("Bye!")
else :
    print("Invalid option")

# challenge 3

username = input("Give me a username: ")

if username != '' and len(username) > 3:
    print('Valid username')
else:
    print('Error...')


