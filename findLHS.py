class Solution:
  def findLHS(self,nums):
    nums.sort()
    i=0
    maxLength=0

    for i in range(len(nums)):
        while nums[i] - nums[j] > 1:
          j += 1
        if nums[i] - nums[j] ==1:
            maxlength = max(maxLength,i-j+1)
      return maxLength
