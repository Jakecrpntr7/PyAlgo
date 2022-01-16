##
# Implements Merge Sort in Python.
# Merge sort works by repeatedly breaking the list in half until the list is trivially sorted by nature of having
# only 1 element. On the way back up the recursion, it then merges trivially sorted base cases and subsequently
# sorted lists to produce a final sorted list of all elements.
# Time Complexity: O(nlog(n))
def merge_sort(data: list, comparator=lambda a, b: a > b) -> list:
    """
    Merge sort works by recursively breaking the list in half until trivially sorted and then merging
    sorted sub-lists on the way back up the recursion.
    Ex: 7 3 1
       1.) Breaks list into sub lists [7], [3, 1]
       2.) breaks list [3, 1] into [3] and [1] producing [7], [3], [1]
       Merges [7] and [3] to produce [3, 7], Other list still contains [1]
       3.) Merges [1] with [3, 7] to produce [1, 3, 7]
    :param data: List to be sorted
    :param comparator: Comparison function to determine how list should be sorted.
    :return: Input list in sorted order as specified by comparator.
    """
    # Store the length of the array for use throughout.
    length = len(data)
    # Base case, list with only one element is trivially sorted as there is only 1 permutation for ordering.
    if length == 1:
        return data
    # Find index to split list in half.
    mid_point = length // 2
    # Split each list in half to approach base case.
    left_partition = merge_sort(data[:mid_point], comparator)
    right_partition = merge_sort(data[mid_point:], comparator)
    # Merge arrays together on the way back up the recursion to create a final sorted list.
    return __merge(left_partition, right_partition, comparator)


def __merge(left_partition: list, right_partition: list, comparator=lambda a, b: a > b) -> list:
    """
    The merge helper function takes two lists as input and creates one sorted list by grabbing the
    next element in sorted order as defined by comparator until all elements have been retrieved.
    :param left_partition: Partition created from splitting original list in merge_sort function.
    :param right_partition: Partition created from splitting original list in merge_sort function.
    :param comparator: Function to determine how elements should be compared / ordered.
    :return: List comprised of elements in left_partition + elements from right partition in sorted order.
    """
    result = []
    # Start at the beginning of each partition and move towards the end as these partitions are sorted.
    left_index = right_index = 0
    # Iteratively select the next element until one list is exhausted.
    while left_index < len(left_partition) and right_index < len(right_partition):
        if comparator(right_partition[right_index], left_partition[left_index]):
            result.append(left_partition[left_index])
            left_index += 1
        else:
            result.append(right_partition[right_index])
            right_index += 1
    # Since elements in each partition are in sorted order, any elements remaining can simply be added
    # to the end of the result list.
    result.extend(left_partition[left_index:])
    result.extend(right_partition[right_index:])

    return result
