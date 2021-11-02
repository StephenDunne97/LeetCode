class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
# Initialize LinkedList
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node3

# Put all values from LinkedList into a single string
current = node1
number = ""
valid = True

while valid is not False:
    if current.next is None:
        number = str(current.data) + number
        valid = False
    else:
        number = str(current.data) + number
        current = current.next

# Create LinkedList from string
head = None
for x in number: 
    if head is None:
        head = Node(x)
        current = head
    else:
        current.next = Node(x)
        current = current.next


# Traverse LinkedList and append values to a list
valid = True
current = head
output = []
while valid is not False:
    if current.next is None:
        output.append(current.data)
        valid = False
    else:
        output.append(current.data)
        current = current.next

print(output)