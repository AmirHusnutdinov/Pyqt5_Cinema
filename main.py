import sys
import sqlite3
from PyQt5 import QtGui, QtWidgets
from start_window import Ui_start_window
from main_window import Ui_main_form
from discounts import Ui_discounts_form
from feedback import Ui_reviems_form
from all_feedback import Ui_all_feedback_form
from add_feedback import Ui_add_feedback
from contacts_form import Ui_Contacts_form
from about_form import Ui_about_form
from film_tod_form import Ui_film1_tod_form
from mars_f import Ui_marc_first
from pay import Ui_pay_form
from change import Ui_Change_form
from change2 import Ui_Change2_form


def start():
    con = sqlite3.connect(r'./rev.db')
    cur = con.cursor()
    result = cur.execute('''SELECT title, way FROM actual_films''').fetchall()
    cur.close()
    con.close()
    return result


def films_today(add=None, id=None):
    con = sqlite3.connect(r'./rev.db')
    cur = con.cursor()
    result2 = cur.execute('''SELECT title, way, time, list_of_places FROM today_films''').fetchall()
    if add:
        cur.execute(f'''update today_films
        set list_of_places = "{result2[id][3]} {add}"
        where id = {id}''')
        con.commit()
    cur.close()
    con.close()
    return result2


app = QtWidgets.QApplication(sys.argv)
start_window = QtWidgets.QMainWindow()
ui = Ui_start_window()
ui.setupUi(start_window)
start_window.setFixedSize(1072, 771)
start_window.show()


def open_main_window():
    main_form = QtWidgets.QWidget()
    ui3 = Ui_main_form()
    ui3.setupUi(main_form)
    ui3.label_2.setPixmap(QtGui.QPixmap(start()[1][1]))
    ui3.label.setPixmap(QtGui.QPixmap(start()[0][1]))
    ui3.pictureAdam.setPixmap(QtGui.QPixmap(start()[2][1]))
    ui3.adam.setText(start()[2][0])
    ui3.heard.setText(start()[1][0])
    ui3.avatar.setText(start()[0][0])
    main_form.setFixedSize(1140, 850)
    main_form.show()
    start_window.close()

    def open_discount_form():
        discounts_form = QtWidgets.QWidget()
        ui = Ui_discounts_form()
        ui.setupUi(discounts_form)
        discounts_form.setFixedSize(1140, 850)
        discounts_form.show()
        main_form.close()

        def return_to_main_form():
            discounts_form.close()
            main_form.show()
        ui.back_btn.clicked.connect(return_to_main_form)

    def open_feedback_form():
        reviems_form = QtWidgets.QWidget()
        ui = Ui_reviems_form()
        ui.setupUi(reviems_form)
        reviems_form.setFixedSize(1140, 850)
        reviems_form.show()
        main_form.close()

        def see_all_feedback():
            all_feedback_form = QtWidgets.QWidget()
            ui = Ui_all_feedback_form()
            ui.setupUi(all_feedback_form)
            all_feedback_form.setFixedSize(1140, 850)
            all_feedback_form.show()
            reviems_form.close()

            def return_to_reviews_form():
                all_feedback_form.close()
                reviems_form.show()
            ui.back_btn.clicked.connect(return_to_reviews_form)

        def add_feedback_form():
            add_feedback = QtWidgets.QWidget()
            ui = Ui_add_feedback()
            ui.setupUi(add_feedback)
            add_feedback.setFixedSize(1140, 850)
            add_feedback.show()
            reviems_form.close()

            def save():
                if len(ui.lineEdit.text().split()) != 2 or not ''.join(ui.lineEdit.text().split()).isalpha():
                    ui.lineEdit.setText('Введите имя и фамилию через один пробел')
                elif ui.lineEdit_2.text() not in ['1', '2', '3', '4', '5']:
                    ui.lineEdit_2.setText('Введите число от 1 до 5')
                elif ui.lineEdit_3.text() == '':
                    ui.lineEdit_3.setText('Введите комментарий')
                else:
                    con = sqlite3.connect(r'./rev.db')
                    cur = con.cursor()
                    cur.execute('''INSERT INTO rev(Name, revi, comment)
                     VALUES(?, ?, ?)''', (' '.join(list(map(lambda s: s.capitalize(), ui.lineEdit.text().split()))),
                                          ui.lineEdit_2.text() + '/5', ui.lineEdit_3.text()))
                    con.commit()
                    con.close()
                    ui.lineEdit.setText('')
                    ui.lineEdit_2.setText('')
                    ui.lineEdit_3.setText('')

            ui.add_feedback_btn.clicked.connect(save)

            def return_to_reviews_form():
                add_feedback.close()
                reviems_form.show()
            ui.back_btn.clicked.connect(return_to_reviews_form)

        def return_to_main_form():
            reviems_form.close()
            main_form.show()
        ui.add_rev.clicked.connect(add_feedback_form)
        ui.see_all_rev.clicked.connect(see_all_feedback)
        ui.back_btn.clicked.connect(return_to_main_form)

    def open_contacts_form():
        Contacts_form = QtWidgets.QWidget()
        ui = Ui_Contacts_form()
        ui.setupUi(Contacts_form)
        Contacts_form.setFixedSize(1140, 850)
        Contacts_form.show()
        main_form.close()

        def return_to_main_form():
            Contacts_form.close()
            main_form.show()
        ui.back_btn.clicked.connect(return_to_main_form)

    def open_about_form():
        about_form = QtWidgets.QWidget()
        ui = Ui_about_form()
        ui.setupUi(about_form)
        about_form.setFixedSize(1140, 850)
        about_form.show()
        main_form.close()

        def return_to_main_form():
            about_form.close()
            main_form.show()
        ui.back_btn.clicked.connect(return_to_main_form)

    def open_chose_film1():
        film1_tod_form = QtWidgets.QWidget()
        ui = Ui_film1_tod_form()
        ui.setupUi(film1_tod_form)
        film1_tod_form.setFixedSize(1140, 850)
        film1_tod_form.show()
        ui.label.setPixmap(QtGui.QPixmap(films_today()[0][1]))
        ui.label_2.setPixmap(QtGui.QPixmap(films_today()[2][1]))
        ui.discount2.setText(films_today()[0][0])
        ui.discount2_2.setText(films_today()[2][0])
        ui.time11.setText(films_today()[0][2])
        ui.time12.setText(films_today()[1][2])
        ui.time21.setText(films_today()[2][2])
        ui.time22.setText(films_today()[3][2])
        film2_tod_form = QtWidgets.QWidget()
        main_form.close()

        def open_change():
            Change2_form = QtWidgets.QWidget()
            ui5 = Ui_Change2_form()
            ui5.setupUi(Change2_form)
            ui5.comboBox.addItems(['1', '2'])
            Change2_form.setFixedSize(1140, 850)
            Change2_form.show()
            ui5.way.setText('./pictures/')
            film1_tod_form.close()

            def save2():
                if ui5.title.text() == '':
                    ui5.title.setText('Введите название')
                elif ui5.way.text() == '':
                    ui5.title.setText('Введите путь на изображение')
                elif ui5.first.text() == '':
                    ui5.first.setText('Введите время')
                else:
                    if ui5.second.text() == '':
                        ui5.second.setText('_')
                    if ui5.list_of_places.text() == '':
                        ui5.list_of_places.setText('_')
                    con = sqlite3.connect(r'./rev.db')
                    cur = con.cursor()
                    cur.execute(f'''Update today_films
                    Set title = "{ui5.title.text()}", way = "{ui5.way.text()}",
                     time = "{ui5.first.text()}", list_of_places = "{ui5.list_of_places.text()}"
                    where id = {ui5.comboBox.currentText()}''')
                    con.commit()
                    cur.execute(f'''Update today_films
                        Set title = "{ui5.title.text()}", way = "{ui5.way.text()}",
                        time = "{ui5.second.text()}",
                        list_of_places = "{ui5.list_of_places.text()}"
                        where id = {int(ui5.comboBox.currentText()) + 1}''')
                    con.commit()
                    con.close()
                    Change2_form.close()
                    film1_tod_form.show()
                    ui.label.setPixmap(QtGui.QPixmap(films_today()[0][1]))
                    ui.label_2.setPixmap(QtGui.QPixmap(films_today()[2][1]))
                    ui.discount2.setText(films_today()[0][0])
                    ui.discount2_2.setText(films_today()[2][0])
                    ui.time11.setText(films_today()[0][2])
                    ui.time12.setText(films_today()[1][2])
                    ui.time21.setText(films_today()[2][2])
                    ui.time22.setText(films_today()[3][2])
            ui5.back_btn_2.clicked.connect(save2)

            def return_to_film1():
                Change2_form.close()
                film1_tod_form.show()
            ui5.back_btn.clicked.connect(return_to_film1)

        def open_mars_f(hall, name, time):
            marc_first = QtWidgets.QWidget()
            ui = Ui_marc_first()
            ui.setupUi(marc_first)
            marc_first.setFixedSize(1140, 850)
            marc_first.show()
            film1_tod_form.close()
            film2_tod_form.close()
            ui.discount2.setText(f'{films_today()[name][0]}\n{films_today()[name][time]}')
            check = films_today()[hall][3]

            def blocked_places():
                if ui.r1c2.objectName() in check:
                    ui.r1c2.setEnabled(False)
                    ui.r1c2.setStyleSheet("background-color: rgb(184, 184, 184); border-radius: 20;")
                if ui.r1c3.objectName() in check:
                    ui.r1c3.setEnabled(False)
                    ui.r1c3.setStyleSheet("background-color: rgb(184, 184, 184); border-radius: 20;")
                if ui.r1c4.objectName() in check:
                    ui.r1c4.setEnabled(False)
                    ui.r1c4.setStyleSheet("background-color: rgb(184, 184, 184); border-radius: 20;")
                if ui.r1c5.objectName() in check:
                    ui.r1c5.setEnabled(False)
                    ui.r1c5.setStyleSheet("background-color: rgb(184, 184, 184); border-radius: 20;")
                if ui.r1c6.objectName() in check:
                    ui.r1c6.setEnabled(False)
                    ui.r1c6.setStyleSheet("background-color: rgb(184, 184, 184); border-radius: 20;")
                if ui.r2c1.objectName() in check:
                    ui.r2c1.setEnabled(False)
                    ui.r2c1.setStyleSheet("background-color: rgb(184, 184, 184); border-radius: 20;")
                if ui.r2c2.objectName() in check:
                    ui.r2c2.setEnabled(False)
                    ui.r2c2.setStyleSheet("background-color: rgb(184, 184, 184); border-radius: 20;")
                if ui.r2c3.objectName() in check:
                    ui.r2c3.setEnabled(False)
                    ui.r2c3.setStyleSheet("background-color: rgb(184, 184, 184); border-radius: 20;")
                if ui.r2c4.objectName() in check:
                    ui.r2c4.setEnabled(False)
                    ui.r2c4.setStyleSheet("background-color: rgb(184, 184, 184); border-radius: 20;")
                if ui.r2c5.objectName() in check:
                    ui.r2c5.setEnabled(False)
                    ui.r2c5.setStyleSheet("background-color: rgb(184, 184, 184); border-radius: 20;")
                if ui.r2c6.objectName() in check:
                    ui.r2c6.setEnabled(False)
                    ui.r2c6.setStyleSheet("background-color: rgb(184, 184, 184); border-radius: 20;")
                if ui.r2c7.objectName() in check:
                    ui.r2c7.setEnabled(False)
                    ui.r2c7.setStyleSheet("background-color: rgb(184, 184, 184); border-radius: 20;")
                if ui.r3c1.objectName() in check:
                    ui.r3c1.setEnabled(False)
                    ui.r3c1.setStyleSheet("background-color: rgb(184, 184, 184); border-radius: 20;")
                if ui.r3c2.objectName() in check:
                    ui.r3c2.setEnabled(False)
                    ui.r3c2.setStyleSheet("background-color: rgb(184, 184, 184); border-radius: 20;")
                if ui.r3c3.objectName() in check:
                    ui.r3c3.setEnabled(False)
                    ui.r3c3.setStyleSheet("background-color: rgb(184, 184, 184); border-radius: 20;")
                if ui.r3c4.objectName() in check:
                    ui.r3c4.setEnabled(False)
                    ui.r3c4.setStyleSheet("background-color: rgb(184, 184, 184); border-radius: 20;")
                if ui.r3c5.objectName() in check:
                    ui.r3c5.setEnabled(False)
                    ui.r3c5.setStyleSheet("background-color: rgb(184, 184, 184); border-radius: 20;")
                if ui.r3c6.objectName() in check:
                    ui.r3c6.setEnabled(False)
                    ui.r3c6.setStyleSheet("background-color: rgb(184, 184, 184); border-radius: 20;")
                if ui.r3c7.objectName() in check:
                    ui.r3c7.setEnabled(False)
                    ui.r3c7.setStyleSheet("background-color: rgb(184, 184, 184); border-radius: 20;")
                if ui.r4c1.objectName() in check:
                    ui.r4c1.setEnabled(False)
                    ui.r4c1.setStyleSheet("background-color: rgb(184, 184, 184); border-radius: 20;")
                if ui.r4c2.objectName() in check:
                    ui.r4c2.setEnabled(False)
                    ui.r4c2.setStyleSheet("background-color: rgb(184, 184, 184); border-radius: 20;")
                if ui.r4c3.objectName() in check:
                    ui.r4c3.setEnabled(False)
                    ui.r4c3.setStyleSheet("background-color: rgb(184, 184, 184); border-radius: 20;")
                if ui.r4c4.objectName() in check:
                    ui.r4c4.setEnabled(False)
                    ui.r4c4.setStyleSheet("background-color: rgb(184, 184, 184); border-radius: 20;")
                if ui.r4c5.objectName() in check:
                    ui.r4c5.setEnabled(False)
                    ui.r4c5.setStyleSheet("background-color: rgb(184, 184, 184); border-radius: 20;")
                if ui.r4c6.objectName() in check:
                    ui.r4c6.setEnabled(False)
                    ui.r4c6.setStyleSheet("background-color: rgb(184, 184, 184); border-radius: 20;")
                if ui.r4c7.objectName() in check:
                    ui.r4c7.setEnabled(False)
                    ui.r4c7.setStyleSheet("background-color: rgb(184, 184, 184); border-radius: 20;")
                if ui.r5c1.objectName() in check:
                    ui.r5c1.setEnabled(False)
                    ui.r5c1.setStyleSheet("background-color: rgb(184, 184, 184); border-radius: 20;")
                if ui.r5c2.objectName() in check:
                    ui.r5c2.setEnabled(False)
                    ui.r5c2.setStyleSheet("background-color: rgb(184, 184, 184); border-radius: 20;")
                if ui.r5c3.objectName() in check:
                    ui.r5c3.setEnabled(False)
                    ui.r5c3.setStyleSheet("background-color: rgb(184, 184, 184); border-radius: 20;")
                if ui.r5c4.objectName() in check:
                    ui.r5c4.setEnabled(False)
                    ui.r5c4.setStyleSheet("background-color: rgb(184, 184, 184); border-radius: 20;")
                if ui.r5c5.objectName() in check:
                    ui.r5c5.setEnabled(False)
                    ui.r5c5.setStyleSheet("background-color: rgb(184, 184, 184); border-radius: 20;")
                if ui.r5c6.objectName() in check:
                    ui.r5c6.setEnabled(False)
                    ui.r5c6.setStyleSheet("background-color: rgb(184, 184, 184); border-radius: 20;")
                if ui.r5c7.objectName() in check:
                    ui.r5c7.setEnabled(False)
                    ui.r5c7.setStyleSheet("background-color: rgb(184, 184, 184); border-radius: 20;")
                if ui.r6c1.objectName() in check:
                    ui.r6c1.setEnabled(False)
                    ui.r6c1.setStyleSheet("background-color: rgb(184, 184, 184); border-radius: 20;")
                if ui.r6c2.objectName() in check:
                    ui.r6c2.setEnabled(False)
                    ui.r6c2.setStyleSheet("background-color: rgb(184, 184, 184); border-radius: 20;")
                if ui.r6c3.objectName() in check:
                    ui.r6c3.setEnabled(False)
                    ui.r6c3.setStyleSheet("background-color: rgb(184, 184, 184); border-radius: 20;")
                if ui.r6c4.objectName() in check:
                    ui.r6c4.setEnabled(False)
                    ui.r6c4.setStyleSheet("background-color: rgb(184, 184, 184); border-radius: 20;")
                if ui.r6c5.objectName() in check:
                    ui.r6c5.setEnabled(False)
                    ui.r6c5.setStyleSheet("background-color: rgb(184, 184, 184); border-radius: 20;")
                if ui.r6c6.objectName() in check:
                    ui.r6c6.setEnabled(False)
                    ui.r6c6.setStyleSheet("background-color: rgb(184, 184, 184); border-radius: 20;")
                if ui.r6c7.objectName() in check:
                    ui.r6c7.setEnabled(False)
                    ui.r6c7.setStyleSheet("background-color: rgb(184, 184, 184); border-radius: 20;")

            def open_pay_form(name):
                pay_form = QtWidgets.QWidget()
                ui2 = Ui_pay_form()
                ui2.setupUi(pay_form)
                pay_form.setFixedSize(1140, 850)
                pay_form.show()
                marc_first.close()
                if name == 'r1c2':
                    ui2.row_2.setText('1')
                    ui2.col.setText('2')
                elif name == 'r1c3':
                    ui2.row_2.setText('1')
                    ui2.col.setText('3')
                elif name == 'r1c4':
                    ui2.row_2.setText('1')
                    ui2.col.setText('4')
                elif name == 'r1c5':
                    ui2.row_2.setText('1')
                    ui2.col.setText('5')
                elif name == 'r1c6':
                    ui2.row_2.setText('1')
                    ui2.col.setText('6')
                elif name == 'r2c1':
                    ui2.row_2.setText('2')
                    ui2.col.setText('1')
                elif name == 'r2c2':
                    ui2.row_2.setText('2')
                    ui2.col.setText('2')
                elif name == 'r2c3':
                    ui2.row_2.setText('2')
                    ui2.col.setText('3')
                elif name == 'r2c4':
                    ui2.row_2.setText('2')
                    ui2.col.setText('4')
                elif name == 'r2c5':
                    ui2.row_2.setText('2')
                    ui2.col.setText('5')
                elif name == 'r2c6':
                    ui2.row_2.setText('2')
                    ui2.col.setText('6')
                elif name == 'r2c7':
                    ui2.row_2.setText('2')
                    ui2.col.setText('7')
                elif name == 'r3c1':
                    ui2.row_2.setText('3')
                    ui2.col.setText('1')
                elif name == 'r3c2':
                    ui2.row_2.setText('3')
                    ui2.col.setText('2')
                elif name == 'r3c3':
                    ui2.row_2.setText('3')
                    ui2.col.setText('3')
                elif name == 'r3c4':
                    ui2.row_2.setText('3')
                    ui2.col.setText('4')
                elif name == 'r3c5':
                    ui2.row_2.setText('3')
                    ui2.col.setText('5')
                elif name == 'r3c6':
                    ui2.row_2.setText('3')
                    ui2.col.setText('6')
                elif name == 'r3c7':
                    ui2.row_2.setText('3')
                    ui2.col.setText('7')
                elif name == 'r4c1':
                    ui2.row_2.setText('4')
                    ui2.col.setText('1')
                elif name == 'r4c2':
                    ui2.row_2.setText('4')
                    ui2.col.setText('2')
                elif name == 'r4c3':
                    ui2.row_2.setText('4')
                    ui2.col.setText('3')
                elif name == 'r4c4':
                    ui2.row_2.setText('4')
                    ui2.col.setText('4')
                elif name == 'r4c5':
                    ui2.row_2.setText('4')
                    ui2.col.setText('5')
                elif name == 'r4c6':
                    ui2.row_2.setText('4')
                    ui2.col.setText('6')
                elif name == 'r4c7':
                    ui2.row_2.setText('4')
                    ui2.col.setText('7')
                elif name == 'r5c1':
                    ui2.row_2.setText('5')
                    ui2.col.setText('1')
                elif name == 'r5c2':
                    ui2.row_2.setText('5')
                    ui2.col.setText('2')
                elif name == 'r5c3':
                    ui2.row_2.setText('5')
                    ui2.col.setText('3')
                elif name == 'r5c4':
                    ui2.row_2.setText('5')
                    ui2.col.setText('4')
                elif name == 'r5c5':
                    ui2.row_2.setText('5')
                    ui2.col.setText('5')
                elif name == 'r5c6':
                    ui2.row_2.setText('5')
                    ui2.col.setText('6')
                elif name == 'r5c7':
                    ui2.row_2.setText('5')
                    ui2.col.setText('7')
                elif name == 'r6c1':
                    ui2.row_2.setText('6')
                    ui2.col.setText('1')
                elif name == 'r6c2':
                    ui2.row_2.setText('6')
                    ui2.col.setText('2')
                elif name == 'r6c3':
                    ui2.row_2.setText('6')
                    ui2.col.setText('3')
                elif name == 'r6c4':
                    ui2.row_2.setText('6')
                    ui2.col.setText('4')
                elif name == 'r6c5':
                    ui2.row_2.setText('6')
                    ui2.col.setText('5')
                elif name == 'r6c6':
                    ui2.row_2.setText('6')
                    ui2.col.setText('6')
                elif name == 'r6c7':
                    ui2.row_2.setText('6')
                    ui2.col.setText('7')
                elif name == 'r7c1':
                    ui2.row_2.setText('7')
                    ui2.col.setText('1')
                elif name == 'r7c2':
                    ui2.row_2.setText('7')
                    ui2.col.setText('2')
                elif name == 'r7c3':
                    ui2.row_2.setText('7')
                    ui2.col.setText('3')
                elif name == 'r7c4':
                    ui2.row_2.setText('7')
                    ui2.col.setText('4')
                elif name == 'r7c5':
                    ui2.row_2.setText('7')
                    ui2.col.setText('5')
                elif name == 'r7c6':
                    ui2.row_2.setText('7')
                    ui2.col.setText('6')
                elif name == 'r7c7':
                    ui2.row_2.setText('7')
                    ui2.col.setText('7')

                def close_pay_form():
                    pay_form.close()
                    marc_first.show()
                    blocked_places()

                def pay():
                    if len(ui2.cart_n.text()) == 16 and ui2.cart_n.text().isdigit():
                        if len(ui2.name_surname.text().split()) == 2 and ui2.name_surname.text().\
                                replace(' ', '').isalpha():
                            if len(ui2.work_before.text()) == 5 and\
                                     len(ui2.work_before.text().split('/')) == 2 and\
                                    ui2.work_before.text().replace('/', '').isdigit():
                                if ui2.cvs.text().isdigit() and len(ui2.cvs.text()) == 3:
                                    films_today(f'r{ui2.row_2.text()}c{ui2.col.text()}', hall + 1)
                                    pay_form.close()
                                    film1_tod_form.show()
                                else:
                                    ui2.cvs.setText('Введите CVC код')
                            else:
                                ui2.work_before.setText('Введите срок службы карты **/**')
                        else:
                            ui2.name_surname.setText('Введите имя и фамилию')
                    else:
                        ui2.cart_n.setText('Введите номер карты 16 цифр (мир)')
                ui2.pay.clicked.connect(pay)
                ui2.back_btn.clicked.connect(close_pay_form)
            blocked_places()
            ui.r1c2.clicked.connect(lambda x: open_pay_form('r1c2'))
            ui.r1c3.clicked.connect(lambda x: open_pay_form('r1c3'))
            ui.r1c4.clicked.connect(lambda x: open_pay_form('r1c4'))
            ui.r1c5.clicked.connect(lambda x: open_pay_form('r1c5'))
            ui.r1c6.clicked.connect(lambda x: open_pay_form('r1c6'))
            ui.r2c1.clicked.connect(lambda x: open_pay_form('r2c1'))
            ui.r2c2.clicked.connect(lambda x: open_pay_form('r2c2'))
            ui.r2c3.clicked.connect(lambda x: open_pay_form('r2c3'))
            ui.r2c4.clicked.connect(lambda x: open_pay_form('r2c4'))
            ui.r2c5.clicked.connect(lambda x: open_pay_form('r2c5'))
            ui.r2c6.clicked.connect(lambda x: open_pay_form('r2c6'))
            ui.r2c7.clicked.connect(lambda x: open_pay_form('r2c7'))
            ui.r3c1.clicked.connect(lambda x: open_pay_form('r3c1'))
            ui.r3c2.clicked.connect(lambda x: open_pay_form('r3c2'))
            ui.r3c3.clicked.connect(lambda x: open_pay_form('r3c3'))
            ui.r3c4.clicked.connect(lambda x: open_pay_form('r3c4'))
            ui.r3c5.clicked.connect(lambda x: open_pay_form('r3c5'))
            ui.r3c6.clicked.connect(lambda x: open_pay_form('r3c6'))
            ui.r3c7.clicked.connect(lambda x: open_pay_form('r3c7'))
            ui.r4c1.clicked.connect(lambda x: open_pay_form('r4c1'))
            ui.r4c2.clicked.connect(lambda x: open_pay_form('r4c2'))
            ui.r4c3.clicked.connect(lambda x: open_pay_form('r4c3'))
            ui.r4c4.clicked.connect(lambda x: open_pay_form('r4c4'))
            ui.r4c5.clicked.connect(lambda x: open_pay_form('r4c5'))
            ui.r4c6.clicked.connect(lambda x: open_pay_form('r4c6'))
            ui.r4c7.clicked.connect(lambda x: open_pay_form('r4c7'))
            ui.r5c1.clicked.connect(lambda x: open_pay_form('r5c1'))
            ui.r5c2.clicked.connect(lambda x: open_pay_form('r5c2'))
            ui.r5c3.clicked.connect(lambda x: open_pay_form('r5c3'))
            ui.r5c4.clicked.connect(lambda x: open_pay_form('r5c4'))
            ui.r5c5.clicked.connect(lambda x: open_pay_form('r5c5'))
            ui.r5c6.clicked.connect(lambda x: open_pay_form('r5c6'))
            ui.r5c7.clicked.connect(lambda x: open_pay_form('r5c7'))
            ui.r6c1.clicked.connect(lambda x: open_pay_form('r6c1'))
            ui.r6c2.clicked.connect(lambda x: open_pay_form('r6c2'))
            ui.r6c3.clicked.connect(lambda x: open_pay_form('r6c3'))
            ui.r6c4.clicked.connect(lambda x: open_pay_form('r6c4'))
            ui.r6c5.clicked.connect(lambda x: open_pay_form('r6c5'))
            ui.r6c6.clicked.connect(lambda x: open_pay_form('r6c6'))
            ui.r6c7.clicked.connect(lambda x: open_pay_form('r6c7'))

            def return_to_film1():
                marc_first.close()
                film1_tod_form.show()
            ui.back_btn.clicked.connect(return_to_film1)

        def return_to_main():
            film1_tod_form.close()
            main_form.show()
        ui.change_film.clicked.connect(open_change)
        ui.time11.clicked.connect(lambda x: open_mars_f(0, 0, 2))
        ui.time12.clicked.connect(lambda x: open_mars_f(1, 1, 2))
        ui.time21.clicked.connect(lambda x: open_mars_f(2, 2, 2))
        ui.time22.clicked.connect(lambda x: open_mars_f(3, 3, 2))
        ui.back_btn.clicked.connect(return_to_main)

    def open_film_chose():
        main_form.close()
        open_chose_film1()

    def open_change_form():
        Change_form = QtWidgets.QWidget()
        ui = Ui_Change_form()
        ui.setupUi(Change_form)
        Change_form.setFixedSize(1140, 850)
        Change_form.show()
        ui.way.setText('./pictures/')

        main_form.close()
        ui.comboBox.addItems(['1', '2', '3'])

        def return_to_main():
            Change_form.close()
            main_form.show()

        def save():
            if ui.title.text() == '':
                ui.title.setText('Введите название')
            elif ui.way.text() == '':
                ui.title.setText('Введите путь на изображение')
            elif ui.first.text() == '':
                ui.first.setText('Введите время')
            else:
                if ui.second.text() == '':
                    ui.second.setText('_')
                if ui.list_of_places.text() == '':
                    ui.list_of_places.setText('_')
                con = sqlite3.connect(r'./rev.db')
                cur = con.cursor()
                cur.execute(f'''Update actual_films
                Set title = "{ui.title.text()}", way = "{ui.way.text()}",
                 time1 = "{ui.first.text()}", time2 = "{ui.second.text()}",
                list_of_places = "{ui.list_of_places.text()}"
                where id = {ui.comboBox.currentText()}''')
                con.commit()
                con.close()
                Change_form.close()
                ui3.label_2.setPixmap(QtGui.QPixmap(start()[1][1]))
                ui3.label.setPixmap(QtGui.QPixmap(start()[0][1]))
                ui3.pictureAdam.setPixmap(QtGui.QPixmap(start()[2][1]))
                ui3.adam.setText(start()[2][0])
                ui3.heard.setText(start()[1][0])
                ui3.avatar.setText(start()[0][0])
                main_form.show()
        ui.back_btn_2.clicked.connect(save)
        ui.back_btn.clicked.connect(return_to_main)
    ui3.avatar.clicked.connect(open_film_chose)
    ui3.heard.clicked.connect(open_film_chose)
    ui3.adam.clicked.connect(open_film_chose)
    ui3.contacts.clicked.connect(open_contacts_form)
    ui3.change_actual.clicked.connect(open_change_form)
    ui3.chose_sians.clicked.connect(open_chose_film1)
    ui3.about_complex.clicked.connect(open_about_form)
    ui3.actious.clicked.connect(open_discount_form)
    ui3.make_reviews.clicked.connect(open_feedback_form)


ui.start.clicked.connect(open_main_window)
sys.exit(app.exec_())
