def mine_sweeper(bombs, rows, cols):
    field = [[0 for i in range(cols)] for i in range(rows)]
    for x, y in bombs:
        field[x][y] = -1
        row_range = range(x-1, x+2)
        col_range = range(y-1, y+2)

        for i in row_range:
            for j in col_range:
                if(0 <= i < rows and 0 <= j <= cols and field[i][j] != -1):
                    field[i][j] += 1

    return field


field = mine_sweeper([[1, 2], [0, 0]], 4, 4)
for row in field:
    print(row)
