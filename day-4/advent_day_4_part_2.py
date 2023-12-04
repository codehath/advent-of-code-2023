from input_data import input_day_04 as file

class ScratchCard():
    def __init__(self, winning_nums, chosen_nums):
        self.winning_nums = winning_nums
        self.chosen_nums = chosen_nums
        self.quantity = 1
        self.matches = self.calculate_matches()
        self.cards_won = None

    def __repr__(self):
        return f"{self.winning_nums} | {self.chosen_nums}"

    def calculate_matches(self):
        matches = 0
        for number in self.winning_nums:
            if number in self.chosen_nums:
                matches += 1
        return matches
    
    def set_cards_won(self, cards_won):
        self.cards_won = cards_won

        for card in self.cards_won:
            card.update_quantity(self.quantity)

    def update_quantity(self, quantity):
        self.quantity += quantity

def part_two():
    scratch_cards = []
    for line in file:
        data = [x.strip() for x in line.split( )][2:]
        pipe_index = data.index("|")
        winning_nums = tuple(data[:pipe_index])
        chosen_nums = data[pipe_index + 1:]
        scratch_cards.append(ScratchCard(winning_nums, chosen_nums))

    for index, scratch_card in enumerate(scratch_cards):
        start_index = index + 1
        won_cards = scratch_cards[start_index: start_index + scratch_card.matches]
        scratch_card.set_cards_won(won_cards)

    total = 0
    for index, card in enumerate(scratch_cards):
        total += card.quantity
    
    print("Total Scratch Cards:", total)


if __name__ == "__main__":
    part_two()