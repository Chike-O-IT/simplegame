a = int(input("Pick a number between 1-100: "))
b = 37

if (a==b):
    print("Congrats!! You win!")
elif (a>b, a<b):
    print("Aw man! Try again.")
    a = int(input("You can do this: "))
    if (a==b):
        print("Congrats!! You win!")
    elif (a>b, a<b):
        print("Dang I thought you had it that time!")
        a = int(input("One more chance: "))
        if (a==b):
            print("Congrats!! You win!")
        elif (a>b, a<b):
            print("You lose! Try again next time!")
print("Goodbye")
