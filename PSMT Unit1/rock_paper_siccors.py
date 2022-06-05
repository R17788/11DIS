import random

print("Hello! Welcome to Paper-Siccors-Rock-Lizard-Spock! ")
print("You have five choices: ")
print("Paper (1), Siccors (2), Rock (3), Lizard (4) and Spock (5)")
print("")
repeat = True

while repeat:
    multi = input("Are there one, or two players? ")

    if multi == "two":
        a = int(input("Player one! What is your move? "))
        b = int(input("Player two! What is your move? "))
        player_1 = "Player One"
        player_2 = "Player Two"
        repeat = False

    elif multi == "one":
        a = int(input("What is your move? "))
        b = random.randint(0, 5)
        player_1 = "You"
        player_2 = "Computer"
        repeat = False

    else:
        repeat = True

if a == 1:
    print(f"{player_1} chose Paper!")
elif a == 2:
    print(f"{player_1} chose Siccors!")
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

d = (5 + a - b) % 5

if d == 1 or d == 3:
    winner = player_1
    print(f"{winner} Wins!")

if d == 2 or d == 4:
    winner = player_2
    print(f"{winner} Wins!")

if d == 0:
    print("Its a Tie!")
