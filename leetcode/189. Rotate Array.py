class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]           
        
class Solution2:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        def twopt(nums,start,end):
            while (start < end):
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
            print(nums)
            return nums
        
        start = 0
        end = len(nums)-1
        k %= len(nums)
        
        twopt(nums,start,end)
        twopt(nums,start,k-1)
        twopt(nums,k,end)
    
