# Pair Research Matching Algorithm

This repository includes two matching algorithms that are used for Pair Research:

1. Stable Roommates Matching
2. Maximum Weighted Matching

## Development and Analysis

We use [pipenv](https://github.com/pypa/pipenv) for managing package dependencies.

1. Install pipenv using the link above.
2. Run `pipenv install` to install package dependencies and `pipenv shell` to start virtual environment with installed dependencies.
3. Run `jupyter notebook` to start a notebook server. Analysis notebooks are contained in the `analysis/` directory.

## Usage

```bash
cat input.json | python pair_research.py
```

Example:

Input: [(0, 1, 93), (0, 2, -20), (0, 3, 2), (1, 2, -13), (1, 3, 10), (2, 3, 80)]

* Matching person 0 and person 1 gives a score of 93
* Matching person 0 and person 2 gives a score of -20
* Matching person 0 and person 3 gives a score of 2
* Matching person 1 and person 2 gives a score of -13
* Matching person 1 and person 3 gives a score of 10
* Matching person 2 and person 3 gives a score of 80

Output: [1, 0, 3, 2]

* Person 0 is matched with person 1
* Person 1 is matched with person 0
* Person 2 is matched with person 3
* Person 3 is matched with person 2
