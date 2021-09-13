from sys import stdout
from random import choice, randrange
from time import sleep

# definitions
cols = 5
lines = 5
cell = "🔳"  # ⬛

char = {
	"images": {
        "normal": "😀",
        "dead": "💀"
    },
    "status": "normal",
	"pos": [2,4]  # [x,y]
}
obstacle = {
	"image": "🎸",
	"pos": [2,3]  # [x,y]
}
food = {
	"image": choice("🍕🍖🌭🍦🍰"),
	"pos": [randrange(0,cols), randrange(0,lines//2)]  # [x,y]
}
enemy = {
    "image": '👻',
    "pos": [randrange(0,cols),randrange(0,lines)]
}

# game loop
while True:

    # print out the board
    for l in range(lines):
        for c in range(cols):
            # place a character in the board
            if [c,l] == char["pos"]:

                print(
                    char["images"][
                        char["status"]
                    ]
                , end=" ")
            elif [c,l] == enemy["pos"]:
                print(enemy["image"], end=" ")
            elif [c,l] == food["pos"]:
                print(food["image"], end=" ")
            elif [c,l] == obstacle["pos"]:
                print(obstacle["image"], end=" ")
            else:
                print(cell, end=" ")
        print()
    
    # if user gets to the enemy, dies
    if char["status"] == "dead":
        print("I think you may have died!")
        sleep(1) # pauses 2 secs
        break
    # if user won, close game loop
    if char["pos"] == food["pos"]:
        print("You got it!!")
        sleep(1) # pauses 2 secs
        break
    
    # asks and waits user to move
    move = input("where to go?\n(a=←, w=↑, d=→, s=↓)\n")
    new_pos = char["pos"].copy()

    if move == "a" and char["pos"][0]>0: new_pos[0] -= 1
    elif move == "d" and char["pos"][0]<cols-1: new_pos[0] += 1
    elif move == "w" and char["pos"][1]>0: new_pos[1] -= 1
    elif move == "s" and char["pos"][1]<lines-1: new_pos[1] += 1
    else:
        print("Wrong direction")
        sleep(2) # pauses 2 secs
        stdout.write("\033[F\033[K") # clear warning
    
    if new_pos == obstacle["pos"]:
        print("Can't go over this")
        sleep(2) # pauses 2 secs
        stdout.write("\033[F\033[K") # clear warning
    else:
        char["pos"] = new_pos
        del new_pos

    # if got to the food, makes a "yummy" face
    if char["pos"] == enemy["pos"]: char["status"] = "dead"

    # update the screen, "returning carriage" before the last printed board
    for l in range(lines+3):
        stdout.write("\033[F") # go to prev line start
        stdout.write("\033[K") # clear line
