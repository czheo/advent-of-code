import re

def sum_valid_conditional_mul_instructions(filename):
    # Read the content of the file
    with open(filename, 'r') as file:
        data = file.read()

    # Regular expressions for instructions
    mul_pattern = r'mul\(\s*(\d+)\s*,\s*(\d+)\s*\)'
    do_pattern = r'do\(\s*\)'
    dont_pattern = r"don't\(\s*\)"

    # Track whether mul instructions are enabled
    mul_enabled = True
    result_sum = 0

    # Find all instructions in the order they appear
    instructions = re.finditer(f'{mul_pattern}|{do_pattern}|{dont_pattern}', data)

    for match in instructions:
        if match.group().startswith('mul('):
            if mul_enabled:
                # Extract numbers from the mul instruction
                x, y = map(int, match.groups()[:2])
                result_sum += x * y
        elif match.group().startswith('do('):
            mul_enabled = True
        elif match.group().startswith("don't("):
            mul_enabled = False

    print(f"The sum of all valid enabled mul results is: {result_sum}")

# Example usage
# Replace 'input.txt' with the path to your actual input file
sum_valid_conditional_mul_instructions('input.txt')

