from .interval import Interval
from dataclasses import dataclass
from .decorations import Decoration
from gmpy2 import mpfr as Number

@dataclass(frozen=True)
class DecoratedInterval:
  interval: Interval
  decoration: Decoration
  nai: bool = False
  def __post_init__(self):
    if not isinstance(self.interval, Interval):
      raise TypeError("Expected Interval")

    if not isinstance(self.decoration, Decoration):
      raise TypeError("Expected Decoration")

    if self.interval.is_empty and not self.nai:
      object.__setattr__(self, "decoration", Decoration.TRV)
    
    if self.nai:
      if self.decoration != Decoration.NAI:
        raise ValueError("NaI must have decoration NAI")
  
  @classmethod
  def empty(cls):
    return cls(Interval.empty(), Decoration.TRV)
  
  @classmethod
  def entire(cls):
    return cls(Interval.entire(), Decoration.DAC)

  @classmethod
  def new_nai(cls):
    return cls(Interval.empty(), Decoration.NAI, nai = True)

  @classmethod
  def _coerce(cls, value):
    if isinstance(value, cls):
      return value

    if isinstance(value, Interval):
      if value.is_empty:
        return cls(value, Decoration.TRV)
      return cls(value, Decoration.DAC)

    try:
      bare_interval = Interval._coerce(value)
      return cls._coerce(bare_interval)
    except Exception as e:
      return cls.new_nai()

  @classmethod
  def from_string(cls, s: str):
    s = s.strip()
    s_lower = s.lower()

    if s_lower in ("[nan]", "[nai]", "nai"):
      return cls.new_nai()

    if "_" in s:
      interval_part, dec_part = s.rsplit("_", 1)
      try:
        dec = Decoration[dec_part.upper()]
      except KeyError:
        raise ValueError(f"Unknown Decoration Suffix {dec_part}")
      bare_int = Interval.from_string(interval_part)
    else:
      bare_int = Interval.from_string(s)
      if bare_int.is_empty:
        dec = Decoration.TRV
      elif bare_int.lo == Number('-inf') or bare_int.hi == Number('inf'):
        dec = Decoration.DAC
      else:
        dec = Decoration.COM
    return cls(bare_int, dec)

  @property
  def is_nai(self):
    return self.nai

  @property
  def is_empty(self):
    return self.interval.is_empty

  @property
  def is_entire(self):
    return self.interval.is_entire

  @property
  def width(self):
    if self.is_nai:
      return Number('nan')
    return self.interval.width

  @property
  def radius(self):
    if self.is_nai:
      return Number('nan')
    return self.interval.radius

  @property
  def midpoint(self):
    if self.is_nai:
      return Number('nan')
    return self.interval.midpoint

  @property
  def magnitude(self):
    if self.is_nai:
      return Number('nan')
    return self.interval.magnitude

  @property
  def mignitude(self):
    if self.is_nai:
      return Number('nan')
    return self.interval.mignitude

  def contains(self, x):
    if self.is_nai:
      return False
    return self.interval.contains(x)

  def subset(self, other):
    other = self._coerce(other)
    if self.is_nai or other.is_nai:
      return False
    return self.interval.subset(other.interval)

  def proper_subset(self, other):
    other = self._coerce(other)
    if self.is_nai or other.is_nai:
      return False
    return self.interval.proper_subset(other.interval)

  def overlaps(self, other):
    other = self._coerce(other)
    if self.is_nai or other.is_nai:
      return False
    return self.interval.overlaps(other.interval)

  def disjoint(self, other):
    other = self._coerce(other)
    if self.is_nai or other.is_nai:
      return False
    return self.interval.disjoint(other.interval)

  def precedes(self, other):
    other = self._coerce(other)
    if self.is_nai or other.is_nai:
      return False
    return self.interval.precedes(other.interval)

  def meets(self, other):
    other = self._coerce(other)
    if self.is_nai or other.is_nai:
      return False
    return self.interval.meets(other.interval)

  def sup_sub(self, other):
    other = self._coerce(other)
    if self.is_nai or other.is_nai:
      return False
    return self.interval.sup_sub(other.interval)

  def inf_sub(self, other):
    other = self._coerce(other)
    if self.is_nai or other.is_nai:
      return False
    return self.interval.inf_sub(other.interval)

  def __repr__(self):
    if self.nai:
      return "DecoratedInterval(NaI)"

    return (
      f"DecoratedInterval("
      f"{self.interval}, "
      f"{str(self.decoration)})")

  def __str__(self):
    if self.nai:
      return "[NaI]"
    int_str = str(self.interval)
    dec_str = self.decoration.name.lower()
    return f"{int_str}_{dec_str}"

  def __add__(self, other):
    from .decorated_arithmetic import add
    other = self._coerce(other)
    if self.is_nai or other.is_nai:
      return DecoratedInterval.new_nai()
    return add(self, other)

  def __sub__(self, other):
    from .decorated_arithmetic import sub
    other = self._coerce(other)
    if self.is_nai or other.is_nai:
      return DecoratedInterval.new_nai()
    return sub(self, other)

  def __mul__(self, other):
    from .decorated_arithmetic import mul
    other = self._coerce(other)
    if self.is_nai or other.is_nai:
      return DecoratedInterval.new_nai()
    return mul(self, other)

  def __truediv__(self, other):
    from .decorated_arithmetic import div
    other = self._coerce(other)
    if self.is_nai or other.is_nai:
      return DecoratedInterval.new_nai()
    return div(self, other)

  def __radd__(self, other):
    from .decorated_arithmetic import add
    other = self._coerce(other)
    if self.is_nai or other.is_nai:
      return DecoratedInterval.new_nai()
    return add(other, self)

  def __rsub__(self, other):
    from .decorated_arithmetic import sub
    other = self._coerce(other)
    if self.is_nai or other.is_nai:
      return DecoratedInterval.new_nai()
    return sub(other, self)

  def __rmul__(self, other):
    from .decorated_arithmetic import mul
    other = self._coerce(other)
    if self.is_nai or other.is_nai:
      return DecoratedInterval.new_nai()
    return mul(other, self)

  def __rtruediv__(self, other):
    from .decorated_arithmetic import div
    other = self._coerce(other)
    if self.is_nai or other.is_nai:
      return DecoratedInterval.new_nai()
    return div(other, self)

  def __lt__(self, other):
    other = self._coerce(other)
    if self.is_nai or other.is_nai:
      return False
    if self.interval.is_empty or other.interval.is_empty:
      return False
    return self.interval.hi < other.interval.lo

  def __gt__(self, other):
    other = self._coerce(other)
    if self.is_nai or other.is_nai:
      return False
    if self.interval.is_empty or other.interval.is_empty:
      return False
    return self.interval.lo > other.interval.hi

  def possibly_less_than(self, other):
    other = self._coerce(other)
    if self.is_nai or other.is_nai:
      return False
    if self.interval.is_empty or other.interval.is_empty:
        return False
    return self.interval.lo <= other.interval.hi
