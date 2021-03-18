class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            newnode = Node(data)
            self.head = newnode
            self.head.prev = None
        else:
            newnode = Node(data)
            currnode = self.head
            while currnode.next:
                currnode = currnode.next
            currnode.next = newnode
            newnode.prev = currnode
            newnode.next = None

    def prepend(self, data):
        if self.head is None:
            return
        else:
            curnode = self.head
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode
            curnode.prev = newnode

    def print_list(self):
        currnode = self.head
        while currnode:
            print(currnode.data)
            currnode = currnode.next

    def length(self):
        if self.head is None:
            return 0
        curnode = self.head
        count = 1
        while curnode.next:
            curnode = curnode.next
            count = count + 1

        return count

    def insert_at_index(self, position, data):
        if self.head is None:
            return
        newnode = Node(data)
        cur_node = self.head
        count = 1
        while cur_node and count < position:
            prev = cur_node
            cur_node.prev = prev
            cur_node = cur_node.next
            count = count + 1
        prev.next = newnode
        newnode.next = cur_node
        newnode.prev = prev
        cur_node.prev = newnode

    def rotate_left(self, position):
        if self.head is None:
            return
        prev = None
        p = self.head
        q = self.head
        count = 0
        while p and count < position:
            prev = p
            p.prev = prev
            p = p.next
            q.prev = prev
            q = q.next
            count = count + 1
        p = prev

        while q:
            prev = q
            q.prev = prev
            q = q.next
        q = prev
        q.next = self.head
        self.head = p.next
        self.head.prev = q
        p.next = None

    def delete_node(self, node_to_deleted):
        if self.head is None:
            return
        prev = None
        curr_node = self.head
        if self.head.next is None and self.head.data == node_to_deleted:
            self.head = self.head.next
            self.head = None
            return

        while curr_node and curr_node.data != node_to_deleted:
            prev = curr_node
            curr_node.prev = prev
            curr_node = curr_node.next
        prev.next = curr_node.next
        curr_node.next = prev
        curr_node = None

    def delete_at_an_index(self, index):
        if self.head is None:
            return
        prev = None
        curr_node = self.head
        if self.head.next is None and index == 1:
            self.head = self.head.next
            self.head = None
            return
        count = 1
        while curr_node and count < index:
            prev = curr_node
            curr_node.prev = prev
            curr_node = curr_node.next
            count += 1
        prev.next = curr_node.next
        curr_node.next = prev
        curr_node = None

    def remove_duplicates(self):
        cur_node = self.head
        l = dict()
        while cur_node:
            if cur_node not in l:
                l[cur_node.data] = 1
                cur_node = cur_node.next
            else:
                nxt = cur_node.next
                self.delete_node(cur_node)
                cur_node = nxt


l = DoublyLinkedList()
l.append("A")
l.append("A")
l.append("B")
l.append("B")
l.append("C")
l.append("D")
l.append("D")
l.append("E")
l.append("A")
l.remove_duplicates()
l.print_list()
