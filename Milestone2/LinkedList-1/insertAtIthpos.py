from os import *
from sys import *
from collections import *
from math import *

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def insert(head, n, pos, val):
    # Write your code here.
    if pos<0 or pos>n:
        return head
    newNode = Node(val)
    curr = head
    prev = None
    count = 0
    while count < pos:
        prev = curr
        curr = curr.next
        count +=1
    newNode = Node(val)
    if prev is None:
        head = newNode
    else:
        prev.next = newNode
    newNode.next = curr
    return head
