from dataclasses import dataclass
from gmpy2 import mpfr

Number = mpfr
@dataclass(frozen = True)
class Interval:
    lo: Number
    hi: Number

    def __post_init__(self):
        lo = Number(self.lo)
        hi = Number(self.hi)

        if lo.isnan() or hi.isnan():
            raise ValueError("NaN Endpoints are Invalid")

        if lo > hi:
            lo = Number('inf')
            hi = Number('-inf')

        object.__setattr__(self, "lo", lo)
        object.__setattr__(self, "hi", hi)

    @classmethod
    def empty(cls):
        return cls(Number('inf'), Number('-inf'))
    @classmethod
    def entire(cls):
        return cls(Number('-inf'), Number('inf'))

    @property
    def is_empty(self):
        return self.lo > self.hi
    
    @property
    def is_entire(self):
        return not self.is_empty and self.lo == Number('-inf') and self.hi == Number('inf')
    
    @property
    def is_bounded(self):
        return not self.is_empty and self.lo != Number('-inf') and self.hi != Number('inf')

    @property
    def is_point(self):
        return not self.is_empty and self.lo == self.hi
    
    @property
    def width(self):
        if self.is_empty:
            return Number('nan')
        return (self.hi - self.lo)
    
    @property
    def radius(self):
        return self.width / 2

    @property
    def midpoint(self):
        if self.is_empty:
            return Number("nan")
        if not self.is_bounded:
            return Number('nan')
        else:
            return self.lo + (self.hi - self.lo) / 2

    def contains(self, x):
        x = Number(x)
        if self.is_empty:
            return False
        return self.lo <= x <= self.hi

    def subset(self, other):
        if not isinstance(other, Interval):
            raise TypeError("Expected Interval")
        if self.is_empty:
            return True
        if other.is_empty:
            return False
        return other.lo <= self.lo and other.hi >= self.hi
    
    def proper_subset(self, other):
        if not isinstance(other, Interval):
            raise TypeError("Expected Interval")
        return self.subset(other) and self != other
    
    def overlaps(self, other):
        if not isinstance(other, Interval):
            raise TypeError("Expected Interval")
        if self.is_empty or other.is_empty:
            return False
        return max(other.lo, self.lo) <= min(self.hi, other.hi)

    def intersection(self, other):
        if not isinstance(other, Interval):
            raise TypeError("Expected Interval")
        if self.is_empty or other.is_empty:
            return Interval.empty()
        return Interval(max(self.lo, other.lo), min(self.hi, other.hi))
    
    def hull(self, other):
        if not isinstance(other, Interval):
            raise TypeError("Expected Interval")
        if self.is_empty:
            return other
        if other.is_empty:
            return self
        return Interval(min(self.lo, other.lo), max(self.hi, other.hi))

    def __repr__(self):
        if self.is_empty:
            return "Interval.empty()"
        return f"Interval({self.lo}, {self.hi})"

    def disjoint(self, other):
        if not isinstance(other, Interval):
            raise TypeError("Expected Interval")
        return not self.overlaps(other)

    def interior_contains(self, x):
        if not isinstance(other, Interval):
            raise TypeError("Expected Interval")
        if self.is_empty:
            return False
        x = Number(x)
        return self.lo < x < self.hi

    def interior_subset(self, other):
        if not isinstance(other, Interval):
            raise TypeError("Expected Interval")
        if self.is_empty:
            return True
        if other.is_empty:
            return False

        return other.lo < self.lo and self.hi < other.hi

    def precedes(self, other):
        if self.is_empty or other.is_empty:
            return False
        return self.hi < other.lo

    def meets(self, other):
        if self.is_empty or other.is_empty:
            return False
        return self.hi == other.lo or other.hi == self.lo

    def __add__(self, other):
        from .arithmetic import add
        if not isinstance(other, Interval):
            other = Interval(other, other)
        return add(self, other)

    def __sub__(self, other):
        from .arithmetic import sub
        if not isinstance(other, Interval):
            other = Interval(other, other)
        return sub(self, other)

    def __mul__(self, other):
        from .arithmetic import mul
        if not isinstance(other, Interval):
            other = Interval(other, other)
        return mul(self, other)

    def __truediv__(self, other):
        from .arithmetic import div
        if not isinstance(other, Interval):
            other = Interval(other, other)
        return div(self, other)
                  


    
