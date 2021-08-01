from random import randint
from typing import List

def select_sort(numbers: List[int]) -> List[int]:
    numbers_len = len(numbers)

    for i in range(numbers_len):
        selected = i
        for j in range(i + 1, numbers_len):
            if selected > numbers[j]:
                selected = numbers[j]

        numbers[i], numbers[selected] = numbers[selected], numbers[i]

    print(numbers)


if __name__ == '__main__':
    nums = [randint(0, 1000) for i in range(10000)]
    select_sort(nums)