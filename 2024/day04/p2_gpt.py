def count_x_mas_occurrences(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    # Helper function to check for a MAS (or SAM) in a specific direction
    def check_mas(x, y, dx, dy):
        pattern = "MAS"
        for i, char in enumerate(pattern):
            nx, ny = x + i * dx, y + i * dy
            if nx < 0 or nx >= rows or ny < 0 or ny >= cols or grid[nx][ny] != char:
                return False
        return True

    # Iterate through each possible center of the X-MAS
    for x in range(1, rows - 1):
        for y in range(1, cols - 1):
            # Check for two MAS patterns in the shape of an X
            top_left = check_mas(x - 1, y - 1, 1, 1)  # Diagonal top-left to center
            bottom_left = check_mas(x + 1, y - 1, -1, 1)  # Diagonal bottom-left to center
            top_right = check_mas(x - 1, y + 1, 1, -1)  # Diagonal top-right to center
            bottom_right = check_mas(x + 1, y + 1, -1, -1)  # Diagonal bottom-right to center

            # NOTE: below is the original line GPT generated, which is wrong.
            # https://chatgpt.com/share/674fffac-94ec-8007-9392-bc80067924aa
            # This is manually fixed by me.
            # AI is not as good as a seasoned programmer yet :)
            # But the generated code is already very impressive.
            # I think AI may generate correct solution if I provide better prompts.
            #
            # if (top_left and bottom_right) or (bottom_left and top_right):
            if (top_left or bottom_right) and (bottom_left or top_right):
                count += 1

    return count


def main():
    # Read the input grid from a file
    input_file = "input.txt"  # Replace with your input file name
    with open(input_file, 'r') as file:
        grid = [line.strip() for line in file.readlines()]

    occurrences = count_x_mas_occurrences(grid)
    print(f"The X-MAS pattern appears {occurrences} times in the grid.")


if __name__ == "__main__":
    main()
