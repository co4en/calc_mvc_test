import sys
import math
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication
from mw import *
from abc import ABCMeta
from PyQt5 import QtCore

from abc import ABCMeta, abstractmethod


class Observer(metaclass=ABCMeta):
   
    @abstractmethod
    def modelIsChanged(self):
        
        pass


from abc import ABCMeta
from PyQt5 import QtCore


class Meta(type(QtCore.QObject), ABCMeta):
    pass


class Money:
    def __init__(self, number):
        self.num = number
        self.w_p = int(number)
        self.frec = int((number - int(number)) * 100)
        self._Observers = []

    def __add__(self, other):
        self.num += other.num

    def __sub__(self, other):
        self.num -= other.num

    def procn(self, obj, k):
        obj *= (k * 0.01)
        return obj

    def mprint(self):
        print(str(self.w_p) + ',' + str(self.frec))

    def convert(self, obj, valuta):
        if valuta == '$':
            obj = obj * (1.0 / 62.77)
            self.w_p = int(obj)
            self.frec = int((obj - int(obj)) * 100)
            return round(obj, 2)
        elif valuta == 'r':
            obj = obj * 62.77
            self.w_p = int(obj)
            self.frec = int((obj - int(obj)) * 100)
            return math.floor(obj) + 1
        else:
            obj = obj

    def addObserver(self, inObserver):
        self._Observers.append(inObserver)

    def removeObserver(self, inObserver):
        self._Observers.remove(inObserver)

    def notifyObservers(self):
        for x in self._Observers:
            x.modelIsChanged()


class rouble(Money):
    def __init__(self, rub, kop):
        super().__init__(rub + kop * 0.01)


class dollar(Money):
    def __init__(self, dol, cent):
        super().__init__(dol + cent * 0.01)


class model(rouble, dollar):
    def __init__(self):
        self.a1 = 0.0
        self.a2 = 0.0
        self.a3 = 0.0
        self.a4 = 0.0
        self.a5 = 0.0
        self.a6 = 0.0
        self.a7 = 0.0
        self.a8 = 0.0
        self.a9 = 0.0
        self.a10 = 0.0
        self.a11 = 0.0


class view(QtWidgets.QMainWindow):

    def __init__(self):
        super(view, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


class Controller():
    def __init__(self):
        self.m = model()
        self.mView = view()

        self.mView.ui.le_a.setText(str(0))
        self.mView.ui.le_b.setText(str(0))
        self.mView.ui.le_a_2.setText(str(0))
        self.mView.ui.le_b_2.setText(str(0))
        self.mView.ui.le_a_3.setText(str(0))
        self.mView.ui.le_b_3.setText(str(0))
        self.mView.ui.le_a_4.setText(str(0))
        self.mView.ui.le_a_4.setText(str(0))
        self.mView.ui.le_b_4.setText(str(0))
        self.mView.ui.le_a_5.setText(str(0))
        self.mView.ui.le_b_5.setText(str(0))

        self.mView.ui.le_a.editingFinished.connect(self.sum)
        self.mView.ui.le_b.editingFinished.connect(self.sum)
        self.mView.ui.le_a_2.editingFinished.connect(self.sub)
        self.mView.ui.le_b_2.editingFinished.connect(self.sub)
        self.mView.ui.le_a_3.editingFinished.connect(self.proc)
        self.mView.ui.le_b_3.editingFinished.connect(self.proc)
        self.mView.ui.le_a_4.editingFinished.connect(self.convert)
        self.mView.ui.le_b_4.editingFinished.connect(self.convert)
        self.mView.ui.le_a_5.editingFinished.connect(self.convert)
        self.mView.ui.le_b_5.editingFinished.connect(self.convert)


    def sum(self):
        self.mView.ui.le_result.clear()
        a = self.mView.ui.le_a.text()
        b = self.mView.ui.le_b.text()
        h = str(a)
        l = str(b)
        self.m.a1 = float(h)
        self.m.a2 = float(l)
        self.m.a3 = self.m.a1.__add__(self.m.a2)
        print("go")
        self.mView.ui.le_result.setText(str(self.m.a3))

    def sub(self):
        self.mView.ui.le_result_2.clear()
        a = self.mView.ui.le_a_2.text()
        b = self.mView.ui.le_b_2.text()
        h = str(a)
        l = str(b)
        self.m.a4 = float(h)
        self.m.a5 = float(l)
        self.m.a6 = self.m.a4.__sub__(self.m.a5)

        print("go")
        self.mView.ui.le_result_2.setText(str(self.m.a6))

    def proc(self):
        self.mView.ui.le_result_3.clear()
        a = self.mView.ui.le_a_3.text()
        b = self.mView.ui.le_b_3.text()
        h = str(a)
        l = str(b)
        self.m.a7 = float(h)
        self.m.a8 = float(l)
        self.m.a9 = self.m.procn(self.m.a7, self.m.a8)

        print("go")
        self.mView.ui.le_result_3.setText(str(self.m.a9))

    def convert(self):
        a1 = self.mView.ui.le_a_4.text()

        a2 = self.mView.ui.le_a_5.text()

        h1 = str(a1)
        k1 = float(h1)
        self.m.a10 = self.m.convert(float(k1), '$')
        print("go")
        self.mView.ui.le_b_4.setText(str(self.m.a10))
        h2 = str(a2)
        k2 = float(h2)
        self.m.a11 = self.m.convert(float(k2), 'r')
        print("go")
        self.mView.ui.le_b_5.setText(str(self.m.a11))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    application = Controller()
    application.mView.show()
    sys.setrecursionlimit(3000)
    sys.exit(app.exec_())
