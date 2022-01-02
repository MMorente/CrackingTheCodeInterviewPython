### REMOVE DUPLICATES FROM UNSORTED LINKED LIST ###

import sys
import os
sys.path.append(os.path.join(os.getcwd(), ".."))

import unittest
from utils import LinkedList, Node


def remove_duplicates(ll: LinkedList) -> LinkedList:
    unique_vals = set()
    current_node = ll._head
    previous = Node(None)
    while(current_node != None):
        if current_node.data in unique_vals:
            previous.next = current_node.next
        else:
            unique_vals.add(current_node.data)
            previous = current_node
        
        current_node = current_node.next

    return ll


class TestRemoveDuplicates(unittest.TestCase):

    def test_example(self):
        #input linkedlist
        ll = LinkedList(0)
        ll.append(1)
        ll.append(4)
        ll.append(3)
        ll.append(2)
        ll.append(1)
        ll.append(3)
        ll.append(0)
        ll.append(3)
        #output linkedlist (correct)
        ll_sol = LinkedList(0)
        ll_sol.append(1)
        ll_sol.append(4)
        ll_sol.append(3)
        ll_sol.append(2)
        #output linkedlist (incorrect)
        ll_sol2 = LinkedList(0)
        ll_sol2.append(1)
        ll_sol2.append(4)
        ll_sol2.append(3)
        ll_sol2.append(11)

        self.assertEqual(ll_sol, remove_duplicates(ll))
        self.assertNotEqual(ll_sol2, remove_duplicates(ll))

if __name__ == "__main__":
    unittest.main()