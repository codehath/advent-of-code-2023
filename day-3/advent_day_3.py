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

def get_submatrix(array_2d, coords, size):
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

# Creates 2D data array from file and finds co-ordinates of chars
# Function would return 2D data array and list of special character co-ordinates
def create_2d_array_find(file, chars_to_find):
    data = []
    coords = []

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
                
                if char in chars_to_find:
                    coords.append((len(data) - 1, len(data[-1]) - 1))
    
    return data, coords

def get_part_numbers(data, coords):
    part_numbers = []
    # Store each co-ordinate and its neighbors in a 3x3 sub-matrix
    for coords in coords:
        part_nums = []
        matrix = get_submatrix(data, coords, 3)
        
        # Append all part nums to matrix, if only 2, add their product to the result sum
        for row in matrix:
            for char in row:
                if isinstance(char, Number) and not char.added:
                    part_nums.append(char.value)
                    char.added = True

        part_numbers.append(part_nums)

    return part_numbers

def part_one():
    data, coords = create_2d_array_find(file, "*@/+$=&-#%")
    part_numbers = get_part_numbers(data, coords)

    # Sum Part Numbers
    # Sum all elements in the 2D part_numbers arry
    part_numbers_sum = [sum(numbers) for numbers in part_numbers]
    part_number_sum = sum(part_numbers_sum)
    print("Part Number Sum:", part_number_sum)

def part_two():
    data, coords = create_2d_array_find(file, "*")
    part_numbers = get_part_numbers(data, coords)

    # Sum Gear Ratios
    # Calculate gear ratio for each pair of part numbers and sum
    gear_ratios = [numbers[0]*numbers[1] for numbers in part_numbers if len(numbers) == 2]
    gear_ratio_sum = sum(gear_ratios)
    print("Gear Ratio Sum:", gear_ratio_sum)


if __name__ == "__main__":
    part_one()
    part_two()