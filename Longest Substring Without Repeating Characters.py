class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Pattern: sliding window with last-seen character indices.
        # Time: O(n); space: O(k), where k is the number of distinct characters.
        last_seen = {}
        window_start = 0
        longest = 0

        for window_end, character in enumerate(s):
            if character in last_seen and last_seen[character] >= window_start:
                window_start = last_seen[character] + 1

            last_seen[character] = window_end
            longest = max(longest, window_end - window_start + 1)

        return longest