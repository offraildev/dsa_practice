from typing import List


class BinarySearch:

    def search(
        self,
        array: List[int],
        target: int,
    ) -> int:
        """Return the index of `target` in the `array`, return -1 if not found."""
        if not array:
            return -1
        left = 0
        right = len(array) - 1
        while right >= left:
            mid = left + (right - left) // 2
            if target == array[mid]:
                return mid
            elif target > array[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return -1


if __name__ == "__main__":

    # generate random test case
    import random

    array = sorted([random.randint(a=0, b=100) for n in range(10)])
    target = -100 if random.choice(["H", "T"]) == "H" else random.choice(array)

    bnSearch = BinarySearch()
    result = bnSearch.search(array, target)
    # print("result", result)
    print("Array:", array)
    print("Target:", target)
    print("Element not found in array") if result == -1 else print("Element found")
