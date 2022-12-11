from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Function to find two indicies of the numbers which add to a 
        target value in a given list.

        O(n) time complexity: Iterate over nums once
        O(n) space complexity: Dictionary for value:index mapping
        """
        d = dict() # Dictionary for storing value indicies

        # Iterates through numbers in list and stores their indicies in dictionary
        for i in range(len(nums)):
            d[nums[i]] = i
        #TEST
        # Iterates through numbers in list
        for i in range(len(nums)):
            compliment = target - nums[i] # Calculates compliment to the value to make the target value
            if compliment in d and d[compliment] != i: # Sees if the value is in the dictionary
                return [i, d[compliment]] # If so return two indices
