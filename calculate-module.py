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


class Calc:
    def __init__(self):
        pass

    def calc(data):
        pass

    def parsingData(self, data: str) -> list:   # возвращает список из элементов выражения
        operations = '+-*/^'
        parsedData = DLL()
        part = ''

        # в элементе может быть 1 точка
        # выражение не может состоять только из точки или быть пустым
        # операторы не могут стоять рядом
        # и ими не может заканчиваться или начинаться выражение
        for i in range(len(data)): 
            if data[i].isdigit():
                part += data[i]
            elif data[i] == '.' and '.' not in part:
                part += data[i]
            elif data[i] in operations and part not in ('', '.') and i != len(data) - 1:
                parsedData.append(part)
                parsedData.append(data[i])
                part = ''
            else:
                return "Invalid syntax"
        if part in ('', '.'):
            return "Invalid syntax" 
        parsedData.append(part)

        return parsedData

    def getResult(self, data):
        steps = ('^', '*/', '+-')

        if data.getLen() > 1:
            for step in steps:
                i = 1
                dataLen = data.getLen()
                while i < dataLen:
                    if data.get(i) in step:
                        result = self.doMath(data.get(i-1), data.get(i+1), data.get(i))
                        data.insertMathResult(i, result)
                        dataLen = data.getLen()
                        i = 0
                    i += 1

        return data.head.value

    def doMath(self, num1, num2, operator):
        num1 = float(num1)
        num2 = float(num2)
        match operator:
            case '^':
                return pow(num1, num2)
            case '*':
                return str(num1*num2)
            case '/':
                return str(num1/num2)
            case '+':
                return str(num1+num2)
            case '-':
                return str(num1-num2)
            

def main():
    # print('0.3'.isdigit())
    a = Calc()
    data = a.parsingData("3^2*3/3+1-5")
    print(data)
    if data != "Invalid syntax":
        print(a.getResult(data=data))

if __name__ == "__main__":
    main()