class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Dictionary to store numbers we have already seen and their indices
        seen = {}
        
        # Loop through the list tracking both the index and the value
        for index, num in enumerate(nums):
            # Calculate the number needed to reach the target
            complement = target - num
            
            # If the complement is already in our dictionary, we found the pair
            if complement in seen:
                return [seen[complement], index]
            
            # Otherwise, add the current number and its index to the dictionary
            seen[num] = index
            
        # Return an empty list if no solution is found (though LeetCode guarantees one)
        return []
