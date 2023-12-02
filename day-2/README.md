# Day 2 - Cube Conundrum

## Part One: Possible Configurations - [Original Puzzle](https://adventofcode.com/2023/day/1)
In this puzzle, you're presented with information about the cubes in a bag based on several games played. Each game has multiple rounds, the cubes are replaced after each round. Your task is to determine which games would have been possible if the bag contained only 12 red, 13 green, and 14 blue cubes.

__Example:__

```
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green  
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue  
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red  
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red  
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green  
```

> In Game 1, three rounds of cubes are revealed:  
`-` Round 1 - 3 blue and 4 red cubes are picked;  
`-` Round 2 - 1 red, 2 green, and 6 blue cubes;  
`-` Round 3 - only 2 green cubes.

> Games 1, 2, and 5 - would have been possible  
Game 3 - would have been impossible because one round had 20 red cubes  
Game 4 - impossible because a round had 15 blue cubes

>If you add up the IDs of the games that would have been possible, you get 8.

Determine which games would have been possible. What is the sum of the IDs of those games?

__[My Solution](https://github.com/codehath/advent-of-code-2023/blob/main/day-2/advent_day_2.1.py)__

```
import re
from input_data import input_day_02 as file

split_characters = ' ,;:'
max_cube_qtys = {"red" : 12, "green" : 13, "blue" : 14}
valid_game_total = 0

# Each line is a game, iterate through them
for line in file:
    cubes = {}
    
    # Split line into parts and remove first 2 elements(Game Number)
    data = re.split(f'[{re.escape(split_characters)}]+', line)
    data.pop(0)
    game_no = int(data.pop(0))

    # Increment by 2 as every other item in list is a number of cubes corresponding to the...
    # ...next item, a colour string ("red", "green" or "blue")
    for x in range(0,len(data),2):
        number = int(data[x])
        colour = data[x+1].rstrip()
        
        # Set the colour as key and highest number of cubes picked for that colour in the game as value
        cubes.setdefault(colour, number)
        if number > cubes[colour]:
            cubes[colour] = number
    
    # If none of this game's cube quantities exceed the max cube quantities for their respective colour, it's a valid game
    if not any(cubes[key] > max_cube_qtys[key] for key in cubes):
        valid_game_total += game_no

print("Sum of Valid Game IDs:", valid_game_total)
```

## Part Two: Minimum Cube Sets - [Original Puzzle](https://adventofcode.com/2023/day/2)

Find the minimum number of cubes of each color needed to make each game possible. The power of a set of cubes is the product of the number of red, green, and blue cubes. 

__Example:__

```
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green  
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue  
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red  
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red  
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green  
```

> Game 1 - could have been played with as few as 4 red, 2 green, and 6 blue cubes. any fewer and the game would have been impossible.  
Game 2 - minimum of 1 red, 3 green, and 4 blue cubes.  
Game 3 - at least 20 red, 13 green, and 6 blue cubes.  
Game 4 - required at least 14 red, 3 green, and 15 blue cubes.  
Game 5 - needed 6 red, 3 green, and 2 blue cubes in the bag.

> The power of the minimum set of cubes in game 1 is 48.  
In games 2-5; 12, 1560, 630, and 36, respectively.  
The sum is 2286.

For each game, find the minimum set of cubes that must have been present. Calculate the sum of the powers of these sets.

__[My Solution](https://github.com/codehath/advent-of-code-2023/blob/main/day-2/advent_day_2.2.py)__

```
import re, math
from input_data import input_day_02 as file

split_characters = ' ,;:'
max_cube_qtys = {"red" : 12, "green" : 13, "blue" : 14}
powers_total = 0

for line in file:
    cubes = {}
    
    # Split line into parts and remove first 2 elements(Game Number)
    data = re.split(f'[{re.escape(split_characters)}]+', line)
    data.pop(0)
    game_no = int(data.pop(0))
    
    # Increment by 2 as every other item in list is a number of cubes corresponding to the...
    # ...next item, a colour string ("red", "green" or "blue")
    for x in range(0, len(data), 2):
        number = int(data[x])
        colour = data[x+1].rstrip()
        
        # Set the colour as key and highest number of cubes picked for that colour in the game as value
        cubes.setdefault(colour, number)
        if number > cubes[colour]:
            cubes[colour] = number
    
    powers_total += math.prod(cubes.values())

print("Sum of Powers:", powers_total)
```

---
[< Back to all solutions](https://github.com/codehath/advent-of-code-2023/tree/main)