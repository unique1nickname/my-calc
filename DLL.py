class DLLNode:
    def __init__(self, value=None, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def __repr__(self):
        return self.value

class DLL:
    def __init__(self):
        self.head = None

    def __repr__(self):
        return str(self.getList())

    def append(self, value):
        if self.head is None:
            self.head = DLLNode(value=value)
        else:
            walk = self.head
            while walk.next is not None:
                walk = walk.next
            walk.next = DLLNode(value=value)
            walk.next.prev = walk

    def getList(self):
        result = list()
        walk = self.head
        while walk is not None:
            result.append(walk.value)
            walk = walk.next
        
        return result
    
    def getLen(self):
        if self.head is None:
            return 0
        count = 1
        walk = self.head
        while walk.next is not None:
            count += 1
            walk = walk.next
        return count

    def get(self, i):
        count = 0
        walk = self.head
        while count < i:
            walk = walk.next
            count += 1
        if walk is None:
            return None
        return walk.value 


    def insertMathResult(self, i, result):
        if self.head is None:
            return
        
        walk = self.head
        for _ in range(i):
            walk = walk.next
        walk.value = result
        num1 = walk.prev
        num2 = walk.next
        
        if num1.prev is not None:
            num1.prev.next = walk
        else:
            self.head = walk
        walk.prev = num1.prev
        
        if num2.next is not None:
            num2.next.prev = walk
        walk.next = num2.next

