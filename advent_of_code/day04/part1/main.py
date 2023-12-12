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

    result = 1 if n_matches > 0 else 0
    result *= pow(2, n_matches - 1)

    return int(result)


def main():
    print("Advent of Code 2023 - Day 04 - part 1")
    dirname = os.path.dirname(__file__)
    input_file = os.path.join(dirname, "input.txt")

    results = []
    with open(input_file, "r") as f:
        for line in f:
            line = line.rstrip("\n")
            res = parse_line(line)
            results.append(res)

    results = np.asarray(results)
    sum = results.sum()
    print(f"Sum: {sum}")


if __name__ == "__main__":
    main()
