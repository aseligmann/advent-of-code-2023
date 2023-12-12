import os
import re
import numpy as np


def parse_line(line):
    splits = re.split(r"[:|]", line)

    winning_numbers = re.findall(r"(\d+)", splits[1])
    for i, winning_number in enumerate(winning_numbers):
        winning_numbers[i] = int(winning_number)
    card_numbers = re.findall(r"(\d+)", splits[2])
    for i, card_number in enumerate(card_numbers):
        card_numbers[i] = int(card_number)

    n_matches = 0
    for card_number in card_numbers:
        if card_number in winning_numbers:
            n_matches += 1

    return n_matches


def main():
    print("Advent of Code 2023 - Day 04 - part 2")
    dirname = os.path.dirname(__file__)
    input_file = os.path.join(dirname, "input.txt")

    n_cards = {}
    with open(input_file, "r") as f:
        # Initialise card counting dictionary
        card_nr = 1
        for line in f:
            n_cards[card_nr] = 1
            card_nr += 1
        total_cards = card_nr - 1
        # Reset file pointer
        f.seek(0)
        # Parse lines
        card_nr = 1
        for line in f:
            line = line.rstrip("\n")
            res = parse_line(line)
            # Update card counting dictionary
            for card in range(card_nr + 1, card_nr + 1 + res):
                if card > total_cards:
                    break
                n_cards[card] += n_cards[card_nr]
            card_nr += 1

    n_cards = np.asarray(list(n_cards.values()))
    sum = n_cards.sum()
    print(f"Sum: {sum}")


if __name__ == "__main__":
    main()
