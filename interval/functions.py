from intervals.interval import Interval
from intervals.rounding import add_up, add_down, sub_up, sub_down, mul_up, mul_down, div_up, div_down, sqrt_up, sqrt_down, exp_down, exp_up, log_up, log_down
from gmpy2 import mpfr

def sqrt(x: Interval) -> Interval:
  if x.is_empty:
    return Interval.empty()
  if x.hi < 0:
    return Interval.empty()
  lo = max(x.lo, mpfr(0))
  return Interval(sqrt_down(lo), sqrt_up(hi))

def exp(x: Interval) -> Interval:
  if x.is_empty:
    return Interval.empty()
  return Interval(exp_down(self.lo), exp_up(self.hi))

def log(x: Interval) -> Interval:
  if x.is_empty:
    return Interval.empty()
  if x.hi <= 0:
    return Interval.empty()
  if x.lo <= 0:
    lo = mpfr('-inf')
  else:
    lo = log_down(x.lo)
  hi = log_up(x.hi)
  return Interval(lo, hi)
