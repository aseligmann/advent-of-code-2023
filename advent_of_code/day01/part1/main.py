import os
import re
import numpy as np


def parse_line(line: str):
    # Get first and last integers
    # Split at digits using regex
    matches = re.split(r"(\d)", line)
    # Filter list down to only digits
    matches = list(filter(lambda x: x.isdigit(), matches))

    if matches:
        # Get first and last matches
        n = len(matches)
        first, second = "", ""
        if n > 1:
            # More than one digit - use first and last
            first = matches[0]
            second = matches[-1]
        else:
            # Only one digit - use digit for both
            first = matches[0]
            second = first

        # Combine digits
        out = first + second  # As string
        out = int(out)  # Convert to number

    return out


def main():
    print("Advent of Code 2023 - Day 01 - part 1")
    dirname = os.path.dirname(__file__)
    input_file = os.path.join(dirname, "input.txt")

    results = []
    with open(input_file, "r") as f:
        for line in f:
            res = parse_line(line)
            results.append(res)

    results = np.asarray(results)
    sum = results.sum()
    print(f"Sum: {sum}")


if __name__ == "__main__":
    main()
