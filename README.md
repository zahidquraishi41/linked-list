# Linked List

This is a basic implementation of a linked list in Python. The `LinkedList` class provides common methods for manipulating linked lists, similar to the built-in Python list.

## Usage

```python
# Example Usage:

from linkedlist import LinkedList

# Create a linked list
my_list = LinkedList([1, 2, 3, 4])

# Append an element
my_list.append(5)

# Remove an element
my_list.remove(3)

# Print the linked list
print(my_list)
```

## Methods

- **`append(e: Any) -> None`**: Append an element to the end of the list.
- **`extend(iterable: Iterable) -> None`**: Extend the list by appending elements from an iterable.
- **`pop(index: int = -1) -> Any`**: Remove and return an item at the specified index (default is the last element).
- **`index(e: Any, start=0, stop=sys.maxsize) -> int`**: Return the first index of a value.
- **`insert(index, e: Any) -> None`**: Insert an object before the specified index.
- **`remove(e: Any) -> None`**: Remove the first occurrence of a value.
- **`sort(reverse: bool = False, key=None) -> None`**: Sort the list in ascending order.
- **`reverse() -> None`**: Reverse the list in-place.

Feel free to clone or fork this repository to use the linked list in your Python projects.
