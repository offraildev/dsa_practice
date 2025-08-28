from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix = [1]
        # for i in range(1, len(nums)):
        #         prefix.append(prefix[-1]* nums[i-1])

        # suffix = [1]
        # for i in range(len(nums)-2, -1, -1):
        #     suffix.append(suffix[-1]*nums[i+1])

        # result = []
        # for a, b in zip(prefix, suffix[::-1]):
        #     result.append(a*b)
        # return result

        result = [1] * len(nums)
        prefix, suffix = 1, 1
        for i in range(1, len(nums)):
            prefix *= nums[i - 1]
            result[i] = prefix

        for i in range(len(nums) - 2, -1, -1):
            suffix *= nums[i + 1]
            result[i] = suffix * result[i]
        return result
