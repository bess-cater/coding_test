class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seen.keys():
                return [seen[diff], i]
            else:
                seen[nums[i]] = i

if __name__ == "__main__":
    new_ = Solution()
    nums = [2,7,11,15]
    target = 9
    answer = new_.twoSum(nums, target)
    print(answer)