from collections import Counter

# Read and process input data
with open("2024/day1/input.txt") as file:
    puzzle_data = [line.split("   ") for line in file.read().strip().split("\n")]

# Separate the two lists
list1, list2 = zip(*puzzle_data)

# Convert to integers
list1 = list(map(int, list1))
list2 = list(map(int, list2))

# Sort the lists
list1.sort()
list2.sort()

# Part 1: Calculate the sum of differences
sum_of_differences = sum(abs(b - a) for a, b in zip(list1, list2))
print(f"Sum of differences: {sum_of_differences}")

# Part 2: Calculate the similarity score
list2_count = Counter(list2)
similarity_score = sum(num * list2_count[num] for num in list1)
print(f"Similarity score: {similarity_score}")