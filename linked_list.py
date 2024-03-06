from typing import Any, Iterable
import sys


class Node:
    def __init__(self, e):
        self.value = e
        self.next = None


class LinkedList:
    """A simple implementation of a linked list."""

    def __init__(self, iterable: Iterable = None) -> None:
        self.head = None
        self.tail = None
        if iterable:
            self.extend(iterable)

    def append(self, e: Any) -> None:
        '''Append object to the end of the list.'''
        new_node = Node(e)
        if not self.head:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node

    def extend(self, iterable: Iterable) -> None:
        '''Extend list by appending elements from the iterable.'''
        for e in iterable:
            self.append(e)

    def pop(self, index: int = -1) -> Any:
        '''Remove and return item at index (default last).

        Raises IndexError if list is empty or index is out of range'''
        size = len(self)

        if index < 0:
            index += size

        if index < 0 or index >= size:
            raise IndexError("Index {index} exceeds list length {size}.")

        curr = self.head
        i = 0
        while i < index:
            curr = curr.next
            i += 1
        self.remove(curr.value)

    def index(self, e: Any, start=0, stop=sys.maxsize) -> int:
        '''Return first index of value.

        Raises ValueError if the value is not present.'''
        curr = self.head
        i = 0

        while curr and i < start:
            curr = curr.next
            i += 1

        while curr and i < stop:
            if curr.value == e:
                return i
            curr = curr.next
            i += 1

        return -1

    def insert(self, index, e: Any) -> None:
        '''Insert object before index.'''
        new_node = Node(e)

        # insert at begining
        if index <= 0:
            new_node.next = self.head
            self.head = new_node
            return

        # insert at end
        if index >= len(self):
            self.tail.next = new_node
            self.tail = new_node
            return

        # insert between
        curr = self.head
        i = 0
        while i < index - 1:
            i += 1
            curr = curr.next
        new_node.next = curr.next
        curr.next = new_node

    def remove(self, e: Any) -> None:
        '''Remove first occurrence of value.

        Raises ValueError if the value is not present.'''
        if not self.head:
            raise ValueError(f"{e} not found: list is empty")

        if self.head.value == e:
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next
            return

        curr = self.head
        while curr.next and curr.next.value != e:
            curr = curr.next

        if not curr.next:
            raise ValueError(f"{e} not found in the list")

        curr.next = curr.next.next

    def sort(self, reverse: bool = False, key=None) -> None:
        '''Sort the list in ascending order and return None.

        The sort is in-place (i.e. the list itself is modified) and stable (i.e. the order of two equal elements is maintained).

        If a key function is given, apply it'''
        if not self.head or not self.head.next:
            return

        swapped = True
        while swapped:
            swapped = False
            curr = self.head
            prev = None

            while curr and curr.next:
                if key:
                    curr_value = key(curr.value)
                    next_value = key(curr.next.value)
                else:
                    curr_value = curr.value
                    next_value = curr.next.value

                if (curr_value > next_value and not reverse) or (curr_value < next_value and reverse):
                    if prev:
                        prev.next, curr.next.next, curr.next = curr.next, prev.next, curr.next.next
                    else:
                        self.head, curr.next.next, curr.next = curr.next, self.head, curr.next.next
                    swapped = True

                prev, curr = curr, curr.next

    def reverse(self) -> None:
        '''Reverse the list in-place.'''
        prev = None
        curr = self.head

        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        self.head = prev

    def __iter__(self) -> Iterable[Any]:
        self.curr = self.head
        return self

    def __next__(self) -> tuple[int, Any]:
        if self.curr:
            e = self.curr.value
            self.curr = self.curr.next
            return e
        raise StopIteration

    def __len__(self) -> int:
        i = 0
        curr = self.head
        while curr:
            i += 1
            curr = curr.next
        return i

    def __str__(self) -> str:
        if not self.head:
            return ''

        result = str(self.head.value)
        curr = self.head.next
        while curr:
            result += f' -> {curr.value}'
            curr = curr.next

        return result

    def __contains__(self, e: Any) -> bool:
        curr = self.head
        while curr:
            if curr.value == e:
                return True
            curr = curr.next
        return False
