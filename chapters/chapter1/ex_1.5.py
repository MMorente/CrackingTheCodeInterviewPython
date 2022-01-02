### ONE ARRAY ###

import unittest

def one_replace(s1: str, s2: str) -> bool:
    diffs = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            diffs += 1
            if diffs > 1:
                return False
    
    return True

def one_edit(s1: str, s2: str) -> bool:
    long_str = s1 if len(s1)>len(s2) else s2
    short_str = s1 if len(s1)<len(s2) else s2

    idx1 = idx2 = 0

    while(idx1 < len(short_str) and idx2 < len(long_str)):
        if short_str[idx1] != long_str[idx2]:
            if idx1 != idx2:
                return False
            else:
                idx2+=1
        else:
            idx1 += 1 
            idx2 += 1
    
    return True

def one_away(s1: str, s2: str) -> bool:
    if len(s1) == len(s2):
        return one_replace(s1, s2)
    elif abs(len(s1)-len(s2)) == 1:
        return one_edit(s1, s2)
    else:
        return False


class TestOneAway(unittest.TestCase):

    def test_examples(self):
        self.assertTrue(one_away("ple", "pale"))
        self.assertTrue(one_away("pales", "pale"))
        self.assertTrue(one_away("pale", "bale"))
        self.assertFalse(one_away("pale", "bake"))
        self.assertFalse(one_away("pale", "paleos"))

if __name__ == "__main__":
    unittest.main()