from random import randint
from typing import List

def merge_sort(numbers: List[int]) -> List[int]:
    if len(numbers) <= 1:
        return numbers

    center = len(numbers) // 2
    left = numbers[:center]
    right = numbers[center:]

    merge_sort(left)
    merge_sort(right)

    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            numbers[k] = left[i]
            i += 1
        else:
            numbers[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        numbers[k] = left[i]
        k += 1
        i += 1

    while j < len(right):
        numbers[k] = right[j]
        k += 1
        j += 1

    return numbers


if __name__ == '__main__':
    nums = [randint(0, 10000) for i in range(100)]
    print(merge_sort(nums))