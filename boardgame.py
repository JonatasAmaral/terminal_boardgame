# definitions
cols = 5
lines = 5
cell = '🔳' # ⬛
cell_white = '🔲'

# print out the board
for l in range(lines):
	for c in range(cols):
		even = (l*lines+c)%2
		odd = 1-even
		print(
			cell * even +
			cell_white * odd
		, end=" ")
	print()
