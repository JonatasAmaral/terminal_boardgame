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
        "dead": "💀",
        "won": "😋",
        "vomit": "🤮",
    },
    "status": "normal",
	"pos": [cols//2,lines-1]  # [x,y]
}
obstacle = {
	"image": choice("🛹🪑🧳⚽🏀🏈💻🎸📺📚📦"),
	"pos": [cols//2,lines-2]  # [x,y]
}
food = {
	"image": choice("🍕🍖🌭🍦🍰"),
	"pos": [randrange(0,cols), randrange(0,lines//2)]  # [x,y]
}
poop = {
	"image": "💩",
	"pos": [randrange(0,cols),randrange(0,lines)]  # random [x,y]
}
enemy = {
    "image": '👻',
    "pos": [randrange(0,cols),randrange(0,lines)]
}

first_iteration = True
# game loop
while True:

    if not first_iteration:
        # update the screen, "returning carriage" before the last printed board
        for l in range(lines+3):
            stdout.write("\033[F") # go to prev line start
            stdout.write("\033[K") # clear line
    else: first_iteration = False

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
            elif [c,l] == poop["pos"]:
                print(poop["image"], end=" ")
            elif [c,l] == food["pos"]:
                print(food["image"], end=" ")
            elif [c,l] == obstacle["pos"]:
                print(obstacle["image"], end=" ")
            else:
                print(cell, end=" ")
        print()
    
    ## check and perform game terminating actions
    # if user gets to the enemy, dies
    if char["status"] == "dead":
        print("I think you may have died!")
        sleep(1) # pauses 2 secs
        break
    # if user steps on poop, trows up
    if char["status"] == "vomit":
        print("ohh... lost my appetite")
        sleep(1) # pauses 2 secs
        break
    # if user won, close game loop
    if char["status"] == "won":
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
        continue # jumps the iteration, so world keeps paused

    # moves the enemy
    enemy_move = choice("wasd")
    if enemy_move == "a" and enemy["pos"][0]>0: enemy["pos"][0] -= 1
    elif enemy_move == "d" and enemy["pos"][0]<cols-1: enemy["pos"][0] += 1
    elif enemy_move == "w" and enemy["pos"][1]>0: enemy["pos"][1] -= 1
    elif enemy_move == "s" and enemy["pos"][1]<lines-1: enemy["pos"][1] += 1
    
    if new_pos == obstacle["pos"]:
        print("Can't go over this")
        sleep(.5) # pauses 2 secs
        stdout.write("\033[F\033[K") # clear warning
    else:
        char["pos"] = new_pos
        del new_pos

    # updates character's status
    if char["pos"] == enemy["pos"]: char["status"] = "dead"
    elif char["pos"] == poop["pos"]: char["status"] = "vomit"
    elif char["pos"] == food["pos"]: char["status"] = "won"
