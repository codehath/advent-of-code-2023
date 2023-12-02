from input_data import input_day_01 as file

sum = 0
for line in file:
    # Store each digit in line
    nums = [char for char in line if char in "0123456789"]
    
    # Use first and last digit to work out calibration value
    calibration_value = int(nums[0] + nums[-1])
    sum += calibration_value

print("Sum of all Calibration Values:", sum)



