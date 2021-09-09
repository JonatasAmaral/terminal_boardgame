# definitions
cols = 5
lines = 5
cell = "🔳" # ⬛

# print out the board
for l in range(lines):
	for c in range(cols):
		# place a character in the board
		if l == 4 and c == 2: print( "😀", end=" ")
		else: print( cell, end=" ")
	print()
