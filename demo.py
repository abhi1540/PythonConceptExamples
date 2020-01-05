#
# lst = [1, 2, 3, 4]
#
# fun = list(map(lambda x:x**2, lst))
# print(fun)
#
# a = [i**2 for i in lst]
# print(a)
#
#
# print(list(filter(lambda x: x > 2, lst)))
# take second element for sort


# import pandas as pd
# raw_data = {'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'],
#         'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd','1st', '1st', '2nd', '2nd'],
#         'name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze', 'Jacon', 'Ryaner', 'Sone', 'Sloan', 'Piger', 'Riani', 'Ali'],
#         'preTestScore': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
#         'postTestScore': [25, 94, 57, 62, 70, 25, 94, 57, 62, 70, 62, 70]}
# df = pd.DataFrame(raw_data, columns = ['regiment', 'company', 'name', 'preTestScore', 'postTestScore'])
#
# import numpy as np
# x = np.ones((5,5))
# print("Original array:")
# print(x)
# print("1 on the border and 0 inside in the array")
# x[1:-1, 1:-1] = 0
# print(x)

class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):

    def __init__(self):
            self.head = None
            self.size = 0


    def insertStart(self, data):

        newNode = Node(data)
        self.size += 1
        if not self.head:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def traverseList(self):

        actualNode = self.head;

        while actualNode is not None:
            print("%d " % actualNode.data);
            actualNode = actualNode.next;


    def reverse(self):

        first = self.head
        second = first.next
        third = second.next
        first.next = None
        second.next = first

        if self.head:
            while third is not None:
                first = second
                second = third
                third = third.next
                second.next = first

            self.head = second


obj = LinkedList()
for i in [2, 3, 4, 5]:
    obj.insertStart(i)

obj.traverseList()
#obj.head.next.next = obj.head.next

obj.reverse()

obj.traverseList()


























