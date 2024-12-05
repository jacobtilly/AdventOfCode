# Read and process input data
with open("2024/day2/input.txt") as file:
    puzzle_data = [line.split(" ") for line in file.read().strip().split("\n")]

def is_safe(report):
    # Check if levels are either all increasing or all decreasing
    differences = [int(report[i + 1]) - int(report[i]) for i in range(len(report) - 1)]
    all_increasing = all(1 <= diff <= 3 for diff in differences)
    all_decreasing = all(-3 <= diff <= -1 for diff in differences)
    
    # A report is safe if it's either all increasing or all decreasing
    return all_increasing or all_decreasing

def is_safe_with_dampener(report):
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]  # Remove the i-th level
        if is_safe(modified_report):
            return True
    return False

# Check each report for safety
safe_reports = sum(1 for report in puzzle_data if is_safe(report))

dampened_safe_reports = 0
for report in puzzle_data:
    if is_safe(report) or is_safe_with_dampener(report):
        dampened_safe_reports += 1

print(f"Number of safe reports: {safe_reports}")
print(f"Number of safe reports with Problem Dampener: {dampened_safe_reports}")