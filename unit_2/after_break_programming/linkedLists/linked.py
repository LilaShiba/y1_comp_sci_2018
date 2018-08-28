# Create nodes
# Create linked list
# Add nodes to linked list
# Print linked list

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def insert(self, newNode):
		if self.head is None:
			self.head = newNode
		else:
			# head => Estelle -> Ben -> Matthew
			lastNode = self.head
			while True:
				if lastNode.next is None:
					break
				lastNode = lastNode.next
			lastNode.next = newNode

	def printList(self):
		# firstNode.data => Estelle, firstNode.next => none
		currentNode = self.head
		while True:
			if currentNode is None:
				break
			print(currentNode.data)
			currentNode = currentNode.next


firstNode = Node("Estelle")
linkedList = LinkedList()
linkedList.insert(firstNode)
secondNode = Node("Ben")
linkedList.insert(secondNode)
thirdNode = Node("Matthew")
linkedList.insert(thirdNode)
linkedList.printList()