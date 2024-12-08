"""
Input text is a text with following contstraints:
1. Input is a sinle character
2. Character could be an alphabet (lower or upper case) or a number.
3. The naming of antenna is case-sensitive.
4. In the example antinodes are represetned by # and 0.


Aim:
1. Find out how many unique antenna positions could be there.
1.1 To do we need to find out how many of the 

Concepts important for problem solving:
1. Antinodes: An antinote occurs at a point that is perfectly in line with the two antennas of the same frequeny
- but only when one of the antennas is twice as far away as the other. 
This means that for any pair of antennas with the same frequency, there are two antinodes, one on either side of them.
example: # a a # 

..........
...#......
..........
....a.....
..........
.....a....
..........
......#...
..........
..........

Reference:
1. Online:  https://adventofcode.com/2024/day/8
2. Offline: ../questions/advent-of-code-2024/day-8.md

"""
import os
print("Current Working Directory:", os.getcwd())
print('Advent of Code 2024 - Day 8')
filec = '../../inputs/advent-day-8/input-set-1.txt'

"""
# Defining the approach
1. Need to the node i.e. either a-z, A-Z or 0-9
2. Need to identify the poisition of the another node inside the inputs stiing
3. Idenfiy the distance between the two nodes
4. Identify the potential antinode position(s) based on the distance between the two nodes and also the positiong inside 
"""

with open(filec, 'r') as file:
    for line in file:
        print(line.strip())  # strip() removes leading/trailing whitespace
        #line.find()