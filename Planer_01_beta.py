# -*- coding: utf-8 -*-
__author__ = 'rafix'




# Form implementation generated from reading ui file 'interfejs_02.ui'
#
# Created: Thu Dec 10 13:36:09 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!



from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_Planer():
    global lista_slownikow
    lista_slownikow = []
    global kontrol2
    kontrol2 = []

    def setupUi(self, Planer):

        self.lista_1 = [] #QtCore.QStringList()

        Planer.setObjectName(_fromUtf8("Planer"))
        Planer.resize(770, 547)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 158, 158))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        Planer.setPalette(palette)

        self.lineEdit = QtGui.QLineEdit(Planer)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 113, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(Planer)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 90, 113, 27))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(Planer)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 150, 113, 27))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_4 = QtGui.QLineEdit(Planer)
        self.lineEdit_4.setGeometry(QtCore.QRect(10, 210, 113, 27))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))

        self.comboBox = QtGui.QComboBox(Planer)
        self.comboBox.setGeometry(QtCore.QRect(220, 30, 111, 27))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox_2 = QtGui.QComboBox(Planer)
        self.comboBox_2.setGeometry(QtCore.QRect(220, 90, 111, 27))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_3 = QtGui.QComboBox(Planer)
        self.comboBox_3.setGeometry(QtCore.QRect(220, 150, 111, 27))
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.comboBox_4 = QtGui.QComboBox(Planer)
        self.comboBox_4.setGeometry(QtCore.QRect(220, 210, 111, 27))
        self.comboBox_4.setObjectName(_fromUtf8("comboBox_4"))
        self.comboBox_5 = QtGui.QComboBox(Planer)
        self.comboBox_5.setGeometry(QtCore.QRect(220, 270, 111, 27))
        self.comboBox_5.setObjectName(_fromUtf8("comboBox_5"))

        self.arch1 = archiwum(self.comboBox,"godzina")
        self.arch2 = archiwum(self.comboBox_2,"klasa")
        self.arch3 = archiwum(self.comboBox_3,"sala")
        self.arch4 = archiwum(self.comboBox_4,"nauczyciel")

        self.dni_tygodnia = QtCore.QStringList([u'Poniedziałek','Wtorek',u'Środa','Czwartek',u'Piątek','Sobota','Niedziela'])

        self.comboBox_5.addItems(self.dni_tygodnia)

        cb1 = dodawanie(self.lineEdit,self.lista_1,self.comboBox)
        cb2 = dodawanie(self.lineEdit_2,self.lista_1,self.comboBox_2)
        cb3 = dodawanie(self.lineEdit_3,self.lista_1,self.comboBox_3)
        cb4 = dodawanie(self.lineEdit_4,self.lista_1,self.comboBox_4)

        self.toolButton = QtGui.QToolButton(Planer)
        self.toolButton.setGeometry(QtCore.QRect(160, 30, 31, 25))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.toolButton.clicked.connect(lambda: cb1.dodanie())

        self.toolButton_2 = QtGui.QToolButton(Planer)
        self.toolButton_2.setGeometry(QtCore.QRect(160, 90, 31, 25))
        self.toolButton_2.setObjectName(_fromUtf8("toolButton_2"))
        self.toolButton_2.clicked.connect(lambda: cb2.dodanie())

        self.toolButton_3 = QtGui.QToolButton(Planer)
        self.toolButton_3.setGeometry(QtCore.QRect(160, 150, 31, 25))
        self.toolButton_3.setObjectName(_fromUtf8("toolButton_3"))
        self.toolButton_3.clicked.connect(lambda: cb3.dodanie())

        self.toolButton_4 = QtGui.QToolButton(Planer)
        self.toolButton_4.setGeometry(QtCore.QRect(160, 210, 31, 25))
        self.toolButton_4.setObjectName(_fromUtf8("toolButton_4"))
        self.toolButton_4.clicked.connect(lambda: cb4.dodanie())

        self.listWidget = QtGui.QListWidget(Planer)
        self.listWidget.setGeometry(QtCore.QRect(460, 30, 71, 271))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.listWidget.itemClicked.connect(self.do_tabeli)

        self.listWidget2 = QtGui.QListWidget(Planer)
        self.listWidget2.setGeometry(QtCore.QRect(550, 30, 71, 271))
        self.listWidget2.setObjectName(_fromUtf8("listWidget2"))

        self.listWidget3 = QtGui.QListWidget(Planer)
        self.listWidget3.setGeometry(QtCore.QRect(640, 30, 71, 271))
        self.listWidget3.setObjectName(_fromUtf8("listWidget3"))


        self.tableWidget = QtGui.QTableWidget(Planer)
        self.tableWidget.setGeometry(QtCore.QRect(10, 321, 451, 211))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels (['Godzina','Klasa','Nauczyciel',u'Dzień tygodnia'])
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.setRowCount(0)




        self.label = QtGui.QLabel(Planer)
        self.label.setGeometry(QtCore.QRect(10, 10, 261, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Planer)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 121, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Planer)
        self.label_3.setGeometry(QtCore.QRect(10, 130, 161, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Planer)
        self.label_4.setGeometry(QtCore.QRect(220, 10, 121, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Planer)
        self.label_5.setGeometry(QtCore.QRect(220, 70, 101, 17))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(Planer)
        self.label_6.setGeometry(QtCore.QRect(220, 130, 91, 17))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(Planer)
        self.label_7.setGeometry(QtCore.QRect(220, 190, 141, 17))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(Planer)
        self.label_8.setGeometry(QtCore.QRect(10, 190, 161, 17))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(Planer)
        self.label_9.setGeometry(QtCore.QRect(220, 250, 161, 17))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(Planer)
        self.label_10.setGeometry(QtCore.QRect(10, 290, 221, 17))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(Planer)
        self.label_11.setGeometry(QtCore.QRect(460, 10, 31, 17))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_13 = QtGui.QLabel(Planer)
        self.label_13.setGeometry(QtCore.QRect(550, 10, 80, 17))
        self.label_13.setObjectName(_fromUtf8("label_13"))


        self.label_12 = QtGui.QLabel(Planer)
        self.label_12.setGeometry(QtCore.QRect(220, 290, 221, 17))

        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)

        self.label_12.setFont(font)
        self.label_12.setObjectName(_fromUtf8("label_12"))





        self.pushButton = QtGui.QPushButton(Planer)
        self.pushButton.setGeometry(QtCore.QRect(380, 130, 61, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.do_slownika)
        self.pushButton.clicked.connect(self.do_tabeli)

        self.pushButton_3 = QtGui.QPushButton(Planer)
        self.pushButton_3.setGeometry(QtCore.QRect(490, 321, 61, 27))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_3.clicked.connect(self.usun)

        self.pushButton_4 = QtGui.QPushButton(Planer)
        self.pushButton_4.setGeometry(QtCore.QRect(490, 350, 61, 27))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_4.clicked.connect(self.sgui)
        self.pushButton_5 = QtGui.QPushButton(Planer)
        self.pushButton_5.setGeometry(QtCore.QRect(490, 380, 61, 27))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_5.clicked.connect(self.rgui)




        self.retranslateUi(Planer)
        QtCore.QMetaObject.connectSlotsByName(Planer)

    def sgui(self):
        global save_directory
        save_directory = QtGui.QFileDialog.getSaveFileName(Planer,'Save file','C:/','Text files (*.txt)')

        for x in xrange(self.listWidget.count()):
            if str(self.listWidget.item(x).text()) not in kontrol2:
                kontrol2.append(str(self.listWidget.item(x).text()))

        self.arch1.savegui()
        self.arch2.savegui()
        self.arch3.savegui()
        self.arch4.savegui()
        print "Done"

    def rgui(self):
        global kontrol2
        kontrol2 = []
        global lista_slownikow
        lista_slownikow = []
        global open_directory
        open_directory = QtGui.QFileDialog.getOpenFileName(Planer,'Open file','C:/','Text files (*.txt)')
        settings = QtCore.QSettings(open_directory, QtCore.QSettings.IniFormat)

        self.arch1.restoregui()
        self.arch2.restoregui()
        self.arch3.restoregui()
        self.arch4.restoregui()

        try:

            for x in QtCore.QVariant.toStringList(settings.value('kontrol2')):
                ui.listWidget.addItem(x)
                kontrol2.append(str(x))
        except:
            pass
        try:
            for x in QtCore.QVariant.toPyObject(settings.value('lista_slownikow')):
                lista_slownikow.append(x)
        except:
            pass
        self.label_12.setText("")
        print lista_slownikow
        print "Done"

    def do_tabeli(self):
        self.tableWidget.setSortingEnabled(False)
        row = 0
        self.tableWidget.setHorizontalHeaderLabels (['Godzina','Klasa','Nauczyciel',u'Dzień tygodnia'])
        try:
            for x in lista_slownikow:

                if x['sala'] == self.listWidget.currentItem().text():

                    self.tableWidget.insertRow(row)
                    self.tableWidget.setItem(row, 0, QtGui.QTableWidgetItem(x['godzina']))
                    self.tableWidget.setItem(row, 1, QtGui.QTableWidgetItem(x['klasa']))
                    self.tableWidget.setItem(row, 2, QtGui.QTableWidgetItem(x['nauczyciel']))
                    self.tableWidget.setItem(row, 3, QtGui.QTableWidgetItem(x['dzien']))

                    row = row + 1
            print row
            self.tableWidget.setRowCount(row)
            self.label_12.setText(self.listWidget.currentItem().text())

            self.tableWidget.setSortingEnabled(True)
            self.tableWidget.sortByColumn(0, QtCore.Qt.AscendingOrder)
            self.tableWidget.sortByColumn(3, QtCore.Qt.AscendingOrder)
        except:
            pass
        #TODO improve sorting by day of week. Custom sorting mechanism by changing __lL__ method


    def retranslateUi(self, Planer):
        Planer.setWindowTitle(_translate("Planer", "Form", None))
        self.toolButton.setText(_translate("Planer", ">>", None))
        self.toolButton_2.setText(_translate("Planer", ">>", None))
        self.toolButton_3.setText(_translate("Planer", ">>", None))
        self.pushButton.setText(_translate("Planer", ">>>", None))
        self.label.setText(_translate("Planer", "Wprowadź godzinę rozpoczęcia lekcji:", None))
        self.label_2.setText(_translate("Planer", "Wprowadź klasę:", None))
        self.label_3.setText(_translate("Planer", "Wprowadź numer sali:", None))
        self.label_4.setText(_translate("Planer", "Wybierz godzinę", None))
        self.label_5.setText(_translate("Planer", "Wybierz klasę", None))
        self.label_6.setText(_translate("Planer", "Wybierz salę", None))
        self.label_7.setText(_translate("Planer", "Wybierz nauczyciela", None))
        self.label_8.setText(_translate("Planer", "Wprowadź nauczyciela", None))
        self.toolButton_4.setText(_translate("Planer", ">>", None))
        self.label_9.setText(_translate("Planer", "Wybierz dzień tygodnia", None))

        self.label_10.setText(_translate("Planer", "Tabela rezerwacji sali lekcyjnej", None))
        self.label_11.setText(_translate("Planer", "Sala", None))
        self.label_13.setText(_translate("Planer", "Nauczuciel", None))



        self.pushButton_3.setText(_translate("Planer", "Usuń", None))
        self.pushButton_4.setText(_translate("Planer", "Zapisz", None))
        self.pushButton_5.setText(_translate("Planer", "Otwórz", None))

    def do_slownika(self):

        self.kontrol = []
        self.slownik = {"godzina":self.comboBox.currentText(), "klasa":self.comboBox_2.currentText(), "sala":self.comboBox_3.currentText(), "nauczyciel":self.comboBox_4.currentText(), "dzien":self.comboBox_5.currentText()}

        for x in lista_slownikow:
            if x["godzina"] == self.slownik["godzina"] and x["sala"] == self.slownik["sala"] and x["dzien"] == self.slownik["dzien"]:
                self.kontrol.append("1")
            elif x["nauczyciel"] == self.slownik["nauczyciel"] and x["godzina"] == self.slownik["godzina"] and x["dzien"] == self.slownik["dzien"]:
                self.kontrol.append("2")
            elif x["klasa"] == self.slownik["klasa"] and x["godzina"] == self.slownik["godzina"] and x["dzien"] == self.slownik["dzien"]:
                self.kontrol.append("3")
        print self.kontrol


        for x in self.kontrol:

            if x == "1":
                print "duplikat"
                QtGui.QMessageBox.information(QtGui.QWidget(), u'UWAGA!!!', u"Sala w tym dniu w tej godzinie już zajęta !!!" , QtGui.QMessageBox.Ok)
            elif x == "2":
                print "duplikat"
                QtGui.QMessageBox.information(QtGui.QWidget(), u'UWAGA!!!', u"Nauczyciel w tym dniu w tej godzinie już zajęty !!!" , QtGui.QMessageBox.Ok)
            elif x == "3":
                print "duplikat"
                QtGui.QMessageBox.information(QtGui.QWidget(), u'UWAGA!!!', u"Klasa w tym dniu w tej godzinie już zajęta !!!" , QtGui.QMessageBox.Ok)

        if len(self.kontrol) == 0:

            lista_slownikow.append(self.slownik)
            print " nie ma duplikatu"


        self.kontrol = []
        sortlistW = []
        sortlistW2 = []

        if self.comboBox_3.currentText() not in kontrol2:
            for x in xrange(self.listWidget.count()):
                sortlistW.append(str(self.listWidget.item(x).text()))
            try:
                for x in sortlistW:
                    try:
                        sortlistW2.append(int(x))
                    except:
                        sortlistW2.append(str(x))
            finally:
                try:
                    sortlistW2.append(int(self.comboBox_3.currentText()))
                except:

                    sortlistW2.append(str(self.comboBox_3.currentText()))
                finally:
                    tostr = []
                    sortlistW2.sort()
                    for x in sortlistW2:
                        tostr.append(str(x))
                    self.listWidget.clear()
                    self.listWidget.addItems(tostr)
                    kontrol2.append(str(self.comboBox_3.currentText()))

        print kontrol2

        for x in lista_slownikow:
            print x

    def usun(self):

        row = self.tableWidget.currentRow()
        try:
            self.slownik_usun = {"godzina":self.tableWidget.item(row,0).text(),"klasa":self.tableWidget.item(row,1).text(),"sala":self.listWidget.currentItem().text(),"dzien":self.tableWidget.item(row,3).text(),"nauczyciel":self.tableWidget.item(row,2).text()}

            for x in lista_slownikow:
                if x == self.slownik_usun:
                    print "True"
                    lista_slownikow.remove(x)
                else:
                    print "False"

            self.tableWidget.removeRow(row)
        except:
            pass

        print lista_slownikow
        print "Done"
        #TODO create multiple removing of rows

class archiwum():

    def __init__(self,cB,typ):
        self.cB = cB
        self.typ = typ


    def savegui(self):

        settings = QtCore.QSettings(save_directory, QtCore.QSettings.IniFormat)
        lista = []

        for index in range(self.cB.count()):
            lista.append(self.cB.itemText(index))
        settings.setValue(self.typ, lista)
        global lista_slownikow
        lista_slownikow=tuple(lista_slownikow)
        settings.setValue('lista_slownikow',lista_slownikow)

        settings.setValue('kontrol2',kontrol2)
        lista_slownikow=list(lista_slownikow)


    def restoregui(self):
        self.cB.clear()
        ui.listWidget.clear()
        ui.tableWidget.clear()
        ui.tableWidget.setHorizontalHeaderLabels (['Godzina','Klasa','Nauczyciel',u'Dzień tygodnia'])
        ui.tableWidget.setRowCount(0)
        settings = QtCore.QSettings(open_directory, QtCore.QSettings.IniFormat)
        self.cB.insertItems(0,QtCore.QVariant.toStringList(settings.value(self.typ)))

class dodawanie():

    def __init__(self,lE,lista,cB):
        self.lE = lE
        self.lista = lista
        self.cB = cB

    def dodanie(self):
        cBsortlist = []
        cBsortlist2 = []
        if self.lE.text() not in self.lista:
            for index in range(self.cB.count()):
                    cBsortlist.append(str(self.cB.itemText(index)))

            try:
                for x in cBsortlist:
                    try:
                        cBsortlist2.append(int(x))
                    except:
                        cBsortlist2.append(str(x))
            finally:

                try:
                    cBsortlist2.append(int(self.lE.text()))
                except:
                    cBsortlist2.append(str(self.lE.text()))
                finally:
                    tostr = []
                    cBsortlist2.sort()
                    for x in cBsortlist2:
                        tostr.append(str(x))
                    self.cB.clear()
                    self.cB.addItems(tostr)
                    self.lista.append(self.lE.text())
            print cBsortlist2

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Planer = QtGui.QWidget()
    ui = Ui_Planer()
    ui.setupUi(Planer)

    Planer.show()
    sys.exit(app.exec_())

