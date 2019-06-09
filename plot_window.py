from PyQt5 import QtCore, QtGui, QtWidgets
from table import Ui_Form

import pyqtgraph as pg
from pyqtgraph import PlotWidget
from pyqtgraph.Qt import QtGui, QtCore
import numpy as np


class Ui_Dialog(object):
    def setupUi(self, Dialog, gen):
        pg.setConfigOption('background', 'w')
        pg.setConfigOption('foreground', 'k')
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 900)
        self.a = 13
        self.i = 0
        self.flag = 0
        self.gen = gen
        (xrange, yrange) = self.makeVector()
        self.next = QtWidgets.QPushButton(Dialog)
        self.next.setGeometry(QtCore.QRect(496, 863, 93, 28))
        self.next.setObjectName("next")
        self.showtable = QtWidgets.QPushButton(Dialog)
        self.showtable.setGeometry(QtCore.QRect(10, 863, 93, 28))
        self.showtable.setObjectName("showtable")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(220, 863, 171, 21))
        self.label.setObjectName("label")
        self.plotw = PlotWidget(Dialog)
        self.plotw.setGeometry(QtCore.QRect(0, 0, 607, 854))
        self.plotw.setObjectName("plotw")
        self.plotw.getViewBox().invertX(True)
        self.plotw.plot([1, -xrange-0.5], [0, 0], pen='k')
        self.plotw.plot([0, 0], [-1, yrange+0.5], pen='k')
        self.plotw.setXRange(0, -xrange)
        self.plotw.getViewBox().setAspectLocked(True)
        self.plotw.setYRange(0, yrange)
        self.plotw.getPlotItem().getAxis("bottom").setLabel(text='d', units='cm')
        self.plotw.getPlotItem().getAxis("left").setLabel(text='q', units='cm')
        self.plotw.addLegend()
        self.initUI()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def initUI(self):
        self.next.clicked.connect(self.plotDiag)
        self.showtable.clicked.connect(self.showTable)

    def makeVector(self):
        Iqpu = np.absolute(self.gen.Igpu) * np.sin(np.radians(self.gen.alfa))
        Idpu = -np.absolute(self.gen.Igpu) * np.cos(np.radians(self.gen.alfa))
        Uqpu = np.absolute(self.gen.Ugpu) * np.sin(np.radians(self.gen.alfa) + np.radians(self.gen.phi))
        Udpu = -np.absolute(self.gen.Ugpu) * np.cos(np.radians(self.gen.alfa) + np.radians(self.gen.phi))
        C = (0, np.absolute(self.gen.Ugpu + (self.gen.Xq * self.gen.Igpu) * 1j))
        B = (Udpu, Uqpu)
        OA = self.gen.OA
        CA = np.absolute(self.gen.Ugpu) * np.sin(np.radians(self.gen.phi)) + np.absolute(self.gen.Igpu) * self.gen.Xq
        if 2 * C[1] != 0:
            y_a = (OA ** 2 + C[1] ** 2 - CA ** 2) / (2 * C[1])
        else:
            y_a = 0
        x_a = -np.sqrt(OA ** 2 - y_a ** 2)
        A = (x_a, y_a)
        IX2 = (B[1] - Idpu * self.gen.Xd2, B[0] + Iqpu * self.gen.Xq2)
        IX1 = (B[1] - Idpu * self.gen.Xd1, B[0] + Iqpu * self.gen.Xq1)
        IX = (B[1] - Idpu * self.gen.Xd, B[0] + Iqpu * self.gen.Xq)

        xrange = -Idpu
        self.x = [0, Idpu, 0, 0, 0, Idpu, 0, Udpu, 0, 0, 0, Udpu]
        self.y = [0, Iqpu, 0, Iqpu, 0, 0, 0, Uqpu, 0, Uqpu, 0, 0]

        if np.absolute(self.gen.Ugpu) > np.absolute(self.gen.Igpu):
            pass
            self.limit = 41
            self.x = self.x + [0, A[0]]
            self.y = self.y + [0, A[1]]
            xrange = -A[0]
        else:
            self.limit = 39
        self.flag = self.limit

        self.x = self.x + [A[0], C[0], B[0], B[0], B[0], B[0], B[0], B[0], B[0], IX[1], B[0], IX1[1], B[0], IX2[1],
                           B[0], IX[1], B[0], IX1[1], B[0], IX2[1], 0, IX[1], 0, IX1[1], 0, IX2[1]]
        self.y = self.y + [A[1], C[1], B[1], IX[0], B[1], IX1[0], B[1], IX2[0], IX[0], IX[0], IX1[0], IX1[0], IX2[0],
                           IX2[0], B[1], IX[0], B[1], IX1[0], B[1], IX2[0], 0, IX[0], 0, IX1[0], 0, IX2[0]]

        return xrange, IX[0]

    def plotDiag(self):
        if self.i < 5:
            color = 4
        elif self.i < 11:
            color = 7
        elif self.i < self.a:
            color = 6
            if self.flag == 41:
                self.flag = 0
                self.a = 15
                color = 4
        elif self.i in [self.a + 1, self.a + 7, self.a + 13, self.a + 19]:
            color = 0
        elif self.i in [self.a + 3, self.a + 9, self.a + 15, self.a + 21]:
            color = 11
        elif self.i in [self.a + 5, self.a + 11, self.a + 17, self.a + 23]:
            color = 13.9

        pen = pg.mkPen(color, width=3)
        if self.i < self.limit:
            if self.i == 0:
                self.plotw.plot(self.x[self.i:self.i + 2], self.y[self.i:self.i + 2], pen=pen, name='I')
            elif self.i == 6:
                self.plotw.plot(self.x[self.i:self.i + 2], self.y[self.i:self.i + 2], pen=pen, name='U')
            elif self.i == self.a - 1:
                self.plotw.plot(self.x[self.i:self.i + 2], self.y[self.i:self.i + 2], pen=pen, name='AC')
            elif self.i == self.a + 1:
                self.plotw.plot(self.x[self.i:self.i + 2], self.y[self.i:self.i + 2], pen=pen, name='E')
            elif self.i == self.a + 3:
                self.plotw.plot(self.x[self.i:self.i + 2], self.y[self.i:self.i + 2], pen=pen, name="E'")
            elif self.i == self.a + 5:
                self.plotw.plot(self.x[self.i:self.i + 2], self.y[self.i:self.i + 2], pen=pen, name='E"')
            else:
                self.plotw.plot(self.x[self.i:self.i + 2], self.y[self.i:self.i + 2], pen=pen)
            self.i = self.i + 2
            if self.i == self.limit - 1:
                self.next.setDisabled(True)

    def showTable(self):
        self.window = QtWidgets.QMainWindow()
        self.ui2 = Ui_Form()
        self.ui2.setupUi(self.window)
        self.ui2.passValues(self.x, self.y)
        self.window.show()
        self.window.setFixedSize(self.window.size())

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Vector Diagram", "Vector Diagram"))
        self.next.setText(_translate("Dialog", "Next"))
        self.showtable.setText(_translate("Dialog", "Show table"))
        self.label.setText(_translate("Dialog", "assumed scale is 1 cm for p.u "))
