from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_about_form(object):
    def setupUi(self, about_form):
        about_form.setObjectName("about_form")
        about_form.resize(1140, 850)
        self.text = QtWidgets.QLabel(about_form)
        self.text.setGeometry(QtCore.QRect(50, 160, 1061, 451))
        self.text.setStyleSheet("font: 63 13pt \"Yu Gothic UI Semibold\";")
        self.text.setObjectName("text")

        self.picture = QtWidgets.QLabel(about_form)
        self.picture.setGeometry(QtCore.QRect(-190, 570, 600, 600))
        self.picture.setText("")
        self.picture.setPixmap(QtGui.QPixmap("./pictures/oak_tree01.jpgE551438F-166F-491C-AE90-13DCE18C6367Large.jpg"))
        self.picture.setObjectName("picture")
        self.picture2 = QtWidgets.QLabel(about_form)
        self.picture2.setGeometry(QtCore.QRect(770, 560, 600, 600))
        self.picture2.setText("")
        self.picture2.setPixmap(QtGui.QPixmap("./pictures/oak_tree01.jpgE551438F-166F-491C-AE90-13DCE18C6367Large.jpg"))
        self.picture2.setObjectName("picture2")
        self.green_l = QtWidgets.QLabel(about_form)
        self.green_l.setGeometry(QtCore.QRect(0, 0, 1141, 81))
        self.green_l.setStyleSheet("background-color: rgb(0, 85, 0);")
        self.green_l.setText("")
        self.green_l.setObjectName("green_l")
        self.black_l = QtWidgets.QLabel(about_form)
        self.black_l.setGeometry(QtCore.QRect(0, 80, 1141, 101))
        self.black_l.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.black_l.setText("")
        self.black_l.setObjectName("black_l")
        self.back_btn = QtWidgets.QPushButton(about_form)
        self.back_btn.setGeometry(QtCore.QRect(920, 100, 181, 71))
        self.back_btn.setStyleSheet("QPushButton{\n" "background-color: rgb(255, 255, 255);"
                                    "\n" "font: 63 20pt \"Yu Gothic UI Semibold\";\n""border-radius: 30;"
                                    "\n""}\n""\n""QPushButton:pressed{\n""    background-color:"
                                    " rgb(200, 200, 200)\n""    \n""}")
        self.back_btn.setObjectName("back_btn")
        self.main_l = QtWidgets.QLabel(about_form)
        self.main_l.setGeometry(QtCore.QRect(10, 10, 161, 61))
        self.main_l.setStyleSheet("background-color: rgb(0, 85, 0);\n"
                                  "\n""font: 20pt \"Adobe Caslon Pro\";\n""color: rgb(255, 255, 255);")
        self.main_l.setObjectName("main_l")
        self.main_l2 = QtWidgets.QLabel(about_form)
        self.main_l2.setGeometry(QtCore.QRect(150, 0, 181, 71))
        self.main_l2.setStyleSheet("background-color: rgb(0, 85, 0);\n""color: rgb(217, 217, 217);")
        self.main_l2.setObjectName("main_l2")
        self.picture.raise_()
        self.picture2.raise_()
        self.green_l.raise_()
        self.black_l.raise_()
        self.back_btn.raise_()
        self.main_l.raise_()
        self.text.raise_()
        self.main_l2.raise_()

        self.retranslateUi(about_form)
        QtCore.QMetaObject.connectSlotsByName(about_form)

    def retranslateUi(self, about_form):
        _translate = QtCore.QCoreApplication.translate
        about_form.setWindowTitle(_translate("about_form", "Form"))
        self.text.setText(_translate("about_form", "1) Корпоративная этика нашей компании основана"
        " на принципах гостеприимства\n"" "
        "и доброжелательности. "
        "Главный приоритет –Гость. \n"
        "Мы любим наших гостей так, как любим свою бабушку, подарившую нам трех комнатную квартиру! \n"
        "2) Мы стремимся следовать нашей Миссии\n"
        " и превосходить ожидания каждого гостя/клиента. \n"
        "3) Мы с уважением относимся к профессиональным навыкам и знаниям,\n"
        "традициям, моральным устоям и взглядам на этику бизнеса, существующим у наших партнеров\n"
        " и гостей, клиентов. Мы всегда готовы идти на компромисс при возникновении\n"
        " трудностей в достижении соглашения, путем переговоров.\n"
        " Мы признаем волеизъявления партнеров и потребителей. \n"
        "4) Мы убеждены, что все потребители услуг сферы гостеприимства,\n"
        " в праве получать качественное обслуживание, и не важно являются ли они нашими гостями.\n"
        " Поэтому мы рассматриваем партнеров не как конкурентов, а как единомышленников и коллег."))
        self.back_btn.setText(_translate("about_form", "Назад"))
        self.main_l.setText(_translate("about_form", "ACinema"))
        self.main_l2.setText(_translate("about_form", "Кинотеатр для\n"
" всей семьи"))
