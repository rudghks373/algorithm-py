class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bsLeft(nums, target):
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
        
        def bsRight(nums, target):
            left = 0 
            right = len(nums) -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right
        
        
        left = bsLeft(nums, target)
        right = bsRight(nums, target)
        return [left, right] if left <= right else [-1, -1]
