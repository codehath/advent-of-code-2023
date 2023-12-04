from input_data import input_day_04 as file

def parse_data(file):
    scratch_cards = []
    for line in file:
        data = [x.strip() for x in line.split( )][2:]
        pipe_index = data.index("|")
        winning_nums = tuple(data[:pipe_index])
        chosen_nums = tuple(data[pipe_index + 1:])
        card = (winning_nums, chosen_nums)
        scratch_cards.append(card)

    return scratch_cards

def calculate_matches(scratch_card):
        matches = 0
        for number in scratch_card[0]:
            if number in scratch_card[1]:
                matches += 1
        return matches

def part_one():
    scratch_cards = parse_data(file)
    points_total = 0
    for scratch_card in  scratch_cards:
        matches = calculate_matches(scratch_card)
        points_total += int(2**(matches-1))

    print ("Points:", points_total)


if __name__ == "__main__":
    part_one()