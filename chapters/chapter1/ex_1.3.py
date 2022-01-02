### URLify ###

import unittest

def urlify(sentence: str, size: int) -> str:
    target = sentence[:size]
    sol = []
    for letter in target:
        sol.append('%20' if letter.isspace() else letter)

    return "".join(sol) # O(n)


class TestUrlify(unittest.TestCase):

    def test_asserts(self):
        self.assertEqual("Mr%20John%20Smith", urlify("Mr John Smith   ", 13))
        self.assertEqual("Mr%20John%20Smith%20", urlify("Mr John Smith   ", 14))


if __name__ == "__main__":
    unittest.main()