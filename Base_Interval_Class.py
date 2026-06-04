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

        object.__setattr__(self, "lo", lo)
        object.__setattr__(self, "hi", hi)

        if lo > hi:
            lo = Number('inf')
            hi = Number('-inf')

    @classmethod
    def empty(cls):
        return cls(Number('inf'), Number('-inf'))

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
        else:
            return self.lo + (self.hi - self.lo) / 2

    def contains(self, x):
        x = Number(x)
        if self.is_empty:
            return False
        return self.lo <= x <= self.hi

    def subset(self, other):
        if self.is_empty:
            return True
        if other.is_empty:
            return False
        return other.lo =< self.lo and other.hi >= self.hi
    
    def proper_subset(self, other):
        if self.is_empty:
            return True
        if other.is_empty:
            return False
        return self.subset(other) and self != other
    
    def overlaps(self, other):
        if self.is_empty or other.is_empty:
            return False
        return max(other.lo, self.lo) <= min(self.hi, other.hi)
    
