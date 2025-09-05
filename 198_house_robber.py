from typing import List


class Solution:

    # def robber(self, nums, i):
    #     if i > len(nums) - 1:
    #         return 0

    #     if self.memo[i] >= 0:
    #         return self.memo[i]

    #     self.memo[i] = max(nums[i] + self.robber(nums, i + 2), self.robber(nums, i + 1))
    #     return self.memo[i]

    # def rob(self, nums: List[int]) -> int:
    #     self.memo = [-1] * (len(nums) + 1)
    #     return self.robber(nums, 0)

    # better solution
    def rob(self, nums: List[int]) -> int:
        prev_1, prev_2 = 0, 0
        for n in nums:
            curr_rob = max(n + prev_1, prev_2)
            prev_1 = prev_2
            prev_2 = curr_rob
        return prev_2
