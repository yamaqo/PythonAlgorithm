from random import randint
from typing import List

def bubble_sort(numbers: List[int]) -> List[int]:
    print(numbers)
    number_len = len(numbers)

    for i in range(number_len):
        for j in range(number_len - 1 - i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    print(numbers)


if __name__ == '__main__':
    nums = [randint(0, 1000) for i in range(100)]
    bubble_sort(nums)