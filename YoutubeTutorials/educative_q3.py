#https://www.educative.io/blog/crack-amazon-coding-interview-questions#prepare
# 3. Merge two sorted linked lists
# Assumption: do not have to be of equal length
# goal: merge two sorted linked lists so the resulting merged list is ordered

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def merge_sorted(head1, head2):
    # 1. choose the head of the merged list by comparing the first nodes of each linked list
    # 2. add to merge linked list based off of smaller of the two comparisons
    # NOTE: add a check for lists being empty
    if head1 == None:
        return head2
    elif head2 == None:
        return head1

    merged_head = None
    if head1.data <= head2.data:
        merged_head = head1
        head1 = head1.next
    else:
        merged_head = head2
        head2 = head2.next

    merged_tail = merged_head #maintaining both pointers?

    while head1 != None and head2 != None:
        temp = None # initiatize a temporary variable
        if head1.data <= head2.data:
            temp = head1
            head1 = head1.next
        else:
            temp = head2
            head2 = head2.next

        merged_tail.next = temp #placing the step after the merged tail pointer in temp
        merged_tail = temp # shifting everyones position 1 over

    if head1 !=None: #head one is not null
        merged_tail.next = head1
    elif head2 !=None:
        merged_tail.next = head2

    return merged_head
