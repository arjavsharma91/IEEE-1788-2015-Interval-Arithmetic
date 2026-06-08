def test_interval_invariants():
  x = rand_interval_mixed()

  assert x.lo <= x.hi or x.is_empty

  # canonical empty form
  if x.is_empty:
    assert x.lo > x.hi

def test_operator_vs_function():
  x = rand_interval_mixed()
  y = rand_interval_mixed()

  assert (x + y).lo == add(x, y).lo
  assert (x - y).hi == sub(x, y).hi
  assert (x * y).lo == mul(x, y).lo

def run_all_tests():
  for _ in range(1000):
    test_add_containment()
    test_sub_containment()
    test_mul_containment()
    test_div_containment()
    test_reciprocal()
    test_interval_invariants()
    test_edge_cases()

  print("All tests passed")
