class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i in range(len(nums)):
            hashtable[nums[i]] = i
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashtable and i != hashtable[diff]:
                return [i, hashtable[diff]]