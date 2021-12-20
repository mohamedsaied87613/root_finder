from math import *
import tkinter as tk

import PyQt5
import matplotlib.pyplot as plt
from tkinter import ttk
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QHeaderView, QScrollBar, QTableWidgetItem

from main import Methods


class Ui_MainWindow(object):
    text = ""
    gtext = ""

    def convert_to_function(self, text, x):
        return eval(text,
                    {'__builtins__': {'cos': cos, "x": x, "sin": sin, "e": e, "tan": tan, "sqrt": sqrt, "pow": pow,
                                      "log": log, "pi": pi, "fabs": fabs}}, None)

    def f(self, x):
        return self.convert_to_function(self.text, x)

    def g(self, x):
        return self.convert_to_function(self.gtext, x)

    def read_file(self):
        file = open("Numerical.txt", "r")

        self.functionField.setText(file.readline())
        self.functionField_G.setText(file.readline())

        file.close()

    def alert_msg(self, msg):
        NORM_FONT = ("DIN", 10)
        popup = tk.Tk()
        popup.wm_title("Test Failed")
        label = ttk.Label(popup, text=msg, font=NORM_FONT)
        label.pack(side="top", fill="x", pady=60, padx=60)
        B1 = ttk.Button(popup, text="done", command=popup.destroy)
        B1.pack()
        popup.mainloop()

    def change_labels(self, MainWindow, label0, label1, label2, label3):
        _translate = QtCore.QCoreApplication.translate

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", label0))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", label1))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", label2))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", label3))

    # _________________________________________________________________________________________________________________#

    def evaluate(self, method=""):
        self.text = self.functionField.text()
        self.gtext = self.functionField_G.text()

        root = 0

        if method == "Bisection":
            xl = float(self.lineEdit_x_low.text())
            xu = float(self.lineEdit_x_up.text())
            es = fabs(float(self.lineEdit_tolerance.text()))
            iterations = abs(int(self.lineEdit_iterations.text()))

            if xl == xu:
                self.alert_msg("Enter An Interval!")
            elif xl > xu:
                self.alert_msg("Xl must be smaller than Xu !")
            elif self.text == "":
                self.alert_msg("Enter An Equation!")
            else:
                self.tableWidget.setRowCount(iterations + 1)
                self.tableWidget.clear()
                for r in range(iterations + 1):
                    item = QTableWidgetItem("{}".format(r))
                    self.tableWidget.setVerticalHeaderItem(r, item)

                try:
                    my_method = Methods(self.text, es, iterations, self)
                    my_method.bisection(xl, xu)
                    root = my_method.root
                except:
                    self.alert_msg("Couldn't Solve Equation!")


        elif method == "False":

            xl = float(self.lineEdit_x_low.text())
            xu = float(self.lineEdit_x_up.text())
            es = fabs(float(self.lineEdit_tolerance.text()))
            iterations = abs(int(self.lineEdit_iterations.text()))

            if xl == xu:
                self.alert_msg("Enter An Interval!")
            elif xl > xu:
                self.alert_msg("Xl must be smaller than Xu !")
            elif self.text == "":
                self.alert_msg("Enter An Equation!")
            else:
                self.tableWidget.setRowCount(iterations + 1)
                self.tableWidget.clear()
                for r in range(iterations + 1):
                    item = QTableWidgetItem("{}".format(r))
                    self.tableWidget.setVerticalHeaderItem(r, item)

                try:
                    my_method = Methods(self.text, es, iterations, self)
                    my_method.false_position(xl, xu)
                    root = my_method.root
                except:
                    self.alert_msg("Couldn't Solve Equation!")

        elif method == "Fixed Point":
            xi = float(self.lineEdit_x_low.text())
            es = fabs(float(self.lineEdit_tolerance.text()))
            iterations = abs(int(self.lineEdit_iterations.text()))

            if self.gtext == "":
                self.alert_msg("Enter An Equation!")
            else:
                self.tableWidget.setRowCount(iterations + 1)
                self.tableWidget.clear()
                for r in range(iterations + 1):
                    item = QTableWidgetItem("{}".format(r))
                    self.tableWidget.setVerticalHeaderItem(r, item)

                try:
                    my_method = Methods(self.text, es, iterations, self)
                    my_method.fixed_point(self.gtext, xi)
                    root = my_method.root
                except:
                    self.alert_msg("Couldn't Solve Equation!")

        elif method == "Newton Raphson":
            xi = float(self.lineEdit_x_low.text())
            es = fabs(float(self.lineEdit_tolerance.text()))
            iterations = abs(int(self.lineEdit_iterations.text()))

            if self.text == "":
                self.alert_msg("Enter An Equation!")
            else:
                self.tableWidget.setRowCount(iterations + 1)
                self.tableWidget.clear()
                for r in range(iterations + 1):
                    item = QTableWidgetItem("{}".format(r))
                    self.tableWidget.setVerticalHeaderItem(r, item)

                try:
                    my_method = Methods(self.text, es, iterations, self)
                    my_method.newton_raphson(xi)
                    root = my_method.root
                except:
                    self.alert_msg("Couldn't Solve Equation!")

        elif method == "Secant":
            xi = float(self.lineEdit_x_low.text())
            xj = float(self.lineEdit_x_up.text())
            es = fabs(float(self.lineEdit_tolerance.text()))
            iterations = abs(int(self.lineEdit_iterations.text()))

            if xi == xj:
                self.alert_msg("Enter Different Initial Values!")
            elif xj > xi:
                self.alert_msg("Xi-1 must be smaller than Xi !")
            elif self.text == "":
                self.alert_msg("Enter An Equation!")
            else:
                self.tableWidget.setRowCount(iterations + 1)
                self.tableWidget.clear()
                for r in range(iterations + 1):
                    item = QTableWidgetItem("{}".format(r))
                    self.tableWidget.setVerticalHeaderItem(r, item)

                try:
                    my_method = Methods(self.text, es, iterations, self)
                    my_method.secant(xi, xj)
                    root = my_method.root
                except:
                    self.alert_msg("Couldn't Solve Equation!")

        self.textEdit.setText(str(root))

    def setItem(self, text, i, j):
        val = str(text)
        item = QtWidgets.QTableWidgetItem(val)
        self.tableWidget.setItem(i, j, item)

    def getItem(self, i, j):
        return self.tableWidget.item(i, j).text()

    # _________________________________________________________________________________________________________________#
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1023, 1163)
        font = QtGui.QFont()
        font.setPointSize(14)
        MainWindow.setFont(font)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # _________________________________________________________________________________________________________________#
        self.functionField = QtWidgets.QLineEdit(self.centralwidget)
        self.functionField.setGeometry(QtCore.QRect(100, 20, 631, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.functionField.setFont(font)
        self.functionField.setText("")
        self.functionField.setObjectName("functionField")
        # _________________________________________________________________________________________________________________#
        #
        self.button_method_bisection = QtWidgets.QPushButton(self.centralwidget)
        self.button_method_bisection.setGeometry(QtCore.QRect(100, 190, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button_method_bisection.setFont(font)
        self.button_method_bisection.setObjectName("button_method_bisection")
        # _________________________________________________________________________________________________________________#
        self.button_method_fixedPoint = QtWidgets.QPushButton(self.centralwidget)
        self.button_method_fixedPoint.setGeometry(QtCore.QRect(325, 190, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button_method_fixedPoint.setFont(font)
        self.button_method_fixedPoint.setObjectName("button_method_fixedPoint")
        # _________________________________________________________________________________________________________________#
        self.button_method_falsePosition = QtWidgets.QPushButton(self.centralwidget)
        self.button_method_falsePosition.setGeometry(QtCore.QRect(550, 190, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button_method_falsePosition.setFont(font)
        self.button_method_falsePosition.setObjectName("button_method_falsePosition")
        # _________________________________________________________________________________________________________________#
        self.button_method_secant = QtWidgets.QPushButton(self.centralwidget)
        self.button_method_secant.setGeometry(QtCore.QRect(100, 250, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button_method_secant.setFont(font)
        self.button_method_secant.setObjectName("button_method_secant")
        # _________________________________________________________________________________________________________________#
        self.button_method_newtonRaphson = QtWidgets.QPushButton(self.centralwidget)
        self.button_method_newtonRaphson.setGeometry(QtCore.QRect(550, 250, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button_method_newtonRaphson.setFont(font)
        self.button_method_newtonRaphson.setObjectName("button_method_newtonRaphson")
        # _________________________________________________________________________________________________________________#
        self.button_READ = QtWidgets.QPushButton(self.centralwidget)
        self.button_READ.setGeometry(QtCore.QRect(590, 830, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button_READ.setFont(font)
        self.button_READ.setObjectName("button_READ")
        # _________________________________________________________________________________________________________________#
        self.label_x_up = QtWidgets.QLabel(self.centralwidget)
        self.label_x_up.setGeometry(QtCore.QRect(150, 330, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_x_up.setFont(font)
        self.label_x_up.setObjectName("label_x_up")

        self.lineEdit_x_up = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_x_up.setGeometry(QtCore.QRect(250, 340, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_x_up.setFont(font)
        self.lineEdit_x_up.setObjectName("lineEdit_x_up")
        # _________________________________________________________________________________________________________________#
        self.label_x_low = QtWidgets.QLabel(self.centralwidget)
        self.label_x_low.setGeometry(QtCore.QRect(150, 300, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_x_low.setFont(font)
        self.label_x_low.setObjectName("label_x_low")

        self.lineEdit_x_low = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_x_low.setGeometry(QtCore.QRect(250, 310, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_x_low.setFont(font)
        self.lineEdit_x_low.setObjectName("lineEdit_x_low")
        # _________________________________________________________________________________________________________________#
        self.label_iteration = QtWidgets.QLabel(self.centralwidget)
        self.label_iteration.setGeometry(QtCore.QRect(520, 330, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_iteration.setFont(font)
        self.label_iteration.setObjectName("label_iteration")

        self.lineEdit_iterations = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_iterations.setGeometry(QtCore.QRect(620, 340, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_iterations.setFont(font)
        self.lineEdit_iterations.setObjectName("lineEdit_iterations")
        # _________________________________________________________________________________________________________________#
        self.label_tolerance = QtWidgets.QLabel(self.centralwidget)
        self.label_tolerance.setGeometry(QtCore.QRect(520, 300, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_tolerance.setFont(font)
        self.label_tolerance.setObjectName("label_tolerance")

        self.lineEdit_tolerance = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_tolerance.setGeometry(QtCore.QRect(620, 310, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_tolerance.setFont(font)
        self.lineEdit_tolerance.setObjectName("lineEdit_tolerance")
        # _________________________________________________________________________________________________________________#

        self.line_up = QtWidgets.QFrame(self.centralwidget)
        self.line_up.setGeometry(QtCore.QRect(20, 160, 771, 20))
        self.line_up.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_up.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_up.setObjectName("line_up")

        self.line_down = QtWidgets.QFrame(self.centralwidget)
        self.line_down.setGeometry(QtCore.QRect(20, 370, 771, 20))
        self.line_down.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_down.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_down.setObjectName("line_down")
        # _________________________________________________________________________________________________________________#

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 830, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(40, 400, 741, 401))
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(51)

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(160, 830, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.textEdit.setFont(font)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")

        self.functionField_G = QtWidgets.QLineEdit(self.centralwidget)
        self.functionField_G.setGeometry(QtCore.QRect(190, 110, 431, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.functionField_G.setFont(font)
        self.functionField_G.setObjectName("functionField_G")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 51, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 110, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.button_RESET = QtWidgets.QPushButton(self.centralwidget)
        self.button_RESET.setGeometry(QtCore.QRect(490, 830, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button_RESET.setFont(font)
        self.button_RESET.setObjectName("button_RESET")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 823, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # button Methods
        self.button_method_bisection.clicked.connect(lambda: self.evaluate("Bisection"))
        self.button_method_fixedPoint.clicked.connect(lambda: self.evaluate("Fixed Point"))
        self.button_method_falsePosition.clicked.connect(lambda: self.evaluate("False"))
        self.button_method_newtonRaphson.clicked.connect(lambda: self.evaluate("Newton Raphson"))
        self.button_method_secant.clicked.connect(lambda: self.evaluate("Secant"))

        self.button_method_bisection.clicked.connect(
            lambda: self.change_labels(MainWindow, "X(l)", "X(u)", "X(r)", "ea %"))
        self.button_method_falsePosition.clicked.connect(
            lambda: self.change_labels(MainWindow, "X(l)", "X(u)", "X(r)", "ea %"))
        self.button_method_fixedPoint.clicked.connect(
            lambda: self.change_labels(MainWindow, "-", "X(i)", "X(i+1)", "ea %"))
        self.button_method_newtonRaphson.clicked.connect(
            lambda: self.change_labels(MainWindow, "-", "X(i)", "X(i+1)", "ea %"))
        self.button_method_secant.clicked.connect(
            lambda: self.change_labels(MainWindow, "X(i-1)", "X(i)", "X(i+1)", "ea %"))

        self.button_RESET.clicked.connect(self.tableWidget.clear)
        self.button_RESET.clicked.connect(lambda: self.functionField.setText(""))
        self.button_RESET.clicked.connect(lambda: self.functionField_G.setText(""))
        self.button_RESET.clicked.connect(lambda: self.textEdit.setText("0"))
        self.button_READ.clicked.connect(self.read_file)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Numerical Project"))
        self.button_method_bisection.setText(_translate("MainWindow", "Bisection"))
        self.button_method_fixedPoint.setText(_translate("MainWindow", "Fixed-Point"))
        self.button_method_falsePosition.setText(_translate("MainWindow", "False Position"))
        self.button_method_secant.setText(_translate("MainWindow", "Secant"))
        self.button_method_newtonRaphson.setText(_translate("MainWindow", "Newton-Raphson"))
        self.button_READ.setText(_translate("MainWindow", "Import File"))
        self.label_x_up.setText(_translate("MainWindow", "X(u) / X(i-1)"))
        self.label_x_low.setText(_translate("MainWindow", "X(l)  / X(i)"))
        self.lineEdit_iterations.setText(_translate("MainWindow", "50"))
        self.lineEdit_tolerance.setText(_translate("MainWindow", "0.00001"))
        self.lineEdit_x_low.setText(_translate("MainWindow", "0"))
        self.lineEdit_x_up.setText(_translate("MainWindow", "0"))
        self.label_iteration.setText(_translate("MainWindow", "Iterations:"))
        self.label_tolerance.setText(_translate("MainWindow", "Tolerance:"))
        self.label_2.setText(_translate("MainWindow", "X (root) = "))
        self.tableWidget.setSortingEnabled(False)

        # for i in range(50):
        #     item = self.tableWidget.verticalHeaderItem(i)
        #     item.setText(_translate("MainWindow", '%d' % i))

        self.textEdit.setHtml(_translate("MainWindow",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">0</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "f(x)"))
        self.label_3.setText(_translate("MainWindow", "g(x) "))
        self.button_RESET.setText(_translate("MainWindow", "Clc"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
