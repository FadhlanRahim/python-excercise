number_grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [0]
]

#print specific element in the number grid
print(number_grid[1][1])

#print whole row in number grid
for row in number_grid:
    print(row)

#print each number in number grid
for row in number_grid:
    for col in row:
        print(col)
