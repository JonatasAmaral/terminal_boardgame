# definitions
cols = 5
lines = 5
cell = "🔳" # ⬛

character_image = "😀"
character_position_col = 2
character_position_line = 4

# print out the board
for l in range(lines):
	for c in range(cols):
		# place a character in the board
		if l == character_position_line and c==character_position_col:
			print( character_image , end=" ")
		else: print( cell, end=" ")
	print()
