"""
DAY 2: Rock Paper Scissors

--- Part 1 ---
What would your total score be if everything goes exactly according to your strategy guide?
- The first column is what your opponent is going to play: 
    A for Rock, 
    B for Paper,
    C for Scissors
- The second column, you reason, must be what you should play in response:
    X for Rock (score 1)
    Y for Paper (score 2)
    Z for Scissors (score 3)
- Your total score is the sum of your scores for each round. The score for a single round is the score for the shape you selected plus the score for the outcome of the round
    0 if you lost
    3 if the round was a draw
    6 if you won

--- Part 2 ---
"Anyway, the second column says how the round needs to end: X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win."

The total score is still calculated in the same way, but now you need to figure out what shape to choose so the round ends as indicated.
"""


from typing import Tuple


INPUT_FILE = "./day02/input.txt"


part1_scores = {
    "A X": 1 + 3,
    "A Y": 2 + 6,
    "A Z": 3 + 0,
    "B X": 1 + 0,
    "B Y": 2 + 3,
    "B Z": 3 + 6,
    "C X": 1 + 6,
    "C Y": 2 + 0,
    "C Z": 3 + 3
}

part2_scores = {
    "A X": 3 + 0,
    "A Y": 1 + 3,
    "A Z": 2 + 6,
    "B X": 1 + 0,
    "B Y": 2 + 3,
    "B Z": 3 + 6,
    "C X": 2 + 0,
    "C Y": 3 + 3,
    "C Z": 1 + 6
}


def calc_score(file: str) -> Tuple[int, int]:
    part1_total = 0
    part2_total = 0
    
    with open(file, "r") as reader:
        for line in reader.readlines():
            if line != "\n":
                game = line[:3]
                part1_total += part1_scores[game]
                part2_total += part2_scores[game]

    return part1_total, part2_total


def main():
    print(calc_score(INPUT_FILE))
    

# Small Test 
import unittest

class Day2Test(unittest.TestCase):
    TEST_FILE = "./day02/test.txt"
    
    def CalcScoreTest(self):
        result = calc_score(Day2Test.TEST_FILE)
        self.assertEqual((15, 12), result)


if __name__ == "__main__":
    main()
    unittest.main()
