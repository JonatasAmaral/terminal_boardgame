# definitions
cols = 5
lines = 5
cell = '🔳' # ⬛
cell_white = '🔲'

# print out the board
for l in range(lines):
	if l%2:
		for c in range(cols):
			if c%2: print(cell, end=" ")
			else: print(cell_white, end=" ")
	else:
		for c in range(cols):
			if c%2: print(cell_white, end=" ")
			else: print(cell, end=" ")
	print()
