from .decorated_interval import DecoratedInterval
from .decorations import Decoration, combine
from .functions import exp as bare_exp, sqrt as bare_sqrt, log as bare_log, pow_int as bare_pow_int, sign as bare_sign, interval_min as bare_interval_min, interval_max as bare_interval_max, nth_root as bare_nth_root, sin as bare_sin, cos as bare_cos, tan as bare_tan, asin as bare_asin, acos as bare_acos, atan as bare_atan, sinh as bare_sinh, cosh as bare_cosh, tanh as bare_tanh, asinh as bare_asinh, acosh as bare_acosh, atanh as bare_atanh, abs as bare_abs, atan2 as bare_atan2, contains_periodic_point as bare_contains_periodic_point 
from .constants import PI, HALF_PI, TWO_PI

def exp(x):
  x = DecoratedInterval._coerce(x)
  if x.is_nai:
    return DecoratedInterval.new_nai()
  interval = bare_exp(x.interval)
  dec = combine(x.decoration)

  if dec == Decoration.COM and not interval.is_bounded:
    dec = Decoration.DAC
  return DecoratedInterval(interval, dec)

def sqrt(x):
  x = DecoratedInterval._coerce(x)
  if x.is_nai:
    return DecoratedInterval.new_nai()
  if x.interval.hi < 0:
    return DecoratedInterval.empty()
  elif x.interval.lo < 0:
    op_dec = Decoration.TRV
  else:
    op_dec = Decoration.COM
  interval = bare_sqrt(x.interval)
  dec = combine(x.decoration, op_dec)

  if dec == Decoration.COM and not interval.is_bounded:
    dec = Decoration.DAC

  return DecoratedInterval(interval, dec)

def log(x):
  x = DecoratedInterval._coerce(x)
  if x.is_nai:
    return DecoratedInterval.new_nai()
  if x.interval.hi < 0:
    return DecoratedInterval.empty()
  elif x.interval.lo < 0:
    op_dec = Decoration.TRV
  else:
    op_dec = Decoration.COM
  interval = bare_log(x.interval)
  dec = combine(x.decoration, op_dec)
  if dec == Decoration.COM and not interval.is_bounded:
    dec = Decoration.DAC
  return DecoratedInterval(interval, dec)

def pow_int(x, n):
  x = DecoratedInterval._coerce(x)
  if x.is_nai:
    return DecoratedInterval.new_nai()

  if n < 0 and x.interval.contains(0):
    op_dec = Decoration.TRV
  else:
    op_dec = Decoration.COM

  interval = bare_pow_int(x.interval, n)
  dec = combine(x.decoration, op_dec)

  if dec == Decoration.COM and not interval.is_bounded:
    dec = Decoration.DAC
  return DecoratedInterval(interval, dec)

def sign(x):
  x = DecoratedInterval._coerce(x)
  if x.is_nai:
    return DecoratedInterval.new_nai()
  if x.interval.contains(0) and not x.interval.is_point:
    op_dec = Decoration.DEF
  else:
    op_dec = Decoration.COM

  interval = bare_sign(x.interval)
  dec = combine(x.decoration, op_dec)

  if dec == Decoration.COM and not interval.is_bounded:
    dec = Decoration.DAC
  return DecoratedInterval(interval, dec)

def interval_min(x, y):
  x = DecoratedInterval._coerce(x)
  y = DecoratedInterval._coerce(y)

  if x.is_nai or y.is_nai:
    return DecoratedInterval.new_nai()
  op_dec = Decoration.COM
  interval = bare_interval_min(x.interval, y.interval)

  dec = combine(op_dec, y.decoration, x.decoration)

  if dec == Decoration.COM and not interval.is_bounded:
    dec = Decoration.DAC
  return DecoratedInterval(interval, dec)

def interval_max(x, y):
  x = DecoratedInterval._coerce(x)
  y = DecoratedInterval._coerce(y)

  if x.is_nai or y.is_nai:
    return DecoratedInterval.new_nai()
  op_dec = Decoration.COM
  interval = bare_interval_max(x.interval, y.interval)

  dec = combine(op_dec, y.decoration, x.decoration)

  if dec == Decoration.COM and not interval.is_bounded:
    dec = Decoration.DAC
  return DecoratedInterval(interval, dec)

def nth_root(x, n):
  x = DecoratedInterval._coerce(x)
  if x.is_nai:
    return DecoratedInterval.new_nai()
  if n <= 0:
    raise ValueError("n must be positive")
  if n % 2 == 1:
    op_dec = Decoration.COM
  else:
    if x.interval.hi < 0:
      return DecoratedInterval.empty()
    elif x.interval.lo < 0:
      op_dec = Decoration.TRV
    else:
      op_dec = Decoration.COM
  interval = bare_nth_root(x.interval, n)
  dec = combine(x.decoration, op_dec)

  if dec == Decoration.COM and not interval.is_bounded:
    dec = Decoration.DAC

  return DecoratedInterval(interval, dec)

def sin(x):
  x = DecoratedInterval._coerce(x)
  if x.is_nai:
    return DecoratedInterval.new_nai()
  op_dec = Decoration.COM

  interval = bare_sin(x.interval)
  dec = combine(op_dec, x.decoration)

  if dec == Decoration.COM and not interval.is_bounded:
    dec = Decoration.DAC

  return DecoratedInterval(interval, dec)


def cos(x):
  x = DecoratedInterval._coerce(x)
  if x.is_nai:
    return DecoratedInterval.new_nai()
  op_dec = Decoration.COM

  interval = bare_cos(x.interval)
  dec = combine(op_dec, x.decoration)

  if dec == Decoration.COM and not interval.is_bounded:
    dec = Decoration.DAC

  return DecoratedInterval(interval, dec)

def tan(x):
  x = DecoratedInterval._coerce(x)
  if x.is_nai:
    return DecoratedInterval.new_nai()

  if bare_contains_periodic_point(x.interval, HALF_PI, PI):
    op_dec = Decoration.TRV
  else:
    op_dec = Decoration.COM

  interval = bare_tan(x.interval)
  dec = combine(x.decoration, op_dec)

  if dec == Decoration.COM and not interval.is_bounded:
    dec = Decoration.DAC

  return DecoratedInterval(interval, dec)

def asin(x):
  x = DecoratedInterval._coerce(x)
  if x.is_nai:
    return DecoratedInterval.new_nai()

  if x.interval.hi < -1 or x.interval.lo > 1:
    return DecoratedInterval.empty()
  elif x.interval.lo < -1 or x.interval.hi > 1:
    op_dec = Decoration.TRV
  else:
    op_dec = Decoration.COM

  interval = bare_asin(x.interval)
  dec = combine(x.decoration, op_dec)

  if dec == Decoration.COM and not interval.is_bounded:
    dec = Decoration.DAC

  return DecoratedInterval(interval, dec)

def acos(x):
  x = DecoratedInterval._coerce(x)
  if x.is_nai:
    return DecoratedInterval.new_nai()

  if x.interval.hi < -1 or x.interval.lo > 1:
    return DecoratedInterval.empty()
  elif x.interval.lo < -1 or x.interval.hi > 1:
    op_dec = Decoration.TRV
  else:
    op_dec = Decoration.COM

  interval = bare_acos(x.interval)
  dec = combine(x.decoration, op_dec)

  if dec == Decoration.COM and not interval.is_bounded:
    dec = Decoration.DAC

  return DecoratedInterval(interval, dec)

def atan(x):
  x = DecoratedInterval._coerce(x)
  if x.is_nai:
    return DecoratedInterval.new_nai()
  op_dec = Decoration.COM

  interval = bare_atan(x.interval)
  dec = combine(x.decoration, op_dec)

  if dec == Decoration.COM and not interval.is_bounded:
    dec = Decoration.DAC

  return DecoratedInterval(interval, dec)

def sinh(x):
  x = DecoratedInterval._coerce(x)
  if x.is_nai:
    return DecoratedInterval.new_nai()
  op_dec = Decoration.COM

  interval = bare_sinh(x.interval)
  dec = combine(x.decoration, op_dec)

  if dec == Decoration.COM and not interval.is_bounded:
    dec = Decoration.DAC

  return DecoratedInterval(interval, dec)

def cosh(x):
  x = DecoratedInterval._coerce(x)
  if x.is_nai:
    return DecoratedInterval.new_nai()
  op_dec = Decoration.COM

  interval = bare_cosh(x.interval)
  dec = combine(x.decoration, op_dec)

  if dec == Decoration.COM and not interval.is_bounded:
    dec = Decoration.DAC

  return DecoratedInterval(interval, dec)

def tanh(x):
  x = DecoratedInterval._coerce(x)
  if x.is_nai:
    return DecoratedInterval.new_nai()
  op_dec = Decoration.COM

  interval = bare_tanh(x.interval)
  dec = combine(x.decoration, op_dec)

  if dec == Decoration.COM and not interval.is_bounded:
    dec = Decoration.DAC

  return DecoratedInterval(interval, dec)
  
def asinh(x):
  x = DecoratedInterval._coerce(x)
  if x.is_nai:
    return DecoratedInterval.new_nai()
  op_dec = Decoration.COM

  interval = bare_asinh(x.interval)
  dec = combine(x.decoration, op_dec)

  if dec == Decoration.COM and not interval.is_bounded:
    dec = Decoration.DAC

  return DecoratedInterval(interval, dec)

def acosh(x):
  x = DecoratedInterval._coerce(x)
  if x.is_nai:
    return DecoratedInterval.new_nai()
  if x.interval.hi < 1:
    return DecoratedInterval.empty()
  elif x.interval.lo < 1:
    op_dec = Decoration.TRV
  else:
    op_dec = Decoration.COM

  interval = bare_acosh(x.interval)
  dec = combine(x.decoration, op_dec)

  if dec == Decoration.COM and not interval.is_bounded:
    dec = Decoration.DAC

  return DecoratedInterval(interval, dec)

def atanh(x):
  x = DecoratedInterval._coerce(x)
  if x.is_nai:
    return DecoratedInterval.new_nai()

  if x.interval.hi <= -1 or x.interval.lo >= 1:
    return DecoratedInterval.empty()
  elif x.interval.lo <= -1 or x.interval.hi >= 1:
    op_dec = Decoration.TRV
  else:
    op_dec = Decoration.COM

  interval = bare_atanh(x.interval)
  dec = combine(x.decoration, op_dec)

  if dec == Decoration.COM and not interval.is_bounded:
    dec = Decoration.DAC

  return DecoratedInterval(interval, dec)


def abs(x):
  x = DecoratedInterval._coerce(x)
  if x.is_nai:
    return DecoratedInterval.new_nai()
  op_dec = Decoration.COM

  interval = bare_abs(x.interval)
  dec = combine(x.decoration, op_dec)

  if dec == Decoration.COM and not interval.is_bounded:
    dec = Decoration.DAC

  return DecoratedInterval(interval, dec)

def atan2(y, x):
  y = DecoratedInterval._coerce(y)
  x = DecoratedInterval._coerce(x)

  if y.is_nai or x.is_nai:
    return DecoratedInterval.new_nai()

  if y.interval.contains(0) and x.interval.contains(0):
    if y.interval.lo == 0 and y.interval.hi == 0 and x.interval.lo == 0 and x.interval.hi == 0:
      return DecoratedInterval.empty()
    op_dec = Decoration.TRV
  elif x.interval.lo < 0 and y.interval.contains(0):
    op_dec = Decoration.DEF
  else:
    op_dec = Decoration.COM

  interval = bare_atan2(y.interval, x.interval)
  dec = combine(x.decoration, op_dec, y.decoration)

  if dec == Decoration.COM and not interval.is_bounded:
    dec = Decoration.DAC

  return DecoratedInterval(interval, dec)
