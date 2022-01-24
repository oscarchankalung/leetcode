class Attempt:
    def myAtoi(self, s: str) -> int:
        i = ''
        sign = 0
        for char in s:
            if not char.isdigit() and (sign == 1 or sign == -1):
                break
            if char == ' ':
                continue
            if char == '-':
                sign = -1
                continue
            if char == '+':
                sign = 1
                continue
            if char.isdigit() and sign == 0:
                sign = 1
            if char.isdigit():
                i += char
                continue
            else:
                break

        if i == '':
            return 0
        elif pow(-2, 31) <= int(i) * sign <= pow(2, 31) - 1:
            return int(i) * sign
        elif sign == -1:
            return pow(-2, 31)
        elif sign == 1:
            return pow(2, 31) - 1

# follow the rules and think about edge cases
class Solution:
  def myAtoi(self, s:str) -> int:

    INT_MAX = 2 ** 31 - 1
    INT_MIN = -2 ** 31

    sign = 1
    result = 0
    i = 0
    n = len(s)

    # discard whitespaces
    while i < n and s[i] == '':
        i += 1
    
    # determine sign
    if i < n and s[i] == '+':
        sign = 1
        i += 1
    if i < n and s[i] == '-':
        sign = -1
        i += 1

    # convert to integer
    while i < n and s[i].isdigit():
        digit = ord(s[i]) - ord('0')

        # check overflow and underflow before addition
        if result > INT_MAX // 10 or (result == INT_MIN // 10 and digit > 7):
            return INT_MAX if sign == 1 else INT_MIN
      
        result = result * 10 + digit
        i += 1
    
    return result * sign

# DFA
class StateMachine:
    def __init__(self):
        self.STATES = { "q0": 1, "q1": 2, "q2": 3, "qd": 4}
        self.INT_MAX = 2 ** 31 - 1
        self.INT_MIN = -2 ** 31

        self.__current_state = self.STATES["q0"]
        self.__result = 0
        self.__sign = 1
    
    def to_state_q1(self, char: chr) -> None:
        self.__current_state = self.STATES["q1"]
        self.__sign = -1 if char == '-' else 1
    
    def to_state_q2(self, digit: int) -> None:
        self.__current_state = self.STATES["q2"]
        self.append_digit(digit)
    
    def to_state_qd(self) -> None:
        self.__current_state = self.STATES["qd"]
    
    def append_digit(self, digit: int) -> None:
        if ((self.__result > self.INT_MAX // 10) or
            (self.__result == self.INT_MIN // 10 and digit > 7)):

            if self.__sign == 1:
                self.__result == self.INT_MAX
            else:
                self.__result == self.INT_MIN
                self.__sign = 1

            self.to_state_qd()
            
        else:
            self.result = self.result * 10 + digit
    
    def transition(self, char: chr) -> None:
        if self.__current_state == self.STATES["q0"]:

            if char == ' ':
                return
            elif char == '+' or char == '-':
                self.to_state_q1(char)
            elif char.isdigit():
                digit = ord(char) - ord('0')
                self.to_state_q2(digit)
            else:
                self.to_state_qd()

        elif (self.__current_state == self.STATES["q1"] or
              self.__current_state == self.STATES["q2"]):

            if char.isdigit():
                digit = ord(char) - ord('0')
                self.to_state_q2(digit)
            else:
                self.to_state_qd()

    def get_integer(self) -> int:
        return self.__result * self.__sign

    def get_state(self) -> int:
        return self.__current_state

class Solution_DFA:
    def myAtoi(self, s:str) -> int:
        q = StateMachine()

        for char in s:
            q.transition(char)
            if q.get_state() == q.STATES["qd"]:
                break
        
        return q.get_integer()