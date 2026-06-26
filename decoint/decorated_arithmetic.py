from .interval import Interval
from .arithmetic import add as bare_add, sub as bare_sub, mul as bare_mul, div as bare_div
from .decorations import Decoration, combine
from .decorated_interval import DecoratedInterval

def _finalize_decoration(base_dec: Decoration, interval: Interval) -> Decoration:
  if base_dec == Decoration.COM and not interval.is_bounded:
    return Decoration.DAC
  return base_dec

def add(x, y):
  x = DecoratedInterval._coerce(x)
  y = DecoratedInterval._coerce(y)

  if x.is_nai or y.is_nai:
    return DecoratedInterval.new_nai()

  interval = bare_add(x.interval, y.interval)
  dec = combine(x.decoration, y.decoration)
  dec = _finalize_decoration(dec, interval)

  return DecoratedInterval(interval, dec)

def sub(x, y):
  x = DecoratedInterval._coerce(x)
  y = DecoratedInterval._coerce(y)

  if x.is_nai or y.is_nai:
    return DecoratedInterval.new_nai()

  interval = bare_sub(x.interval, y.interval)
  dec = combine(x.decoration, y.decoration)
  dec = _finalize_decoration(dec, interval)

  return DecoratedInterval(interval, dec)

def mul(x, y):
  x = DecoratedInterval._coerce(x)
  y = DecoratedInterval._coerce(y)

  if x.is_nai or y.is_nai:
    return DecoratedInterval.new_nai()

  interval = bare_mul(x.interval, y.interval)
  dec = combine(x.decoration, y.decoration)
  dec = _finalize_decoration(dec, interval)

  return DecoratedInterval(interval, dec)

def div(x, y):
  x = DecoratedInterval._coerce(x)
  y = DecoratedInterval._coerce(y)

  if x.is_nai or y.is_nai:
    return DecoratedInterval.new_nai()

  if y.interval.contains(0):
    if y.interval.lo < 0 and y.interval.hi > 0:
      return DecoratedInterval(Interval.entire(), Decoration.TRV)
    elif x.interval.contains(0):
      return DecoratedInterval(Interval.entire(), Decoration.TRV)
    else:
      interval = bare_div(x.interval, y.interval)
      dec = combine(x.decoration, y.decoration, Decoration.DEF)
      dec = _finalize_decoration(dec, interval)
      return DecoratedInterval(interval, dec)

  interval = bare_div(x.interval, y.interval)
  dec = combine(x.decoration, y.decoration)
  dec = _finalize_decoration(dec, interval)

  return DecoratedInterval(interval, dec)
  
