# definitions
cols = 5
lines = 5
cell = '🔳' # ⬛

# print out the board
for l in range(-1,lines):
	# if on line of columns' labels
	if l == -1:
		for c in range(-1, cols):
			# if on column of lines' labels
			if c == -1:
				# print empty space
				print('  ', end=" ")
			else:
				# print columns number
				print(c, end="  ")

	else:
		for c in range(-1, cols):
			# if on column of lines' labels
			if c == -1:
				# print line number
				print(l, end=" ")
			else:
				# print cell
				print( cell, end=" ")

	print()
