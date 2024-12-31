import unittest


def reverse_words(text: str) -> str:
    words = text.split(" ")
    result = ""

    for word in words:
        result += " "
        result += word[::-1]

    return result[1:]


class TestReverseWords(unittest.TestCase):

    def test_1(self):
        self.assertEqual("etseT", reverse_words("Teste"))

    def test_2(self):
        self.assertEqual(
            "etseT amU avoN oãçnuF", reverse_words("Teste Uma Nova Função")
        )

    def test_3(self):
        self.assertEqual("ietseT", reverse_words("Testei"))
