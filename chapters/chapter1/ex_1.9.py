### STRING ROTATION ###
# You may use isSubstring function to check if one str is
# a substr of the other

import unittest

def isSubstring(s1: str, s2: str) -> bool:
    pass

def is_rotated(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    s1s1 = s1 + s1
    return isSubstring(s1s1, s2)


if __name__ == "__main__":
    pass