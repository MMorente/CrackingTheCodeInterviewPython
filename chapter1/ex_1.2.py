### Check if one string is a permutation of the other ###

import unittest

def is_permutation(a: str, b: str) -> bool:
    a, b = a.strip(), b.strip()

    if len(a) != len(b):
        return False

    return sorted(a) == sorted(b) #O(n*log(n))

def is_permutation_v2(a: str, b: str) -> bool:
    a, b = a.strip(), b.strip()
        
    if len(a) != len(b):
        return False
    
    letters = dict()
    for letter in a:
        letters[letter] = 1

    for letter in b:
        try:
            letters[letter] -= 1
            if letters[letter] < 0:
                return False
        except KeyError:
            return False
    
    return True #O(n)



class TestPermuts(unittest.TestCase):
    
    def test_asserts_v1(self):
        self.assertTrue(is_permutation("abcd", "acdb"))
        self.assertFalse(is_permutation("abcd", "acde"))
        self.assertFalse(is_permutation("abcd", "acdbe"))
        self.assertTrue(is_permutation("a", "a"))

    def test_asserts_v2(self):
        self.assertTrue(is_permutation_v2("abcd", "acdb"))
        self.assertFalse(is_permutation_v2("abcd", "acde"))
        self.assertFalse(is_permutation_v2("abcd", "acdbe"))
        self.assertTrue(is_permutation_v2("a", "a"))

if __name__ == "__main__":
    unittest.main()

