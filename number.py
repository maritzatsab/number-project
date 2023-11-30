# Guess the Number from 1-5

num = ["1", "2", "3", "4", "5"]
guess = num[randint(0,4)]
result = str(input())

if result != guess:
    print("Wrong! Try again.")

else:
    print("Congrats!")
