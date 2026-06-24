from .interval import Interval
from dataclasses import dataclass
from .decorations import Decoration

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
      if self.decoration != Decoration.ILL:
        raise ValueError("NaI must have decoration ILL")
  
  @classmethod
  def empty(cls):
    return cls(Interval.empty(), Decoration.TRV)
  
  @classmethod
  def entire(cls):
    return cls(Interval.entire(), Decoration.TRV)

  @classmethod
  def new_nai(cls):
    return cls(Interval.empty(), Decoration.ILL, nai = True)

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
    return self.interval.width

  @property
  def radius(self):
    return self.interval.radius

  @property
  def midpoint(self):
    return self.interval.midpoint

  @property
  def magnitude(self):
    return self.interval.magnitude

  @property
  def mignitude(self):
    return self.interval.mignitude

  def contains(self, x):
    return self.interval.contains(x)

  def __repr__(self):
    if self.nai:
      return "DecoratedInterval(NaI)"

    return (
      f"DecoratedInterval("
      f"{self.interval}, "
      f"{str(self.decoration)})")

  def __add__(self, other):
    from .decorated_arithmetic import add
    if self.is_nai or other.is_nai:
      return DecoratedInterval.new_nai()
    other = self._coerce(other)
    return add(self, other)

  def __sub__(self, other):
    from .decorated_arithmetic import sub
    if self.is_nai or other.is_nai:
      return DecoratedInterval.new_nai()
    other = self._coerce(other)
    return sub(self, other)

  def __mul__(self, other):
    from .decorated_arithmetic import mul
    if self.is_nai or other.is_nai:
      return DecoratedInterval.new_nai()
    other = self._coerce(other)
    return mul(self, other)

  def __truediv__(self, other):
    from .decorated_arithmetic import div
    if self.is_nai or other.is_nai:
      return DecoratedInterval.new_nai()
    other = self._coerce(other)
    return div(self, other)

  def __radd__(self, other):
    from .decorated_arithmetic import add
    if self.is_nai or other.is_nai:
      return DecoratedInterval.new_nai()
    other = self._coerce(other)
    return add(other, self)

  def __rsub__(self, other):
    from .decorated_arithmetic import sub
    if self.is_nai or other.is_nai:
      return DecoratedInterval.new_nai()
    other = self._coerce(other)
    return sub(other, self)

  def __rmul__(self, other):
    from .decorated_arithmetic import mul
    if self.is_nai or other.is_nai:
      return DecoratedInterval.new_nai()
    other = self._coerce(other)
    return mul(other, self)

  def __rtruediv__(self, other):
    from .decorated_arithmetic import div
    if self.is_nai or other.is_nai:
      return DecoratedInterval.new_nai()
    other = self._coerce(other)
    return div(other, self)
