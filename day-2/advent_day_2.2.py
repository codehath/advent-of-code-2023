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
