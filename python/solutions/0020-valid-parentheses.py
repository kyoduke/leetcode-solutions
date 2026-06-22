import unittest


def is_valid(text: str) -> bool:
    pairs = {"(": ")", "[": "]", "{": "}"}
    stack = []
    for char in text:
        if char in pairs:
            stack.append(char)
        elif not stack:
            return False

        else:
            top = stack[-1]
            if char != pairs[top]:
                return False
            stack.pop()

    return not len(stack)


class TestValidParentheses(unittest.TestCase):

    def test_1(self):
        self.assertEqual(True, is_valid("[](){}"))

    def test_2(self):
        self.assertEqual(False, is_valid("[(){}"))

    def test_3(self):
        self.assertEqual(False, is_valid("[]){}"))

    def test_4(self):
        self.assertEqual(True, is_valid("({}[][[]]()([()]))"))

    def test_5(self):
        self.assertEqual(False, is_valid("({}[][[]]()([()])))"))
