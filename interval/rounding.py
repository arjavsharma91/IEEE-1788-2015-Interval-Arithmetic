from gmpy2 import RoundDown, RoundUp, context, get_context, exp, log, mpfr, sin, cos
Number = mpfr

def add_down(a, b):
    a = Number(a)
    b = Number(b)
    with context(get_context()) as ctx:
        ctx.round = RoundDown
        return a+b

def add_up(a, b):
    a = Number(a)
    b = Number(b)
    with context(get_context()) as ctx:
        ctx.round = RoundUp
        return a+b

def sub_down(a, b):
    a = Number(a)
    b = Number(b)
    with context(get_context()) as ctx:
        ctx.round = RoundDown
        return a-b

def sub_up(a, b):
    a = Number(a)
    b = Number(b)
    with context(get_context()) as ctx:
        ctx.round = RoundUp
        return a-b

def mul_down(a, b):
    a = Number(a)
    b = Number(b)
    with context(get_context()) as ctx:
        ctx.round = RoundDown
        return a*b

def mul_up(a, b):
    a = Number(a)
    b = Number(b)
    with context(get_context()) as ctx:
        ctx.round = RoundUp
        return a*b

def div_down(a, b):
    a = Number(a)
    b = Number(b)
    with context(get_context()) as ctx:
        ctx.round = RoundDown
        return a / b

def div_up(a, b):
    a = Number(a)
    b = Number(b)
    with context(get_context()) as ctx:
        ctx.round = RoundUp
        return a / b

def sqrt_up(a):
    a = Number(a)
    with context(get_context()) as ctx:
        ctx.round = RoundUp
        return sqrt(a)

def sqrt_down(a):
    a = Number(a)
    with context(get_context()) as ctx:
        ctx.round = RoundDown
        return sqrt(a)

def exp_up(a):
    a = Number(a)
    with context(get_context()) as ctx:
        ctx.round = RoundUp
        return exp(a)

def exp_down(a):
    a = Number(a)
    with context(get_context()) as ctx:
        ctx.round = RoundDown
        return exp(a)

def log_down(a):
    a = Number(a)
    with context(get_context()) as ctx:
        ctx.round = RoundDown
        return log(a)

def log_up(a):
    a = Number(a)
    with context(get_context()) as ctx:
        ctx.round = RoundUp
        return log(a)

def pow_up(a, n):
    a = Number(a)
    with context(get_context()) as ctx:
        ctx.round = RoundUp
        return a ** n
def pow_down(a, n):
    a = Number(a)
    with context(get_context()) as ctx:
        ctx.round = RoundDown
        return a ** n

def root_up(a, n):
    a = Number(a)
    with context(get_context()) as ctx:
        ctx.round = RoundUp
        if a < 0 and n % 2 == 1:
            return -root_down(-a, n)
        return a ** (mpfr(1) / n)
def root_down(a, n):
    a = Number(a)
    with context(get_context()) as ctx:
        ctx.round = RoundDown
        if a < 0 and n % 2 == 1:
            return -root_up(-a, n)
        return a ** (mpfr(1) / n)

def sin_up(a):
    a = Number(a)
    with context(get_context()) as ctx:
        ctx.round = RoundUp
        return sin(a)

def sin_down(a):
    a = Number(a)
    with context(get_context()) as ctx:
        ctx.round = RoundDown
        return sin(a)

def cos_down(a):
    a = Number(a)
    with context(get_context()) as ctx:
        ctx.round = RoundDown
        return cos(a)

def sin_up(a):
    a = Number(a)
    with context(get_context()) as ctx:
        ctx.round = RoundUp
        return cos(a)
