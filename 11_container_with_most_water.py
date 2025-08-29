from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = (right - left) * min(height[left], height[right])
        while left < right:
            if height[left] <= height[right]:
                left += 1
                max_area = max(
                    (right - left) * min(height[left], height[right]), max_area
                )
            else:
                right -= 1
                max_area = max(
                    (right - left) * min(height[left], height[right]), max_area
                )
        return max_area
