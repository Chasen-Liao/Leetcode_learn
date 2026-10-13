#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        #? 暴力循环法
        # # 需要返回的是下标 
        # for i, item in enumerate(nums):
        #     for j in range(i + 1, len(nums)):
        #         post = nums[j]
        #         if item + post == target:
        #             return [i, j] # 返回列表
        
        #? 通过哈希表去记住已经遍历过的元素下标
        
        # # 这里要注意不能同时使用同一个元素两次
        # cache = {}
        # for i, item in enumerate(nums):
        #     # 简历哈希表 | 字典
        #     cache[item] = i
        
        # for i, item in enumerate(nums):
        #     other = target - item
            
        #     if  other in cache and cache[other] != i:
        #         return [i, cache[other]]
        
        #? 不用两次遍历，一次遍历，一边变论 
        # 一边加 然后一边和前面出现的去匹配
        cache = {}
        for i, item in enumerate(nums):
            other = target - item # 我们要找的
            # 先查再存
            if other in cache and cache[other] != i:
                return [cache[other], i]
            
            cache[item] = i
            
# @lc code=end

