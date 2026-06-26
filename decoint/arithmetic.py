from .interval import Interval
from .rounding import add_down, add_up, sub_down, sub_up, div_down, div_up, mul_down, mul_up
from gmpy2 import mpfr

# Without interval unions,
# division by an interval containing zero
# returns the entire interval.

def add(x, y) -> Interval:
  x = Interval._coerce(x)
  y = Interval._coerce(y)
  if x.is_empty or y.is_empty:
    return Interval.empty()
  lo = add_down(x.lo, y.lo)
  hi = add_up(x.hi, y.hi)
  return Interval(lo, hi)

def sub(x, y) -> Interval:
  x = Interval._coerce(x)
  y = Interval._coerce(y)
  if x.is_empty or y.is_empty:
    return Interval.empty()
  lo = sub_down(x.lo, y.hi)
  hi = sub_up(x.hi, y.lo)
  return Interval(lo, hi)

def mul(x, y) -> Interval:
  x = Interval._coerce(x)
  y = Interval._coerce(y)
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

def reciprocal(x) -> Interval:
  x = Interval._coerce(x)
  if x.is_empty:
    return Interval.empty()
  if x.contains_zero:
    if x.lo == 0 and x.hi == 0:
      return Interval.empty()
    if x.lo == 0:
      return Interval(div_down(mpfr(1), x.hi), mpfr('inf'))
    if x.hi == 0:
      return Interval(mpfr('-inf'), div_up(mpfr(1), x.lo))
    return Interval.entire()

  return Interval(div_down(mpfr(1), x.hi), div_up(mpfr(1), x.lo))

def div(x, y) -> Interval:
  x = Interval._coerce(x)
  y = Interval._coerce(y)
  if x.is_empty or y.is_empty:
    return Interval.empty()

  if y.contains_zero:
    if y.hi == 0 and y.lo == 0:
      if x.hi == 0 and x.lo == 0:
        return Interval.empty()
      return Interval.entire()
    if x.contains(0):
      return Interval.entire()
  
  return mul(x, reciprocal(y))
  
