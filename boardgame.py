# definitions
cols = 5
lines = 5
cell = "🔳"  # ⬛

char = {
	"image": "😀",
	"pos": [2,4]  # [x,y]
}

# print out the board
for l in range(lines):
    for c in range(cols):
        # place a character in the board
        if [c,l] == char["pos"]:
            print(char["image"], end=" ")
        else:
            print(cell, end=" ")
    print()
