# Write a program that asks for a start and end of a range, generates a random number within the range, asks the user to guess the number and keeps track of the total attempts.
# After guessing the correct number the program should inform the user how many attempts it took to guess the number.

import random

start_range = input("Enter the start of the range: ")
while not start_range.isdigit():
    print("Please enter a valid number.")
    start_range = input("Enter the start of the range: ")

end_range = input("Enter the end of the range: ")
while not end_range.isdigit() or int(end_range) < int(start_range):
    print("Please enter a valid number.")
    end_range = input("Enter the end of the range: ")

random_number = random.randint(int(start_range), int(end_range))

guess = None
attempts = 0

while guess != random_number:
    guess_number = input("Guess a number: ")
    if not guess_number.isdigit():
        print("Please enter a valid number.")
        continue
    attempts += 1
    guess = int(guess_number)

suffix = ""
if attempts > 1:
    suffix = "s"

print(f"You guessed the number in {attempts} attempt{suffix}")