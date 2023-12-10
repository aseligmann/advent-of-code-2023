import os
import re
import numpy as np


def parse_line(line: str):
    # Get first and last integers
    # Split at digits using regex
    digits = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    regex_digits = ""
    regex_digits = regex_digits.join([f"({key})|" for key in digits.keys()])
    regex = regex_digits + r"(\d)"
    matches = []
    while len(line) > 0:
        match = re.search(regex, line)
        if match:
            # Get match
            match_string = match.group()
            matches.append(match_string)
            # Shorten string to search
            next_start_index = match.start() + 1
            if next_start_index < len(line):
                line = line[next_start_index:]
        else:
            break

    if matches:
        # Convert to digits
        matches_as_digits = []
        for match in matches:
            # Ensure valid
            if not match:
                continue
            if not match.isalnum():
                continue

            # If already digit, then just append and continue
            if match.isdigit():
                matches_as_digits.append(match)
                continue

            # Otherwise, match string and set string of value
            for digit, value in digits.items():
                if match == digit:
                    matches_as_digits.append(str(value))

        # Get first and last matches
        n = len(matches_as_digits)
        first, second = "", ""
        if n > 1:
            # More than one digit - use first and last
            first = matches_as_digits[0]
            second = matches_as_digits[-1]
        else:
            # Only one digit - use digit for both
            first = matches_as_digits[0]
            second = first

        # Combine digits
        out = first + second  # As string
        out = int(out)  # Convert to number
        print(out)

    return out


def main():
    print("Advent of Code 2023 - Day 01 - part 2")
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
