# Day 2 - Cube Conundrum

## Part One: Possible Games - [Original Puzzle](https://adventofcode.com/2023/day/1)
In this puzzle, you're presented with information about the cubes in a bag based on several games played. Each game has multiple rounds, the cubes are replaced after each round. A game is considered possible if it can be played with only the cubes contained in the bag, 12 red, 13 green, and 14 blue cubes. Otherwise, the game is impossible.

__Example:__

```
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green  
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue  
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red  
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red  
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green  
```

> In __Game 1__, three rounds of cubes are revealed:  
`-` Round One - 3 blue and  4 red cubes  
`-` Round Two - 1 red, 2 green, 6 blue cubes  
`-` Round Three - 2 green cubes

> __Games 1, 2, and 5__ - would have been possible  
__Game 3__ - would have been impossible because one round had 20 red cubes  
__Game 4__ - impossible because a round had 15 blue cubes

>If you add up the IDs of the games that would have been possible, you get 8.

Your task is to determine which games would have been possible. What is the sum of the IDs of those games?

__[My Solution](https://github.com/codehath/advent-of-code-2023/blob/main/day-2/advent_day_2.1.py)__ - [Input Data](https://github.com/codehath/advent-of-code-2023/blob/main/day-2/input/input_day_02.txt)

## Part Two: Minimum Cube Sets - [Original Puzzle](https://adventofcode.com/2023/day/2)

The minimum set of cubes is the fewest number of cubes of each color that could have been in the bag to make the game possible. The power of a set of cubes is the product of the number of red, green, and blue cubes. 

__Example:__

```
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green  
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue  
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red  
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red  
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green  
```

> __Game 1__ - could have been played with as few as 4 red, 2 green, and 6 blue cubes. any fewer and the game would have been impossible.  
__Game 2__ - minimum of 1 red, 3 green, and 4 blue cubes.  
__Game 3__ - at least 20 red, 13 green, and 6 blue cubes.  
__Game 4__ - required at least 14 red, 3 green, and 15 blue cubes.  
__Game 5__ - needed 6 red, 3 green, and 2 blue cubes in the bag.

> The power of the minimum set of cubes in __Game 1__ is 48.  
In __Games 2-5__; 12, 1560, 630, and 36, respectively.  The sum is 2286.

For each game, find the minimum set of cubes that must have been present. Calculate the sum of the powers of these sets.

__[My Solution](https://github.com/codehath/advent-of-code-2023/blob/main/day-2/advent_day_2.2.py)__ - [Input Data](https://github.com/codehath/advent-of-code-2023/blob/main/day-2/input/input_day_02.txt)

---
[< Back to all solutions](https://github.com/codehath/advent-of-code-2023/tree/main)