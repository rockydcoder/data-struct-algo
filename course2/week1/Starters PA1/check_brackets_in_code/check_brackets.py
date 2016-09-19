# python3

import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

if __name__ == "__main__":
    text = sys.stdin.read()

    opening_brackets_stack = []
    ordered = True
    for i, next in enumerate(text):
        if next == '(' or next == '[' or next == '{':
            opening_brackets_stack.append(Bracket(next, i))

        if next == ')' or next == ']' or next == '}':
            if not opening_brackets_stack:
                print (i + 1)
                ordered = False
                opening_brackets_stack = []
                break
            last_opening_bracket = opening_brackets_stack.pop()
            if not (last_opening_bracket.Match(next)):
                print (i + 1)
                ordered = False
                opening_brackets_stack = []
                break

    if ordered and not opening_brackets_stack:
        print ("Success")

    if opening_brackets_stack:
        print (opening_brackets_stack.pop().position + 1)


