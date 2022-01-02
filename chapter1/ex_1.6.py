### STRING COMPRESSION ###

import unittest

def compress_str(s: str) -> str:
    sol = []
    prev_letter = False
    for letter in s:
        if len(sol) >= len(s):
            return s
        if not prev_letter:
            prev_letter = letter
            counter = 1
        elif letter == prev_letter:
            counter += 1
        else:
            sol.append(prev_letter)
            sol.append(str(counter))
            prev_letter = letter
            counter = 1
    
    sol.append(prev_letter)
    sol.append(str(counter))

    return "".join(sol)


class TestCompression(unittest.TestCase):

    def test_asserts(self):
        self.assertEqual(compress_str("aabcccccaaa"), "a2b1c5a3")
        self.assertEqual(compress_str("a"), "a1")
        self.assertEqual(compress_str("aaabcc"), "a3b1c2")


if __name__ == "__main__":
    unittest.main()