#!/usr/bin/python3
'''0x09. Island Perimeter'''

def island_perimeter(grid):
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:  # Land cell
                # Check each side of the cell
                if r == 0 or grid[r - 1][c] == 0:  # Top
                    perimeter += 1
                if r == rows - 1 or grid[r + 1][c] == 0:  # Bottom
                    perimeter += 1
                if c == 0 or grid[r][c - 1] == 0:  # Left
                    perimeter += 1
                if c == cols - 1 or grid[r][c + 1] == 0:  # Right
                    perimeter += 1
    return perimeter
