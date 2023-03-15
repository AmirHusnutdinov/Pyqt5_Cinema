from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_marc_first(object):
    def setupUi(self, marc_first):
        marc_first.setObjectName("marc_first")
        marc_first.resize(1140, 857)
        self.green_l = QtWidgets.QLabel(marc_first)
        self.green_l.setGeometry(QtCore.QRect(0, 0, 1141, 81))
        self.green_l.setStyleSheet("background-color: rgb(0, 85, 0);")
        self.green_l.setText("")
        self.green_l.setObjectName("green_l")
        self.main_l = QtWidgets.QLabel(marc_first)
        self.main_l.setGeometry(QtCore.QRect(20, 10, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Adobe Caslon Pro")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.main_l.setFont(font)
        self.main_l.setStyleSheet("background-color: rgb(0, 85, 0);\n""\n""font: 20pt \"Adobe Caslon Pro\";\n"
                                  "color: rgb(255, 255, 255);")
        self.main_l.setObjectName("main_l")
        self.main_l2 = QtWidgets.QLabel(marc_first)
        self.main_l2.setGeometry(QtCore.QRect(180, 10, 201, 61))
        self.main_l2.setMaximumSize(QtCore.QSize(201, 16777215))
        font = QtGui.QFont()
        font.setFamily("Adobe Caslon Pro")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.main_l2.setFont(font)
        self.main_l2.setStyleSheet("background-color: rgb(0, 85, 0);\n""color: rgb(217, 217, 217);")
        self.main_l2.setObjectName("main_l2")
        self.black_line = QtWidgets.QLabel(marc_first)
        self.black_line.setGeometry(QtCore.QRect(0, 80, 1141, 101))
        self.black_line.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.black_line.setText("")
        self.black_line.setObjectName("black_line")
        self.back_btn = QtWidgets.QPushButton(marc_first)
        self.back_btn.setGeometry(QtCore.QRect(940, 90, 181, 71))
        self.back_btn.setStyleSheet("QPushButton{\n""background-color: rgb(255, 255, 255);\n"
                                    "font: 63 20pt \"Yu Gothic UI Semibold\";\n"
                                    "border-radius: 30;\n""}\n""\n"
                                    "QPushButton:pressed{\n""    background-color: rgb(200, 200, 200)\n""    \n""}")
        self.back_btn.setObjectName("back_btn")
        self.discount2 = QtWidgets.QLabel(marc_first)
        self.discount2.setGeometry(QtCore.QRect(10, 90, 221, 91))
        self.discount2.setStyleSheet("font: 63 20pt \"Yu Gothic UI Semibold\";\n""color: rgb(255, 255, 255);")
        self.discount2.setObjectName("discount2")
        self.picture2 = QtWidgets.QLabel(marc_first)
        self.picture2.setGeometry(QtCore.QRect(830, 640, 551, 511))
        self.picture2.setText("")
        self.picture2.setPixmap(QtGui.QPixmap("./oak_tree01.jpgE551438F-166F-491C-AE90-13DCE18C6367Large.jpg"))
        self.picture2.setObjectName("picture2")
        self.picture = QtWidgets.QLabel(marc_first)
        self.picture.setGeometry(QtCore.QRect(-210, 690, 551, 511))
        self.picture.setText("")
        self.picture.setPixmap(QtGui.QPixmap("./oak_tree01.jpgE551438F-166F-491C-AE90-13DCE18C6367Large.jpg"))
        self.picture.setObjectName("picture")
        self.line_3 = QtWidgets.QFrame(marc_first)
        self.line_3.setGeometry(QtCore.QRect(1110, 310, 41, 351))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.r2c2 = QtWidgets.QPushButton(marc_first)
        self.r2c2.setGeometry(QtCore.QRect(310, 300, 81, 71))
        self.r2c2.setStyleSheet("QPushButton{\n""background-color: rgb(0, 170, 0);\n"
                                "font: 63 20pt \"Yu Gothic UI Semibold\";\n"
                                "border-radius: 10;\n""}\n""\n""QPushButton:pressed{\n"
                                "    background-color: rgb(200, 200, 200)\n""    \n""}")
        self.r2c2.setText("")
        self.r2c2.setObjectName("r2c2")
        self.r1c2 = QtWidgets.QPushButton(marc_first)
        self.r1c2.setGeometry(QtCore.QRect(310, 210, 81, 71))
        self.r1c2.setStyleSheet("QPushButton{\n""background-color: rgb(0, 170, 0);\n"
                                "font: 63 20pt \"Yu Gothic UI Semibold\";\n"
                                "border-radius: 10;\n""}\n""\n""QPushButton:pressed{\n"
                                "    background-color: rgb(200, 200, 200)\n""    \n""}")
        self.r1c2.setText("")
        self.r1c2.setObjectName("r1c2")
        self.r1c3 = QtWidgets.QPushButton(marc_first)
        self.r1c3.setGeometry(QtCore.QRect(410, 210, 81, 71))
        self.r1c3.setStyleSheet("QPushButton{\n""background-color: rgb(0, 170, 0);\n"
                                "font: 63 20pt \"Yu Gothic UI Semibold\";\n"
                                "border-radius: 10;\n""}\n""\n""QPushButton:pressed{\n"
                                "    background-color: rgb(200, 200, 200)\n""    \n""}")
        self.r1c3.setText("")
        self.r1c3.setObjectName("r1c3")
        self.r1c4 = QtWidgets.QPushButton(marc_first)
        self.r1c4.setGeometry(QtCore.QRect(510, 210, 81, 71))
        self.r1c4.setStyleSheet("QPushButton{\n""background-color: rgb(0, 170, 0);\n"
                                "font: 63 20pt \"Yu Gothic UI Semibold\";\n"
                                "border-radius: 10;\n""}\n""\n""QPushButton:pressed{\n"
                                "    background-color: rgb(200, 200, 200)\n""    \n""}")
        self.r1c4.setText("")
        self.r1c4.setObjectName("r1c4")
        self.r1c5 = QtWidgets.QPushButton(marc_first)
        self.r1c5.setGeometry(QtCore.QRect(610, 210, 81, 71))
        self.r1c5.setStyleSheet("QPushButton{\n""background-color: rgb(0, 170, 0);\n"
                                "font: 63 20pt \"Yu Gothic UI Semibold\";\n"
                                "border-radius: 10;\n""}\n""\n""QPushButton:pressed{\n"
                                "    background-color: rgb(200, 200, 200)\n""    \n""}")
        self.r1c5.setText("")
        self.r1c5.setObjectName("r1c5")
        self.r1c6 = QtWidgets.QPushButton(marc_first)
        self.r1c6.setGeometry(QtCore.QRect(710, 210, 81, 71))
        self.r1c6.setStyleSheet("QPushButton{\n""background-color: rgb(0, 170, 0);\n"
                                "font: 63 20pt \"Yu Gothic UI Semibold\";\n"
                                "border-radius: 10;\n""}\n""\n""QPushButton:pressed{\n"
                                "    background-color: rgb(200, 200, 200)\n""    \n""}")
        self.r1c6.setText("")
        self.r1c6.setObjectName("r1c6")
        self.r2c1 = QtWidgets.QPushButton(marc_first)
        self.r2c1.setGeometry(QtCore.QRect(220, 300, 81, 71))
        self.r2c1.setStyleSheet("QPushButton{\n""background-color: rgb(0, 170, 0);\n"
                                "font: 63 20pt \"Yu Gothic UI Semibold\";\n"
                                "border-radius: 10;\n""}\n""\n""QPushButton:pressed{\n"
                                "    background-color: rgb(200, 200, 200)\n""    \n""}")
        self.r2c1.setText("")
        self.r2c1.setObjectName("r2c1")
        self.r2c3 = QtWidgets.QPushButton(marc_first)
        self.r2c3.setGeometry(QtCore.QRect(410, 300, 81, 71))
        self.r2c3.setStyleSheet("QPushButton{\n""background-color: rgb(0, 170, 0);\n"
                                "font: 63 20pt \"Yu Gothic UI Semibold\";\n"
                                "border-radius: 10;\n""}\n""\n""QPushButton:pressed{\n"
                                "    background-color: rgb(200, 200, 200)\n""    \n""}")
        self.r2c3.setText("")
        self.r2c3.setObjectName("r2c3")
        self.r2c4 = QtWidgets.QPushButton(marc_first)
        self.r2c4.setGeometry(QtCore.QRect(510, 300, 81, 71))
        self.r2c4.setStyleSheet("QPushButton{\n""background-color: rgb(0, 170, 0);\n"
                                "font: 63 20pt \"Yu Gothic UI Semibold\";\n"
                                "border-radius: 10;\n""}\n""\n""QPushButton:pressed{\n"
                                "    background-color: rgb(200, 200, 200)\n""    \n""}")
        self.r2c4.setText("")
        self.r2c4.setObjectName("r2c4")
        self.r2c5 = QtWidgets.QPushButton(marc_first)
        self.r2c5.setGeometry(QtCore.QRect(610, 300, 81, 71))
        self.r2c5.setStyleSheet("QPushButton{\n""background-color: rgb(0, 170, 0);\n"
                                "font: 63 20pt \"Yu Gothic UI Semibold\";\n"
                                "border-radius: 10;\n""}\n""\n""QPushButton:pressed{\n"
                                "    background-color: rgb(200, 200, 200)\n""    \n""}")
        self.r2c5.setText("")
        self.r2c5.setObjectName("r2c5")
        self.r2c6 = QtWidgets.QPushButton(marc_first)
        self.r2c6.setGeometry(QtCore.QRect(710, 300, 81, 71))
        self.r2c6.setStyleSheet("QPushButton{\n""background-color: rgb(0, 170, 0);\n"
                                "font: 63 20pt \"Yu Gothic UI Semibold\";\n"
                                "border-radius: 10;\n""}\n""\n""QPushButton:pressed{\n"
                                "    background-color: rgb(200, 200, 200)\n""    \n""}")
        self.r2c6.setText("")
        self.r2c6.setObjectName("r2c6")
        self.r2c7 = QtWidgets.QPushButton(marc_first)
        self.r2c7.setGeometry(QtCore.QRect(800, 300, 81, 71))
        self.r2c7.setStyleSheet("QPushButton{\n""background-color: rgb(0, 170, 0);\n"
                                "font: 63 20pt \"Yu Gothic UI Semibold\";\n"
                                "border-radius: 10;\n""}\n""\n""QPushButton:pressed{\n"
                                "    background-color: rgb(200, 200, 200)\n""    \n""}")
        self.r2c7.setText("")
        self.r2c7.setObjectName("r2c7")
        self.r3c1 = QtWidgets.QPushButton(marc_first)
        self.r3c1.setGeometry(QtCore.QRect(220, 390, 81, 71))
        self.r3c1.setStyleSheet("QPushButton{\n""background-color: rgb(0, 170, 0);\n"
                                "font: 63 20pt \"Yu Gothic UI Semibold\";\n"
                                "border-radius: 10;\n""}\n""\n""QPushButton:pressed{\n"
                                "    background-color: rgb(200, 200, 200)\n""    \n""}")
        self.r3c1.setText("")
        self.r3c1.setObjectName("r3c1")
        self.r3c2 = QtWidgets.QPushButton(marc_first)
        self.r3c2.setGeometry(QtCore.QRect(310, 390, 81, 71))
        self.r3c2.setStyleSheet("QPushButton{\n""background-color: rgb(0, 170, 0);\n"
                                "font: 63 20pt \"Yu Gothic UI Semibold\";\n"
                                "border-radius: 10;\n""}\n""\n""QPushButton:pressed{\n"
                                "    background-color: rgb(200, 200, 200)\n""    \n""}")
        self.r3c2.setText("")
        self.r3c2.setObjectName("r3c2")
        self.r3c3 = QtWidgets.QPushButton(marc_first)
        self.r3c3.setGeometry(QtCore.QRect(410, 390, 81, 71))
        self.r3c3.setStyleSheet("QPushButton{\n""background-color: rgb(0, 170, 0);\n"
                                "font: 63 20pt \"Yu Gothic UI Semibold\";\n"
                                "border-radius: 10;\n""}\n""\n""QPushButton:pressed{\n"
                                "    background-color: rgb(200, 200, 200)\n""    \n""}")
        self.r3c3.setText("")
        self.r3c3.setObjectName("r3c3")
        self.r3c4 = QtWidgets.QPushButton(marc_first)
        self.r3c4.setGeometry(QtCore.QRect(510, 390, 81, 71))
        self.r3c4.setStyleSheet("QPushButton{\n""background-color: rgb(0, 170, 0);\n"
                                "font: 63 20pt \"Yu Gothic UI Semibold\";\n"
                                "border-radius: 10;\n""}\n""\n""QPushButton:pressed{\n"
                                "    background-color: rgb(200, 200, 200)\n""    \n""}")
        self.r3c4.setText("")
        self.r3c4.setObjectName("r3c4")
        self.r3c5 = QtWidgets.QPushButton(marc_first)
        self.r3c5.setGeometry(QtCore.QRect(610, 390, 81, 71))
        self.r3c5.setStyleSheet("QPushButton{\n""background-color: rgb(0, 170, 0);\n"
                                "font: 63 20pt \"Yu Gothic UI Semibold\";\n"
                                "border-radius: 10;\n""}\n""\n""QPushButton:pressed{\n"
                                "    background-color: rgb(200, 200, 200)\n""    \n""}")
        self.r3c5.setText("")
        self.r3c5.setObjectName("r3c5")
        self.r3c6 = QtWidgets.QPushButton(marc_first)
        self.r3c6.setGeometry(QtCore.QRect(710, 390, 81, 71))
        self.r3c6.setStyleSheet("QPushButton{\n""background-color: rgb(0, 170, 0);\n"
                                "font: 63 20pt \"Yu Gothic UI Semibold\";\n"
                                "border-radius: 10;\n""}\n""\n""QPushButton:pressed{\n"
                                "    background-color: rgb(200, 200, 200)\n""    \n""}")
        self.r3c6.setText("")
        self.r3c6.setObjectName("r3c6")
        self.r3c7 = QtWidgets.QPushButton(marc_first)
        self.r3c7.setGeometry(QtCore.QRect(800, 390, 81, 71))
        self.r3c7.setStyleSheet("QPushButton{\n""background-color: rgb(0, 170, 0);\n"
                                "font: 63 20pt \"Yu Gothic UI Semibold\";\n"
                                "border-radius: 10;\n""}\n""\n""QPushButton:pressed{\n"
                                "    background-color: rgb(200, 200, 200)\n""    \n""}")
        self.r3c7.setText("")
        self.r3c7.setObjectName("r3c7")
        self.r4c1 = QtWidgets.QPushButton(marc_first)
        self.r4c1.setGeometry(QtCore.QRect(220, 480, 81, 71))
        self.r4c1.setStyleSheet("QPushButton{\n""background-color: rgb(0, 170, 0);\n"
                                "font: 63 20pt \"Yu Gothic UI Semibold\";\n"
                                "border-radius: 10;\n""}\n""\n""QPushButton:pressed{\n"
                                "    background-color: rgb(200, 200, 200)\n""    \n""}")
        self.r4c1.setText("")
        self.r4c1.setObjectName("r4c1")
        self.r4c2 = QtWidgets.QPushButton(marc_first)
        self.r4c2.setGeometry(QtCore.QRect(310, 480, 81, 71))
        self.r4c2.setStyleSheet("QPushButton{\n""background-color: rgb(0, 170, 0);\n"
                                "font: 63 20pt \"Yu Gothic UI Semibold\";\n"
                                "border-radius: 10;\n""}\n""\n""QPushButton:pressed{\n"
                                "    background-color: rgb(200, 200, 200)\n""    \n""}")
        self.r4c2.setText("")
        self.r4c2.setObjectName("r4c2")
        self.r4c3 = QtWidgets.QPushButton(marc_first)
        self.r4c3.setGeometry(QtCore.QRect(410, 480, 81, 71))
        self.r4c3.setStyleSheet("QPushButton{\n""background-color: rgb(0, 170, 0);\n"
                                "font: 63 20pt \"Yu Gothic UI Semibold\";\n"
                                "border-radius: 10;\n""}\n""\n""QPushButton:pressed{\n"
                                "    background-color: rgb(200, 200, 200)\n""    \n""}")
        self.r4c3.setText("")
        self.r4c3.setObjectName("r4c3")
        self.r4c4 = QtWidgets.QPushButton(marc_first)
        self.r4c4.setGeometry(QtCore.QRect(510, 480, 81, 71))
        self.r4c4.setStyleSheet("QPushButton{\n""background-color: rgb(0, 170, 0);\n"
                                "font: 63 20pt \"Yu Gothic UI Semibold\";\n"
                                "border-radius: 10;\n""}\n""\n""QPushButton:pressed{\n"
                                "    background-color: rgb(200, 200, 200)\n""    \n""}")
        self.r4c4.setText("")
        self.r4c4.setObjectName("r4c4")
        self.r4c5 = QtWidgets.QPushButton(marc_first)
        self.r4c5.setGeometry(QtCore.QRect(610, 480, 81, 71))
        self.r4c5.setStyleSheet("QPushButton{\n""background-color: rgb(0, 170, 0);\n"
                                "font: 63 20pt \"Yu Gothic UI Semibold\";\n"
                                "border-radius: 10;\n""}\n""\n""QPushButton:pressed{\n"
                                "    background-color: rgb(200, 200, 200)\n""    \n""}")
        self.r4c5.setText("")
        self.r4c5.setObjectName("r4c5")
        self.r4c6 = QtWidgets.QPushButton(marc_first)
        self.r4c6.setGeometry(QtCore.QRect(710, 480, 81, 71))
        self.r4c6.setStyleSheet("QPushButton{\n""background-color: rgb(0, 170, 0);\n"
                                "font: 63 20pt \"Yu Gothic UI Semibold\";\n"
                                "border-radius: 10;\n""}\n""\n""QPushButton:pressed{\n"
                                "    background-color: rgb(200, 200, 200)\n""    \n""}")
        self.r4c6.setText("")
        self.r4c6.setObjectName("r4c6")
        self.r4c7 = QtWidgets.QPushButton(marc_first)
        self.r4c7.setGeometry(QtCore.QRect(800, 480, 81, 71))
        self.r4c7.setStyleSheet("QPushButton{\n""background-color: rgb(0, 170, 0);\n"
                                "font: 63 20pt \"Yu Gothic UI Semibold\";\n"
                                "border-radius: 10;\n""}\n""\n""QPushButton:pressed{\n"
                                "    background-color: rgb(200, 200, 200)\n""    \n""}")
        self.r4c7.setText("")
        self.r4c7.setObjectName("r4c7")
        self.r5c3 = QtWidgets.QPushButton(marc_first)
        self.r5c3.setGeometry(QtCore.QRect(410, 570, 81, 71))
        self.r5c3.setStyleSheet("QPushButton{\n""background-color: rgb(0, 170, 0);\n"
                                "font: 63 20pt \"Yu Gothic UI Semibold\";\n"
                                "border-radius: 10;\n""}\n""\n""QPushButton:pressed{\n"
                                "    background-color: rgb(200, 200, 200)\n""    \n""}")
        self.r5c3.setText("")
        self.r5c3.setObjectName("r5c3")
        self.r5c4 = QtWidgets.QPushButton(marc_first)
        self.r5c4.setGeometry(QtCore.QRect(510, 570, 81, 71))
        self.r5c4.setStyleSheet("QPushButton{\n""background-color: rgb(0, 170, 0);\n"
                                "font: 63 20pt \"Yu Gothic UI Semibold\";\n"
                                "border-radius: 10;\n""}\n""\n""QPushButton:pressed{\n"
                                "    background-color: rgb(200, 200, 200)\n""    \n""}")
        self.r5c4.setText("")
        self.r5c4.setObjectName("r5c4")
        self.r5c1 = QtWidgets.QPushButton(marc_first)
        self.r5c1.setGeometry(QtCore.QRect(220, 570, 81, 71))
        self.r5c1.setStyleSheet("QPushButton{\n""background-color: rgb(0, 170, 0);\n"
                                "font: 63 20pt \"Yu Gothic UI Semibold\";\n"
                                "border-radius: 10;\n""}\n""\n""QPushButton:pressed{\n"
                                "    background-color: rgb(200, 200, 200)\n""    \n""}")
        self.r5c1.setText("")
        self.r5c1.setObjectName("r5c1")
        self.r5c7 = QtWidgets.QPushButton(marc_first)
        self.r5c7.setGeometry(QtCore.QRect(800, 570, 81, 71))
        self.r5c7.setStyleSheet("QPushButton{\n""background-color: rgb(0, 170, 0);\n"
                                "font: 63 20pt \"Yu Gothic UI Semibold\";\n"
                                "border-radius: 10;\n""}\n""\n""QPushButton:pressed{\n"
                                "    background-color: rgb(200, 200, 200)\n""    \n""}")
        self.r5c7.setText("")
        self.r5c7.setObjectName("r5c7")
        self.r5c6 = QtWidgets.QPushButton(marc_first)
        self.r5c6.setGeometry(QtCore.QRect(710, 570, 81, 71))
        self.r5c6.setStyleSheet("QPushButton{\n""background-color: rgb(0, 170, 0);\n"
                                "font: 63 20pt \"Yu Gothic UI Semibold\";\n"
                                "border-radius: 10;\n""}\n""\n""QPushButton:pressed{\n"
                                "    background-color: rgb(200, 200, 200)\n""    \n""}")
        self.r5c6.setText("")
        self.r5c6.setObjectName("r5c6")
        self.r5c2 = QtWidgets.QPushButton(marc_first)
        self.r5c2.setGeometry(QtCore.QRect(310, 570, 81, 71))
        self.r5c2.setStyleSheet("QPushButton{\n""background-color: rgb(0, 170, 0);\n"
                                "font: 63 20pt \"Yu Gothic UI Semibold\";\n"
                                "border-radius: 10;\n""}\n""\n""QPushButton:pressed{\n"
                                "    background-color: rgb(200, 200, 200)\n""    \n""}")
        self.r5c2.setText("")
        self.r5c2.setObjectName("r5c2")
        self.r5c5 = QtWidgets.QPushButton(marc_first)
        self.r5c5.setGeometry(QtCore.QRect(610, 570, 81, 71))
        self.r5c5.setStyleSheet("QPushButton{\n""background-color: rgb(0, 170, 0);\n"
                                "font: 63 20pt \"Yu Gothic UI Semibold\";\n"
                                "border-radius: 10;\n""}\n""\n""QPushButton:pressed{\n"
                                "    background-color: rgb(200, 200, 200)\n""    \n""}")
        self.r5c5.setText("")
        self.r5c5.setObjectName("r5c5")
        self.r6c3 = QtWidgets.QPushButton(marc_first)
        self.r6c3.setGeometry(QtCore.QRect(410, 660, 81, 71))
        self.r6c3.setStyleSheet("QPushButton{\n""background-color: rgb(0, 170, 0);\n"
                                "font: 63 20pt \"Yu Gothic UI Semibold\";\n"
                                "border-radius: 10;\n""}\n""\n""QPushButton:pressed{\n"
                                "    background-color: rgb(200, 200, 200)\n""    \n""}")
        self.r6c3.setText("")
        self.r6c3.setObjectName("r6c3")
        self.r6c4 = QtWidgets.QPushButton(marc_first)
        self.r6c4.setGeometry(QtCore.QRect(510, 660, 81, 71))
        self.r6c4.setStyleSheet("QPushButton{\n""background-color: rgb(0, 170, 0);\n"
                                "font: 63 20pt \"Yu Gothic UI Semibold\";\n"
                                "border-radius: 10;\n""}\n""\n""QPushButton:pressed{\n"
                                "    background-color: rgb(200, 200, 200)\n""    \n""}")
        self.r6c4.setText("")
        self.r6c4.setObjectName("r6c4")
        self.r6c1 = QtWidgets.QPushButton(marc_first)
        self.r6c1.setGeometry(QtCore.QRect(220, 660, 81, 71))
        self.r6c1.setStyleSheet("QPushButton{\n""background-color: rgb(0, 170, 0);\n"
                                "font: 63 20pt \"Yu Gothic UI Semibold\";\n"
                                "border-radius: 10;\n""}\n""\n""QPushButton:pressed{\n"
                                "    background-color: rgb(200, 200, 200)\n""    \n""}")
        self.r6c1.setText("")
        self.r6c1.setObjectName("r6c1")
        self.r6c7 = QtWidgets.QPushButton(marc_first)
        self.r6c7.setGeometry(QtCore.QRect(800, 660, 81, 71))
        self.r6c7.setStyleSheet("QPushButton{\n""background-color: rgb(0, 170, 0);\n"
                                "font: 63 20pt \"Yu Gothic UI Semibold\";\n"
                                "border-radius: 10;\n""}\n""\n""QPushButton:pressed{\n"
                                "    background-color: rgb(200, 200, 200)\n""    \n""}")
        self.r6c7.setText("")
        self.r6c7.setObjectName("r6c7")
        self.r6c6 = QtWidgets.QPushButton(marc_first)
        self.r6c6.setGeometry(QtCore.QRect(710, 660, 81, 71))
        self.r6c6.setStyleSheet("QPushButton{\n""background-color: rgb(0, 170, 0);\n"
                                "font: 63 20pt \"Yu Gothic UI Semibold\";\n"
                                "border-radius: 10;\n""}\n""\n""QPushButton:pressed{\n"
                                "    background-color: rgb(200, 200, 200)\n""    \n""}")
        self.r6c6.setText("")
        self.r6c6.setObjectName("r6c6")
        self.r6c2 = QtWidgets.QPushButton(marc_first)
        self.r6c2.setGeometry(QtCore.QRect(310, 660, 81, 71))
        self.r6c2.setStyleSheet("QPushButton{\n""background-color: rgb(0, 170, 0);\n"
                                "font: 63 20pt \"Yu Gothic UI Semibold\";\n"
                                "border-radius: 10;\n""}\n""\n""QPushButton:pressed{\n"
                                "    background-color: rgb(200, 200, 200)\n""    \n""}")
        self.r6c2.setText("")
        self.r6c2.setObjectName("r6c2")
        self.r6c5 = QtWidgets.QPushButton(marc_first)
        self.r6c5.setGeometry(QtCore.QRect(610, 660, 81, 71))
        self.r6c5.setStyleSheet("QPushButton{\n""background-color: rgb(0, 170, 0);\n"
                                "font: 63 20pt \"Yu Gothic UI Semibold\";\n"
                                "border-radius: 10;\n""}\n""\n""QPushButton:pressed{\n"
                                "    background-color: rgb(200, 200, 200)\n""    \n""}")
        self.r6c5.setText("")
        self.r6c5.setObjectName("r6c5")
        self.r1 = QtWidgets.QLabel(marc_first)
        self.r1.setGeometry(QtCore.QRect(170, 220, 20, 51))
        self.r1.setStyleSheet("font: 63 20pt \"Yu Gothic UI Semibold\";")
        self.r1.setObjectName("r1")
        self.r2 = QtWidgets.QLabel(marc_first)
        self.r2.setGeometry(QtCore.QRect(170, 300, 20, 51))
        self.r2.setStyleSheet("font: 63 20pt \"Yu Gothic UI Semibold\";")
        self.r2.setObjectName("r2")
        self.r3 = QtWidgets.QLabel(marc_first)
        self.r3.setGeometry(QtCore.QRect(170, 390, 20, 51))
        self.r3.setStyleSheet("font: 63 20pt \"Yu Gothic UI Semibold\";")
        self.r3.setObjectName("r3")
        self.r6 = QtWidgets.QLabel(marc_first)
        self.r6.setGeometry(QtCore.QRect(170, 660, 20, 51))
        self.r6.setStyleSheet("font: 63 20pt \"Yu Gothic UI Semibold\";")
        self.r6.setObjectName("r6")
        self.r4 = QtWidgets.QLabel(marc_first)
        self.r4.setGeometry(QtCore.QRect(170, 480, 20, 51))
        self.r4.setStyleSheet("font: 63 20pt \"Yu Gothic UI Semibold\";")
        self.r4.setObjectName("r4")
        self.r5 = QtWidgets.QLabel(marc_first)
        self.r5.setGeometry(QtCore.QRect(170, 570, 20, 51))
        self.r5.setStyleSheet("font: 63 20pt \"Yu Gothic UI Semibold\";")
        self.r5.setObjectName("r5")
        self.c1 = QtWidgets.QLabel(marc_first)
        self.c1.setGeometry(QtCore.QRect(240, 740, 20, 51))
        self.c1.setStyleSheet("font: 63 20pt \"Yu Gothic UI Semibold\";")
        self.c1.setObjectName("c1")
        self.c3 = QtWidgets.QLabel(marc_first)
        self.c3.setGeometry(QtCore.QRect(440, 740, 20, 51))
        self.c3.setStyleSheet("font: 63 20pt \"Yu Gothic UI Semibold\";")
        self.c3.setObjectName("c3")
        self.c2 = QtWidgets.QLabel(marc_first)
        self.c2.setGeometry(QtCore.QRect(340, 740, 20, 51))
        self.c2.setStyleSheet("font: 63 20pt \"Yu Gothic UI Semibold\";")
        self.c2.setObjectName("c2")
        self.c4 = QtWidgets.QLabel(marc_first)
        self.c4.setGeometry(QtCore.QRect(530, 740, 20, 51))
        self.c4.setStyleSheet("font: 63 20pt \"Yu Gothic UI Semibold\";")
        self.c4.setObjectName("c4")
        self.c5 = QtWidgets.QLabel(marc_first)
        self.c5.setGeometry(QtCore.QRect(630, 740, 20, 51))
        self.c5.setStyleSheet("font: 63 20pt \"Yu Gothic UI Semibold\";")
        self.c5.setObjectName("c5")
        self.c6 = QtWidgets.QLabel(marc_first)
        self.c6.setGeometry(QtCore.QRect(730, 740, 20, 51))
        self.c6.setStyleSheet("font: 63 20pt \"Yu Gothic UI Semibold\";")
        self.c6.setObjectName("c6")
        self.c7 = QtWidgets.QLabel(marc_first)
        self.c7.setGeometry(QtCore.QRect(830, 740, 20, 51))
        self.c7.setStyleSheet("font: 63 20pt \"Yu Gothic UI Semibold\";")
        self.c7.setObjectName("c7")
        self.picture.raise_()
        self.picture2.raise_()
        self.green_l.raise_()
        self.main_l.raise_()
        self.main_l2.raise_()
        self.black_line.raise_()
        self.back_btn.raise_()
        self.discount2.raise_()
        self.line_3.raise_()
        self.r2c2.raise_()
        self.r1c2.raise_()
        self.r1c3.raise_()
        self.r1c4.raise_()
        self.r1c5.raise_()
        self.r1c6.raise_()
        self.r2c1.raise_()
        self.r2c3.raise_()
        self.r2c4.raise_()
        self.r2c5.raise_()
        self.r2c6.raise_()
        self.r2c7.raise_()
        self.r3c1.raise_()
        self.r3c2.raise_()
        self.r3c3.raise_()
        self.r3c4.raise_()
        self.r3c5.raise_()
        self.r3c6.raise_()
        self.r3c7.raise_()
        self.r4c1.raise_()
        self.r4c2.raise_()
        self.r4c3.raise_()
        self.r4c4.raise_()
        self.r4c5.raise_()
        self.r4c6.raise_()
        self.r4c7.raise_()
        self.r5c3.raise_()
        self.r5c4.raise_()
        self.r5c1.raise_()
        self.r5c7.raise_()
        self.r5c6.raise_()
        self.r5c2.raise_()
        self.r5c5.raise_()
        self.r6c3.raise_()
        self.r6c4.raise_()
        self.r6c1.raise_()
        self.r6c7.raise_()
        self.r6c6.raise_()
        self.r6c2.raise_()
        self.r6c5.raise_()
        self.r1.raise_()
        self.r2.raise_()
        self.r3.raise_()
        self.r6.raise_()
        self.r4.raise_()
        self.r5.raise_()
        self.c1.raise_()
        self.c3.raise_()
        self.c2.raise_()
        self.c4.raise_()
        self.c5.raise_()
        self.c6.raise_()
        self.c7.raise_()

        self.retranslateUi(marc_first)
        QtCore.QMetaObject.connectSlotsByName(marc_first)

    def retranslateUi(self, marc_first):
        _translate = QtCore.QCoreApplication.translate
        marc_first.setWindowTitle(_translate("marc_first", "Form"))
        self.main_l.setToolTip(_translate("marc_first", "<html><head/><body><p><span style=\" font-size:16pt;"
                                                        " color:#ffffff;\">WCinema</span></p></body></html>"))
        self.main_l.setWhatsThis(_translate("marc_first", "<html><head/><body><p>ACinema</p></body></html>"))
        self.main_l.setText(_translate("marc_first", "ACinema"))
        self.main_l2.setText(_translate("marc_first", "Кинотеатр для\n"
" всей семьи"))
        self.back_btn.setText(_translate("marc_first", "Назад"))

        self.r1.setText(_translate("marc_first", "1"))
        self.r2.setText(_translate("marc_first", "2"))
        self.r3.setText(_translate("marc_first", "3"))
        self.r6.setText(_translate("marc_first", "6"))
        self.r4.setText(_translate("marc_first", "4"))
        self.r5.setText(_translate("marc_first", "5"))
        self.c1.setText(_translate("marc_first", "1"))
        self.c3.setText(_translate("marc_first", "3"))
        self.c2.setText(_translate("marc_first", "2"))
        self.c4.setText(_translate("marc_first", "4"))
        self.c5.setText(_translate("marc_first", "5"))
        self.c6.setText(_translate("marc_first", "6"))
        self.c7.setText(_translate("marc_first", "7"))
