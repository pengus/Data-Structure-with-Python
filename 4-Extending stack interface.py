
#python3
import sys

class MaxValue():
    def __init__ (self, value=None):
        self.value = value

class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.max_value = []
        
    def Push(self, a):
        self.__stack.append(a)
        if self.max_value :
            if a >= self.max_value[-1].value:
                self.max_value.append(MaxValue(a))
                return True
            else:
                self.max_value.append(MaxValue(self.max_value[-1].value))
                return True
        self.max_value.append(MaxValue(a))

    def Pop(self):
        assert(len(self.__stack))
        self.__stack.pop()
        self.max_value.pop()


    def Max(self):
        assert(len(self.__stack))
        return self.max_value[-1].value


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
