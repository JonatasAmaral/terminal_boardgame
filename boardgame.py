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

    if move == "a": char["pos"][0] -= 1
    elif move == "d": char["pos"][0] += 1
    elif move == "w": char["pos"][1] += 1
    elif move == "s": char["pos"][1] -= 1
    else: print("Wrong direction")


    # fake _update_ the screen, hiding previous board prints
    print("\n"*10)
