def count_word_occurrences(grid, word):
    rows = len(grid)
    cols = len(grid[0])
    word_length = len(word)
    count = 0

    # Helper function to check a word in a specific direction
    def check_direction(x, y, dx, dy):
        for i in range(word_length):
            nx, ny = x + i * dx, y + i * dy
            if nx < 0 or nx >= rows or ny < 0 or ny >= cols or grid[nx][ny] != word[i]:
                return False
        return True

    # Iterate through each cell in the grid
    for x in range(rows):
        for y in range(cols):
            # Check all 8 directions
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1),  # vertical and horizontal
                          (-1, -1), (-1, 1), (1, -1), (1, 1)]  # diagonal
            for dx, dy in directions:
                if check_direction(x, y, dx, dy):
                    count += 1

    return count


def main():
    # Read the input grid from a file
    input_file = "input.txt"  # Replace with your input file name
    with open(input_file, 'r') as file:
        grid = [line.strip() for line in file.readlines()]

    word = "XMAS"
    occurrences = count_word_occurrences(grid, word)
    print(f"The word '{word}' appears {occurrences} times in the grid.")


if __name__ == "__main__":
    main()

