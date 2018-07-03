def solve_minesweeper(puzzle_array):
    score = [[0] * (len(puzzle_array[0]) + 2) for i in range(len(puzzle_array) + 2)]
    result = []
    mines = []
    unique_corners = set()
    unique_row = set()
    for i in range(len(puzzle_array)):
        for j in range(len(puzzle_array[0])):
            if puzzle_array[i][j] == 'm':
                mines.append(tuple([i,j]))

    for point in mines:
        i, j = point
        # store unique corners
        unique_corners.add(tuple([i,j]))
        unique_corners.add(tuple([i, j+2]))
        unique_corners.add(tuple([i+2, j]))
        unique_corners.add(tuple([i+2, j+2]))

        # Rule 1
        score[i][j] += 1
        score[i][j+1] += 1
        score[i][j+2] += 1
        score[i+1][j] += 1
        score[i+1][j+2] += 1
        score[i+2][j] += 1
        score[i+2][j+1] += 1
        score[i+2][j+2] += 1

    for point in mines:
        i, j = point
        # Rule 2
        score[i + 2][j + 1] = 2

    for point in mines:
        i, j = point
        # Rule 3
        score[i + 1][j + 2] = 0

    for point in mines:
        i, j = point
        # Rule 4
        if i % 2 != 0 and i not in unique_row:
            unique_row.add(i)
            for pos in range(len(score[i+1])):
                score[i+1][pos] *= 3

    # Rule 5
    for point in unique_corners:
        i, j = point
        score[i][j] *= 2

    # Rule 6
    for point in mines:
        i, j = point
        score[i + 1][j + 1] = -1

    for row in score[1:-1]:
        result.append(row[1:-1])

    return result


puzzle = [ ['.','m','.','.'],['.','.','m','.'] ]
x = solve_minesweeper(puzzle)
print(x)
