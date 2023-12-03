from input_data import input_day_03 as file

class Number:
    def __init__(self):
        self.value = ""
        self.added = False
    
    def __repr__(self):
        return self.value
    
    # Concatenate new digits to value
    def update(self, digit):
        self.value = int(str(self.value) + digit)

def generate_matrix(array_2d, coords, size):
    rows, cols = size, size
    diff = size//2 # Used to adjust sub-matrix size if co-ords too close to edge of 2D array for full size
    # Adjust start co-ords and size if start co-ords negative
    start_row, start_col = coords[0] - diff, coords[1] - diff
    if start_row < 0:
        start_row, rows = 0, rows - diff
    if start_col < 0:
        start_col, cols = 0, cols - diff
    
    # Return the size x size slice from 2d array - in this case, a 3x3 slice
    return [row[start_col:start_col+rows] for row in array_2d[start_row:start_row+cols]]

data = []
special = "*@/+$=&-#%"
gear_coords = []
for line in file:
    part_num = None
    data.append([])
    for char in line.rstrip():
        # Find adjacent digits, store them as same instance of Number class
        # Concatate digits of same part number together with .update() method of Number Class
        if char.isdigit():
            if part_num == None:
                part_num = Number()
            part_num.update(char)
            data[-1].append(part_num)
        # else, char is not digit, reset part_num so it no longer reference same instance
        else:
            data[-1].append(char)
            part_num = None
            
            if char == "*":
                gear_coords.append((len(data) - 1, len(data[-1]) - 1))

gear_ratio_sum = 0
# Store each co-ordinate and its neighbours in a 3x3 sub matrix
for coords in gear_coords:
    part_nums = []
    matrix = generate_matrix(data, coords, 3)
    
    # Append all part nums to matrix, if only 2, add their product to gear ratio sum
    for row in matrix:
        for char in row:
            if isinstance(char, Number) and char.added == False:
                part_nums.append(char)
                char.added = True

    if len(part_nums) == 2:
        gear_ratio_sum += part_nums[0].value * part_nums[1].value
    
print("Gear Ratio Sum:", gear_ratio_sum)