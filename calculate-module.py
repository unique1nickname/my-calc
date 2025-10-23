class DLLNode:
    def __init__(self, value=None, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

class DLL:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = DLLNode(value=value)
        else:
            walk = self.head
            while walk.next is not None:
                walk = walk.next
            walk.next = DLLNode(value=value)

    def getList(self):
        result = list()
        walk = self.head
        while walk.next is not None:
            result.append(walk.value)
            walk = walk.next
        return result
    
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
        first_step = '^'
        second_step = '*/'
        third_step = '+-'
        
        temp_data = tuple()

        for i in range(1, len(data)-1):
            if data[i] in first_step:
                result = self.doMath(data[i-1], data[i+1], data[i])
                
            pass

    def doMath(self, num1, num2, operator):
        match operator:
            case '^':
                return pow(num1, num2)
            case '*':
                return num1*num2
            case '/':
                return num1/num2
            case '+':
                return num1+num2
            case '-':
                return num1-num2
            

def main():
    # print('0.3'.isdigit())
    a = Calc()
    print(a.parsingData(""))
    print(float('2.'))
    pass

if __name__ == "__main__":
    main()