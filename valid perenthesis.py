class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Map closing brackets to their corresponding opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []
        
        for char in s:
            # If the character is a closing bracket
            if char in bracket_map:
                # Pop the top element if stack isn't empty, else use a dummy variable
                top_element = stack.pop() if stack else '#'
                
                # Check if the opened bracket matches the required closing bracket
                if bracket_map[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it onto the stack
                stack.append(char)
                
        # The string is valid only if the stack is completely empty
        return len(stack) == 0
