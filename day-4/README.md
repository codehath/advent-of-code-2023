# Day 4 - Puzzle Name

## Part One: List Comparisons - [Original Puzzle](https://adventofcode.com/2023/day/4)

You find yourself surrounded by colorful scratchcards and an Elf seeking assistance. Each scratchcard has two lists of numbers: a list of winning numbers and a list of your numbers. The goal is to count the points, where the first match earns 1 point, and subsequent matches double the point value. 

__Example:__

```
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
```

> __Card 1__ has five winning numbers (41, 48, 83, 86, and 17)  
and the eight numbers you have (83, 86, 6, 31, 17, 9, 48, and 53).  
Four of your numbers, 48, 83, 17, and 86 are winning numbers!  
`-` That means __Card 1__ is worth 8 points (1 for the first match, then doubled three times for each of the three matches after the first).

> `-` That means __Card 1__ is worth 8 points (1 for the first match, then doubled three times for each of the three matches after the first).
__Card 2__ has two winning numbers (32 and 61), so it is worth 2 points.  
__Card 3__ has two winning numbers (1 and 21), so it is worth 2 points.  
__Card 4__ has one winning number (84), so it is worth 1 point.  
__Card 5__ has no winning numbers, so it is worth no points.  
__Card 6__ has no winning numbers, so it is worth no points.  

> So, in this example, the Elf's pile of scratchcards is worth 13 points.

How many points are they worth in total?

__[My Solution](https://github.com/codehath/advent-of-code-2023/blob/main/day-4/advent_day_4.1.py)__ - [Input Data](https://github.com/codehath/advent-of-code-2023/blob/main/day-4/input/input_day_04.txt)

## Part Two: Recursive Functions - [Original Puzzle](https://adventofcode.com/2023/day/4)

Upon realizing that the rules are printed on the back of each card, you discover that winning scratchcards grants you additional copies equal to the number of matching numbers. The process repeats until no more scratchcards are won.

__Example:__

```
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
```
> Once all of the originals and copies have been processed, you end up with:  
1 instance of __Card 1__  
2 instances of __Card 2__  
4 instances of __Card 3__  
8 instances of __Card 4__  
14 instances of __Card 5__ and  
1 instance of __Card 6__  
 

> In total, this example pile of scratchcards causes you to ultimately have 30 scratchcards! 

Process all of the original and copied scratchcards until no more scratchcards are won. Including the original set of scratchcards, how many total scratchcards do you end up with?

__[My Solution](https://github.com/codehath/advent-of-code-2023/blob/main/day-4/advent_day_4.2.py)__ - [Input Data](https://github.com/codehath/advent-of-code-2023/blob/main/day-4/input/input_day_04.txt)

---
[< Back to all solutions](https://github.com/codehath/advent-of-code-2023/tree/main)