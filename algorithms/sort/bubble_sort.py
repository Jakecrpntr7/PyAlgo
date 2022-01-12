###
# Implements Bubble sort in Python
# Bubble sort is an academic sorting algorithm that is often taught as a starting point for learning
# about sorting algorithms. It is too slow to actually use in production.
# Time Complexity O(N^2)
def bubble_sort(data: list, comparator=lambda a, b: a > b) -> None:
    """
    Bubble sort works by 'Bubbling' the largest value to the end of the array.
    Example data:    7   3   1
    Outer Loop Iteration 1:
        Inner Loop Iteration 1:
                7 <-> 3 1 -> 3  7   1
        Inner Loop Iteration 2:
                3   7 <-> 1 ->  3 1 7
    Outer Loop Iteration 2:
        Inner Loop Iteration 1:
            3 <-> 1 7 -> 1 3 7
    Result: 1 3 7
    :param data: List to be sorted.
    :param comparator: Comparison function to determine sort direction.
    :return: None. Side effect that array is sorted.
    """
    array_length = len(data)
    # At each iteration of outer loop, all elements at indices greater than i are sorted.
    for i in range(array_length):
        # Inner loop bubbles largest value into position i.
        for j in range(0, array_length - i - 1):
            if comparator(data[j], data[j + 1]):
                # Swap values if value is larger than the value to the right.
                data[j], data[j + 1] = data[j + 1], data[j]
