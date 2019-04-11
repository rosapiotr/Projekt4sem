from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Generator import Generator
from Layout import Ui_MainWindow
import sys


class MyWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        self.position = 38
        self.gen = Generator()
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initUI()
        self.setFixedSize(self.size())

    def initUI(self):
        self.ui.browse.triggered.connect(self.get_files)
        self.bind_fields()
        self.bind_last_change()
        self.ui.help.clicked.connect(self.display_help)
        self.ui.calculate.clicked.connect(lambda: self.gen.calculate(self))
        self.ui.save.clicked.connect(self.save_file)

    def bind_fields(self):
        self.ui.Sn.textChanged.connect(self.gen.setSn)
        self.ui.Sb.textChanged.connect(self.gen.setSb)
        self.ui.Ub.textChanged.connect(self.gen.setUb)
        self.ui.Xd.textChanged.connect(self.gen.setXd)
        self.ui.Xq.textChanged.connect(self.gen.setXq)
        self.ui.Xd1.textChanged.connect(self.gen.setXd1)
        self.ui.Xq1.textChanged.connect(self.gen.setXq1)
        self.ui.Xd2.textChanged.connect(self.gen.setXd2)
        self.ui.Xq2.textChanged.connect(self.gen.setXq2)
        self.ui.S2.textChanged.connect(self.gen.setS2)
        self.ui.Ug.textChanged.connect(self.gen.setUg)
        self.ui.Zb.textChanged.connect(self.gen.setZb)
        self.ui.Ib.textChanged.connect(self.gen.setIb)
        self.ui.S2pu.textChanged.connect(self.gen.setS2pu)
        self.ui.Ugpu.textChanged.connect(self.gen.setUgpu)
        self.ui.Igpu.textChanged.connect(self.gen.setIgpu)
        self.ui.deltaIgpu.textChanged.connect(self.gen.setdeltaIgpu)
        self.ui.EQ.textChanged.connect(self.gen.setEQ)
        self.ui.phi.textChanged.connect(self.gen.setphi)
        self.ui.BC.textChanged.connect(self.gen.setBC)
        self.ui.OA.textChanged.connect(self.gen.setOA)
        self.ui.AB.textChanged.connect(self.gen.setAB)
        self.ui.alfa.textChanged.connect(self.gen.setalfa)
        self.ui.gamma.textChanged.connect(self.gen.setgamma)
        self.ui.Iqpu.textChanged.connect(self.gen.setIqpu)
        self.ui.Idpu.textChanged.connect(self.gen.setIdpu)
        self.ui.Uqpu.textChanged.connect(self.gen.setUqpu)
        self.ui.Udpu.textChanged.connect(self.gen.setUdpu)
        self.ui.Edpu2.textChanged.connect(self.gen.setEdpu2)
        self.ui.Eqpu2.textChanged.connect(self.gen.setEqpu2)
        self.ui.Edpu1.textChanged.connect(self.gen.setEdpu1)
        self.ui.Eqpu1.textChanged.connect(self.gen.setEqpu1)
        self.ui.Edpu.textChanged.connect(self.gen.setEdpu)
        self.ui.Eqpu.textChanged.connect(self.gen.setEqpu)
        self.ui.Epu.textChanged.connect(self.gen.setEpu)
        self.ui.Epu1.textChanged.connect(self.gen.setEpu1)
        self.ui.Epu2.textChanged.connect(self.gen.setEpu2)
        self.ui.delta.textChanged.connect(self.gen.setdelta)

    def bind_last_change(self):
        self.ui.Sn.textChanged.connect(lambda: self.set_position(38))
        self.ui.Sb.textChanged.connect(lambda: self.set_position(37))
        self.ui.Ub.textChanged.connect(lambda: self.set_position(36))
        self.ui.Xd.textChanged.connect(lambda: self.set_position(35))
        self.ui.Xq.textChanged.connect(lambda: self.set_position(34))
        self.ui.Xd1.textChanged.connect(lambda: self.set_position(33))
        self.ui.Xq1.textChanged.connect(lambda: self.set_position(32))
        self.ui.Xd2.textChanged.connect(lambda: self.set_position(31))
        self.ui.Xq2.textChanged.connect(lambda: self.set_position(30))
        self.ui.S2.textChanged.connect(lambda: self.set_position(29))
        self.ui.Ug.textChanged.connect(lambda: self.set_position(28))
        self.ui.Zb.textChanged.connect(lambda: self.set_position(27))
        self.ui.Ib.textChanged.connect(lambda: self.set_position(26))
        self.ui.S2pu.textChanged.connect(lambda: self.set_position(25))
        self.ui.Ugpu.textChanged.connect(lambda: self.set_position(24))
        self.ui.Igpu.textChanged.connect(lambda: self.set_position(23))
        self.ui.deltaIgpu.textChanged.connect(lambda: self.set_position(22))
        self.ui.EQ.textChanged.connect(lambda: self.set_position(21))
        self.ui.phi.textChanged.connect(lambda: self.set_position(20))
        self.ui.BC.textChanged.connect(lambda: self.set_position(19))
        self.ui.OA.textChanged.connect(lambda: self.set_position(18))
        self.ui.AB.textChanged.connect(lambda: self.set_position(17))
        self.ui.alfa.textChanged.connect(lambda: self.set_position(16))
        self.ui.gamma.textChanged.connect(lambda: self.set_position(15))
        self.ui.Iqpu.textChanged.connect(lambda: self.set_position(14))
        self.ui.Idpu.textChanged.connect(lambda: self.set_position(13))
        self.ui.Uqpu.textChanged.connect(lambda: self.set_position(12))
        self.ui.Udpu.textChanged.connect(lambda: self.set_position(11))
        self.ui.Edpu2.textChanged.connect(lambda: self.set_position(10))
        self.ui.Eqpu2.textChanged.connect(lambda: self.set_position(9))
        self.ui.Edpu1.textChanged.connect(lambda: self.set_position(8))
        self.ui.Eqpu1.textChanged.connect(lambda: self.set_position(7))
        self.ui.Edpu.textChanged.connect(lambda: self.set_position(6))
        self.ui.Eqpu.textChanged.connect(lambda: self.set_position(5))
        self.ui.Epu.textChanged.connect(lambda: self.set_position(4))
        self.ui.Epu1.textChanged.connect(lambda: self.set_position(3))
        self.ui.Epu2.textChanged.connect(lambda: self.set_position(2))
        self.ui.delta.textChanged.connect(lambda: self.set_position(1))

        # self.ui.calculate.clicked.connect(self.printname)
    #
    # def setName(self, name):
    #     self.name = name
    #

    def save_file(self):
        file_name, _ = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File', QtCore.QDir.rootPath(), '*.txt')
        if file_name != "":
            file = open(file_name, 'w')
            self.write_file(file)

    def write_file(self, file):
        Snm = Generator.check_combo_VA(self)
        Sbm = Generator.check_combo_VA(self)
        Ubm = Generator.check_combo_V(self)
        S2m = Generator.check_combo_VA(self)
        file.write("Sn = " + str(float(self.gen.Sn)*Snm))
        file.write("\nSb = " + str(float(self.gen.Sb)*Sbm))
        file.write("\nUb = " + str(float(self.gen.Ub)*Ubm))
        file.write("\nXd = " + str(self.gen.Xd))
        file.write("\nXq = " + str(self.gen.Xq))
        file.write("\nXd1 = " + str(self.gen.Xd1))
        file.write("\nXq1 = " + str(self.gen.Xq1))
        file.write("\nXd2 = " + str(self.gen.Xd2))
        file.write("\nXq2 = " + str(self.gen.Xq2))
        if self.gen.S2*S2m != 0j:
            file.write("\nS2 = " + str(complex(self.gen.S2*S2m))[1:-1])
        else:
            file.write("\nS2 = " + str(complex(self.gen.S2 * S2m)))
        if self.gen.Ug != 0j:
            file.write("\nUg = " + str(complex(self.gen.Ug))[1:-1])
        else:
            file.write("\nUg = " + str(complex(self.gen.Ug)))
        file.write("\nZb = " + str(self.gen.Zb))
        if self.gen.Ib != 0j:
            file.write("\nIb = " + str(complex(self.gen.Ib))[1:-1])
        else:
            file.write("\nIb = " + str(complex(self.gen.Ib)))
        if self.gen.S2pu != 0j:
            file.write("\nS2pu = " + str(complex(self.gen.S2pu))[1:-1])
        else:
            file.write("\nS2pu = " + str(complex(self.gen.S2pu)))
        if self.gen.Ugpu != 0j:
            file.write("\nUgpu = " + str(complex(self.gen.Ugpu))[1:-1])
        else:
            file.write("\nUgpu = " + str(complex(self.gen.Ugpu)))
        if self.gen.Igpu != 0j:
            file.write("\nIgpu = " + str(complex(self.gen.Igpu))[1:-1])
        else:
            file.write("\nIgpu = " + str(complex(self.gen.Igpu)))
        file.write("\ndeltaIgpu = " + str(self.gen.deltaIgpu))
        if self.gen.EQ != 0j:
            file.write("\nEQ = " + str(complex(self.gen.EQ))[1:-1])
        else:
            file.write("\nEQ = " + str(complex(self.gen.EQ)))
        file.write("\nphi = " + str(self.gen.phi))
        file.write("\nBC = " + str(self.gen.BC))
        file.write("\nOA = " + str(self.gen.OA))
        file.write("\nAB = " + str(self.gen.AB))
        file.write("\nalfa = " + str(self.gen.alfa))
        file.write("\ngamma = " + str(self.gen.gamma))
        file.write("\nIqpu = " + str(self.gen.Iqpu))
        file.write("\nIdpu = " + str(self.gen.Idpu))
        file.write("\nUqpu = " + str(self.gen.Uqpu))
        file.write("\nUdpu = " + str(self.gen.Udpu))
        file.write("\nEdpu2 = " + str(self.gen.Edpu2))
        file.write("\nEqpu2 = " + str(self.gen.Eqpu2))
        file.write("\nEdpu1 = " + str(self.gen.Edpu1))
        file.write("\nEqpu1 = " + str(self.gen.Eqpu1))
        file.write("\nEdpu = " + str(self.gen.Edpu))
        file.write("\nEqpu = " + str(self.gen.Eqpu))
        file.write("\nEpu = " + str(self.gen.Epu))
        file.write("\nEpu1 = " + str(self.gen.Epu1))
        file.write("\nEpu2 = " + str(self.gen.Epu2))
        file.write("\ndelta = " + str(self.gen.delta))

        file.close()

    def display_help(self):
        m_box = QMessageBox()
        m_box.setIcon(QMessageBox.Information)
        m_box.setWindowTitle("Help")
        m_box.setText("You can specify all the data int the file.\n"
                      "The values of the parameters have to be numeric.\n"
                      "For example you can't write:\n"
                      "Sn = 250 MVA\n"
                      "You have to write:\n"
                      "Sn = 250000000\n"
                      "If you want to specify parameters such as Xd', Xd'', Xq' and so on, "
                      "you need to write Xd1, Xd2, Xq1 respectively. "
                      "To refer to greek letters you need to give their name and subscript.\n"
                      "If you are not sure what are the names of parameters, click the button "
                      "\"Save to a File\" to generate a template.\n"
                      "Make sure to delete the values, you don't want to specify.\n"
                      "The calculations start from the last specified parameter. Previous values won't be"
                      "calculated or overwritten")
        m_box.exec_()

    def set_position(self, n):
        self.position = n

    def printname(self):
        print(self.position)
        # Ug = str(12+21j)
        # print(Ug)
        # self.ui.Ug.setText(Ug[1:-1])
        # self.gen.setSb(self.gen.Sn*2, self)
        # print(self.gen.Sb)

    def get_files(self):
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', QtCore.QDir.rootPath(), '*.txt')
        if file_name != "":
            file = open(file_name, 'r')
            content = file.readlines()
            data = {}
            for line in content:
                d = line.split(" = ")
                data[d[0]] = d[1]
            if data.__contains__("Sn"):
                Sn = float(data["Sn"])
                if Sn % 1000 == 0:
                    if Sn % 1000000000 == 0:
                        Sn = Sn / 1000000000
                        self.ui.comboSn.setCurrentText("GVA")
                    elif Sn % 1000000 == 0:
                        Sn = Sn / 1000000
                        self.ui.comboSn.setCurrentText("MVA")
                    else:
                        Sn = Sn / 1000
                        self.ui.comboSn.setCurrentText("KVA")
                self.ui.Sn.setText(str(Sn))
            if data.__contains__("Ub"):
                Ub = float(data["Ub"])
                if Ub % 1000 == 0:
                    if Ub % 1000000 == 0:
                        Ub = Ub / 1000000
                        self.ui.comboUb.setCurrentText("MV")
                    else:
                        Ub = Ub / 1000
                        self.ui.comboUb.setCurrentText("KV")
                self.ui.Ub.setText(str(Ub))
            if data.__contains__("Sb"):
                Sb = float(data["Sb"])
                if Sb % 1000 == 0:
                    if Sb % 1000000000 == 0:
                        Sb = Sb / 1000000000
                        self.ui.comboSb.setCurrentText("GVA")
                    elif Sb % 1000000 == 0:
                        Sb = Sb / 1000000
                        self.ui.comboSb.setCurrentText("MVA")
                    else:
                        Sb = Sb / 1000
                        self.ui.comboSb.setCurrentText("KVA")
                self.ui.Sb.setText(str(Sb))
            if data.__contains__("S2"):
                S2 = complex(data["S2"])
                if S2.real % 1000 == 0 and S2.imag % 1000 == 0:
                    if S2.real % 1000000000 == 0 and S2.imag % 1000000000 == 0:
                        S2 = S2 / 1000000000
                        self.ui.comboS2.setCurrentText("GVA")
                    elif S2.real % 1000000 == 0 and S2.imag % 1000000 == 0:
                        S2 = S2 / 1000000
                        self.ui.comboS2.setCurrentText("MVA")
                    else:
                        S2 = S2 / 1000
                        self.ui.comboS2.setCurrentText("KVA")
                    self.ui.S2.setText(str(S2)[1:-1])
                if S2 == 0j:
                    self.ui.S2.setText(str(S2))

            if data.__contains__("Xd"):
                self.ui.Xd.setText(str(data["Xd"]))
            if data.__contains__("Xq"):
                self.ui.Xq.setText(str(data["Xq"]))
            if data.__contains__("Xd1"):
                self.ui.Xd1.setText(str(data["Xd1"]))
            if data.__contains__("Xq1"):
                self.ui.Xq1.setText(str(data["Xq1"]))
            if data.__contains__("Xd2"):
                self.ui.Xd2.setText(str(data["Xd2"]))
            if data.__contains__("Xq2"):
                self.ui.Xq2.setText(str(data["Xq2"]))

            if data.__contains__("Ug"):
                self.ui.Ug.setText(str(data["Ug"]))
            if data.__contains__("Zb"):
                self.ui.Zb.setText(str(data["Zb"]))
            if data.__contains__("Ib"):
                self.ui.Ib.setText(str(data["Ib"]))
            if data.__contains__("S2pu"):
                self.ui.S2pu.setText(str(data["S2pu"]))
            if data.__contains__("Ugpu"):
                self.ui.Ugpu.setText(str(data["Ugpu"]))
            if data.__contains__("Igpu"):
                self.ui.Igpu.setText(str(data["Igpu"]))
            if data.__contains__("deltaIgpu"):
                self.ui.deltaIgpu.setText(str(data["deltaIgpu"]))
            if data.__contains__("EQ"):
                self.ui.EQ.setText(str(data["EQ"]))
            if data.__contains__("phi"):
                self.ui.phi.setText(str(data["phi"]))
            if data.__contains__("BC"):
                self.ui.BC.setText(str(data["BC"]))
            if data.__contains__("OA"):
                self.ui.OA.setText(str(data["OA"]))
            if data.__contains__("AB"):
                self.ui.AB.setText(str(data["AB"]))
            if data.__contains__("alfa"):
                self.ui.alfa.setText(str(data["alfa"]))
            if data.__contains__("gamma"):
                self.ui.gamma.setText(str(data["gamma"]))
            if data.__contains__("Iqpu"):
                self.ui.Iqpu.setText(str(data["Iqpu"]))
            if data.__contains__("Idpu"):
                self.ui.Idpu.setText(str(data["Idpu"]))
            if data.__contains__("Uqpu"):
                self.ui.Uqpu.setText(str(data["Uqpu"]))
            if data.__contains__("Udpu"):
                self.ui.Udpu.setText(str(data["Udpu"]))
            if data.__contains__("Edpu2"):
                self.ui.Edpu2.setText(str(data["Edpu2"]))
            if data.__contains__("Eqpu2"):
                self.ui.Eqpu2.setText(str(data["Eqpu2"]))
            if data.__contains__("Edpu1"):
                self.ui.Edpu1.setText(str(data["Edpu1"]))
            if data.__contains__("Eqpu1"):
                self.ui.Eqpu1.setText(str(data["Eqpu1"]))
            if data.__contains__("Edpu"):
                self.ui.Edpu.setText(str(data["Edpu"]))
            if data.__contains__("Eqpu"):
                self.ui.Eqpu.setText(str(data["Eqpu"]))
            if data.__contains__("Epu"):
                self.ui.Epu.setText(str(data["Epu"]))
            if data.__contains__("Epu1"):
                self.ui.Epu1.setText(str(data["Epu1"]))
            if data.__contains__("Epu2"):
                self.ui.Epu2.setText(str(data["Epu2"]))
            if data.__contains__("delta"):
                self.ui.delta.setText(str(data["delta"]))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MyWindow()
    MainWindow.show()
    sys.exit(app.exec_())
