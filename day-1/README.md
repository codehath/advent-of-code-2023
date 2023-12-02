# Day 1 - Trebuchet?! - Deciphering Calibration Values

## Part One: Identifying Digits - [Original Puzzle](https://adventofcode.com/2023/day/1)
You're tasked with deciphering calibration values hidden within a modified document. The calibration values are derived by extracting the first and last digits from each line and summing them up.

__Example:__

> 1abc2  
> pqr3stu8vwx  
> a1b2c3d4e5f  
> treb7uchet  

> The calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?

__[My Solution](https://github.com/codehath/advent-of-code-2023/blob/main/day-1/advent_day_1.1.py)__ - [Input Data](https://github.com/codehath/advent-of-code-2023/blob/main/day-1/input/input_day_01.txt)
```
from input_data import input_day_01 as file

sum = 0
for line in file:
    # Store each digit in line
    nums = [char for char in line if char in "0123456789"]
    
    # Use first and last digit to work out calibration value
    calibration_value = int(nums[0] + nums[-1])
    sum += calibration_value

print("Sum of all Calibration Values:", sum)
```

## Part Two: Lettered Digits - [Original Puzzle](https://adventofcode.com/2023/day/1)
After realizing that some digits are spelled out, you're required to identify the real first and last digits on each line. 

__Example:__

> two1nine  
> eightwothree  
> abcone2threexyz  
> xtwone3four  
> 4nineeightseven2  
> zoneight234  
> 7pqrstsixteen  

> The calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values?

__[My Solution](https://github.com/codehath/advent-of-code-2023/blob/main/day-1/advent_day_1.2.py)__ - [Input Data](https://github.com/codehath/advent-of-code-2023/blob/main/day-1/input/input_day_01.txt)

---
[< Back to all solutions](https://github.com/codehath/advent-of-code-2023/tree/main)