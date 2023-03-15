from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_film1_tod_form(object):
    def setupUi(self, film1_tod_form):
        film1_tod_form.setObjectName("film1_tod_form")
        film1_tod_form.resize(1140, 857)
        self.green_l = QtWidgets.QLabel(film1_tod_form)
        self.green_l.setGeometry(QtCore.QRect(0, 0, 1141, 81))
        self.green_l.setStyleSheet("background-color: rgb(0, 85, 0);")
        self.green_l.setText("")
        self.green_l.setObjectName("green_l")
        self.main_l = QtWidgets.QLabel(film1_tod_form)
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
        self.main_l2 = QtWidgets.QLabel(film1_tod_form)
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
        self.black_line = QtWidgets.QLabel(film1_tod_form)
        self.black_line.setGeometry(QtCore.QRect(0, 80, 1141, 101))
        self.black_line.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.black_line.setText("")
        self.black_line.setObjectName("black_line")
        self.back_btn = QtWidgets.QPushButton(film1_tod_form)
        self.back_btn.setGeometry(QtCore.QRect(940, 90, 181, 71))
        self.back_btn.setStyleSheet("QPushButton{\n""background-color: rgb(255, 255, 255);\n"
                                    "font: 63 20pt \"Yu Gothic UI Semibold\";\n""border-radius: 30;\n""}\n""\n"
                                    "QPushButton:pressed{\n""    background-color: rgb(200, 200, 200)\n""    \n""}")
        self.back_btn.setObjectName("back_btn")
        self.discount2 = QtWidgets.QLabel(film1_tod_form)
        self.discount2.setGeometry(QtCore.QRect(310, 310, 191, 61))
        self.discount2.setStyleSheet("font: 63 20pt \"Yu Gothic UI Semibold\";")
        self.discount2.setObjectName("discount2")
        self.label_10 = QtWidgets.QLabel(film1_tod_form)
        self.label_10.setGeometry(QtCore.QRect(820, 670, 551, 511))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("./pictures/oak_tree01.jpgE551438F-166F-491C-AE90-13DCE18C6367Large.jpg"))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(film1_tod_form)
        self.label_11.setGeometry(QtCore.QRect(-210, 690, 551, 511))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("./pictures/oak_tree01.jpgE551438F-166F-491C-AE90-13DCE18C6367Large.jpg"))
        self.label_11.setObjectName("label_11")
        self.change_film = QtWidgets.QPushButton(film1_tod_form)
        self.change_film.setGeometry(QtCore.QRect(570, 90, 331, 71))
        self.change_film.setStyleSheet("QPushButton{\n""background-color: rgb(255, 255, 255);\n"
                                       "font: 63 20pt \"Yu Gothic UI Semibold\";\n"
                                       "border-radius: 30;\n""}\n""\n""QPushButton:pressed{\n""    background-color:"
                                       " rgb(200, 200, 200)\n""    \n""}")
        self.change_film.setObjectName("change_film")
        self.label = QtWidgets.QLabel(film1_tod_form)
        self.label.setGeometry(QtCore.QRect(20, 320, 271, 331))
        self.label.setText("")
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.time11 = QtWidgets.QPushButton(film1_tod_form)
        self.time11.setGeometry(QtCore.QRect(310, 380, 201, 61))
        self.time11.setStyleSheet("QPushButton{\n""background-color: rgb(0, 170, 0);\n"
                                  "font: 63 20pt \"Yu Gothic UI Semibold\";\n"
                                  "border-radius: 20;\n""}\n""\n""QPushButton:pressed{\n"
                                  "    background-color: rgb(200, 200, 200)\n""    \n""}")
        self.time11.setObjectName("time11")
        self.time12 = QtWidgets.QPushButton(film1_tod_form)
        self.time12.setGeometry(QtCore.QRect(310, 450, 201, 61))
        self.time12.setStyleSheet("QPushButton{\n""background-color: rgb(0, 170, 0);\n"
                                  "font: 63 20pt \"Yu Gothic UI Semibold\";\n""border-radius: 20;\n""}\n""\n"
                                  "QPushButton:pressed{\n""    background-color: rgb(200, 200, 200)\n""    \n""}")
        self.time12.setObjectName("time12")
        self.label_2 = QtWidgets.QLabel(film1_tod_form)
        self.label_2.setGeometry(QtCore.QRect(600, 320, 281, 331))
        self.label_2.setText("")
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.time21 = QtWidgets.QPushButton(film1_tod_form)
        self.time21.setGeometry(QtCore.QRect(900, 380, 201, 61))
        self.time21.setStyleSheet("QPushButton{\n""background-color: rgb(0, 170, 0);\n"
                                  "font: 63 20pt \"Yu Gothic UI Semibold\";\n""border-radius: 20;\n""}\n""\n"
                                  "QPushButton:pressed{\n""    background-color: rgb(200, 200, 200)\n""    \n""}")
        self.time21.setObjectName("time21")
        self.time22 = QtWidgets.QPushButton(film1_tod_form)
        self.time22.setGeometry(QtCore.QRect(900, 450, 201, 61))
        self.time22.setStyleSheet("QPushButton{\n""background-color: rgb(0, 170, 0);\n"
                                  "font: 63 20pt \"Yu Gothic UI Semibold\";\n""border-radius: 20;\n""}\n""\n"
                                  "QPushButton:pressed{\n""    background-color: rgb(200, 200, 200)\n""    \n""}")
        self.time22.setObjectName("time22")
        self.discount2_2 = QtWidgets.QLabel(film1_tod_form)
        self.discount2_2.setGeometry(QtCore.QRect(910, 310, 191, 61))
        self.discount2_2.setStyleSheet("font: 63 20pt \"Yu Gothic UI Semibold\";")
        self.discount2_2.setObjectName("discount2_2")
        self.line = QtWidgets.QFrame(film1_tod_form)
        self.line.setGeometry(QtCore.QRect(0, 650, 1131, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(film1_tod_form)
        self.line_2.setGeometry(QtCore.QRect(520, 310, 20, 351))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(film1_tod_form)
        self.line_3.setGeometry(QtCore.QRect(1110, 310, 41, 351))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(film1_tod_form)
        self.line_4.setGeometry(QtCore.QRect(0, 300, 1141, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_11.raise_()
        self.label_10.raise_()
        self.green_l.raise_()
        self.main_l.raise_()
        self.main_l2.raise_()
        self.black_line.raise_()
        self.back_btn.raise_()
        self.discount2.raise_()
        self.change_film.raise_()
        self.label.raise_()
        self.time11.raise_()
        self.time12.raise_()
        self.label_2.raise_()
        self.time21.raise_()
        self.time22.raise_()
        self.discount2_2.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.line_3.raise_()
        self.line_4.raise_()

        self.retranslateUi(film1_tod_form)
        QtCore.QMetaObject.connectSlotsByName(film1_tod_form)

    def retranslateUi(self, film1_tod_form):
        _translate = QtCore.QCoreApplication.translate
        film1_tod_form.setWindowTitle(_translate("film1_tod_form", "Form"))
        self.main_l.setToolTip(_translate("film1_tod_form",
                                          "<html><head/><body><p><span style=\" ""font-size:16pt;"
                                          "\ color:#ffffff;\">WCinema</span></p></body></html>"))
        self.main_l.setWhatsThis(_translate("film1_tod_form", "<html><head/><body><p>ACinema</p></body></html>"))
        self.main_l.setText(_translate("film1_tod_form", "ACinema"))
        self.main_l2.setText(_translate("film1_tod_form", "Кинотеатр для\n"" всей семьи"))
        self.back_btn.setText(_translate("film1_tod_form", "Назад"))
        self.change_film.setText(_translate("film1_tod_form", "изменить фильмы"))
        self.time11.setText(_translate("film1_tod_form", "9:00"))
        self.time12.setText(_translate("film1_tod_form", "14:40"))
        self.time21.setText(_translate("film1_tod_form", "11:20"))
        self.time22.setText(_translate("film1_tod_form", "16:05"))