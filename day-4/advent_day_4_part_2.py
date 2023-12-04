from input_data import input_day_04 as file

# Take the first item
def calculate_quantities(scratch_cards):
    if scratch_cards == {}:
        return {}
    
    all_cards = list(scratch_cards.keys())
    scratch_card = all_cards.pop(0)
    quantity = scratch_cards.pop(scratch_card )

    won_cards = all_cards[: calculate_matches(scratch_card)]
    for card in won_cards:
            scratch_cards[card] += quantity

    scratch_cards = calculate_quantities(scratch_cards)

    return {**{scratch_card:quantity}, **scratch_cards}

def calculate_matches(scratch_card):
        matches = 0
        for number in scratch_card[0]:
            if number in scratch_card[1]:
                matches += 1
        return matches

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

def part_two():
    scratch_cards = parse_data(file)
    processed_cards = calculate_quantities(dict.fromkeys(scratch_cards, 1))
    total = 0
    for quantity in processed_cards.values():
        total += quantity

    print("Total Scratch Cards:", total)

if __name__ == "__main__":
    part_two()