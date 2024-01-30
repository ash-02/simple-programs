import IterativeMaxHeapify
import DefaultMaxHeapify
import test
from time import perf_counter

A = list(range(10000000, 0, -1))

default_start = perf_counter()
DefaultMaxHeapify.buildMaxHeap(A)
default_stop = perf_counter()

print("Time for default: ", default_stop - default_start)

iterative_start = perf_counter()
IterativeMaxHeapify.buildMaxHeap(A)
iterative_stop = perf_counter()

print("Time for Iterative: ", iterative_stop - iterative_start)

test_start = perf_counter()
test.buildMaxHeap(A)
test_stop = perf_counter()

print("Time for Test: ", test_stop - test_start)