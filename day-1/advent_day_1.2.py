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
