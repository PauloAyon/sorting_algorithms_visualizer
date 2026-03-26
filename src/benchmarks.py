import time
import numpy as np
from src.algorithms import (
    bubble_sort, selection_sort, insertion_sort,
    merge_sort, quick_sort
)

ALGORITHMS = {
    "Bubble Sort":    bubble_sort,
    "Selection Sort": selection_sort,
    "Insertion Sort": insertion_sort,
    "Merge Sort":     merge_sort,
    "Quick Sort":     quick_sort
}


def measure_time(func, arr: list) -> float:
    """Measure execution time of a sorting function in milliseconds."""
    start = time.perf_counter()
    func(arr)
    end = time.perf_counter()
    return (end - start) * 1000


def run_benchmark(sizes: list, runs: int = 3) -> dict:
    """
    Run all algorithms on random arrays of increasing sizes.
    Returns a dict with average execution times per algorithm per size.
    """
    results = {name: [] for name in ALGORITHMS}

    for size in sizes:
        print(f"Testing size: {size}")
        for name, func in ALGORITHMS.items():
            times = []
            for _ in range(runs):
                arr = np.random.randint(0, 10000, size).tolist()
                t = measure_time(func, arr)
                times.append(t)
            avg = sum(times) / len(times)
            results[name].append(round(avg, 4))

    return results