# definitions
cols = 5
lines = 5
cell = '🔳' # ⬛

# print out the board
for l in range(lines):
	for c in range(cols):
		print( cell, end=" ")
	print()
