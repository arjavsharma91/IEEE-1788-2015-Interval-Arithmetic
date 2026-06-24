from .interval import Interval
from .rounding import add_up, add_down, sub_up, sub_down, mul_up, mul_down, div_up, div_down, sqrt_up, sqrt_down, exp_down, exp_up, log_up, log_down, pow_up, pow_down, root_up, root_down, sin_up, sin_down, tan_up, tan_down, asin_up, asin_down, acos_up, acos_down, atan_up, atan_down, sinh_up, sinh_down, cosh_up, cosh_down, tanh_up, tanh_down, atanh_up, atanh_down, asinh_up, asinh_down, acosh_up, acosh_down
from gmpy2 import mpfr, floor, ceil
from .arithmetic import reciprocal
from .constants import PI, TWO_PI, HALF_PI

Number = mpfr

def sqrt(x: Interval) -> Interval:
  x = Interval._coerce(x)
  if x.is_empty:
    return Interval.empty()
  if x.hi < 0:
    return Interval.empty()
  lo = max(x.lo, mpfr(0))
  return Interval(sqrt_down(lo), sqrt_up(x.hi))

def exp(x) -> Interval:
  x = Interval._coerce(x)
  if x.is_empty:
    return Interval.empty()
  return Interval(exp_down(x.lo), exp_up(x.hi))

def log(x) -> Interval:
  x = Interval._coerce(x)
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
  x = Interval._coerce(x)
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
    hi = max(
    pow_up(abs(x.hi), n),
    pow_up(abs(x.lo), n)
    )
    return Interval(mpfr(0), hi)

def sign(x) -> Interval:
  x = Interval._coerce(x)
  if x.is_empty:
    return Interval.empty()
  if x.lo > 0:
    return Interval(Number(1), Number(1))
  if x.hi < 0:
    return Interval(Number(-1), Number(-1))
  if x.lo == 0 and x.hi == 0:
    return Interval(Number(0), Number(0))
  if x.lo == 0:
    return Interval(Number(0), Number(1))
  if x.hi == 0:
    return Interval(Number(-1), Number(0))
  return Interval(Number(-1), Number(1))

def interval_min(x, y) -> Interval:
  x = Interval._coerce(x)
  y = Interval._coerce(y)
  if x.is_empty or y.is_empty:
    return Interval.empty()
  return Interval(min(x.lo, y.lo), min(x.hi, y.hi))

def interval_max(x, y) -> Interval:
  x = Interval._coerce(x)
  y = Interval._coerce(y)
  if x.is_empty or y.is_empty:
    return Interval.empty()
  return Interval(max(x.lo, y.lo), max(x.hi, y.hi))
  
def nth_root(x, n) -> Interval:
  x = Interval._coerce(x)
  if n <= 0:
    raise ValueError("n must be positive")
  if x.is_empty:
    return Interval.empty()
  if n % 2 == 1:
    return Interval(root_down(x.lo, n), root_up(x.hi, n))
  if x.hi < 0:
    return Interval.empty()
  lo = max(x.lo, mpfr(0))
  return Interval(root_down(lo, n), root_up(x.hi, n))

def contains_periodic_point(x, offset, period):
  lower = div_down(sub_down(x.lo - offset), period)
  higher = div_up(sub_up(x.hi - offset), period)
  return ceil(lower) <= floor(higher)


def sin(x) -> Interval:
  x = Interval._coerce(x)
  if x.is_empty:
    return Interval.empty()
  if x.width >= TWO_PI:
    return Interval(mpfr(-1), mpfr(1))
  s1 = sin_down(x.lo)
  s2 = sin_down(x.hi)
  t1 = sin_up(x.lo)
  t2 = sin_up(x.hi)
  lo = min(s1, s2)
  hi = max(t1, t2)

  if contains_periodic_point(x, HALF_PI, TWO_PI):
    hi = mpfr(1)
  if contains_periodic_point(x, -HALF_PI, TWO_PI):
    lo = mpfr(-1)
  return Interval(lo, hi)

def cos(x) -> Interval:
  x = Interval._coerce(x)
  if x.is_empty:
    return Interval.empty()
  if x.width >= TWO_PI:
    return Interval(mpfr(-1), mpfr(1))
        
  c1 = cos_down(x.lo)
  c2 = cos_down(x.hi)
  d1 = cos_up(x.lo)
  d2 = cos_up(x.hi)
  lo = min(c1, c2)
  hi = max(d1, d2)

    # Cosine peaks at 0 (mod 2pi), troughs at pi (mod 2pi)
  if contains_periodic_point(x, mpfr(0), TWO_PI):
    hi = mpfr(1)
  if contains_periodic_point(x, PI, TWO_PI):
    lo = mpfr(-1)
  return Interval(lo, hi)
  
def tan(x):
  x = Interval._coerce(x)
  if x.is_empty:
    return Interval.empty()
  if contains_periodic_point(x, HALF_PI, PI):
    return Interval.entire()
  lo = tan_down(x.lo)
  hi = tan_up(x.hi)
  return Interval(lo, hi)

def asin(x):
  x = Interval._coerce(x)
  if x.is_empty:
    return Interval.empty()
  x = x.intersection(Interval(-1, 1))

  if x.is_empty:
    return Interval.empty()
  return Interval(asin_down(x.lo), asin_up(x.hi))

def acos(x):
  x = Interval._coerce(x)
  if x.is_empty:
    return Interval.empty()
  x = x.intersection(Interval(-1, 1))
  if x.is_empty:
    return Interval.empty()
  return Interval(acos_down(x.hi), acos_up(x.lo))

def atan(x):
  x = Interval._coerce(x)

  if x.is_empty:
    return Interval.empty()

  return Interval(
    atan_down(x.lo),
    atan_up(x.hi)
    )

def sinh(x):
  x = Interval._coerce(x)
  if x.is_empty:
    return Interval.empty()
  return Interval(sinh_down(x.lo), sinh_up(x.hi))

def tanh(x):
  x = Interval._coerce(x)
  if x.is_empty():
    return Interval.empty()
  return Interval(tanh_down(x.lo), tanh_up(x.hi))

def cosh(x):
  x = Interval._coerce(x)
  if x.is_empty():
    return Interval.empty()

  if x.lo >= 0:
    return Interval(cosh_down(x.lo), cosh_up(x.hi))
  if x.hi <= 0:
    return Interval(cosh_down(x.hi), cosh_up(x.lo))

def asinh(x) -> Interval:
  x = Interval._coerce(x)
  if x.is_empty:
    return Interval.empty()
  return Interval(asinh_down(x.lo), asinh_up(x.hi))

def acosh(x) -> Interval:
  x = Interval._coerce(x)
  if x.is_empty:
    return Interval.empty()
  if x.hi < 1:
    return Interval.empty()
        

  lo = max(x.lo, mpfr(1))
  return Interval(acosh_down(lo), acosh_up(x.hi))

def atanh(x) -> Interval:
  x = Interval._coerce(x)
  if x.is_empty:
    return Interval.empty()
    
  x = x.intersection(Interval(-1, 1))
  if x.is_empty:
    return Interval.empty()
        
  lo = mpfr('-inf') if x.lo == -1 else atanh_down(x.lo)
  hi = mpfr('inf') if x.hi == 1 else atanh_up(x.hi)
    
  return Interval(lo, hi)
