# conftest.py
import time
import pytest
from collections import defaultdict

@pytest.fixture(scope="session")
def _timing_store():
    totals = defaultdict(float)   # name -> total seconds
    counts = defaultdict(int)     # name -> #runs
    yield totals, counts
    # ---- session teardown: print averages ----
    print()
    for name, total in totals.items():
        n = counts[name]
        avg = (total / n) if n else 0.0
        print(f"\nAverage run time for {name}: {avg:.10f} seconds over {n} runs")
    print()

@pytest.fixture
def timeit(_timing_store):
    totals, counts = _timing_store
    def run(name, func, *args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        totals[name] += (time.perf_counter() - start)
        counts[name] += 1
        return result
    return run
