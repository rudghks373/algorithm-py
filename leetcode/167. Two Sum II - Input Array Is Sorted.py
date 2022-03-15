class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]: 
        start = 0
        end = len(numbers)-1
        while start < end:
            sum = numbers[start] + numbers[end]
            if sum == target:
                return [start+1, end+1]
            elif sum < target:
                start += 1
            else: 
                end -= 1
        
class Solution2:
    def twoSum2(self, numbers: List[int], target: int) -> List[int]: 
        for i in range(len(numbers)):
            start = i+1
            end = len(numbers)-1
            temp = target - numbers[i]
            while start <= end:
                mid = start + (end - start)//2
                if numbers[mid] == temp:
                    return [i+1, mid+1]
                elif numbers[mid] < temp:
                    start = mid+1
                else:
                    end = mid-1
