from gmpy2 import RoundDown, RoundUp, context, get_context, exp, log, mpfr, sin, cos, asin, atan, acos, tan, sqrt, sinh, tanh, cosh, asinh, acosh, atanh, atan2, pow, root
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
        return pow(a, n)
def pow_down(a, n):
    a = Number(a)
    with context(get_context()) as ctx:
        ctx.round = RoundDown
        return pow(a, n)

def root_up(a, n):
    a = Number(a)
    with context(get_context()) as ctx:
        ctx.round = RoundUp
        return root(a, int(n))

def root_down(a, n):
    a = Number(a)
    with context(get_context()) as ctx:
        ctx.round = RoundDown
        return root(a, int(n))

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

def cos_up(a):
    a = Number(a)
    with context(get_context()) as ctx:
        ctx.round = RoundUp
        return cos(a)

def tan_up(a):
    a = Number(a)
    with context(get_context()) as ctx:
        ctx.round = RoundUp
        return tan(a)

def tan_down(a):
    a = Number(a)
    with context(get_context()) as ctx:
        ctx.round = RoundDown
        return tan(a)

def asin_up(a):
    a = Number(a)
    with context(get_context()) as ctx:
        ctx.round = RoundUp
        return asin(a)

def asin_down(a):
    a = Number(a)
    with context(get_context()) as ctx:
        ctx.round = RoundDown
        return asin(a)

def atan_down(a):
    a = Number(a)
    with context(get_context()) as ctx:
        ctx.round = RoundDown
        return atan(a)

def atan_up(a):
    a = Number(a)
    with context(get_context()) as ctx:
        ctx.round = RoundUp
        return atan(a)

def acos_up(a):
    a = Number(a)
    with context(get_context()) as ctx:
        ctx.round = RoundUp
        return acos(a)

def acos_down(a):
    a = Number(a)
    with context(get_context()) as ctx:
        ctx.round = RoundDown
        return acos(a)

def sinh_up(a):
    a = Number(a)
    with context(get_context()) as ctx:
        ctx.round = RoundUp
        return sinh(a)

def sinh_down(a):
    a = Number(a)
    with context(get_context()) as ctx:
        ctx.round = RoundDown
        return sinh(a)

def cosh_down(a):
    a = Number(a)
    with context(get_context()) as ctx:
        ctx.round = RoundDown
        return cosh(a)

def cosh_up(a):
    a = Number(a)
    with context(get_context()) as ctx:
        ctx.round = RoundUp
        return cosh(a)

def tanh_up(a):
    a = Number(a)
    with context(get_context()) as ctx:
        ctx.round = RoundUp
        return tanh(a)

def tanh_down(a):
    a = Number(a)
    with context(get_context()) as ctx:
        ctx.round = RoundDown
        return tanh(a)

def asinh_up(a):
    a = Number(a)
    with context(get_context()) as ctx:
        ctx.round = RoundUp
        return asinh(a)

def asinh_down(a):
    a = Number(a)
    with context(get_context()) as ctx:
        ctx.round = RoundDown
        return asinh(a)

def acosh_up(a):
    a = Number(a)
    with context(get_context()) as ctx:
        ctx.round = RoundUp
        return acosh(a)

def acosh_down(a):
    a = Number(a)
    with context(get_context()) as ctx:
        ctx.round = RoundDown
        return acosh(a)

def atanh_up(a):
    a = Number(a)
    with context(get_context()) as ctx:
        ctx.round = RoundUp
        return atanh(a)

def atanh_down(a):
    a = Number(a)
    with context(get_context()) as ctx:
        ctx.round = RoundDown
        return atanh(a)

def atan2_down(y, x):
    x = Number(x)
    y = Number(y)
    with context(get_context()) as ctx:
        ctx.round = RoundDown
        return atan2(y, x)

def atan2_up(y, x):
    x = Number(x)
    y = Number(y)
    with context(get_context()) as ctx:
        ctx.round = RoundUp
        return atan2(y, x)
