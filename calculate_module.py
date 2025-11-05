from DLL import DLL


SYNTAX_ERROR = 'Invalid syntax'

def calc(data: str):
    if data.isdigit():
        return data
    if data == SYNTAX_ERROR:
        return SYNTAX_ERROR
    finalData = ''
    parenthesesPart = ''
    openingParenthesisCount = 0
    closingParenthesisCount = 0
    for i in data:
        if i == ')':
            closingParenthesisCount += 1
            if openingParenthesisCount == closingParenthesisCount:
                parenthesesResult = calc(parenthesesPart)
                if parenthesesResult == SYNTAX_ERROR:
                    return SYNTAX_ERROR
                if parenthesesResult[0] == '-': # если в ответе из скобок пришло отрицательное число
                    if finalData != '' and finalData[-1] == '+':
                        finalData = finalData[:-1]
                finalData += parenthesesResult
                parenthesesPart = ''
                continue
        if openingParenthesisCount > closingParenthesisCount:
            parenthesesPart += i
        if i == '(':
            openingParenthesisCount += 1
        if openingParenthesisCount == closingParenthesisCount:
            finalData += i

    if openingParenthesisCount > closingParenthesisCount:
        difference = openingParenthesisCount - closingParenthesisCount
        finalData = calc(data + ')'*difference)

    if closingParenthesisCount > openingParenthesisCount:
        return SYNTAX_ERROR
    
    parsedData = __parsingData(finalData)
    if parsedData == SYNTAX_ERROR:
        return SYNTAX_ERROR
    return __getResult(parsedData)
            

def __parsingData(data: str) -> list:   # возвращает список из элементов выражения
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
        elif data[i] in operations and i != len(data) - 1:
            if data[i] == '-' and part == '':   # add 0 before negative number 
                part = 0
            elif part in ('', '.'):
                return SYNTAX_ERROR
            parsedData.append(part)
            parsedData.append(data[i])
            part = ''
        else:
            return SYNTAX_ERROR
    if part in ('', '.'):
        return SYNTAX_ERROR 
    parsedData.append(part)

    return parsedData

def __getResult(data):
    steps = ('^', '*/', '+-')

    if data.getLen() > 1:
        for step in steps:
            i = 1
            dataLen = data.getLen()
            while i < dataLen:
                if data.get(i) in step:
                    result = __doMath(data.get(i-1), data.get(i+1), data.get(i))
                    data.insertMathResult(i, result)
                    dataLen = data.getLen()
                    i = 0
                i += 1

    return data.head.value

def __doMath(num1, num2, operator):
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
    print(calc(input()))
    # print('0.3'.isdigit())
    # print(calc("-10"))                #true
    # print(calc("qwerty"))             #false
    # print(calc("3^(2*3)/3+1-5"))      #true
    # print(calc("(3^(2*3)/3+1-5"))     #true
    # print(calc("3^(2*3)/3+1-5)"))     #false
    # print(calc('3^(2*3)/3+(1-5)'))    #true
    # print(calc("(3^(2*3)/3+(1-5))"))  #true
    # print(calc("(3^(2*3)/3+(1-5)"))   #true
    # print(calc("(3^(2*3)/3+(1-5"))    #true

if __name__ == "__main__":
    main()