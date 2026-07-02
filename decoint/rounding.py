from gmpy2 import RoundDown, RoundUp, context, get_context, exp, log, mpfr, sin, cos, asin, atan, acos, tan, sqrt, sinh, tanh, cosh, asinh, acosh, atanh, atan2, root, square
Number = mpfr

def add_down(a, b):
    with context(get_context(), round = RoundDown):
        mpfr_a = Number(a)
        mpfr_b = Number(b)
        return mpfr_a + mpfr_b

def add_up(a, b):
    with context(get_context(), round = RoundUp):
        mpfr_a = Number(a)
        mpfr_b = Number(b)
        return mpfr_a + mpfr_b

def sub_down(a, b):
    with context(get_context(), round = RoundDown):
        mpfr_a = Number(a)
        mpfr_b = Number(b)
        return mpfr_a - mpfr_b

def sub_up(a, b):
    with context(get_context(), round = RoundUp):
        mpfr_a = Number(a)
        mpfr_b = Number(b)
        return mpfr_a - mpfr_b

def mul_down(a, b):
    with context(get_context(), round = RoundDown):
        mpfr_a = Number(a)
        mpfr_b = Number(b)
        return mpfr_a*mpfr_b

def mul_up(a, b):
    with context(get_context(), round = RoundUp):
        mpfr_a = Number(a)
        mpfr_b = Number(b)
        return mpfr_a*mpfr_b

def div_down(a, b):
    with context(get_context(), round = RoundDown):
        mpfr_a = Number(a)
        mpfr_b = Number(b)
        return mpfr_a / mpfr_b

def div_up(a, b):
    with context(get_context(), round = RoundUp):
        mpfr_a = Number(a)
        mpfr_b = Number(b)
        return mpfr_a / mpfr_b

def sqrt_up(a):
    with context(get_context(), round = RoundUp):
        mpfr_a = Number(a)
        return sqrt(mpfr_a)

def sqrt_down(a):
    with context(get_context(), round = RoundDown):
        mpfr_a = Number(a)
        return sqrt(mpfr_a)

def exp_up(a):
    with context(get_context(), round = RoundUp):
        mpfr_a = Number(a)
        return exp(mpfr_a)

def exp_down(a):
    with context(get_context(), round = RoundDown):
        mpfr_a = Number(a)
        return exp(mpfr_a)

def log_down(a):
    with context(get_context(), round = RoundDown):
        mpfr_a = Number(a)
        return log(mpfr_a)

def log_up(a):
    with context(get_context(), round = RoundUp):
        mpfr_a = Number(a)
        return log(mpfr_a)

def pow_up(a, n):
    with context(get_context(), round = RoundUp):
        mpfr_a = Number(a)
        return mpfr_a ** n

def pow_down(a, n):
    with context(get_context(), round = RoundDown):
        mpfr_a = Number(a)
        return mpfr_a ** n

def root_up(a, n):
    with context(get_context(), round = RoundUp):
        mpfr_a = Number(a)
        return root(mpfr_a, int(n))

def root_down(a, n):
    with context(get_context(), round = RoundDown):
        mpfr_a = Number(a)
        return root(mpfr_a, int(n))

def sin_up(a):
    with context(get_context(), round = RoundUp):
        mpfr_a = Number(a)
        return sin(mpfr_a)

def sin_down(a):
    with context(get_context(), round = RoundDown):
        mpfr_a = Number(a)
        return sin(mpfr_a)

def cos_down(a):
    with context(get_context(), round = RoundDown):
        mpfr_a = Number(a)
        return cos(mpfr_a)

def cos_up(a):
    with context(get_context(), round = RoundUp):
        mpfr_a = Number(a)
        return cos(mpfr_a)

def tan_up(a):
    with context(get_context(), round = RoundUp):
        mpfr_a = Number(a)
        return tan(mpfr_a)

def tan_down(a):
    with context(get_context(), round = RoundDown):
        mpfr_a = Number(a)
        return tan(mpfr_a)

def asin_up(a):
    with context(get_context(), round = RoundUp):
        mpfr_a = Number(a)
        return asin(mpfr_a)

def asin_down(a):
    with context(get_context(), round = RoundDown):
        mpfr_a = Number(a)
        return asin(mpfr_a)

def atan_down(a):
    with context(get_context(), round = RoundDown):
        mpfr_a = Number(a)
        return atan(mpfr_a)

def atan_up(a):
    with context(get_context(), round = RoundUp):
        mpfr_a = Number(a)
        return atan(mpfr_a)

def acos_up(a):
    with context(get_context(), round = RoundUp):
        mpfr_a = Number(a)
        return acos(mpfr_a)

def acos_down(a):
    with context(get_context(), round = RoundDown):
        mpfr_a = Number(a)
        return acos(mpfr_a)

def sinh_up(a):
    with context(get_context(), round = RoundUp):
        mpfr_a = Number(a)
        return sinh(mpfr_a)

def sinh_down(a):
    with context(get_context(), round = RoundDown):
        mpfr_a = Number(a)
        return sinh(mpfr_a)

def cosh_down(a):
    with context(get_context(), round = RoundDown):
        mpfr_a = Number(a)
        return cosh(mpfr_a)

def cosh_up(a):
    with context(get_context(), round = RoundUp):
        mpfr_a = Number(a)
        return cosh(mpfr_a)

def tanh_up(a):
    with context(get_context(), round = RoundUp):
        mpfr_a = Number(a)
        return tanh(mpfr_a)

def tanh_down(a):
    with context(get_context(), round = RoundDown):
        mpfr_a = Number(a)
        return tanh(mpfr_a)

def asinh_up(a):
    with context(get_context(), round = RoundUp):
        mpfr_a = Number(a)
        return asinh(mpfr_a)

def asinh_down(a):
    with context(get_context(), round = RoundDown):
        mpfr_a = Number(a)
        return asinh(mpfr_a)

def acosh_up(a):
    with context(get_context(), round = RoundUp):
        mpfr_a = Number(a)
        return acosh(mpfr_a)

def acosh_down(a):
    with context(get_context(), round = RoundDown):
        mpfr_a = Number(a)
        return acosh(mpfr_a)

def atanh_up(a):
    with context(get_context(), round = RoundUp):
        mpfr_a = Number(a)
        return atanh(mpfr_a)

def atanh_down(a):
    with context(get_context(), round = RoundDown):
        mpfr_a = Number(a)
        return atanh(mpfr_a)

def atan2_down(y, x):
    with context(get_context(), round = RoundDown):
        mpfr_x = Number(x)
        mpfr_y = Number(y)
        return atan2(mpfr_y, mpfr_x)

def atan2_up(y, x):
    with context(get_context(), round = RoundUp):
        mpfr_x = Number(x)
        mpfr_y = Number(y)
        return atan2(mpfr_y, mpfr_x)

def sqr_up(a):
    with context(get_context(), round = RoundUp):
        mpfr_a = Number(a)
        return square(mpfr_a)

def sqr_down(a):
    with context(get_context(), round = RoundDown):
        mpfr_a = Number(a)
        return square(mpfr_a)
