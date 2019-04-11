from math import sqrt, exp, sin, cos
from numpy import conjugate, arctan, absolute, math


class Generator:
    def __init__(self):
        self.Sn = 0
        self.Sb = 0
        self.Ub = 0
        self.Xd = 0
        self.Xq = 0
        self.Xd1 = 0
        self.Xq1 = 0
        self.Xd2 = 0
        self.Xq2 = 0
        self.S2 = 0 + 0j
        self.Ug = 0 + 0j
        self.Zb = 0
        self.Ib = 0 + 0j
        self.S2pu = 0 + 0j
        self.Ugpu = 0 + 0j
        self.Igpu = 0 + 0j
        self.deltaIgpu = 0
        self.EQ = 0 + 0j
        self.phi = 0
        self.BC = 0
        self.OA = 0
        self.AB = 0
        self.alfa = 0
        self.gamma = 0
        self.Iqpu = 0
        self.Idpu = 0
        self.Uqpu = 0
        self.Udpu = 0
        self.Edpu2 = 0
        self.Eqpu2 = 0
        self.Edpu1 = 0
        self.Eqpu1 = 0
        self.Edpu = 0
        self.Eqpu = 0
        self.Epu = 0
        self.Epu1 = 0
        self.Epu2 = 0
        self.delta = 0

    def setSn(self, value):
        try:
            self.Sn = float(value)
        except ValueError:
            pass

    def setSb(self, value):
        try:
            self.Sb = float(value)
        except ValueError:
            pass

    def setUb(self, value):
        try:
            self.Ub = float(value)
        except ValueError:
            pass

    def setXd(self, value):
        try:
            self.Xd = float(value)
        except ValueError:
            pass

    def setXq(self, value):
        try:
            self.Xq = float(value)
        except ValueError:
            pass

    def setXd1(self, value):
        try:
            self.Xd1 = float(value)
        except ValueError:
            pass

    def setXq1(self, value):
        try:
            self.Xq1 = float(value)
        except ValueError:
            pass

    def setXd2(self, value):
        try:
            self.Xd2 = float(value)
        except ValueError:
            pass

    def setXq2(self, value):
        try:
            self.Xq2 = float(value)
        except ValueError:
            pass

    def setS2(self, value):
        try:
            self.S2 = complex(value)
        except ValueError:
            pass

    def setUg(self, value):
        try:
            self.Ug = complex(value)
        except ValueError:
            pass

    def setZb(self, value):
        try:
            self.Zb = float(value)
        except ValueError:
            pass

    def setIb(self, value):
        try:
            self.Ib = complex(value)
        except ValueError:
            pass

    def setS2pu(self, value):
        try:
            self.S2pu = complex(value)
        except ValueError:
            pass

    def setUgpu(self, value):
        try:
            self.Ugpu = complex(value)
        except ValueError:
            pass

    def setIgpu(self, value):
        try:
            self.Igpu = complex(value)
        except ValueError:
            pass

    def setdeltaIgpu(self, value):
        try:
            self.deltaIgpu = float(value)
        except ValueError:
            pass

    def setEQ(self, value):
        try:
            self.EQ = complex(value)
        except ValueError:
            pass

    def setphi(self, value):
        try:
            self.phi = float(value)
        except ValueError:
            pass

    def setBC(self, value):
        try:
            self.BC = float(value)
        except ValueError:
            pass

    def setOA(self, value):
        try:
            self.OA = float(value)
        except ValueError:
            pass

    def setAB(self, value):
        try:
            self.AB = float(value)
        except ValueError:
            pass

    def setalfa(self, value):
        try:
            self.alfa = float(value)
        except ValueError:
            pass

    def setgamma(self, value):
        try:
            self.gamma = float(value)
        except ValueError:
            pass

    def setIqpu(self, value):
        try:
            self.Iqpu = float(value)
        except ValueError:
            pass

    def setIdpu(self, value):
        try:
            self.Idpu = float(value)
        except ValueError:
            pass

    def setUqpu(self, value):
        try:
            self.Uqpu = float(value)
        except ValueError:
            pass

    def setUdpu(self, value):
        try:
            self.Udpu = float(value)
        except ValueError:
            pass

    def setEdpu2(self, value):
        try:
            self.Edpu2 = float(value)
        except ValueError:
            pass

    def setEqpu2(self, value):
        try:
            self.Eqpu2 = float(value)
        except ValueError:
            pass

    def setEdpu1(self, value):
        try:
            self.Edpu1 = float(value)
        except ValueError:
            pass

    def setEqpu1(self, value):
        try:
            self.Eqpu1 = float(value)
        except ValueError:
            pass

    def setEqpu(self, value):
        try:
            self.Eqpu = float(value)
        except ValueError:
            pass

    def setEdpu(self, value):
        try:
            self.Edpu = float(value)
        except ValueError:
            pass

    def setEpu(self, value):
        try:
            self.Epu = float(value)
        except ValueError:
            pass

    def setEpu1(self, value):
        try:
            self.Epu1 = float(value)
        except ValueError:
            pass

    def setEpu2(self, value):
        try:
            self.Epu2 = float(value)
        except ValueError:
            pass

    def setdelta(self, value):
        try:
            self.delta = float(value)
        except ValueError:
            pass

    @staticmethod
    def check_combo_VA(window):
        if (window.ui.comboSn.currentText()) == "KVA":
            mn = 1000
        elif (window.ui.comboSn.currentText()) == "MVA":
            mn = 1000000
        elif (window.ui.comboSn.currentText()) == "GVA":
            mn = 1000000000
        else:
            return 1
        return mn

    @staticmethod
    def check_combo_V(window):
        if (window.ui.comboUb.currentText()) == "KV":
            mn = 1000
        elif (window.ui.comboUb.currentText()) == "MV":
            mn = 1000000
        else:
            return 1
        return mn

    def calculate(self, window):
        Snm = Generator.check_combo_VA(window)
        Sbm = Generator.check_combo_VA(window)
        Ubm = Generator.check_combo_V(window)
        S2m = Generator.check_combo_VA(window)

        if window.position > 28:
            Ug = 1.05 * self.Ub * Ubm * (cos(math.pi/36) + 1j*sin(math.pi/36))
            window.ui.Ug.setText(str((round(Ug.real, 5) + round(Ug.imag, 5) * 1j))[1:-1])
        else:
            Ug = complex(window.ui.Ug.text())
        try:
            if window.position > 27:
                Zb = (self.Ub*Ubm)**2/(self.Sb*Sbm)
                window.ui.Zb.setText(str(round(Zb, 5)))
            if window.position > 26:
                Ib = conjugate((self.Sb*Sbm)/(sqrt(3)*self.Ub*Ubm))
                window.ui.Ib.setText(str((round(Ib.real, 5) + round(Ib.imag, 5) * 1j))[1:-1])
            if window.position > 25:
                S2pu = complex(self.S2*S2m)/(self.Sb*Sbm)
                window.ui.S2pu.setText(str((round(S2pu.real, 5) + round(S2pu.imag, 5) * 1j))[1:-1])
            else:
                S2pu = complex(window.ui.S2pu.text())
            if window.position > 24:
                Ugpu = complex(Ug/(self.Ub*Ubm))
                window.ui.Ugpu.setText(str((round(Ugpu.real, 5) + round(Ugpu.imag, 5) * 1j))[1:-1])
            else:
                Ugpu = complex(window.ui.Ugpu.text())
            if window.position > 23:
                Igpu = conjugate(S2pu/Ugpu)
                window.ui.Igpu.setText(str((round(Igpu.real, 5) + round(Igpu.imag, 5) * 1j))[1:-1])
            else:
                Igpu = complex(window.ui.Igpu.text())
            if window.position > 22:
                deltaIgpu = arctan(Igpu.imag/Igpu.real)
                deltaIgpudeg = math.degrees(deltaIgpu)
                window.ui.deltaIgpu.setText(str(round(deltaIgpudeg, 5)))
            else:
                deltaIgpu = float(window.ui.deltaIgpu.text())
            if window.position > 21:
                EQ = Ugpu + 1j * (self.Xq * Igpu)
                window.ui.EQ.setText(str((round(EQ.real, 5) + round(EQ.imag, 5) * 1j))[1:-1])
            if window.position > 20:
                phi = arctan(Ugpu.imag / Ugpu.real) - deltaIgpu
                phideg = math.degrees(phi)
                window.ui.phi.setText(str(round(phideg, 5)))
            else:
                phi = float(window.ui.phi.text())
            if window.position > 19:
                BC = absolute(Igpu)*absolute(self.Xq)
                window.ui.BC.setText(str(round(BC, 5)))
            else:
                BC = float(window.ui.BC.text())
            if window.position > 18:
                OA = absolute(absolute(Ugpu) * cos(phi))
                window.ui.OA.setText(str(round(OA, 5)))
            else:
                OA = float(window.ui.OA.text())
            if window.position > 17:
                AB = absolute(Ugpu)*sin(phi)
                window.ui.AB.setText(str(round(AB, 5)))
            else:
                AB = float(window.ui.AB.text())
            if window.position > 16:
                alfa = arctan(OA/(AB + BC))
                alfadeg = math.degrees(alfa)
                window.ui.alfa.setText(str(round(alfadeg, 5)))
            else:
                alfa = float(window.ui.alfa.text())
            if window.position > 15:
                gamma = alfa + phi
                gammadeg = math.degrees(gamma)
                window.ui.gamma.setText(str(round(gammadeg, 5)))
            else:
                gamma = float(window.ui.gamma.text())
            if window.position > 14:
                Iqpu = absolute(Igpu) * sin(alfa)
                window.ui.Iqpu.setText(str(round(Iqpu, 5)))
            else:
                Iqpu = float(window.ui.Iqpu.text())
            if window.position > 13:
                Idpu = -absolute(Igpu) * cos(alfa)
                window.ui.Idpu.setText(str(round(Idpu, 5)))
            else:
                Idpu = float(window.ui.Idpu.text())
            if window.position > 12:
                Uqpu = absolute(Ugpu) * sin(alfa + phi)
                window.ui.Uqpu.setText(str(round(Uqpu, 5)))
            else:
                Uqpu = float(window.ui.Uqpu.text())
            if window.position > 11:
                Udpu = -absolute(Ugpu) * cos(alfa + phi)
                window.ui.Udpu.setText(str(round(Udpu, 5)))
            else:
                Udpu = float(window.ui.Udpu.text())
            if window.position > 10:
                Edpu2 = Udpu + absolute(self.Xq2)*Iqpu
                window.ui.Edpu2.setText(str(round(Edpu2, 5)))
            else:
                Edpu2 = float(window.ui.Edpu2.text())
            if window.position > 9:
                Eqpu2 = Uqpu - absolute(self.Xd2)*Idpu
                window.ui.Eqpu2.setText(str(round(Eqpu2, 5)))
            else:
                Eqpu2 = float(window.ui.Eqpu2.text())
            if window.position > 8:
                Edpu1 = Udpu + absolute(self.Xq1)*Iqpu
                window.ui.Edpu1.setText(str(round(Edpu1, 5)))
            else:
                Edpu1 = float(window.ui.Edpu1.text())
            if window.position > 7:
                Eqpu1 = Uqpu - absolute(self.Xd1)*Idpu
                window.ui.Eqpu1.setText(str(round(Eqpu1, 5)))
            else:
                Eqpu1 = float(window.ui.Eqpu1.text())
            if window.position > 6:
                Edpu = Udpu + absolute(self.Xq)*Iqpu
                window.ui.Edpu.setText(str(round(Edpu, 5)))
            else:
                Edpu = float(window.ui.Edpu.text())
            if window.position > 5:
                Eqpu = Uqpu - absolute(self.Xd)*Idpu
                window.ui.Eqpu.setText(str(round(Eqpu, 5)))
            else:
                Eqpu = float(window.ui.Eqpu.text())
            if window.position > 4:
                Epu = sqrt(Edpu**2+Eqpu**2)
                window.ui.Epu.setText(str(round(Epu, 5)))
            if window.position > 3:
                Epu1 = sqrt(Edpu1**2+Eqpu1**2)
                window.ui.Epu1.setText(str(round(Epu1, 5)))
            if window.position > 2:
                Epu2 = sqrt(Edpu2**2+Eqpu2**2)
                window.ui.Epu2.setText(str(round(Epu2, 5)))
            if window.position > 1:
                delta = (math.degrees(math.pi) / 2) - math.degrees(gamma)
                window.ui.delta.setText(str(round(delta, 5)))
        except ZeroDivisionError:
            pass
