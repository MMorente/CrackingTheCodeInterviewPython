class Node:
    def __init__(self, data):
        self._data = data
        self.next = None

    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, value):
        self._data = value
    
    def __repr__(self):
        return f"Node with value {self.data}"

class LinkedList:
    def __init__(self, data):
        self._head = Node(data)
        self.__size = 1
    
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.__size = size

    def append(self, data):
        new = Node(data)
        last = self._head
        
        while(last.next):
            last = last.next
        last.next = new
        self.__size += 1

    def __len__(self):
        return self.__size

    def __repr__(self):
        current_node = self._head
        output = list()
        while(current_node != None):
            output.append(str(current_node.data))
            current_node = current_node.next
        
        return "-".join(output)

    def __eq__(self, other):
        if len(self) != len(other):
            return False
            
        current_node = self._head
        other_node = other._head
        
        while(current_node != None):
            if current_node.data != other_node.data:
                return False
            else:
                current_node = current_node.next
                other_node = other_node.next
        
        return True
