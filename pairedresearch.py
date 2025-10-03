import sys
from mwmatching import maximum_weighted_matching


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.stderr.write("Usage: python pairedresearch.py weights.txt\n")
        sys.exit(1)

    with open(sys.argv[1]) as file:
        lines = file.readlines()

    # weights
    weights = eval(lines[0])

    matches = maximum_weighted_matching(weights)

    print(matches)
