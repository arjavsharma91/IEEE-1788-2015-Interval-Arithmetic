from .decorated_interval import DecoratedInterval
from .decorations import Decoration, combine
#Ill import the functions later cuz im stupid and lazy

def exp(x):
  x = DecoratedInterval._coerce(x)
  if x.is_nai:
    return DecoratedInterval.new_nai()
  interval = bare_exp(x.interval)
  dec = combine(x.decoration)
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

  interval = bare_pow_int(x.interval)
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

  interval = bare_sin(x)
  dec = combine(op_dec, x.decoration)

  if dec == Decoration.COM and not interval.is_bounded:
    dec = Decoration.DAC

  return DecoratedInterval(interval, dec)


def cos(x):
  x = DecoratedInterval._coerce(x)
  if x.is_nai:
    return DecoratedInterval.new_nai()
  op_dec = Decoration.COM

  interval = bare_cos(x)
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

  interval = bare_asin(x)
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

  interval = bare_acos(x)
  dec = combine(x.decoration, op_dec)

  if dec == Decoration.COM and not interval.is_bounded:
    dec = Decoration.DAC

  return DecoratedInterval(interval, dec)

def atan(x):
  x = DecoratedInterval._coerce(x)
  if x.is_nai:
    return DecoratedInterval.is_nai()
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
  
