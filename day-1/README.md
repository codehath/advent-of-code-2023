# [Day 1 -  Deciphering Calibration Values](https://adventofcode.com/2023/day/1)

##### [< Back to all solutions](https://github.com/codehath/advent-of-code-2023/tree/main)

---

### Part One: The Basics
You're tasked with deciphering calibration values hidden within a modified document. The calibration values are derived by extracting the first and last digits from each line and summing them up.

#### Example:
```
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
```
> The calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?

#### My Solution:
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

### Part Two: Lettered Digits
After realizing that some digits are spelled out, you're required to identify the real first and last digits on each line. 

#### Example:
```
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
```

> two1nine  
> eightwothree  
> abcone2threexyz  
> xtwone3four  
> 4nineeightseven2  
> zoneight234  
> 7pqrstsixteen  

> The calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values?


#### My Solution:
```
from input_data import input_day_01 as file

nums_as_words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
nums_as_short_words = [word[:3] for word in nums_as_words] # List of first 3 letters of number word - ['one', 'two', 'thr', 'fou', 'fiv', 'six', 'sev', 'eig', 'nin']
word_length_map = {short_word: len(full_word) for short_word, full_word in zip(nums_as_short_words, nums_as_words)} # 3 letter number word mapped to length of full word
word_value = {short_word: str(index + 1) for index, short_word in enumerate(nums_as_short_words)} # 3 letter number word mapped to its corresponding int value

def contains_digits(string):
    return any(char.isdigit() for char in string)

def is_word_number(word):
    if word in nums_as_words:
        return True
    return False

# Returns int value of word
def return_number(word):
    return word_value[word]

sum = 0
for line in file:
    ### Find Word Numbers - and store them with indexes as key in word_numbers dict
    word_numbers = {i: return_number(line[i:i+3]) for i in range(len(line) - 3) # Store index as key : int value of word as value...
                    if not contains_digits(line[i:i+3]) # if this three letter substring doesn't contain any digits
                    and (line[i:i+3] in nums_as_short_words) # and if this three letter substring is in nums_as_short_words
                    and (is_word_number(line[i:i+word_length_map[line[i:i+3]]]) == True)} # and if full word is a number
    # Using 3 letter substrings above as the shortest numbers as words are 3 letters long
    # And can then use the length of the word to see if the whole word is actually at that index location
    
    ### Find Numbers - and store them with indexes as key in digit_numbers
    digit_numbers = {index : char for index, char in enumerate(line) if char.isdigit()}

    # Combine word_numbers and digit_numbers into one dict
    # Keys are indexes of where the number occurs in line, values are the int value
    numbers = {**word_numbers, **digit_numbers}
            
    # min of numbers will be lowest index i.e. first number
    # max of numbers will be highest index i.e. last number
    calibration_value = int(str(numbers[min(numbers)]) + str(numbers[max(numbers)]))
    sum += calibration_value

print("Sum of all Calibration Values:", sum)
```

---
[< Back to all solutions](https://github.com/codehath/advent-of-code-2023/tree/main)