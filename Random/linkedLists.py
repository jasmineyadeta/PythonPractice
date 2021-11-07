class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def append(self, data):
        new_node = Node(data)

        if self.head is None: # first thing we want to do is check if the list is empty
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data): #add node to the beginning of the list
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        #check if previous node exists
        if not prev_node:
            print ("Previous node is not in the list")
            return

        new_node = Node(data) # make the new node
        new_node.next = prev_node.next # the new node needs to point to where the previous node pointed to
        prev_node.next = new_node #the previous node needs to point to new node

    def delete_node(self, key):
        current_node = self.head # store head node

        if current_node is not None: # check to make current node is active
            if (current_node.data == key): # check to see if the node passed holds the key to be deleted
                self.head = current_node.next # setting the next head
                current_node = None # deleting the current node
                return

        # Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        while (current_node is not None):
            if current_node.data == key:
                break
            prev = current_node
            current_node = current_node.next

        # if key was not present in linked list
        if (current_node == None):
            return

        # Unlink the node from linked list
        prev.next = current_node.next

        current_node = None

    def delete_node_position(self, position):
        if self.head == None: # check if the linked list is empty
            return

        current_node = self.head #store the head node

        if position == 0: # check if the head is to be removed
            self.head = current_node.next # set the head as the next available
            current_node = None # deletion
            return

        for i in range(position -1): #find previous node of the node to be deleted
            current_node = current_node.next # set the next
            if current_node is None: # check if that node is null
                break

        if current_node is None: #if position is more than the number of nodes and doesn't exist
            return
        if current_node.next is None: #if no next exists
            return

        next_node = current_node.next.next # current node.next is the one we need to delete, so store the next pointer of the one to be deleted
        current_node.next = None # unlink the node from the linked list
        current_node.next = next_node


# activities
ll = LinkedList()
print ("This is my full linked list: ")
ll.append("Bottom")
ll.append("Boots")
ll.append("with the fur")
ll.prepend("Apple")
ll.insert_after_node(ll.head.next, "Jeans")
ll.print_list()
print ("This is my linked list post deletion + added extra: ")
ll.delete_node("Jeans")
ll.prepend("Apple")
ll.print_list()
print ("This is my linked list post deletion at position: ")
ll.delete_node_position(1)
ll.print_list()