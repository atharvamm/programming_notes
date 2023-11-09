# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

test = [
    # {"s": "()", "op": True},
    {"s": "()[]{}", "op": True},
    {"s": "(]", "op": False},
    {"s": "([)]", "op": False},
    {"s": "{[]}", "op": True},
    {"s": "()", "op": True},
    {"s": "(()())", "op": True},
    {"s": "({[()]})", "op": True},
    {"s": "(", "op": False},
    {"s": ")", "op": False},
    {"s": "[", "op": False},
    {"s": "]", "op": False},
    {"s": "{", "op": False},
    {"s": "}", "op": False},
    {"s": "({[", "op": False},
    {"s": ")]}", "op": False},
    {"s": "((()))", "op": True},
    {"s": "(()[{}])", "op": True},
    {"s": "({[()]})", "op": True},
    {"s": "({[()()]})", "op": True},
    {"s": "({[(())]})", "op": True},
    {"s": "((", "op": False},
    {"s": "))", "op": False},
    {"s": "(()))", "op": False},
    {"s": "({[()]})(", "op": False},
    {"s": "({[()]})", "op": True},
    {"s": "{[()}", "op": False},
    {"s": "{[()]}}", "op": False},
    {"s": "({[()]})", "op": True},
]

class Solution:
    def isValid(self, s: str) -> bool:
        chars = list(s)
        closing_chars = {')':'(', '}':'{', ']':'['}
        brackets = []
        while len(chars) > 0:
            cur_char = chars.pop()
            if len(brackets) == 0:
                brackets.append(cur_char)
                continue
            if cur_char == closing_chars.get(brackets[0],"!"):
                del brackets[0]
            else:
                brackets.insert(0,cur_char)
        if len(brackets) == 0:
            return True
        return False





for ele in test:
    ip = ele["s"]
    print("ip:",ip, end = " ")
    ans = isValid(ip)
    print(ans == ele["op"])
    # break






























