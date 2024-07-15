class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' ')
            current_node = current_node.next
        print()
        
    def to_number(self):
        current_node = self.head
        number = 0
        place = 1
        while current_node:
            number += current_node.data * place
            place *= 10
            current_node = current_node.next
        return number
        
    def from_number(self, number):
        self.head = None
        for digit in str(number)[::-1]:
            self.append(int(digit))
        
    def add(self, other):
        result = LinkedList()
        result.from_number(self.to_number() + other.to_number())
        return result
        
    def subtract(self, other):
        result = LinkedList()
        result.from_number(self.to_number() - other.to_number())
        return result
        
    def multiply(self, other):
        result = LinkedList()
        result.from_number(self.to_number() * other.to_number())
        return result

ll1 = LinkedList()
ll1.from_number(6543)
ll2 = LinkedList()
ll2.from_number(1234)

print("List 1:")
ll1.print_list()
print("List 2:")
ll2.print_list()

print("Addition:")
result_add = ll1.add(ll2)
result_add.print_list()

print("Subtraction:")
result_subtract = ll1.subtract(ll2)
result_subtract.print_list()

print("Multiplication:")
result_multiply = ll1.multiply(ll2)
result_multiply.print_list()
