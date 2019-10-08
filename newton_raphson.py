def newton_raphson(func, x0, tol, max_iter, f_prime):
    """
    Iterative function that calculates a functions root. Know as the Newton-Raphson method.
    :param func: the function handle
    :param x0: the initial guess to start approximations from
    :param tol: the tolerance interval [-tol,tol]
    :param max_iter: maximum number of iterations allowed
    :param f_prime: the derivative function -> computed without external libraries if None
    :return: the approximation of the root of xn
    """
    func_val = func(x0)  # the callable function return value is stored, expediency
    counter = 0

    while abs(func_val) > tol and counter < max_iter:

        if f_prime is None:
            func_prime_val = derive(func, x0)  # compute the derivative numerically.
        else:
            func_prime_val = f_prime(x0)  # compute the derivative normally

        try:
            x0 = x0 - float(func_val) / func_prime_val

        except ZeroDivisionError as e:
            print("Error - f_prime turned out as zero, x0 at %s" % x0)
            return e

        func_val = func(x0)  # recalculated the callable function
        counter += 1

    # the function call should terminate when f(xn) is in the interval, or when too many iterations
    if abs(func_val) > tol or counter > max_iter:
        raise RuntimeError("Error - No solution could be found with given constraints")
    return x0


def derive(function, value):
    h = 1.0e-10
    top = function(value + h) - function(value)
    bottom = h
    slope = top / bottom

    return float("%.3f" % slope)


# the test functions below.

def func(x):
    return x ** 2 - 9


def f_prime(x):
    return 2 * x


def func1(x):
    return 1 / x - 0.01


def f_prime1(x):
    return -1 / x ** 2


def func2(x):
    return x ** 4 - 1


def f_prime2(x):
    return 4 * x ** 3


if __name__ == "__main__":
    res = newton_raphson(func=func, x0=1000, tol=1.0e-6, max_iter=100, f_prime=f_prime)
    print("NR method: %s" % res)
    res1 = newton_raphson(func=func1, x0=1, tol=1.0e-6, max_iter=100, f_prime=f_prime1)
    print("NR method: %s" % res1)
    # finding the other root is dependant on using a different x0 at this point.
    res2 = newton_raphson(func=func2, x0=2, tol=1.0e-6, max_iter=100, f_prime=f_prime2)
    print("NR method: %s" % res2)
