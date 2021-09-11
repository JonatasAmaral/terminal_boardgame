# definitions
cols = 5
lines = 5
cell = "🔳" # ⬛

character_image = "😀"
character_position = [2,4] # [x,y]

# print out the board
for l in range(lines):
	for c in range(cols):
		# place a character in the board
		if l==character_position[1] and c==character_position[0]:
			print( character_image , end=" ")
		else: print( cell, end=" ")
	print()
