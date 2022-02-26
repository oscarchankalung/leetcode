from collections import deque

class Attempt:
    def isValid(self, s: str) -> bool:
        string = deque(s)
        stack = []
        opening_brackets = '([{'
        closing_brackets = ')]}'
        pairing_brackets = {'(':')', '[':']', '{':'}'}
        
        while string:
            bracket = string.popleft()
            if bracket in opening_brackets:
                stack.append(bracket)
            if bracket in closing_brackets:
                if not stack:
                    return False
                if pairing_brackets[stack.pop()] != bracket:
                    return False
        return True if not stack else False

class Solution_Dict:
    def isValid(self, s: str) -> bool:
        stack = []
        pairing_brackets = {')':'(', ']':'[', '}':'{'}
        opening_brackets = pairing_brackets.values()
        closing_brackets = pairing_brackets.keys()
        
        for char in s:
            if char in opening_brackets:
                stack.append(char)
            if char in closing_brackets:
                if not stack:
                    return False
                if stack.pop() != pairing_brackets[char]:
                    return False
        return stack == []

class Solution_Set:
    def isValid(self, s: str) -> bool:
        stack = []
        pairing_brackets = set([('(', ')'),('[', ']'),('{', '}')])
        opening_brackets = set('([{')
        closing_brackets = set(')]}')
        
        for char in s:
            if char in opening_brackets:
                stack.append(char)
            if char in closing_brackets:
                if not stack:
                    return False
                if (stack.pop(), char) not in pairing_brackets:
                    return False
        return stack == []