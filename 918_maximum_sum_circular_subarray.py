from typing import List


class Solution:

    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sum, curr_sum, total = nums[0], nums[0], nums[0]
        min_sum, curr_min_sum = nums[0], nums[0]
        for n in nums[1:]:
            curr_sum = max(n, curr_sum + n)
            max_sum = max(curr_sum, max_sum)

            curr_min_sum = min(n, curr_min_sum + n)
            min_sum = min(min_sum, curr_min_sum)
            total += n

        if max_sum < 0:
            return max_sum
        return max(max_sum, total - min_sum)
