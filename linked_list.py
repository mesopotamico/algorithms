class Node:
    data = None
    next_node = None 

    def __init__(self,data):
        self.data = data
    
    def __repr__(self):
        return "<Node data: %s>" %self.data


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0

        while current:
            count += 1 
            current = current.next_node

        return count
    
    def search(self,key):
        current = self.head

        while current:
            if current.data == key:
                return current
            current = current.next_node

        return None

    def add(self,data):
       #Adds new node at head
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node


    def insert(self,data,index):
        if index == 0:
            self.add = data

        if index > 0:
            new = Node(data)
            position = index
            current = self.head

        while position > 1:
            current = current.next_node
            position -= 1

        prev = current
        next = current.next_node

        prev.next_node = new
        new.next_node = next

    def remove(self,key):
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True 
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
    
            previous = current
            current = current.next_node

        return current

    def __repr__(self):
        
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append(f"[Head : {current.data}]")
            elif current.next_node is None:
                nodes.append(f"[Tail : {current.data}]")
            else:
                nodes.append(f"[{current.data}]")
            
            current = current.next_node

        return '->'.join(nodes)

def main():
    l = LinkedList()
    for i in range(0,15):
        l.add(i)
    
    print(l)
    data_delete = int(input())
    print(l.remove(data_delete))
    print(l)

main()
