
class Element():
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

class Sequence():
    def __init__(self):
        self.head = None
        self.tail = None
    
    def print_(self):
        init = self.head
        printer =[]
        while init != None:
            printer.append(init.value)
            init = init.next
        print(printer)
        return printer

    def append_ (self, value):
        
        if self.head != None:
            node = Element(value)
            node.prev = self.tail
            self.tail.next = node
            
            self.tail = node 
        else: 
            node = Element(value)
            self.head = node
            self.tail = node

    def leftappend_(self, value):
        if self.head != None:
            node = Element(value)
            node.next = self.head
            self.head.prev = node
            self.head = node
        else: 
            node = Element(value,None)
            self.head = node
            self.tail = node

    def pop_ (self):
        if self.tail.prev != None:
            self.tail.prev.next = None
        else:
           self.head = None
        self.tail = self.tail.prev

    def leftpop_(self):        
        if self.head.next != None:
            self.head = self.head.next
            self.head.prev = None
        else:
            self.tail = None
            self.head = None
        
      
    def is_not_empty(self):
        if self.head == None :
            return False 
        return True

    def give_item(self, index):

        if index >= 0 :
            counter = 1
            temp = self.head   
            while self.is_not_empty() and counter <= index:
                temp = temp.next
                counter += 1
            return temp.value
        else:
            temp = self.tail
            counter = -1
            while self.is_not_empty() and counter > index:
                temp = temp.prev
                counter -=1
            return temp.value

def max_sliding_window(sequence, m):
    maximums = []
    deq = Sequence()
    for i in range(m):

        while deq.is_not_empty() and sequence[deq.give_item(-1)] <= sequence[i]:
            deq.pop_()
        deq.append_(i)

    for j in range(m,len(sequence)):
        print(str(sequence[deq.give_item(0)]) + " ", end = "")

        while deq.is_not_empty() and deq.give_item(0) < j-i:
            deq.leftpop_()
        while deq.is_not_empty() and sequence[deq.give_item(-1)] <= sequence[j]:
            deq.pop_()
        deq.append_(j)
    print(str(sequence[deq.give_item(0)]))

        

if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())
    max_sliding_window(input_sequence,window_size)


    #s = Sequence()
    #s.append_(1)
    #s.leftpop_()
    ##s.append_(1)
    ##s.append_(1)
    ##s.append_(1)
    ##s.append_(1)
    ##s.append_(1)
    ##s.append_(1)
    ##s.print_()
    ##s.pop_()
    ##s.pop_()
    #s.print_()
    ##s.pop_()
    ##s.pop_()
    ##s.pop_()
    ##s.pop_()


