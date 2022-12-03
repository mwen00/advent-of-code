"""
DAY 1: Calorie Counting

--- Part 1 ---
Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?

--- Part 2 ---
Get the total Calories carried by the top three Elves carrying the most Calories.
That way, even if one of those Elves runs out of snacks, they still have two backups.
"""


INPUT_FILE = "./day01/input.txt"


def calc_top_three(file: str) -> int:
    top_three = []

    with open(file, "r") as reader:
        data = reader.read()
        max = 0
        sum_ = 0

        for i in data.split("\n"):
            if i == "":
                max = sum_ if sum_ > max else max
                top_three.append(sum_)
                    
                sum_ = 0
                continue

            sum_ += int(i)

    top_three.sort(reverse=True)
    del top_three[3:]

    return sum(top_three)


def main():
    print(calc_top_three(INPUT_FILE))


# Small Test 
import unittest

class Day1Test(unittest.TestCase):
    TEST_FILE = "./day01/test.txt"
    TOP_THREE = [24000, 11000, 6000]

    def testCalcTopThree(self):
        result = calc_top_three(Day1Test.TEST_FILE)
        self.assertEqual(sum(Day1Test.TOP_THREE), result)


if __name__ == "__main__":
    main()
    unittest.main()
