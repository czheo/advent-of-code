def is_safe(report):
    """Check if a report is safe based on the given rules."""
    # Check if all adjacent differences are between 1 and 3
    for i in range(len(report) - 1):
        diff = abs(report[i] - report[i + 1])
        if diff < 1 or diff > 3:
            return False

    # Check if the report is strictly increasing or strictly decreasing
    is_increasing = all(report[i] < report[i + 1] for i in range(len(report) - 1))
    is_decreasing = all(report[i] > report[i + 1] for i in range(len(report) - 1))
    
    return is_increasing or is_decreasing

def can_be_safe_with_dampener(report):
    """Check if a report can be made safe by removing a single level."""
    for i in range(len(report)):
        # Create a new report excluding the current level
        modified_report = report[:i] + report[i + 1:]
        if is_safe(modified_report):
            return True
    return False

def count_safe_reports_with_dampener(file_path):
    """Count the number of safe reports with the Problem Dampener."""
    safe_count = 0
    
    with open(file_path, 'r') as file:
        for line in file:
            report = list(map(int, line.split()))
            if is_safe(report) or can_be_safe_with_dampener(report):
                safe_count += 1
    
    return safe_count

if __name__ == "__main__":
    # Input file containing reports
    input_file = "input.txt"
    
    # Count safe reports with the Problem Dampener
    safe_reports_count = count_safe_reports_with_dampener(input_file)
    
    # Output the result
    print("Number of safe reports with dampener:", safe_reports_count)
