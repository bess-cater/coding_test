from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        while left<right:
            interim = numbers[left]+numbers[right]
            if interim == target:
                answer = [left+1, right+1]
                return answer
            elif interim > target:
                right-=1
            if interim < target:
                left+=1

if __name__ == "__main__":
    new_ = Solution()
    nums = [2,7,11,15]
    target = 9
    answer = new_.twoSum(nums, target)
    print(answer)