def rotate_left(row, k):
    k %= len(row)
    return row[k:] + row[:k]

def rotate_right(row, k):
    k %= len(row)
    return row[-k:] + row[:-k]

def solve_problem1():
    with open("inputs/problem1_input.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    grid = []
    directions = []

    # Format assumption:
    # GRID ROWS FIRST
    # Then a blank line
    # Then directions like: L2, R1, L3 ...
    parse_dirs = False
    for line in lines:
        if line == "":
            parse_dirs = True
            continue

        if not parse_dirs:
            grid.append(list(line))  # characters
        else:
            directions = line.split()  # e.g. ["L2", "R1", "L3"]

    # Rotate each row
    for i, d in enumerate(directions):
        direction = d[0]       # 'L' or 'R'
        amount = int(d[1:])    # number after it
        if direction == 'L':
            grid[i] = rotate_left(grid[i], amount)
        else:
            grid[i] = rotate_right(grid[i], amount)

    # Take the middle row
    mid_row = grid[len(grid)//2]

    # ASCII sum
    ascii_sum = sum(ord(ch) for ch in mid_row)

    # Print or return
    print(ascii_sum)
    return ascii_sum

if __name__ == "_main_":
    solve_problem1()