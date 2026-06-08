from intervals.interval import Interval
from intervals.arithmetic import add, sub, mul, div

EDGE_CASES = [
  Interval.empty(),
  Interval.entire(),
  Interval(0, 0),
  Interval(-1, 1),
  Interval(1, 2),
  Interval(-5, -2),
]

def test_edge_cases():
  for x in EDGE_CASES:
    for y in EDGE_CASES:
      _ = x + y
      _ = x - y
      _ = x * y
