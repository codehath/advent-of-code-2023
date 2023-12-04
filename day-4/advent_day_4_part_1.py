from input_data import input_day_04 as file

scratch_cards = {}
for line in file:
    data = [x.strip() for x in line.split( )][2:]
    pipe_index = data.index("|")
    winning_nums = tuple(data[:pipe_index])
    chosen_nums = data[pipe_index + 1:]
    scratch_cards[winning_nums] = chosen_nums
    # print (winning_nums)
    # print ("Chosen: ",chosen_nums)

points_total = 0
for winning in  scratch_cards:
    points = 0.5
    for number in winning:
        if number in scratch_cards[winning]:
            points *= 2
    points_total += points//1

print (points_total)







#     part_num = None
#     data.append([])
#     for char in line.rstrip():
#         # Find adjacent digits, store them as same instance of Number class
#         # Concatate digits of same part number together with .update() method of Number Class
#         if char.isdigit():
#             if part_num == None:
#                 part_num = Number()
#             part_num.update(char)
#             data[-1].append(part_num)
#         # else, char is not digit, reset part_num so it no longer reference same instance
#         else:
#             data[-1].append(char)
#             part_num = None
            
#             if char == "*":
#                 gear_coords.append((len(data) - 1, len(data[-1]) - 1))

# gear_ratio_sum = 0
# # Store each co-ordinate and its neighbours in a 3x3 sub matrix
# for coords in gear_coords:
#     part_nums = []
#     matrix = generate_matrix(data, coords, 3)
    
#     # Append all part nums to matrix, if only 2, add their product to gear ratio sum
#     for row in matrix:
#         for char in row:
#             if isinstance(char, Number) and char.added == False:
#                 part_nums.append(char)
#                 char.added = True

#     if len(part_nums) == 2:
#         gear_ratio_sum += part_nums[0].value * part_nums[1].value
    
# print("Gear Ratio Sum:", gear_ratio_sum)