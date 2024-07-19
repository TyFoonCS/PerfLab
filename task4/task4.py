import sys


def find_min_moves(nums):
    nums.sort()
    median = nums[len(nums) // 2]
    return sum(abs(num - median) for num in nums)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python task4.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    with open(filename, 'r') as file:
        nums = [int(line.strip()) for line in file.readlines()]

    result = find_min_moves(nums)
    print(result)
