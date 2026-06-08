from .interval import Interval
from .rounding import add_down, add_up, sub_down, sub_up, div_down, div_up, mul_down, mul_up
from gmpy2 import mpfr
# Arithmetic layer rule:
# never modify Interval class
# never implement rounding here
# only combine endpoints using rounding.py
# always return Interval

def add(x: Interval, y:Interval) -> Interval:
  if x.is_empty or y.is_empty:
    return Interval.empty()
  lo = add_down(x.lo, y.lo)
  hi = add_up(x.hi, y.hi)
  return Interval(lo, hi)

def sub(x: Interval, y:Interval) -> Interval:
  if x.is_empty or y.is_empty:
    return Interval.empty()
  lo = sub_down(x.lo, y.hi)
  hi = sub_up(x.hi, y.lo)
  return Interval(lo, hi)

def mul(x: Interval, y:Interval) -> Interval:
  if x.is_empty or y.is_empty:
    return Interval.empty()
  p1 = mul_down(x.lo, y.lo)
  p2 = mul_down(x.lo, y.hi)
  p3 = mul_down(x.hi, y.lo)
  p4 = mul_down(x.hi, y.hi)
  
  lo = min(p1, p2, p3, p4)

  q1 = mul_up(x.lo, y.lo)
  q2 = mul_up(x.lo, y.hi)
  q3 = mul_up(x.hi, y.lo)
  q4 = mul_up(x.hi, y.hi)
  
  hi = max(q1, q2, q3, q4)

  return Interval(lo, hi)

def reciprocal(x: Interval) -> Interval:
  if x.is_empty:
    return Interval.empty()

  if x.contains(0):
    raise ZeroDivisionError("Cannot take reciprocal of interval containing 0")
  lo = div_down(mpfr(1), x.hi)
  hi = div_up(mpfr(1), x.lo)

  return Interval(lo, hi)

# This is primitive form of division right now, will work on edge cases and such when we get into decorations and stuff

def div(x: Interval, y: Interval) -> Interval:
  if x.is_empty or y.is_empty:
    return Interval.empty()
  return mul(x, reciprocal(y))
  
