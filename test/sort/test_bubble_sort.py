import time
import random
from unittest import TestCase
from algorithms.sort.bubble_sort import bubble_sort

TEST_DATA_SIZE = 100


class BubbleSortTest(TestCase):

    def test_bubble_sort_ascending(self):
        '''
        Tests to ensure a list of size TEST_DATA_SIZE integers is sorted in ascending order by Bubble Sort.
        '''
        data = [random.randint(0, 1000) for _ in range(TEST_DATA_SIZE)]
        start = time.time()
        bubble_sort(data)
        print(f'Runtime for dataset of size {TEST_DATA_SIZE}: {time.time() - start}')
        for i in range(len(data) - 2):
            self.assertTrue(data[i] <= data[i + 1])

    def test_bubble_sort_descending(self):
        '''
        Tests to ensure a list of size TEST_DATA_SIZE integers is sorted in descending order by Bubble Sort.
        '''
        data = [random.randint(0, 1000) for _ in range(TEST_DATA_SIZE)]
        start = time.time()
        bubble_sort(data, lambda a, b: a < b)
        print(f'Runtime for dataset of size {TEST_DATA_SIZE}: {time.time() - start}')
        for i in range(len(data) - 2):
            self.assertTrue(data[i] >= data[i + 1])