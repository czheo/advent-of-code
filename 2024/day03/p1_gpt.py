import re

def sum_valid_mul_instructions(filename):
    # Read the content of the file
    with open(filename, 'r') as file:
        data = file.read()

    # Regular expression to find valid mul(X,Y) instructions
    pattern = r'mul\(\s*(\d+)\s*,\s*(\d+)\s*\)'

    # Find all matches of the pattern
    matches = re.findall(pattern, data)

    # Compute the sum of the results of valid mul instructions
    result_sum = sum(int(x) * int(y) for x, y in matches)

    print(f"The sum of all valid mul results is: {result_sum}")

# Example usage
# Replace 'input.txt' with the path to your actual input file
sum_valid_mul_instructions('input.txt')
