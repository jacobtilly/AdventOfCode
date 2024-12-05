from aocd import get_data
import pandas as pd

# Jacob Tilly, dec 2022

puzzleData = get_data(year=2022, day=5)
puzzleData = """
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""

stacks, instructions = puzzleData.split("\n\n")[0], puzzleData.split("\n\n")[1]

def create_stacks(tabular_stacks):
    # Initialize the stacks as an empty list
    stacks = []

    # Iterate over the lines of the tabular representation
    for line in tabular_stacks:
        # Split the line into a list of crates
        crates = line.split()

        # Reverse the order of the crates so that the top crate is at the end
        crates = list(reversed(crates))

        # Add the crates to the stacks
        stacks.append(crates)

    # Return the stacks
    return stacks

# Test the function with the stacks from the previous examples
tabular_stacks = [
    '[D]',
    '[N] [C]',
    '[Z] [M] [P]'
]
stacks = create_stacks(tabular_stacks)
print(stacks)