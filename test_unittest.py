"""What is unit Testing:"""
"""unit testing is a software testing method by which individual units of 
   source code are tested to determine whether they are fit for use"""

from Functionstobetested import Queue,Product
import pytest
import sys
a_queue = Queue()
prod = Product(10, 10)


a_queue.enqueue(10)
a_queue.enqueue(12)
a_queue.enqueue(14)


def test_queue():
    assert a_queue.dequeue() == 10
    assert a_queue.dequeue() == 12
    assert a_queue.dequeue() == 14


"""You can skip a test case with reason"""
# @pytest.mark.skip(reason="don't execute this")
# def test_prod():
#     assert prod.mul() == 10


# """you can skip when satisfied some condition """
# @pytest.mark.skipif(sys.version_info < (3, 6), reason="don't execute this")
# def test_prod():
#     assert prod.mul() == 100
#     print("-----------Executed Successfully------------")
#
#
# @pytest.mark.parametrize('num1, num2, result',
#                          [
#                              (7, 3, 21),
#                              (10, 12, 120),
#                              (11, 10, 110)
#                          ]
#                          )
# def test_prod1(num1, num2, result):
#     prod = Product(num1, num2)
#     assert prod.mul() == result


