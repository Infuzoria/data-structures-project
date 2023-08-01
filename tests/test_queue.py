import pytest
from src import queue


def test_node():
    n2 = queue.Node(10, None)
    n1 = queue.Node("hello", n2)

    assert n1.data == "hello"
    assert n2.data == 10
    assert n1.next_node == n2


def test_constructor():
    queue_test = queue.Queue()
    assert queue_test.head is None
    assert queue_test.tail is None


def test_enqueue():
    queue_test = queue.Queue()
    queue_test.enqueue('data1')
    queue_test.enqueue('data2')
    queue_test.enqueue('data3')

    assert queue_test.head.data == 'data1'
    assert queue_test.head.next_node.data == 'data2'
    assert queue_test.tail.data == 'data3'
    assert queue_test.tail.next_node is None


def test_dequeue():
    queue_test = queue.Queue()
    queue_test.enqueue('data1')
    queue_test.enqueue('data2')
    queue_test.enqueue('data3')

    assert queue_test.dequeue() == "data1"
    assert queue_test.dequeue() == "data2"
    assert queue_test.head.data == "data3"
    queue_test.dequeue()
    assert queue_test.dequeue() is None


def test_str():
    queue_test = queue.Queue()
    assert str(queue.Queue()) == ""

    queue_test.enqueue('data1')
    queue_test.enqueue('data2')
    queue_test.enqueue('data3')
    assert str(queue_test) == "data1\ndata2\ndata3"
