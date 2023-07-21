import pytest
from src import stack


def test_node():
    n1 = stack.Node("hello", None)
    n2 = stack.Node(10, n1)

    assert n1.data == "hello"
    assert n2.data == 10
    assert n1 == n2.next_node


def test_constructor():
    stack_test = stack.Stack()
    assert stack_test.top is None


def test_push():
    stack_test = stack.Stack()
    stack_test.push('data1')
    stack_test.push('data2')
    stack_test.push('data3')

    assert stack_test.top.data == "data3"
    assert stack_test.top.next_node.data == "data2"
    assert stack_test.top.next_node.next_node.data == "data1"
    assert stack_test.top.next_node.next_node.next_node is None
    with pytest.raises(AttributeError):
        stack_test.top.next_node.next_node.next_node.data


def test_pop():
    stack_test = stack.Stack()
    stack_test.push('data1')
    data = stack_test.pop()

    assert stack_test.top is None
    assert data == 'data1'


def test_str():
    stack_test = stack.Stack()
    assert str(stack.Stack()) == ""

    stack_test.push('data1')
    stack_test.push('data2')
    stack_test.push('data3')

    assert str(stack_test) == "data3 data2 data1 "
