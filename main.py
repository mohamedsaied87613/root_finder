import timeit
from sympy import *
from numpy.distutils.fcompiler import none
from sympy.abc import x
import numpy as np


class Methods:

    def __init__(self, func, rd, error=0.00001, it=50):
        self.func = func
        self.error = error
        self.it = it
        self.round = rd

        self.bis_root = none
        self.bis_it = 0
        self.bis_time = 0

        self.fp_root = none
        self.fp_it = 0
        self.fp_time = 0

        self.fixed_root = none
        self.fixed_it = 0
        self.fixed_time = 0

        self.newton_root = none
        self.newton_it = 0
        self.newton_time = 0

    def bisection(self, xl, xu):
        start = timeit.default_timer()
        i = none
        xr = none
        prev = 0
        f = lambdify(x, self.func)
        for i in range(1, self.it):
            xr = round((xu + xl) / 2, self.round)
            fr = round(f(xr), self.round)
            fl = round(f(xl), self.round)
            # update
            if fr * fl < 0:
                xu = xr
            elif fr * fl > 0:
                xl = xr
            elif fr * fl == 0:
                break
            # if i<3:
            bis_error = abs(xr - prev)
            print("it", i, "xl=", xl, "f(xl)=", fl, "xu=", xu, "xr=", xr, "f(xr)=", fr,
                  "prev=", prev, "error= ", bis_error)
            if bis_error < self.error:
                break
            prev = xr

        self.bis_root = xr
        # it
        self.bis_it = i
        # time
        end = timeit.default_timer()
        self.bis_time = (end - start)
        # per , all_iterations

    def false_position(self, xl, xu):

        start = timeit.default_timer()
        i = none
        xr = none
        prev = 0
        f = lambdify(x, self.func)

        for i in range(1, self.it):
            fl = round(f(xl), self.round)
            fxu = round(f(xu), self.round)
            xr = round(((xl * fxu) - (xu * fl)) / (fxu - fl), self.round)
            fr = round(f(xr), self.round)
            if fr < 0:
                xl = xr
            if fr > 0:
                xu = xr
            if fr == 0:
                break
            fp_error = abs(xr - prev)
            print("it", i, "xl=", xl, "f(xl)=", fl, "xu=", xu, "f(xu)=", fxu, "xr=", xr,
                  "f(xr)=", fr, "prev=", prev, "error=", fp_error)
            if fp_error < self.error:
                break
            prev = xr

        self.fp_root = xr
        # it
        self.fp_it = i
        # time
        end = timeit.default_timer()
        self.fp_time = (end - start)

    def fixed_point(self, gx, guess):
        start = timeit.default_timer()
        i = none
        Xr = guess
        prev = guess
        for i in range(1, self.it):
            gx = gx.replace("x", "Xr")
            Xr = round(eval(gx), self.round)
            fixed_error = abs(Xr - prev)
            print("i=", i, "xr=", Xr, "prev=", prev, "error=", fixed_error)
            prev = Xr
            if fixed_error < self.error:
                break

        self.fixed_root = Xr
        self.fixed_it = i
        end = timeit.default_timer()
        self.fixed_time = (end - start)

    def newton_raphson(self, guess, n_mod=1):
        start = timeit.default_timer()
        i = None
        xr = guess
        prev = xr
        # x (sympy.abc)
        fx = lambdify(x, self.func)
        fdx = diff(self.func, x)
        fddx = diff(fdx, x)
        fdx = lambdify(x, fdx)
        fddx = lambdify(x, fddx)
        for i in range(1, self.it):
            if n_mod != 0:
                numerator = round(fx(xr), self.round)
                denominator = round(fdx(xr), self.round)
                xr = round(xr - n_mod * (numerator / denominator), self.round)
                newton_error = abs(xr - prev)
                print("i=", i, "x=", prev, "fx=", numerator, "fdx=", denominator, "xr=", xr, "error=", newton_error)
                if newton_error < self.error:
                    break
                prev = xr
            elif n_mod == 0:
                numerator = round(fx(xr) * fdx(xr), 5)
                denominator = round(fdx(xr) ** 2 - fx(xr) * fddx(xr), 5)
                xr = round(xr - (numerator / denominator), 5)
                newton_error = abs(xr - prev)
                print("i=", i, "x=", prev, "fx=", numerator, "fdx=", denominator, "xr=", xr, "error=", newton_error)
                if newton_error < self.error:
                    break
                prev = xr

        self.newton_it = i
        self.newton_root = xr
        end = timeit.default_timer()
        self.newton_time = (end - start)


func1 = "x**3 -2*x**2-4*x+8"
g = "6/(x**2-7*x+14)"
x_l = 1
x_u = 2
it_ = 11
error_ = 0.0001
# rd rounding
round_d = 5
cl = Methods(func1, error=error_, rd=round_d)
# cl.bisection(1, 2)
# print(
# "-------------------------------------------------------------------------------------------------------------------------------------")
# cl.false_position(1, 2)
# print(
#    "-------------------------------------------------------------------------------------------------------------------------------------")

# cl.fixed_point(g, 1.5)
# print(
#    "-------------------------------------------------------------------------------------------------------------------------------------")

# n_mod= 0 second mod
# n_mod= 1 normal default
# n_mod=m first mod where m is the multiplicity of root
cl.newton_raphson(1.2, 2)
