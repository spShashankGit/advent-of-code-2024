"""
Input text is a text with following contstraints:
1. Input is a sinle character
2. Character could be an alphabet (lower or upper case) or a number.
3. The naming of antenna is case-sensitive.
4. In the example antinodes are represetned by # and 0.



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
2. Offline: ../../questions/advent-of-code-2024/day-8.md

"""


print('Advent of Code 2024 - Day 8')
