class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.LRU = None
        self.MRU = None
        self.map = {}
        self.capacity = capacity
        self.currentCapacity = 0

    def get(self, key:int) -> int:
        print(f"get key:{key}")
        if key not in self.map:
            self.printLinkedList()
            return -1
        value = self.map[key].value
        # don't need to do anything if the key is already the most recently used node
        if self.map[key] == self.MRU:
            print(f"get: map[{key}]={value} is MRU")
            
        elif self.map[key] == self.LRU:
            nodeToMove = self.map[key]
            nextNode = nodeToMove.next
            self.LRU = nextNode
            nextNode.prev = None
            self.makeMRU(nodeToMove)
        else:
            nodeToMove = self.map[key]
            prevNode = nodeToMove.prev
            nextNode = nodeToMove.next
            prevNode.next = nextNode
            nextNode.prev = prevNode
            self.makeMRU(nodeToMove)
        self.printLinkedList()
        return value
     

    def put(self, key:int, value:int) -> None:
        print(f"put key:{key} value:{value}")
        # if key exists
        if key in self.map:
            self.map[key].value = value
            # update the linked list
            # don't need to do anything if the key is already the most recently used node
            if self.map[key] == self.MRU:
                return
            elif self.map[key] == self.LRU:
                nodeToMove = self.map[key]
                self.LRU = nodeToMove.next
                self.LRU.prev = None
                self.makeMRU(nodeToMove)
            else:
                nodeToMove = self.map[key]
                prevNode = nodeToMove.prev
                nextNode = nodeToMove.next
                prevNode.next = nextNode
                nextNode.prev = prevNode
                self.makeMRU(nodeToMove)

        # if key doesn't exist
        else:
            # first node in the cache
            if not self.LRU and not self.MRU and self.currentCapacity==0:
                newNode = Node(key,value)
                self.LRU = newNode
                self.MRU = newNode
                self.map[key] = newNode
                self.currentCapacity += 1
                print(f'first node in the cache')
            else:
                # not the first node
               
                if self.currentCapacity != self.capacity:
                    newNode = Node(key, value)
                    self.map[key] = newNode
                    self.currentCapacity += 1
                    self.makeMRU(newNode)
                # cache is at capacity
                else:
                    #remove the LRU node for this new node
                    if self.LRU == self.MRU:
                        self.map.pop(self.LRU.key)
                        newNode = Node(key, value)
                        self.map[key] = newNode
                        self.LRU = newNode
                        self.MRU = newNode
                    else:
                        oldLRU = self.LRU
                        self.map.pop(oldLRU.key)
                        self.LRU = oldLRU.next
                        self.LRU.prev = None
                        newNode = Node(key, value)
                        self.map[key] = newNode
                        self.makeMRU(newNode)
        self.printLinkedList()
    

    def makeMRU(self, node):
        oldMRU = self.MRU
        oldMRU.next=node
        node.prev = oldMRU
        node.next = None
        self.MRU = node
    
    def printLinkedList(self):
        node = self.LRU
        while node:
            print(f"({node.key}, {node.value})")
            node = node.next