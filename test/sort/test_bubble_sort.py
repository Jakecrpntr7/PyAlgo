import time
import random
from unittest import TestCase
from algorithms.sort.bubble_sort import bubble_sort

TEST_DATA_SIZE = 100
TIME_SORT = True

class BubbleSortTest(TestCase):

    def test_bubble_sort(self):
        '''
        Tests to ensure a list of size TEST_DATA_SIZE integers is sorted correctly by Bubble Sort.
        '''
        data = [random.randint(0, 1000) for _ in range(TEST_DATA_SIZE)]
        start = time.time()
        bubble_sort(data)
        print(f'Runtime for dataset of size {TEST_DATA_SIZE}: {time.time() - start}')
        for i in range(len(data) - 2):
            self.assertTrue(data[i] <= data[i + 1])