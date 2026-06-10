from .interval import Interval
from .rounding import add_up, add_down, sub_up, sub_down, mul_up, mul_down, div_up, div_down, sqrt_up, sqrt_down, exp_down, exp_up, log_up, log_down, pow_up, pow_down
from gmpy2 import mpfr
from .arithmetic import reciprocal

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

def pow_int(x, n):
  if x.is_empty:
    return Interval.empty()
  if n == 0:
    return Interval(mpfr(1), mpfr(1))
  if n < 0:
    return reciprocal(pow_int(x, -n))
  if n % 2 == 1:
    lo = pow_down(x.lo, n)
    hi = pow_up(x.hi, n)
    return Interval(lo, hi)
  if n % 2 == 0:
    if x.lo >= 0:
      lo = pow_down(x.lo, n)
      hi = pow_up(x.hi, n)
      return Interval(lo, hi)
    if x.hi <= 0:
      lo = pow_down(abs(x.hi), n)
      hi = pow_up(abs(x.lo), n)
      return Interval(lo, hi)
    hi = max(pow_up(abs(x.hi), n), pow_up(abs(x.lo)), n)
    return Interval(mpfr(0), hi)
