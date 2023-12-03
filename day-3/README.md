# Day 3 - Gear Ratios

## Part One: Visual Grid Manipulation - [Original Puzzle](https://adventofcode.com/2023/day/3)

An engineer asks for your help in figuring out which engine part is missing. The engine schematics are represented visually. Numbers adjacent diagonally or horizontally to symbols (except periods ( . ) ) are considered part numbers.

__Example:__

```
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
```

> In this schematic, two numbers are not part numbers because they are not adjacent to a symbol:  
`-` 114 (top right) and  
`-` 58 (middle right)  
Every other number is adjacent to a symbol and so is a part number.

> The sum of all the part numbers is 4361.

Your task is to sum all the part numbers in the engine schematic.

__[My Solution](https://github.com/codehath/advent-of-code-2023/blob/main/day-3/advent_day_3.1.py)__ - [Input Data](https://github.com/codehath/advent-of-code-2023/blob/main/day-3/input/input_day_03.txt)

## Part Two: Valid Gear Identification - [Original Puzzle](https://adventofcode.com/2023/day/3)

After finding the missing part, you discover that one of the gears in the engine is wrong. Gears are identified as * symbols adjacent to exactly two part numbers. The gear ratio is the result of multiplying these two numbers together. Your goal is to find the gear ratio of every gear and sum them up.

__Example:__

```
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
```

> In this schematic, there are two gears:  
`-` The first is in the top left; it has part numbers 467 and 35, so its gear ratio is 16345.  
`-` The second gear is in the lower right; its gear ratio is 451490.  
`-` (The * adjacent to 617 is not a gear because it is only adjacent to one part number.) 

> Adding up all of the gear ratios produces 467835.

What is the sum of all of the gear ratios in the engine schematic?

__[My Solution](https://github.com/codehath/advent-of-code-2023/blob/main/day-3/advent_day_3.2.py)__ - [Input Data](https://github.com/codehath/advent-of-code-2023/blob/main/day-3/input/input_day_03.txt)

---
[< Back to all solutions](https://github.com/codehath/advent-of-code-2023/tree/main)