def calculate_total_distance(file_path):
    with open(file_path, 'r') as file:
        # Read the two lists from the file
        left_list = []
        right_list = []
        for line in file:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)
    
    # Sort both lists
    left_list.sort()
    right_list.sort()
    
    # Calculate total distance
    total_distance = sum(abs(a - b) for a, b in zip(left_list, right_list))
    
    # Print the result
    print("Total Distance:", total_distance)

# Example usage:
# Replace 'input.txt' with the path to your file
file_path = input("Enter the path to the input file: ")
calculate_total_distance(file_path)
