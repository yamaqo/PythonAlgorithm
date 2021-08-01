from random import randint
from typing import List

def cocktail_sort(numbers: List[int]) -> List[int]:
    number_len = len(numbers)
    swapped = True

    start = 0
    end = number_len - 1

    while swapped:
        swapped = False
        for i in range(start, end):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                swapped = True

        if not swapped:
            break

        swapped = False
        end = end - 1

        for i in range(end - 1, start - 1, -1):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                swapped = True

        start = start + 1

    print(numbers)

if __name__ == '__main__':
    nums = [randint(0, 1000) for i in range(1000)]
    cocktail_sort(nums)