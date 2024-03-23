class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return None
        result = self.stack.pop()
        return result

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def size(self):
        return len(self.stack)


if __name__ == '__main__':

    while True:
        line_under_test = input('Введите строку для проверки сбалансированности скобок (Выход-[ENTER]):')

        if len(line_under_test) == 0:
            break

        stack = Stack()
        opposite = {']': '[', '}': '{', ')': '('}

        try:
            for char in line_under_test:
                if char in '[{(':
                    stack.push(char)
                if char in ']})':
                    assert stack.pop() == opposite[char]
        except AssertionError:
            print('Строка несбалансирована')
            continue

        print('Строка сбалансирована')
