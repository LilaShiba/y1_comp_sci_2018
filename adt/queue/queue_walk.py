# First in Frist out
class Queue():
    # init
    def __init__(self):
        self.items = []

    #enqueue
    def enqueue(self, item):
        # insert(index, item)
        # if insert is always at index 0
        # then first item gets pushed to back
        # niccce
       return self.items.insert(0,item)

    #deqeue
    def dequeue(self):
        return self.items.pop()

    #show all
    def list(self):
        for x in self.items:
            print(x)

# q is an instance of class Queue
# q is of type Queue
q=Queue()
# adding to the queue
q.enqueue('cat')
q.enqueue('dog')
# debug, see list before dequeue
print("this is poped ")
print(q.dequeue())
# debug, see list after the dequeue
q.list()
