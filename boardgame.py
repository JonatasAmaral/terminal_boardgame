# definitions
cols = 5
lines = 5
cell = '🔳' # ⬛

# print out the board
for l in range(-1,lines):
	print( "%2i"%l if (l>=0) else '  ', end=" ")
	for c in range(cols):
		if (l==-1): print("%2i"%c, end=' ')
		else: print( cell, end=" ")
	print()
