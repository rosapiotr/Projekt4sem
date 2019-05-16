# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'plot_window.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget
import numpy as np


class Ui_Dialog(object):
    def setupUi(self, Dialog, gen):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 900)
        self.i = 0
        self.gen = gen
        (xrange, yrange) = self.makeVector()
        self.next = QtWidgets.QPushButton(Dialog)
        self.next.setGeometry(QtCore.QRect(496, 863, 93, 28))
        self.next.setObjectName("next")
        # self.gen = Generator()
        self.plotw = PlotWidget(Dialog)
        self.plotw.setGeometry(QtCore.QRect(0, 0, 607, 854))
        self.plotw.setObjectName("plotw")
        self.plotw.getViewBox().invertX(True)
        self.plotw.setXRange(0, -xrange)
        # self.plotw.setYRange(0, yrange)
        self.plotw.getViewBox().setAspectLocked(True)
        self.plotw.setYRange(0, yrange)
        self.plotw.getPlotItem().getAxis("bottom").setLabel(text='d')  # , units="x")
        self.plotw.getPlotItem().getAxis("left").setLabel(text='q')  # , units="y")
        self.initUI()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def initUI(self):
        self.next.clicked.connect(self.plotDiag)

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

        self.x = self.x + [A[0], C[0], B[0], B[0], B[0], B[0], B[0], B[0], B[0], IX2[1], B[0], IX1[1], B[0], IX[1],
                           B[0], IX2[1], B[0], IX1[1], B[0], IX[1], 0, IX2[1], 0, IX1[1], 0, IX[1]]
        self.y = self.y + [A[1], C[1], B[1], IX2[0], B[1], IX1[0], B[1], IX[0], IX2[0], IX2[0], IX1[0], IX1[0], IX[0],
                           IX[0], B[1], IX2[0], B[1], IX1[0], B[1], IX[0], 0, IX2[0], 0, IX1[0], 0, IX[0]]
        return xrange, IX[0]

    def plotDiag(self):
        if self.i < self.limit:
            self.plotw.plot(self.x[self.i:self.i + 2], self.y[self.i:self.i + 2])
            self.i = self.i + 2
            if self.i == self.limit - 1:
                self.next.setDisabled(True)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.next.setText(_translate("Dialog", "Next"))