class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        count1,count2=1,1
        max_1=1
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                count1+=1
                count2=1     
            elif nums[i]>nums[i+1]:
                count2+=1
                count1=1
            else:
                count1=count2=1
            max_1=max(count1,count2,max_1)

        return max_1