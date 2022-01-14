##
# Implements Insertion Sort in Python.
# Insertion sort works by starting at the second value (as the first is trivially sorted) and maintaining
# a list to the left of the outer index that is sorted. On each iteration it takes the current value and
# places it in sorted position within the sub-list to the left of the outer index.
# Time Complexity: O(N^2). Runs best on nearly sorted datasets.
def insertion_sort(data: list, comparator=lambda a, b: a > b) -> None:
    """
    Insertion sort works by inserting the current value into the sorted position within
    the left sub-list.
    Ex: 7 3 1 comparator sorting in ascending order.
    Outer Iteration 1:
    Start: 7 3 1
    Place three in sorted position relative to sub-list only containing 7 so move to first position.
    End 3 7 1
    Outer Iteration 2:
    Look at one and shift sub-list to the left until sorted position found.
    Shifts 7 right and 3 right then places in the first position.
    End 1 3 7
    :param data: List to be sorted.
    :param comparator: comparator function to determine how the list should be sorted.
    :return: None. Side effect data is sorted.
    """
    # Items in the list left of outer_index will be in sorted order.
    # Each iteration places the value at position outer_index in sorted position.
    for outer_index in range(1, len(data)):
        # Current Value to place in sorted position relative to left sub-list.
        value = data[outer_index]
        # Pointer to determine where to place value.
        current_position = outer_index
        # As long as the value we are looking to place is larger than the value at the next position.
        while current_position > 0 and comparator(data[current_position - 1], value):
            # Shift the value in the next position right.
            data[current_position] = data[current_position - 1]
            # Update pointer to consider the next value.
            current_position -= 1
        # Place the current value in the position where it belongs.
        data[current_position] = value
