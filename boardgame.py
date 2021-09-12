from sys import stdout
from time import sleep

# definitions
cols = 5
lines = 5
cell = "🔳"  # ⬛

char = {
	"image": "😀",
	"pos": [2,4]  # [x,y]
}
obstacle = {
	"image": "🎸",
	"pos": [2,3]  # [x,y]
}

# game loop
while True:

    # print out the board
    for l in range(lines):
        for c in range(cols):
            # place a character in the board
            if [c,l] == char["pos"]:
                print(char["image"], end=" ")
            elif [c,l] == obstacle["pos"]:
                print(obstacle["image"], end=" ")
            else:
                print(cell, end=" ")
        print()
    
    
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



    # update the screen, "returning carriage" before the last printed board
    for l in range(lines+3):
        stdout.write("\033[F") # go to prev line start
        stdout.write("\033[K") # clear line
