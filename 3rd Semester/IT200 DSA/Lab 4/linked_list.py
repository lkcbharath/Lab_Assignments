class LinkedList:
    """Defines a Singly Linked List.

    attributes: head
    """
    
    def __init__(self):
        """Create a new list with a Sentinel Node"""
        self.head = ListNode()

    def insertLL(self,x,pos):
        """Insert element x in the position after pos"""
        new = ListNode()
        new.value = x
        new.next = pos.next
        pos.next = new

    def deleteLL(self,pos):
        """Delete the node following node pos in the linked list."""
        pos.next = pos.next.next

    def printLL(self):
        """ Print all the elements of a list in a row."""
        temp = self.head
        while temp.next!=None:
            temp = temp.next
            print(temp.value, end= ' ')
        print("")

    def insertAtIndexLL(self,x,i):
        """Insert value x at list position i. (The position of the first element is taken to be 0.)"""
        temp = self.head

        for j in range(0,i):
            if temp.next==None:
                return 1
            temp = temp.next

        new = ListNode()
        new.value = x
        new.next = temp.next
        temp.next = new


    def searchLL(self, x):
        """Search for value x in the list. Return a reference to the first node with value x; return None if no such node is found."""
        temp = self.head
        
        while temp.next!=None:
            temp = temp.next
            if x == temp.value:
                return "Found"       

        return "Not Found"

    def searchLLHash(self, x):
        """Search for value x in the list. Return a reference to the first node with value x; return None if no such node is found."""
        temp = self.head
        result = []
        while temp.next!=None:
            temp = temp.next
            if x == temp.value:
                result.append(temp.value)
        return result          


    def lenLL(self):
        """Return the length (the number of elements) in the Linked List."""
        count = 0
        temp = self.head
        while temp.next!=None:
            count += 1
            temp = temp.next
        return(count)

    def isEmptyLL(self):
        """Return True if the Linked List has no elements, False otherwise."""
        if self.head.next == None:
            return True
        return False


class ListNode:
    """Represents a node of a Singly Linked List.

    attributes: value = hashed value, next, key = our string(NOT IN CURRENT EXAMPLE)
    """
    def __init__(self,valuex=None,nxt=None):
        self.value = valuex
        self.next = nxt