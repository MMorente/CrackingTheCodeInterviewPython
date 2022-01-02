### Return Kth to last element. Suppose we don't know the size of the list. ###

import __init__
import unittest
from utils import LinkedList, Node

def find_kth(ListNode: Node, pos: int) -> Node:
    if not ListNode:
        return 0
    
    idx = find_kth(ListNode.next, pos) + 1
    if (idx == pos):
        print(f"{pos}th to last node is {ListNode.data}")
    return idx

def find_kth_v2(ListNode: Node, pos: int) -> Node:
    class Index:
        index = 0

    def find_kth_element(ListNode: Node, pos: int, i: Index) -> Node:
        if not ListNode:
            return None
        
        nd = find_kth_element(ListNode.next, pos, i)
        i.index += 1
        if i.index==pos:
            return ListNode
        return nd

    return find_kth_element(ListNode, pos, Index())

def find_kth_iter(ListNode: Node, pos: int) -> Node:
    p1 = ListNode
    p2 = ListNode

    for _ in range(pos):
        if not p1:
            return None
        p1 = p1.next

    while (p1 != None):
        p1 = p1.next
        p2 = p2.next

    return p2

if __name__ == "__main__":
    test = LinkedList(0)
    test.append(2)
    test.append(3)
    test.append(4)
    test.append(5)
    test.append(6)
    test.append(7)
    test.append(8)
    test.append(9)
    test.append(10)
    test.append(11)

    sol = find_kth(test._head, 5)
    sol2 = find_kth_v2(test._head, 5)
    print(sol2)
    sol3 = find_kth_iter(test._head, 5)
    print(sol3)