import os
import re
import numpy as np


def parse_line(line: str, max_red: int, max_green: int, max_blue: int):
    # Split at game delimiters
    splits = re.split(r"[:;]", line)
    # Get game id
    game_id = int(re.findall(r"(\d+)", splits[0])[0])

    # Parse splits for colours
    for split in splits[1:]:
        # Get number of each coloured cubes
        n_reds, n_greens, n_blues = 0, 0, 0
        red = re.search(r"(\d+) red", split)
        green = re.search(r"(\d+) green", split)
        blue = re.search(r"(\d+) blue", split)
        if red:
            n_reds = int(red.group(1))
        if green:
            n_greens = int(green.group(1))
        if blue:
            n_blues = int(blue.group(1))

        # Check against max allowable
        if (n_reds > max_red) or (n_greens > max_green) or (n_blues > max_blue):
            return None

    return game_id


def main():
    print("Advent of Code 2023 - Day 02 - part 1")
    dirname = os.path.dirname(__file__)
    input_file = os.path.join(dirname, "input.txt")

    max_red = 12
    max_green = 13
    max_blue = 14

    results = []
    with open(input_file, "r") as f:
        for line in f:
            res = parse_line(line, max_red, max_green, max_blue)
            if res:
                results.append(res)

    results = np.asarray(results)
    sum = results.sum()
    print(f"Sum: {sum}")


if __name__ == "__main__":
    main()
