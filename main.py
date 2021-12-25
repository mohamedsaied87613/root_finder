from math import *
import timeit
from sympy import *
from numpy.distutils.fcompiler import none
from sympy.abc import x
import numpy as np


class Methods:

    def __init__(self, func, es, max_iterations, ui_interface):
        self.ui_interface = ui_interface
        self.func = func
        self.max_iterations = max_iterations
        self.es = es
        self.ea = 0
        self.root = None

    def bisection(self, xl, xu):

        f = lambdify(x, self.func)

        if f(xl) * f(xu) <= 0:
            start = timeit.default_timer()

            xr = 0
            for i in range(1, self.max_iterations + 1):

                fl = f(xl)
                xrold = xr
                xr = (xu + xl) / 2
                fr = f(xr)

                # update
                if fr * fl < 0:
                    xu = xr
                elif fr * fl > 0:
                    xl = xr
                elif fr * fl == 0:
                    if fl == 0:
                        xr = xl
                    self.ea = 0
                    self.ui_interface.setItem(xl, i, 0)
                    self.ui_interface.setItem(xu, i, 1)
                    self.ui_interface.setItem(xr, i, 2)
                    self.ui_interface.setItem(self.ea, i, 3)
                    break

                self.ea = fabs(((xu - xl) / (xu + xl)) * 100)

                self.ui_interface.setItem(xl, i, 0)
                self.ui_interface.setItem(xu, i, 1)
                self.ui_interface.setItem(xr, i, 2)
                self.ui_interface.setItem(self.ea, i, 3)

                if self.ea < self.es:
                    break

            self.root = xr
            # time
            end = timeit.default_timer()
            self.ui_interface.setTime((end - start))

        else:
            self.ui_interface.alert_msg("No sign Change over the interval!")

    def false_position(self, xl, xu):

        f = lambdify(x, self.func)

        if f(xl) * f(xu) <= 0:
            start = timeit.default_timer()

            xr = 0

            for i in range(1, self.max_iterations + 1):

                fl = f(xl)
                fxu = f(xu)
                xrold = xr
                xr = ((xl * fxu) - (xu * fl)) / (fxu - fl)
                fr = f(xr)

                if fr < 0:
                    xl = xr
                if fr > 0:
                    xu = xr
                if fr == 0:
                    self.ea = 0
                    self.ui_interface.setItem(xl, i, 0)
                    self.ui_interface.setItem(xu, i, 1)
                    self.ui_interface.setItem(xr, i, 2)
                    self.ui_interface.setItem(self.ea, i, 3)
                    break

                self.ea = fabs(((xu - xl) / (xu + xl)) * 100)

                self.ui_interface.setItem(xl, i, 0)
                self.ui_interface.setItem(xu, i, 1)
                self.ui_interface.setItem(xr, i, 2)
                self.ui_interface.setItem(self.ea, i, 3)

                if self.ea < self.es:
                    break

            self.root = xr
            # time
            end = timeit.default_timer()
            self.ui_interface.setTime((end - start))

        else:
            self.ui_interface.alert_msg("No sign Change over the interval!")

    def fixed_point(self, gx, xi):
        start = timeit.default_timer()

        xr = xi
        g = lambdify(x, gx)

        for i in range(1, self.max_iterations + 1):

            xrold = xr
            xr = g(xrold)

            if xr != 0:
                self.ea = fabs((xr - xrold) * 100 / xr)

            self.ui_interface.setItem(xrold, i, 1)
            self.ui_interface.setItem(xr, i, 2)
            self.ui_interface.setItem(self.ea, i, 3)

            if self.ea < self.es:
                break

        self.root = xr
        # time
        end = timeit.default_timer()
        self.ui_interface.setTime((end - start))

    def newton_raphson(self, xi):
        start = timeit.default_timer()

        xr = xi

        fx = lambdify(x, self.func)
        fdx = diff(self.func, x)
        fdx = lambdify(x, fdx)

        for i in range(1, self.max_iterations + 1):

            xrold = xr
            numerator = fx(xr)
            denominator = fdx(xr)
            xr = xrold - (numerator / denominator)

            if xr != 0:
                self.ea = fabs((xr - xrold) * 100 / xr)

            self.ui_interface.setItem(xrold, i, 1)
            self.ui_interface.setItem(xr, i, 2)
            self.ui_interface.setItem(self.ea, i, 3)

            if self.ea < self.es:
                break

        self.root = xr
        # time
        end = timeit.default_timer()
        self.ui_interface.setTime((end - start))

    def secant(self, xi, xj):
        start = timeit.default_timer()

        xr = 0

        fx = lambdify(x, self.func)

        for i in range(1, self.max_iterations + 1):

            numerator = fx(xi) * (xi - xj)
            denominator = fx(xi) - fx(xj)
            xr = xi - (numerator / denominator)

            if xr != 0:
                self.ea = fabs((xr - xi) * 100 / xr)

            self.ui_interface.setItem(xj, i, 0)
            self.ui_interface.setItem(xi, i, 1)
            self.ui_interface.setItem(xr, i, 2)
            self.ui_interface.setItem(self.ea, i, 3)

            if self.ea < self.es:
                break

            xj = xi
            xi = xr

        self.root = xr
        # time
        end = timeit.default_timer()
        self.ui_interface.setTime((end - start))
