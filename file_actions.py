from PyQt5 import QtCore, QtWidgets

from generator import Generator


def save_file(window):
    file_name, _ = QtWidgets.QFileDialog.getSaveFileName(window, 'Save File', QtCore.QDir.rootPath(), '*.txt')
    if file_name != "":
        file = open(file_name, 'w')
        write_file(window, file)


def write_file(window, file):
    Snm = Generator.check_combo_VA(window)
    Sbm = Generator.check_combo_VA(window)
    Ubm = Generator.check_combo_V(window)
    S2m = Generator.check_combo_VA(window)
    file.write("Sn = " + str(float(window.gen.Sn) * Snm))
    file.write("\nSb = " + str(float(window.gen.Sb) * Sbm))
    file.write("\nUb = " + str(float(window.gen.Ub) * Ubm))
    file.write("\nXd = " + str(window.gen.Xd))
    file.write("\nXq = " + str(window.gen.Xq))
    file.write("\nXd1 = " + str(window.gen.Xd1))
    file.write("\nXq1 = " + str(window.gen.Xq1))
    file.write("\nXd2 = " + str(window.gen.Xd2))
    file.write("\nXq2 = " + str(window.gen.Xq2))
    if window.gen.S2 * S2m != 0j:
        file.write("\nS2 = " + str(complex(window.gen.S2 * S2m))[1:-1])
    else:
        file.write("\nS2 = " + str(complex(window.gen.S2 * S2m)))
    if window.gen.Ug != 0j:
        file.write("\nUg = " + str(complex(window.gen.Ug))[1:-1])
    else:
        file.write("\nUg = " + str(complex(window.gen.Ug)))
    file.write("\nZb = " + str(window.gen.Zb))
    if window.gen.Ib != 0j:
        file.write("\nIb = " + str(complex(window.gen.Ib))[1:-1])
    else:
        file.write("\nIb = " + str(complex(window.gen.Ib)))
    if window.gen.S2pu != 0j:
        file.write("\nS2pu = " + str(complex(window.gen.S2pu))[1:-1])
    else:
        file.write("\nS2pu = " + str(complex(window.gen.S2pu)))
    if window.gen.Ugpu != 0j:
        file.write("\nUgpu = " + str(complex(window.gen.Ugpu))[1:-1])
    else:
        file.write("\nUgpu = " + str(complex(window.gen.Ugpu)))
    if window.gen.Igpu != 0j:
        file.write("\nIgpu = " + str(complex(window.gen.Igpu))[1:-1])
    else:
        file.write("\nIgpu = " + str(complex(window.gen.Igpu)))
    file.write("\ndeltaIgpu = " + str(window.gen.deltaIgpu))
    if window.gen.EQ != 0j:
        file.write("\nEQ = " + str(complex(window.gen.EQ))[1:-1])
    else:
        file.write("\nEQ = " + str(complex(window.gen.EQ)))
    file.write("\nphi = " + str(window.gen.phi))
    file.write("\nBC = " + str(window.gen.BC))
    file.write("\nOA = " + str(window.gen.OA))
    file.write("\nAB = " + str(window.gen.AB))
    file.write("\nalfa = " + str(window.gen.alfa))
    file.write("\ngamma = " + str(window.gen.gamma))
    file.write("\nIqpu = " + str(window.gen.Iqpu))
    file.write("\nIdpu = " + str(window.gen.Idpu))
    file.write("\nUqpu = " + str(window.gen.Uqpu))
    file.write("\nUdpu = " + str(window.gen.Udpu))
    file.write("\nEdpu2 = " + str(window.gen.Edpu2))
    file.write("\nEqpu2 = " + str(window.gen.Eqpu2))
    file.write("\nEdpu1 = " + str(window.gen.Edpu1))
    file.write("\nEqpu1 = " + str(window.gen.Eqpu1))
    file.write("\nEdpu = " + str(window.gen.Edpu))
    file.write("\nEqpu = " + str(window.gen.Eqpu))
    file.write("\nEpu = " + str(window.gen.Epu))
    file.write("\nEpu1 = " + str(window.gen.Epu1))
    file.write("\nEpu2 = " + str(window.gen.Epu2))
    file.write("\ndelta = " + str(window.gen.delta))

    file.close()


def get_files(window):
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(window, 'Open File', QtCore.QDir.rootPath(), '*.txt')
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
                        window.ui.comboSn.setCurrentText("GVA")
                    elif Sn % 1000000 == 0:
                        Sn = Sn / 1000000
                        window.ui.comboSn.setCurrentText("MVA")
                    else:
                        Sn = Sn / 1000
                        window.ui.comboSn.setCurrentText("KVA")
                window.ui.Sn.setText(str(Sn))
            if data.__contains__("Ub"):
                Ub = float(data["Ub"])
                if Ub % 1000 == 0:
                    if Ub % 1000000 == 0:
                        Ub = Ub / 1000000
                        window.ui.comboUb.setCurrentText("MV")
                    else:
                        Ub = Ub / 1000
                        window.ui.comboUb.setCurrentText("KV")
                window.ui.Ub.setText(str(Ub))
            if data.__contains__("Sb"):
                Sb = float(data["Sb"])
                if Sb % 1000 == 0:
                    if Sb % 1000000000 == 0:
                        Sb = Sb / 1000000000
                        window.ui.comboSb.setCurrentText("GVA")
                    elif Sb % 1000000 == 0:
                        Sb = Sb / 1000000
                        window.ui.comboSb.setCurrentText("MVA")
                    else:
                        Sb = Sb / 1000
                        window.ui.comboSb.setCurrentText("KVA")
                window.ui.Sb.setText(str(Sb))
            if data.__contains__("S2"):
                S2 = complex(data["S2"])
                if S2.real % 1000 == 0 and S2.imag % 1000 == 0:
                    if S2.real % 1000000000 == 0 and S2.imag % 1000000000 == 0:
                        S2 = S2 / 1000000000
                        window.ui.comboS2.setCurrentText("GVA")
                    elif S2.real % 1000000 == 0 and S2.imag % 1000000 == 0:
                        S2 = S2 / 1000000
                        window.ui.comboS2.setCurrentText("MVA")
                    else:
                        S2 = S2 / 1000
                        window.ui.comboS2.setCurrentText("KVA")
                    window.ui.S2.setText(str(S2)[1:-1])
                if S2 == 0j:
                    window.ui.S2.setText(str(S2))

            if data.__contains__("Xd"):
                window.ui.Xd.setText(str(data["Xd"]))
            if data.__contains__("Xq"):
                window.ui.Xq.setText(str(data["Xq"]))
            if data.__contains__("Xd1"):
                window.ui.Xd1.setText(str(data["Xd1"]))
            if data.__contains__("Xq1"):
                window.ui.Xq1.setText(str(data["Xq1"]))
            if data.__contains__("Xd2"):
                window.ui.Xd2.setText(str(data["Xd2"]))
            if data.__contains__("Xq2"):
                window.ui.Xq2.setText(str(data["Xq2"]))

            if data.__contains__("Ug"):
                window.ui.Ug.setText(str(data["Ug"]))
            if data.__contains__("Zb"):
                window.ui.Zb.setText(str(data["Zb"]))
            if data.__contains__("Ib"):
                window.ui.Ib.setText(str(data["Ib"]))
            if data.__contains__("S2pu"):
                window.ui.S2pu.setText(str(data["S2pu"]))
            if data.__contains__("Ugpu"):
                window.ui.Ugpu.setText(str(data["Ugpu"]))
            if data.__contains__("Igpu"):
                window.ui.Igpu.setText(str(data["Igpu"]))
            if data.__contains__("deltaIgpu"):
                window.ui.deltaIgpu.setText(str(data["deltaIgpu"]))
            if data.__contains__("EQ"):
                window.ui.EQ.setText(str(data["EQ"]))
            if data.__contains__("phi"):
                window.ui.phi.setText(str(data["phi"]))
            if data.__contains__("BC"):
                window.ui.BC.setText(str(data["BC"]))
            if data.__contains__("OA"):
                window.ui.OA.setText(str(data["OA"]))
            if data.__contains__("AB"):
                window.ui.AB.setText(str(data["AB"]))
            if data.__contains__("alfa"):
                window.ui.alfa.setText(str(data["alfa"]))
            if data.__contains__("gamma"):
                window.ui.gamma.setText(str(data["gamma"]))
            if data.__contains__("Iqpu"):
                window.ui.Iqpu.setText(str(data["Iqpu"]))
            if data.__contains__("Idpu"):
                window.ui.Idpu.setText(str(data["Idpu"]))
            if data.__contains__("Uqpu"):
                window.ui.Uqpu.setText(str(data["Uqpu"]))
            if data.__contains__("Udpu"):
                window.ui.Udpu.setText(str(data["Udpu"]))
            if data.__contains__("Edpu2"):
                window.ui.Edpu2.setText(str(data["Edpu2"]))
            if data.__contains__("Eqpu2"):
                window.ui.Eqpu2.setText(str(data["Eqpu2"]))
            if data.__contains__("Edpu1"):
                window.ui.Edpu1.setText(str(data["Edpu1"]))
            if data.__contains__("Eqpu1"):
                window.ui.Eqpu1.setText(str(data["Eqpu1"]))
            if data.__contains__("Edpu"):
                window.ui.Edpu.setText(str(data["Edpu"]))
            if data.__contains__("Eqpu"):
                window.ui.Eqpu.setText(str(data["Eqpu"]))
            if data.__contains__("Epu"):
                window.ui.Epu.setText(str(data["Epu"]))
            if data.__contains__("Epu1"):
                window.ui.Epu1.setText(str(data["Epu1"]))
            if data.__contains__("Epu2"):
                window.ui.Epu2.setText(str(data["Epu2"]))
            if data.__contains__("delta"):
                window.ui.delta.setText(str(data["delta"]))
