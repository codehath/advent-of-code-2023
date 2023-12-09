from input_data import input_day_09 as file

def parse_data(file):
    data = []
    for line in file:
        data.append([int(x) for x in line.split( )])
    return data

def next_in_sequence(sequence):
    increments = []
    for index, num in enumerate(sequence):
        if index != len(sequence) -1:
            increments.append(sequence[index+1] - num)

    if set(increments) == {0}: return sequence[-1]
    return sequence[-1] + next_in_sequence(increments)

def prev_in_sequence(sequence):
    increments = []
    for index, num in enumerate(sequence):
        if index != len(sequence) -1:
            increments.append(sequence[index+1] - num)

    if set(increments) == {0}: return sequence[0]
    return sequence[0] - prev_in_sequence(increments)

def run(function):
    data = parse_data(file)
    sum_values = 0
    for sequence in data:
        sum_values += function(sequence)
    print("Sum of Extrapolated Values:", sum_values)

def part_one():
    run(next_in_sequence)
def part_two():
    run(prev_in_sequence)

if __name__ == "__main__":
    part_one()
    part_two()
