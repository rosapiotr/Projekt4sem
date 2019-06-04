from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from plot_window import Ui_Dialog

import file_actions as fa
from layout import Ui_MainWindow
from generator import Generator


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
        self.ui.browse.triggered.connect(lambda: fa.get_files(self))
        self.bind_fields()
        self.bind_last_change()
        self.ui.help.clicked.connect(self.display_help)
        self.ui.calculate.clicked.connect(lambda: self.gen.calculate(self))
        self.ui.save.clicked.connect(lambda: fa.save_file(self))
        self.ui.plot.clicked.connect(self.plot_diagram)

    def plot_diagram(self):
        self.window = QtWidgets.QMainWindow()
        self.ui2 = Ui_Dialog()
        self.ui2.setupUi(self.window, self.gen)
        self.window.show()
        self.window.setFixedSize(self.window.size())

    def closeEvent(self, event):
        self.close()
        try:
            self.window.close()
            self.ui2.window.close()
        except Exception:
            pass

    def bind_fields(self):
        self.ui.Sn.textChanged.connect(self.gen.set_Sn)
        self.ui.Sb.textChanged.connect(self.gen.set_Sb)
        self.ui.Ub.textChanged.connect(self.gen.set_Ub)
        self.ui.Xd.textChanged.connect(self.gen.set_Xd)
        self.ui.Xq.textChanged.connect(self.gen.set_Xq)
        self.ui.Xd1.textChanged.connect(self.gen.set_Xd1)
        self.ui.Xq1.textChanged.connect(self.gen.set_Xq1)
        self.ui.Xd2.textChanged.connect(self.gen.set_Xd2)
        self.ui.Xq2.textChanged.connect(self.gen.set_Xq2)
        self.ui.S2.textChanged.connect(self.gen.set_S2)
        self.ui.Ug.textChanged.connect(self.gen.set_Ug)
        self.ui.Zb.textChanged.connect(self.gen.set_Zb)
        self.ui.Ib.textChanged.connect(self.gen.set_Ib)
        self.ui.S2pu.textChanged.connect(self.gen.set_S2pu)
        self.ui.Ugpu.textChanged.connect(self.gen.set_Ugpu)
        self.ui.Igpu.textChanged.connect(self.gen.set_Igpu)
        self.ui.deltaIgpu.textChanged.connect(self.gen.setdelta_Igpu)
        self.ui.EQ.textChanged.connect(self.gen.set_EQ)
        self.ui.phi.textChanged.connect(self.gen.set_phi)
        self.ui.BC.textChanged.connect(self.gen.set_BC)
        self.ui.OA.textChanged.connect(self.gen.set_OA)
        self.ui.AB.textChanged.connect(self.gen.set_AB)
        self.ui.alfa.textChanged.connect(self.gen.set_alfa)
        self.ui.gamma.textChanged.connect(self.gen.set_gamma)
        self.ui.Iqpu.textChanged.connect(self.gen.set_Iqpu)
        self.ui.Idpu.textChanged.connect(self.gen.set_Idpu)
        self.ui.Uqpu.textChanged.connect(self.gen.set_Uqpu)
        self.ui.Udpu.textChanged.connect(self.gen.set_Udpu)
        self.ui.Edpu2.textChanged.connect(self.gen.set_Edpu2)
        self.ui.Eqpu2.textChanged.connect(self.gen.set_Eqpu2)
        self.ui.Edpu1.textChanged.connect(self.gen.set_Edpu1)
        self.ui.Eqpu1.textChanged.connect(self.gen.set_Eqpu1)
        self.ui.Edpu.textChanged.connect(self.gen.set_Edpu)
        self.ui.Eqpu.textChanged.connect(self.gen.set_Eqpu)
        self.ui.Epu.textChanged.connect(self.gen.set_Epu)
        self.ui.Epu1.textChanged.connect(self.gen.set_Epu1)
        self.ui.Epu2.textChanged.connect(self.gen.set_Epu2)
        self.ui.delta.textChanged.connect(self.gen.set_delta)

    def bind_last_change(self):
        self.ui.Sn.textChanged.connect(lambda: self.set_position(38))
        self.ui.comboSn.currentTextChanged.connect(lambda: self.set_position(38))
        self.ui.Sb.textChanged.connect(lambda: self.set_position(37))
        self.ui.comboSb.currentTextChanged.connect(lambda: self.set_position(37))
        self.ui.Ub.textChanged.connect(lambda: self.set_position(36))
        self.ui.comboUb.currentTextChanged.connect(lambda: self.set_position(36))
        self.ui.Xd.textChanged.connect(lambda: self.set_position(35))
        self.ui.Xq.textChanged.connect(lambda: self.set_position(34))
        self.ui.Xd1.textChanged.connect(lambda: self.set_position(33))
        self.ui.Xq1.textChanged.connect(lambda: self.set_position(32))
        self.ui.Xd2.textChanged.connect(lambda: self.set_position(31))
        self.ui.Xq2.textChanged.connect(lambda: self.set_position(30))
        self.ui.S2.textChanged.connect(lambda: self.set_position(29))
        self.ui.comboS2.currentTextChanged.connect(lambda: self.set_position(29))
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


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MyWindow()
    MainWindow.show()
    sys.exit(app.exec_())
