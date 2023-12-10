import os
import re
import numpy as np


def parse_line(line: str):
    # Split at game delimiters
    splits = re.split(r"[:;]", line)

    n_reds, n_greens, n_blues = 0, 0, 0
    for split in splits[1:]:
        red = re.search(r"(\d+) red", split)
        green = re.search(r"(\d+) green", split)
        blue = re.search(r"(\d+) blue", split)
        if red:
            n_reds = max(n_reds, int(red.group(1)))
        if green:
            n_greens = max(n_greens, int(green.group(1)))
        if blue:
            n_blues = max(n_blues, int(blue.group(1)))

    power = n_reds * n_greens * n_blues
    return power


def main():
    print("Advent of Code 2023 - Day 02 - part 2")
    dirname = os.path.dirname(__file__)
    input_file = os.path.join(dirname, "input.txt")

    results = []
    with open(input_file, "r") as f:
        for line in f:
            res = parse_line(line)
            if res:
                results.append(res)

    results = np.asarray(results)
    sum = results.sum()
    print(f"Sum: {sum}")


if __name__ == "__main__":
    main()
