# Day 4 - Puzzle Name

## Part One: List Comparisons - [Original Puzzle](https://adventofcode.com/2023/day/4)

You find a pile of scratchcards. Each scratchcard has two lists of numbers: a list of winning numbers and a list of your numbers. The goal is to count the points, where the first match earns 1 point, and subsequent matches double the point value. 

__Example:__

```
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
```

> __Card 1__ has five winning numbers - 41, 48, 83, 86, and 17  
and the eight numbers you have - 83, 86, 6, 31, 17, 9, 48, and 53.  
Four of your numbers, 48, 83, 17, and 86 are winning numbers!  

> `-` That means __Card 1__ is worth 8 points (1 for the first match, then doubled three times for each of the three matches after the first).  
`-` __Card 2__ - two winning numbers (32 and 61), worth 2 points.  
`-` __Card 3__ - two winning numbers (1 and 21), worth 2 points.  
`-` __Card 4__ - one winning number (84), worth 1 point.  
`-` __Card 5__ - no winning numbers, worth no points.  
`-` __Card 6__ - no winning numbers, worth no points.  

> This pile of scratchcards is worth 13 points.

Look at the larger pile of scratchcards. How many points are they worth in total?

__[My Solution](https://github.com/codehath/advent-of-code-2023/blob/main/day-4/advent_day_4.1.py)__ - [Input Data](https://github.com/codehath/advent-of-code-2023/blob/main/day-4/input/input_day_04.txt)

## Part Two: Recursive Functions - [Original Puzzle](https://adventofcode.com/2023/day/4)

Upon realizing that the rules are printed on the back of each card, you discover there are no such thing as points! Instead, winning scratchcards grants you more scratchcards equal to the number of winning numbers you have.  
Specifically, you win copies of the scratchcards below the winning card equal to the number of matches.  
So, if card 10 were to have 5 matching numbers, you would win one copy each of cards 11, 12, 13, 14, and 15.
The process repeats until no more scratchcards are won.

__Example:__

```
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
```
> __Card 1__ has four matches, so you win one copy each of the next four cards: __Cards 2, 3, 4, and 5__.  
Your original __Card 2__ has two matching numbers, so you win one copy each of __Cards 3 and 4__.  
Your copy of __Card 2__ also wins _one_ copy each of __Cards 3 and 4__.  
Your four instances of __Card 3__ (one original and three copies) have two matching numbers, so you win four copies each of __Cards 4 and 5__.  
Your eight instances of __Card 4__ (one original and seven copies) have one matching number, so you win eight copies of __Card 5__.  
Your fourteen instances of __Card 5__ (one original and thirteen copies) have no matching numbers and win no more cards.  
Your one instance of __Card 6__ (one original) has no matching numbers and wins no more cards.  

> Once all of the originals and copies have been processed, you end up with:  
`-` 1 instance of __Card 1__  
`-` 2 instances of __Card 2__  
`-` 4 instances of __Card 3__  
`-` 8 instances of __Card 4__  
`-` 14 instances of __Card 5__ and  
`-` 1 instance of __Card 6__  
 

> In total, this example pile of scratchcards causes you to ultimately have 30 scratchcards! 

Process all of the original and copied scratchcards until no more scratchcards are won. How many total scratchcards do you end up with?

__[My Solution](https://github.com/codehath/advent-of-code-2023/blob/main/day-4/advent_day_4.2.py)__ - [Input Data](https://github.com/codehath/advent-of-code-2023/blob/main/day-4/input/input_day_04.txt)

---
[< Back to all solutions](https://github.com/codehath/advent-of-code-2023/tree/main)