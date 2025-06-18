import random

start_range = int(input("Enter the start range: "))
end_range = int(input("Enter the end range: "))

my_list = []

for i in range(start_range, end_range+1):
    my_list.append(i)

random_guess = random.choice(my_list)
user_guess = int(input("Enter The Guess: "))
while user_guess != random_guess:     #We use While loop because we don't have a pre-defined universe to iterate
    if user_guess > random_guess:
        print("Your Guess is High!!")
        print("Try Again")

    if user_guess < random_guess:
        print("Your Guess is Low!!")
        print("Try Again")
    user_guess = int(input("Enter The New Guess: "))
print("Your Guess is Absolutely Correct!! 🎉")