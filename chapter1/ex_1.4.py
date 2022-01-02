### Check if any permutation is a palindrome ###

import unittest

def check_palin(sentence: str) -> bool:
    target = sentence.lower()
    letters = dict()
    odd_count = 0
    for letter in target:    
        if letter.isalpha():
            if letter not in letters:
                letters[letter] = 1
            else:
                letters[letter] += 1
            
            if letters[letter]%2:
                odd_count +=1
            else:
                odd_count -= 1

    return True if odd_count <=1 else False


class TestPalin(unittest.TestCase):
    
    def test_asserts(self):
        self.assertTrue(check_palin("Tact Coa"))
        self.assertTrue(check_palin("a"))
        self.assertTrue(check_palin("aaaaa aaa"))
        self.assertFalse(check_palin("ab"))
        self.assertFalse(check_palin("abca"))

if __name__ == "__main__":
    unittest.main()