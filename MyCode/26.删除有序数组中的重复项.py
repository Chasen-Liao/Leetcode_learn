#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # 能不能用异或
        # 但是还要去修改数组
        # 用双指针
        right = 0
        left = 0
        
        while (left < len(nums)) :
            if nums[right] == nums[left]:
                left += 1
            else:
                right += 1
                nums[right] = nums[left]
        
        return len(nums[:right+1])
        
        
# @lc code=end

