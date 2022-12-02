"""
DAY 1: Calorie Counting

--- Part 1 ---
Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?

--- Part 2 ---
Get the total Calories carried by the top three Elves carrying the most Calories.
That way, even if one of those Elves runs out of snacks, they still have two backups.
"""

TEST_FILE = "./2022/day01/test.txt"
INPUT_FILE = "./2022/day01/input.txt"

TEST_ANSWER = [24000, 11000, 6000]

top_three = []

with open(INPUT_FILE, "r") as reader:
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

    print(f"Max: {max}")

top_three.sort(reverse=True)
del top_three[3:]

print(f"Top Three Total: {sum(top_three)}")
