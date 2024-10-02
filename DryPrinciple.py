winning_number=43
guess=1
number=int(input("enter a number between 0 to 100:"))
game_over=False
while not game_over:
    if number==winning_number:
        print(f"winner winner chicken dinner in {guess} times")
        game_over=True
    else:
        if number<winning_number:
            print("too low")
       
        else:
            print("too high")
    guess+=1
    number=input("guess again")
    #DRY-dont repeat yourself