from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5.QtWidgets import QTableWidgetItem


class Ui_all_feedback_form(object):
    def setupUi(self, all_feedback_form):
        all_feedback_form.setObjectName("all_feedback_form")
        all_feedback_form.resize(1140, 850)
        self.main_l2 = QtWidgets.QLabel(all_feedback_form)
        self.main_l2.setGeometry(QtCore.QRect(160, 10, 201, 61))
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
        self.main_l = QtWidgets.QLabel(all_feedback_form)
        self.main_l.setGeometry(QtCore.QRect(10, 10, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Adobe Caslon Pro")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.main_l.setFont(font)
        self.main_l.setStyleSheet("background-color: rgb(0, 85, 0);\n""\n" "font: 20pt \"Adobe Caslon Pro\";\n"
                                  "color: rgb(255, 255, 255);")
        self.main_l.setObjectName("main_l")
        self.black_l = QtWidgets.QLabel(all_feedback_form)
        self.black_l.setGeometry(QtCore.QRect(0, 80, 1141, 101))
        self.black_l.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.black_l.setText("")
        self.black_l.setObjectName("black_l")
        self.all_feedback_l = QtWidgets.QLabel(all_feedback_form)
        self.all_feedback_l.setGeometry(QtCore.QRect(220, 40, 741, 131))
        self.all_feedback_l.setStyleSheet("font: 63 80pt \"Yu Gothic UI Semibold\";\n""color: rgb(255, 255, 255);\n""")
        self.all_feedback_l.setObjectName("all_feedback_l")
        self.green_l = QtWidgets.QLabel(all_feedback_form)
        self.green_l.setGeometry(QtCore.QRect(0, 0, 1141, 81))
        self.green_l.setStyleSheet("background-color: rgb(0, 85, 0);")
        self.green_l.setText("")
        self.green_l.setObjectName("green_l")
        self.line_2 = QtWidgets.QFrame(all_feedback_form)
        self.line_2.setGeometry(QtCore.QRect(190, 180, 20, 431))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line = QtWidgets.QFrame(all_feedback_form)
        self.line.setGeometry(QtCore.QRect(200, 600, 801, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.picture1 = QtWidgets.QLabel(all_feedback_form)
        self.picture1.setGeometry(QtCore.QRect(-170, 580, 551, 511))
        self.picture1.setText("")
        self.picture1.setPixmap(QtGui.QPixmap("./pictures/oak_tree01.jpgE551438F-166F-491C-AE90-13DCE18C6367Large.jpg"))
        self.picture1.setObjectName("picture1")
        self.back_btn = QtWidgets.QPushButton(all_feedback_form)
        self.back_btn.setGeometry(QtCore.QRect(950, 100, 181, 71))
        self.back_btn.setStyleSheet("QPushButton{\n""background-color: rgb(255, 255, 255);\n"
                                    "font: 63 20pt \"Yu Gothic UI Semibold\";\n""border-radius: 30;\n""}\n""\n"
                                    "QPushButton:pressed{\n""    background-color: rgb(200, 200, 200)\n""    \n""}")
        self.back_btn.setObjectName("back_btn")
        self.picture2 = QtWidgets.QLabel(all_feedback_form)
        self.picture2.setGeometry(QtCore.QRect(800, 580, 551, 511))
        self.picture2.setText("")
        self.picture2.setPixmap(QtGui.QPixmap("./pictures/oak_tree01.jpgE551438F-166F-491C-AE90-13DCE18C6367Large.jpg"))
        self.picture2.setObjectName("picture2")
        self.line_3 = QtWidgets.QFrame(all_feedback_form)
        self.line_3.setGeometry(QtCore.QRect(990, 180, 20, 431))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.all_feedback = QtWidgets.QTableWidget(all_feedback_form)
        self.all_feedback.setGeometry(QtCore.QRect(210, 190, 781, 411))
        self.all_feedback.setObjectName("all_feedback")
        self.all_feedback.setColumnCount(0)
        self.all_feedback.setRowCount(0)
        self.black_l.raise_()
        self.green_l.raise_()
        self.picture1.raise_()
        self.back_btn.raise_()
        self.main_l.raise_()
        self.main_l2.raise_()
        self.all_feedback_l.raise_()
        self.picture2.raise_()
        self.line_2.raise_()
        self.line.raise_()
        self.line_3.raise_()
        self.all_feedback.raise_()

        self.retranslateUi(all_feedback_form)
        QtCore.QMetaObject.connectSlotsByName(all_feedback_form)

    def retranslateUi(self, all_feedback_form):
        _translate = QtCore.QCoreApplication.translate
        all_feedback_form.setWindowTitle(_translate("all_feedback_form", "Form"))
        self.main_l2.setText(_translate("all_feedback_form", "Кинотеатр для\n"" всей семьи"))
        self.main_l.setToolTip(_translate("all_feedback_form", "<html><head/><body><p><span style=\""
                                                               " font-size:16pt; color:#ffffff;\""
                                                               ">WCinema</span></p></body></html>"))
        self.main_l.setWhatsThis(_translate("all_feedback_form", "<html><head/><body><p>ACinema</p></body></html>"))
        self.main_l.setText(_translate("all_feedback_form", "ACinema"))
        self.all_feedback_l.setText(_translate("all_feedback_form", "Все отзывы"))
        self.back_btn.setText(_translate("all_feedback_form", "Назад"))
        self.update()

    def update(self):
        con = sqlite3.connect(r'./rev.db')
        cur = con.cursor()
        result = cur.execute('''SELECT * FROM rev''').fetchall()
        self.all_feedback.setRowCount(len(result))
        self.all_feedback.setColumnCount(3)
        self.all_feedback.setHorizontalHeaderLabels(['Имя и фамилия', 'Оценка', 'Коментарий'])
        count = 0
        for item in result:
            self.all_feedback.setItem(count, 0, QTableWidgetItem(f'{item[1]}'))
            count += 1
        count = 0
        for item in result:
            self.all_feedback.setItem(count, 1, QTableWidgetItem(f'{item[2]}'))
            count += 1
        count = 0
        for item in result:
            self.all_feedback.setItem(count, 2, QTableWidgetItem(f'{item[3]}'))
            count += 1
        header = self.all_feedback.horizontalHeader()
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        con.close()
