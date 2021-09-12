from pynput import keyboard
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
    with keyboard.Events() as events:
        event = events.get(1e6)
        move = event.key
        sleep(.2)


    if move == keyboard.KeyCode.from_char("a") and char["pos"][0]>0:
        char["pos"][0] -= 1
    elif move == keyboard.KeyCode.from_char("d") and char["pos"][0]<cols-1:
        char["pos"][0] += 1
    elif move == keyboard.KeyCode.from_char("w") and char["pos"][1]>0:
        char["pos"][1] -= 1
    elif move == keyboard.KeyCode.from_char("s") and char["pos"][1]<lines-1:
        char["pos"][1] += 1
    else:
        print("Wrong direction")
        sleep(2) # pauses 2 secs
        stdout.write("\033[F\033[K") # clear warning


    # update the screen, "returning carriage" before the last printed board
    for l in range(lines+3):
        stdout.write("\033[F") # go to prev line start
        stdout.write("\033[K") # clear line
