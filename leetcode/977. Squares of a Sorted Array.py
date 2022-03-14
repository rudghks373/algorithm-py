class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        aws = []
        for index in range(len(nums)):
            aws.append(nums[index] ** 2)
        aws.sort()
        return aws
        
