from collections import Counter

def calculate_similarity_score(file_path):
    with open(file_path, 'r') as file:
        # Read the two lists from the file
        left_list = []
        right_list = []
        for line in file:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)
    
    # Count the occurrences of each number in the right list
    right_count = Counter(right_list)
    
    # Calculate the similarity score
    similarity_score = sum(num * right_count[num] for num in left_list)
    
    # Print the result
    print("Similarity Score:", similarity_score)

# Example usage:
# Replace 'input.txt' with the path to your file
file_path = input("Enter the path to the input file: ")
calculate_similarity_score(file_path)
