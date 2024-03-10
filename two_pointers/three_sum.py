from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        if len(nums)<3:
            return triplets
        nums_s = sorted(nums)
        for i in range(len(nums_s)):
            if i!=0 and nums_s[i]==nums_s[i-1]:
                continue
            first = i

        #middle = len(nums_s)//2
            second = i+1
            third = len(nums_s)-1
            while second < third:
                if nums_s[first]+nums_s[second]+nums_s[third]==0:
                    triplets.append([nums_s[first],nums_s[second],nums_s[third]])
                    second+=1
                    third-=1
                    #avoid duplicates
                    while second<third and nums_s[second]==nums_s[second-1]:
                        second+=1
                    while second<third and nums_s[third]==nums_s[third+1]:
                        third-=1
                    
                elif nums_s[first]+nums_s[second]+nums_s[third] > 0:
                    third-=1
                if nums_s[first]+nums_s[second]+nums_s[third] < 0:
                    second+=1
        return triplets
    
if __name__ == "__main__":
    new_ = Solution()
    nums = [-1,0,1,2,2, 2,-1,-4]
    answer = new_.threeSum(nums)
    print(answer)