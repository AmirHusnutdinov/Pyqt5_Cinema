import sqlite3
import random
from PyQt5 import QtCore, QtGui, QtWidgets


def update():
    con = sqlite3.connect(r'.\rev.db')
    cur = con.cursor()
    mass = []
    result = cur.execute('''SELECT id FROM rev''').fetchall()
    for i in result:
        mass.append(int(i[0]))

    n1 = random.randrange(1, mass[-1] + 1)
    result_t1 = cur.execute('''select Name, revi, comment from rev
    where id = ? ''', (n1,)).fetchall()
    n2 = random.randrange(1, mass[-1] + 1)
    while n2 == n1:
        n2 = random.randrange(1, (mass[-1] + 1))
    result_t2 = cur.execute('''select Name, revi, comment from rev
    where id = ? ''', (n2,)).fetchall()
    n3 = random.randrange(1, mass[-1] + 1)
    while n1 == n3 or n2 == n3:
        n3 = random.randrange(1, mass[-1] + 1)
    result_t3 = cur.execute('''select Name, revi, comment from rev
    where id = ? ''', (n3,)).fetchall()
    return result_t1, result_t2, result_t3


class Ui_reviems_form(object):
    def setupUi(self, reviems_form):
        reviems_form.setObjectName("reviems_form")
        reviems_form.resize(1140, 852)
        self.green_l = QtWidgets.QLabel(reviems_form)
        self.green_l.setGeometry(QtCore.QRect(-10, 0, 1151, 111))
        self.green_l.setStyleSheet("background-color: rgb(0, 85, 0);")
        self.green_l.setText("")
        self.green_l.setObjectName("green_l")
        self.main_l = QtWidgets.QLabel(reviems_form)
        self.main_l.setGeometry(QtCore.QRect(10, 30, 161, 61))
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
        self.main_l2 = QtWidgets.QLabel(reviems_form)
        self.main_l2.setGeometry(QtCore.QRect(160, 30, 201, 61))
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
        self.black_l = QtWidgets.QLabel(reviems_form)
        self.black_l.setGeometry(QtCore.QRect(0, 110, 1141, 101))
        self.black_l.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.black_l.setText("")
        self.black_l.setObjectName("black_l")
        self.reviems = QtWidgets.QLabel(reviems_form)
        self.reviems.setGeometry(QtCore.QRect(310, 70, 501, 131))
        self.reviems.setStyleSheet("font: 63 80pt \"Yu Gothic UI Semibold\";\n"
                                   "color: rgb(255, 255, 255);\n""")
        self.reviems.setObjectName("reviems")
        self.random_rev = QtWidgets.QLabel(reviems_form)
        self.random_rev.setGeometry(QtCore.QRect(20, 220, 321, 61))
        self.random_rev.setStyleSheet("font: 63 20pt \"Yu Gothic UI Semibold\";")
        self.random_rev.setObjectName("random_rev")
        self.add_rev = QtWidgets.QPushButton(reviems_form)
        self.add_rev.setGeometry(QtCore.QRect(350, 220, 271, 81))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.add_rev.setFont(font)
        self.add_rev.setStyleSheet("QPushButton{\n""background-color: rgb(0, 170, 0);\n"
                                   "font: 63 20pt \"Yu Gothic UI Semibold\";\n""border-radius: 30;\n""}\n""\n"
                                   "QPushButton:pressed{\n""    background-color: rgb(85, 255, 0)\n""}\n""")
        self.add_rev.setObjectName("add_rev")
        self.first_rev = QtWidgets.QTextEdit(reviems_form)
        self.first_rev.setEnabled(False)
        self.first_rev.setGeometry(QtCore.QRect(20, 340, 331, 311))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.first_rev.setFont(font)
        self.first_rev.setStyleSheet("font: 63 15pt \"Yu Gothic UI Semibold\";")
        self.first_rev.setObjectName("first_rev")
        a = update()
        result_t1 = a[0]
        result_t2 = a[1]
        result_t3 = a[2]
        self.first_rev.insertPlainText(f'{result_t1[0][0]}\n{result_t1[0][1]}\n{result_t1[0][2]}')
        self.line_4 = QtWidgets.QFrame(reviems_form)
        self.line_4.setGeometry(QtCore.QRect(0, 320, 1131, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line = QtWidgets.QFrame(reviems_form)
        self.line.setGeometry(QtCore.QRect(10, 650, 911, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(reviems_form)
        self.line_2.setGeometry(QtCore.QRect(740, 330, 20, 321))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(reviems_form)
        self.line_3.setGeometry(QtCore.QRect(360, 330, 20, 321))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.picture2 = QtWidgets.QLabel(reviems_form)
        self.picture2.setGeometry(QtCore.QRect(710, 610, 571, 541))
        self.picture2.setText("")
        self.picture2.setPixmap(QtGui.QPixmap("./pictures/oak_tree01.jpgE551438F-166F-491C-AE90-13DCE18C6367Large.jpg"))
        self.picture2.setObjectName("picture2")
        self.third_rev = QtWidgets.QTextEdit(reviems_form)
        self.third_rev.setEnabled(False)
        self.third_rev.setGeometry(QtCore.QRect(780, 340, 331, 311))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.third_rev.setFont(font)
        self.third_rev.setStyleSheet("font: 63 15pt \"Yu Gothic UI Semibold\";")
        self.third_rev.setObjectName("third_rev")
        self.third_rev.insertPlainText(f'{result_t3[0][0]}\n{result_t3[0][1]}\n{result_t3[0][2]}')
        self.second_rev = QtWidgets.QTextEdit(reviems_form)
        self.second_rev.setEnabled(False)
        self.second_rev.setGeometry(QtCore.QRect(390, 340, 331, 311))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.second_rev.setFont(font)
        self.second_rev.setStyleSheet("font: 63 15pt \"Yu Gothic UI Semibold\";")
        self.second_rev.setObjectName("second_rev")
        self.see_all_rev = QtWidgets.QPushButton(reviems_form)
        self.see_all_rev.setGeometry(QtCore.QRect(650, 220, 261, 81))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.second_rev.insertPlainText(f'{result_t2[0][0]}\n{result_t2[0][1]}\n{result_t2[0][2]}')
        self.see_all_rev.setFont(font)
        self.see_all_rev.setStyleSheet("QPushButton{\n""background-color: rgb(0, 170, 0);\n"
                                       "font: 63 20pt \"Yu Gothic UI Semibold\";\n""border-radius: 30;\n""}\n""\n"
                                       "QPushButton:pressed{\n""    background-color: rgb(85, 255, 0)\n""}\n""")
        self.see_all_rev.setObjectName("see_all_rev")
        self.back_btn = QtWidgets.QPushButton(reviems_form)
        self.back_btn.setGeometry(QtCore.QRect(910, 120, 181, 71))
        self.back_btn.setStyleSheet("QPushButton{\n""background-color: rgb(255, 255, 255);\n"
                                    "font: 63 20pt \"Yu Gothic UI Semibold\";\n""border-radius: 30;\n""}\n""\n"
                                    "QPushButton:pressed{\n""    background-color: rgb(200, 200, 200)\n""    \n""}")
        self.back_btn.setObjectName("back_btn")
        self.picture = QtWidgets.QLabel(reviems_form)
        self.picture.setGeometry(QtCore.QRect(-150, 620, 571, 541))
        self.picture.setText("")
        self.picture.setPixmap(QtGui.QPixmap("./pictures/oak_tree01.jpgE551438F-166F-491C-AE90-13DCE18C6367Large.jpg"))
        self.picture.setObjectName("picture")
        self.line_5 = QtWidgets.QFrame(reviems_form)
        self.line_5.setGeometry(QtCore.QRect(0, 330, 20, 321))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(reviems_form)
        self.line_6.setGeometry(QtCore.QRect(1110, 330, 20, 321))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.picture.raise_()
        self.picture2.raise_()
        self.green_l.raise_()
        self.main_l.raise_()
        self.main_l2.raise_()
        self.black_l.raise_()
        self.reviems.raise_()
        self.random_rev.raise_()
        self.add_rev.raise_()
        self.first_rev.raise_()
        self.line_4.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.line_3.raise_()
        self.third_rev.raise_()
        self.second_rev.raise_()
        self.see_all_rev.raise_()
        self.back_btn.raise_()
        self.line_5.raise_()
        self.line_6.raise_()

        self.retranslateUi(reviems_form)
        QtCore.QMetaObject.connectSlotsByName(reviems_form)

    def retranslateUi(self, reviems_form):
        _translate = QtCore.QCoreApplication.translate
        reviems_form.setWindowTitle(_translate("reviems_form", "Form"))
        self.main_l.setToolTip(_translate("reviems_form", "<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">WCinema</span></p></body></html>"))
        self.main_l.setWhatsThis(_translate("reviems_form", "<html><head/><body><p>ACinema</p></body></html>"))
        self.main_l.setText(_translate("reviems_form", "ACinema"))
        self.main_l2.setText(_translate("reviems_form", "Кинотеатр для\n"" всей семьи"))
        self.reviems.setText(_translate("reviems_form", "Отзывы"))
        self.random_rev.setText(_translate("reviems_form", "Случайные отзывы:"))
        self.add_rev.setText(_translate("reviems_form", "Добавить отзыв"))
        self.see_all_rev.setText(_translate("reviems_form", "Посмотреть все"))
        self.back_btn.setText(_translate("reviems_form", "Назад"))