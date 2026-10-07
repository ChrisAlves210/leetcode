class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Pattern: sort, then use two pointers to find complementary pairs.
        # Time: O(n^2); space: O(n) for sorting, excluding the result.
        nums.sort()
        triplets = []

        for index in range(len(nums) - 2):
            if index > 0 and nums[index] == nums[index - 1]:
                continue
            if nums[index] > 0:
                break

            left = index + 1
            right = len(nums) - 1

            while left < right:
                total = nums[index] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    triplets.append([nums[index], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return triplets