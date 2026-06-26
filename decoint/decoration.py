from enum import IntEnum

class Decoration(IntEnum):
  NAI = 0
  TRV = 1
  DEF = 2
  DAC = 3
  COM = 4

  def __str__(self):
    return self.name.lower()

def combine(*decorations: Decoration) -> Decoration:
  # IEEE 1788 requires that the minimum decoration has to be the one that is returned
  if not decorations:
    raise ValueError("combine() requires at least one decoration")

  return min(decorations)


  
