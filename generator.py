import numpy as np


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

    def set_Sn(self, value):
        try:
            self.Sn = float(value)
        except ValueError:
            pass

    def set_Sb(self, value):
        try:
            self.Sb = float(value)
        except ValueError:
            pass

    def set_Ub(self, value):
        try:
            self.Ub = float(value)
        except ValueError:
            pass

    def set_Xd(self, value):
        try:
            self.Xd = float(value)
        except ValueError:
            pass

    def set_Xq(self, value):
        try:
            self.Xq = float(value)
        except ValueError:
            pass

    def set_Xd1(self, value):
        try:
            self.Xd1 = float(value)
        except ValueError:
            pass

    def set_Xq1(self, value):
        try:
            self.Xq1 = float(value)
        except ValueError:
            pass

    def set_Xd2(self, value):
        try:
            self.Xd2 = float(value)
        except ValueError:
            pass

    def set_Xq2(self, value):
        try:
            self.Xq2 = float(value)
        except ValueError:
            pass

    def set_S2(self, value):
        try:
            self.S2 = complex(value)
        except ValueError:
            pass

    def set_Ug(self, value):
        try:
            self.Ug = complex(value)
        except ValueError:
            pass

    def set_Zb(self, value):
        try:
            self.Zb = float(value)
        except ValueError:
            pass

    def set_Ib(self, value):
        try:
            self.Ib = complex(value)
        except ValueError:
            pass

    def set_S2pu(self, value):
        try:
            self.S2pu = complex(value)
        except ValueError:
            pass

    def set_Ugpu(self, value):
        try:
            self.Ugpu = complex(value)
        except ValueError:
            pass

    def set_Igpu(self, value):
        try:
            self.Igpu = complex(value)
        except ValueError:
            pass

    def setdelta_Igpu(self, value):
        try:
            self.deltaIgpu = float(value)
        except ValueError:
            pass

    def set_EQ(self, value):
        try:
            self.EQ = complex(value)
        except ValueError:
            pass

    def set_phi(self, value):
        try:
            self.phi = float(value)
        except ValueError:
            pass

    def set_BC(self, value):
        try:
            self.BC = float(value)
        except ValueError:
            pass

    def set_OA(self, value):
        try:
            self.OA = float(value)
        except ValueError:
            pass

    def set_AB(self, value):
        try:
            self.AB = float(value)
        except ValueError:
            pass

    def set_alfa(self, value):
        try:
            self.alfa = float(value)
        except ValueError:
            pass

    def set_gamma(self, value):
        try:
            self.gamma = float(value)
        except ValueError:
            pass

    def set_Iqpu(self, value):
        try:
            self.Iqpu = float(value)
        except ValueError:
            pass

    def set_Idpu(self, value):
        try:
            self.Idpu = float(value)
        except ValueError:
            pass

    def set_Uqpu(self, value):
        try:
            self.Uqpu = float(value)
        except ValueError:
            pass

    def set_Udpu(self, value):
        try:
            self.Udpu = float(value)
        except ValueError:
            pass

    def set_Edpu2(self, value):
        try:
            self.Edpu2 = float(value)
        except ValueError:
            pass

    def set_Eqpu2(self, value):
        try:
            self.Eqpu2 = float(value)
        except ValueError:
            pass

    def set_Edpu1(self, value):
        try:
            self.Edpu1 = float(value)
        except ValueError:
            pass

    def set_Eqpu1(self, value):
        try:
            self.Eqpu1 = float(value)
        except ValueError:
            pass

    def set_Eqpu(self, value):
        try:
            self.Eqpu = float(value)
        except ValueError:
            pass

    def set_Edpu(self, value):
        try:
            self.Edpu = float(value)
        except ValueError:
            pass

    def set_Epu(self, value):
        try:
            self.Epu = float(value)
        except ValueError:
            pass

    def set_Epu1(self, value):
        try:
            self.Epu1 = float(value)
        except ValueError:
            pass

    def set_Epu2(self, value):
        try:
            self.Epu2 = float(value)
        except ValueError:
            pass

    def set_delta(self, value):
        try:
            self.delta = float(value)
        except ValueError:
            pass

    @staticmethod
    def check_combo_Sn(window):
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
    def check_combo_Sb(window):
        if (window.ui.comboSb.currentText()) == "KVA":
            mn = 1000
        elif (window.ui.comboSb.currentText()) == "MVA":
            mn = 1000000
        elif (window.ui.comboSb.currentText()) == "GVA":
            mn = 1000000000
        else:
            return 1
        return mn

    @staticmethod
    def check_combo_S2(window):
        if (window.ui.comboS2.currentText()) == "KVA":
            mn = 1000
        elif (window.ui.comboS2.currentText()) == "MVA":
            mn = 1000000
        elif (window.ui.comboS2.currentText()) == "GVA":
            mn = 1000000000
        else:
            return 1
        return mn

    @staticmethod
    def check_comboUb(window):
        if (window.ui.comboUb.currentText()) == "KV":
            mn = 1000
        elif (window.ui.comboUb.currentText()) == "MV":
            mn = 1000000
        else:
            return 1
        return mn

    def calculate(self, window):
        Snm = Generator.check_combo_Sn(window)
        Sbm = Generator.check_combo_Sb(window)
        Ubm = Generator.check_comboUb(window)
        S2m = Generator.check_combo_S2(window)

        if window.position > 28:
            Ug = 1.05 * self.Ub * Ubm * (np.cos(np.pi/36) + 1j*np.sin(np.pi/36))
            if Ug != 0j:
                window.ui.Ug.setText(str((round(Ug.real, 5) + round(Ug.imag, 5) * 1j))[1:-1])
            else:
                window.ui.Ug.setText("0j")
        else:
            Ug = window.ui.Ug.text()
        try:
            if window.position > 27:
                Zb = (self.Ub*Ubm)**2/(self.Sb*Sbm)
                window.ui.Zb.setText(str(round(Zb, 5)))
            if window.position > 26:
                Ib = np.conjugate((self.Sb*Sbm)/(np.sqrt(3)*self.Ub*Ubm))
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
                Igpu = np.conjugate(S2pu/Ugpu)
                window.ui.Igpu.setText(str((round(Igpu.real, 5) + round(Igpu.imag, 5) * 1j))[1:-1])
            else:
                Igpu = complex(window.ui.Igpu.text())
            if window.position > 22:
                deltaIgpu = np.arctan(Igpu.imag/Igpu.real)
                deltaIgpudeg = float(np.degrees(deltaIgpu))
                window.ui.deltaIgpu.setText(str(round(deltaIgpudeg, 5)))
            else:
                deltaIgpu = np.radians(float(window.ui.deltaIgpu.text()))
            if window.position > 21:
                EQ = Ugpu + 1j * (self.Xq * Igpu)
                window.ui.EQ.setText(str((round(EQ.real, 5) + round(EQ.imag, 5) * 1j))[1:-1])
            if window.position > 20:
                phi = np.arctan(Ugpu.imag / Ugpu.real) - deltaIgpu
                phideg = float(np.degrees(phi))
                window.ui.phi.setText(str(round(phideg, 5)))
            else:
                phi = np.radians(float(window.ui.phi.text()))
            if window.position > 19:
                BC = np.absolute(Igpu)*np.absolute(self.Xq)
                window.ui.BC.setText(str(round(BC, 5)))
            else:
                BC = float(window.ui.BC.text())
            if window.position > 18:
                OA = np.absolute(np.absolute(Ugpu) * np.cos(phi))
                window.ui.OA.setText(str(round(OA, 5)))
            else:
                OA = float(window.ui.OA.text())
            if window.position > 17:
                AB = np.absolute(Ugpu)*np.sin(phi)
                window.ui.AB.setText(str(round(AB, 5)))
            else:
                AB = float(window.ui.AB.text())
            if window.position > 16:
                alfa = np.arctan(OA/(AB + BC))
                alfadeg = float(np.degrees(alfa))
                window.ui.alfa.setText(str(round(alfadeg, 5)))
            else:
                alfa = np.radians(float((window.ui.alfa.text())))
            if window.position > 15:
                gamma = alfa + phi
                gammadeg = float(np.degrees(gamma))
                window.ui.gamma.setText(str(round(gammadeg, 5)))
            else:
                gamma = np.radians(float(window.ui.gamma.text()))
            if window.position > 14:
                Iqpu = np.absolute(Igpu) * np.sin(alfa)
                window.ui.Iqpu.setText(str(round(Iqpu, 5)))
            else:
                Iqpu = float(window.ui.Iqpu.text())
            if window.position > 13:
                Idpu = -np.absolute(Igpu) * np.cos(alfa)
                window.ui.Idpu.setText(str(round(Idpu, 5)))
            else:
                Idpu = float(window.ui.Idpu.text())
            if window.position > 12:
                Uqpu = np.absolute(Ugpu) * np.sin(alfa + phi)
                window.ui.Uqpu.setText(str(round(Uqpu, 5)))
            else:
                Uqpu = float(window.ui.Uqpu.text())
            if window.position > 11:
                Udpu = -np.absolute(Ugpu) * np.cos(alfa + phi)
                window.ui.Udpu.setText(str(round(Udpu, 5)))
            else:
                Udpu = float(window.ui.Udpu.text())
            if window.position > 10:
                Edpu2 = Udpu + np.absolute(self.Xq2)*Iqpu
                window.ui.Edpu2.setText(str(round(Edpu2, 5)))
            else:
                Edpu2 = float(window.ui.Edpu2.text())
            if window.position > 9:
                Eqpu2 = Uqpu - np.absolute(self.Xd2)*Idpu
                window.ui.Eqpu2.setText(str(round(Eqpu2, 5)))
            else:
                Eqpu2 = float(window.ui.Eqpu2.text())
            if window.position > 8:
                Edpu1 = Udpu + np.absolute(self.Xq1)*Iqpu
                window.ui.Edpu1.setText(str(round(Edpu1, 5)))
            else:
                Edpu1 = float(window.ui.Edpu1.text())
            if window.position > 7:
                Eqpu1 = Uqpu - np.absolute(self.Xd1)*Idpu
                window.ui.Eqpu1.setText(str(round(Eqpu1, 5)))
            else:
                Eqpu1 = float(window.ui.Eqpu1.text())
            if window.position > 6:
                Edpu = Udpu + np.absolute(self.Xq)*Iqpu
                window.ui.Edpu.setText(str(round(Edpu, 5)))
            else:
                Edpu = float(window.ui.Edpu.text())
            if window.position > 5:
                Eqpu = Uqpu - np.absolute(self.Xd)*Idpu
                window.ui.Eqpu.setText(str(round(Eqpu, 5)))
            else:
                Eqpu = float(window.ui.Eqpu.text())
            if window.position > 4:
                Epu = np.sqrt(Edpu**2+Eqpu**2)
                window.ui.Epu.setText(str(round(Epu, 5)))
            if window.position > 3:
                Epu1 = np.sqrt(Edpu1**2+Eqpu1**2)
                window.ui.Epu1.setText(str(round(Epu1, 5)))
            if window.position > 2:
                Epu2 = np.sqrt(Edpu2**2+Eqpu2**2)
                window.ui.Epu2.setText(str(round(Epu2, 5)))
            if window.position > 1:
                delta = (np.degrees(np.pi) / 2) - np.degrees(gamma)
                window.ui.delta.setText(str(round(delta, 5)))
        except ZeroDivisionError:
            pass
