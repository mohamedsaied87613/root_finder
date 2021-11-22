
from math import *
import timeit
from sympy import *

from numpy.distutils.fcompiler import none


class Methods:

    def __init__(self, func, error=0.00001, it=50):
        self.func = func
        # self.fl = none
        # self.fu = none
        self.error = error
        self.count = 0
        # while self.error != 1:
        #     self.error = self.error * 10
        #     self.count += 1
        self.it = it
        self.xr = none
        self.fr = none
        self.bis = none

    def bisection(self, xl, xu):
        start = timeit.default_timer()
        self.xl = xl
        self.xu = xu
        self.bis_error = none
        prev = none
        for i in range(1, self.it):
            self.xr = (self.xu + self.xl) / 2
            x = self.xr
            self.fr = eval(self.func)
            x = self.xl
            self.fl = eval(self.func)

            print("it", i, "xl=", self.xl, "xu=", self.xu, "xr=", self.xr, "fxl=", self.fl, "fxr=", self.fr)
            # check persion
            #    c = str(self.xr)[::-1].find('.')
            #    if c > self.count:
            #        break

            if self.fr * self.fl < 0:
                self.xu = self.xr
            elif self.fr * self.fl > 0:
                self.xl = self.xr
            elif self.fr * self.fl == 0:
                break
            if i != 1:
                self.bis_error = abs(self.xr - self.prev) / abs(self.xr)
                if self.bis_error < self.error:
                    print("finito", self.bis_error - self.error)
                    break
                print("prev=", self.prev, "error=", self.bis_error)

            self.prev = self.xr

        # root
        self.bis_root = self.xr
        # it
        self.bis_it = i
        # time
        end = timeit.default_timer()
        self.bis_time = (end - start)
        # per , all_iterations

    def false_position(self, xl, xu):
        start = timeit.default_timer()
        self.xl = xl
        self.xu = xu
        self.fp_error = none
        self.fp_root = none
        prev = none
        for i in range(1, self.it):
            x = self.xl
            self.fl = eval(self.func)
            x = self.xu
            self.fu = eval(self.func)
            self.xr = ((self.xl * self.fu) - (self.xu * self.fl)) / (self.fu - self.fl)
            x = self.xr
            self.fr = eval(self.func)
            print("it", i, "xl=", self.xl, "fl=", self.fl, "xu=", self.xu, "fu=", self.fu, "xr=", self.xr, "fr=",
                  self.fr)
            if self.fr < 0:
                self.xl = self.xr
            if self.fr > 0:
                self.xu = self.xr
            if self.fr == 0:
                break
            if i != 1:
                self.fp_error = abs(self.xr - self.prev) / abs(self.xr)
                if self.fp_error < self.error:
                    print("finito", self.fp_error - self.error)
                    break
                print("prev=", self.prev, "error=", self.fp_error)

            self.prev = self.xr

            # root
        self.fp_root = self.xr
        # it
        self.fp_it = i

        # time
        end = timeit.default_timer()
        self.fp_time = (end - start)
        # per , all_iterations

    def fixed_point(self, gx, guess):
        start = timeit.default_timer()
        self.gx = gx
        self.guess = guess
        self.xr = self.guess
        prev = 0

        for i in range(1, self.it):
            # if guess =0 fixed error /0
            if self.xr != 0:
                self.fixed_error = abs((self.xr - prev) / self.xr)
                prev = self.xr

                print("it=", i, "xr=", self.xr, "error=", self.fixed_error)
                #                print("self=",self.error)
                if self.fixed_error < self.error:
                    print("done   it=", i, "error=", self.fixed_error)
                    break
            x = self.guess
            self.xr = eval(gx)
            self.guess = self.xr

        self.fixed_it = i
        self.fixed_root = self.xr
        # time
        end = timeit.default_timer()
        self.fixed_time = (end - start)

    def newton_raphson(self, root):
        start = timeit.default_timer()
        self.xr = root
        prev = root
        x = Symbol('x')
        for i in range(1, self.it):
            print(self.xr)
            sec = lambdify(x, eval(self.func))
            sec = sec(self.xr)
            third = lambdify(x, (diff(eval(self.func), x)))
            third = third(self.xr)
            self.xr = self.xr - sec / third
            self.newton_error = abs(self.xr - prev / self.xr)

            if self.newton_error < self.error:
                break
            prev = self.xr
        self.newton_it = i
        self.newton_root = self.xr
        # time
        end = timeit.default_timer()
        self.newton_time = (end - start)


func = "x**3 - x - 1"

xl = 1
xu = 2
it = 11
error = 0.00001
cl = Methods(func, it=it + 1)
cl.newton_raphson(1.5)
print(cl.newton_error, cl.newton_time, cl.newton_root, cl.newton_it)
