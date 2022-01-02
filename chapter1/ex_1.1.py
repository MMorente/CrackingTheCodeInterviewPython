### Implement an algorithm to check if a string has all unique chars ###

import unittest

def is_unique(word: str) -> bool:
    
    if len(word) > 128:
        return False
        
    letters = set()

    for letter in word:
        if letter not in letters:
            letters.add(letter)
        else:
            return False

    return True

class TestUnique(unittest.TestCase):
    
    def test_asserts(self):
        self.assertTrue(is_unique("Manuel"))
        self.assertFalse(is_unique("ANA"))
        self.assertFalse(is_unique("aaaaa"))
        self.assertTrue(is_unique("a"))

if __name__ == "__main__":
    unittest.main()