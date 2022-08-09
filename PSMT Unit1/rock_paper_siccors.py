import random  # used for the random computer choice

#  introduce the game and rules
print("Hello! Welcome to Paper-Siccors-Rock-Lizard-Spock! ")
print("""
Here are the rules:
1) Scissors beats Paper and Lizard 
2) Paper beats Rock and Spock
3) Rock beats Scissors and Lizard
4) Lizard beats Spock and Paper 
5) Spock beats Scissors and Rock
""")
print("You have five choices: ")
print("To chose paper enter 1, scissors is 2, rock is 3, lizard is 4 and spock is 5")
print("")
repeat = True
players = True
equal = True

multi = input("Are there one, or two players? ")  # ask input for one or two players
while repeat:  # repeat if number of players isn't correct
    if multi == "two":  # if two players
        while players:  # if one or two players is correct
            while equal:  # if a and b are between 1 and 5
                a = input("Player one! What is your move? ")  # input player one move as numbers between 1 and 5
                b = input("Player two! What is your move? ")  # input player two move as numbers between 1 and 5
                if a.isdigit() and b.isdigit():  # if a and b are numbers
                    a = int(a)
                    b = int(b)
                    if 1 <= a <= 5 and 1 <= b <= 5:  # if a and b aren't numbers
                        players = False
                        repeat = False
                        equal = False
                    else:
                        print("Please enter your choice: paper (1), scissors (2), rock (3), lizard (4) or spock (5).")
                        players = False
                        repeat = False
                        equal = True
                else:
                    print("Please enter a number.")
                    print("")
                    players = True
                    repeat = False
                    equal = False

    elif multi == "one":  # if one player
        num = True
        while num:
            a = input("What is your move? ")  # input player move
            digit = True
            while digit:
                if a.isdigit():  # if a is number
                    if a > 5 or a < 1:  # if a below 5 or above 1
                        a = int(a)
                        b = random.randint(0, 5)  # computer input random number = b
                        repeat = False
                        digit = False
                    else:
                        print("Please enter your choice: paper (1), scissors (2), rock (3), lizard (4) or spock (5).")
                        num = True
                        digit = False
                else:
                    print("Please enter a number.")
                    digit = True

    else:
        print("Please enter one or two players.")  # if one or two players is not entered, ask question again
        repeat = True                              # and tell user to enter one or two players
if multi == "one":
    player_1 = "You"
    player_2 = "Computer"
elif multi == "two":
    player_1 = "Player One"
    player_2 = "Player Two"

#  show choices:

if a == 1:
    print(f"{player_1} chose Paper!")
elif a == 2:
    print(f"{player_1} chose Scissors!")
elif a == 3:
    print(f"{player_1} chose Rock!")
elif a == 4:
    print(f"{player_1} chose Lizard!")
else:
    print(f"{player_1} chose Spock!")

if b == 1:
    print(f"{player_2} chose Paper!")
elif b == 2:
    print(f"{player_2} chose Siccors!")
elif b == 3:
    print(f"{player_2} chose Rock!")
elif b == 4:
    print(f"{player_2} chose Lizard!")
else:
    print(f"{player_2} chose Spock!")
print("")

w = (5 + a - b) % 5  # winner

if w == 1 or w == 3:  # if w equals 1 or 3, player one wins
    winner = player_1
    print(f"{winner} Wins!")

if w == 2 or w == 4:  # if w equals 2 or 4, player two wins
    winner = player_2
    print(f"{winner} Wins!")

if w == 0:  # if w equals 0, its a tie
    print("Its a Tie!")
