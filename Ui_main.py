# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\DESARROLLO\ADMINISTRACION\maxCopia\main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_maxCopia(object):
    def setupUi(self, maxCopia):
        maxCopia.setObjectName("maxCopia")
        maxCopia.resize(472, 452)
        self.lbl_lectura = QtWidgets.QLabel(maxCopia)
        self.lbl_lectura.setGeometry(QtCore.QRect(30, 80, 411, 16))
        self.lbl_lectura.setObjectName("lbl_lectura")
        self.btn_leerCarpeta = QtWidgets.QPushButton(maxCopia)
        self.btn_leerCarpeta.setGeometry(QtCore.QRect(30, 40, 411, 41))
        self.btn_leerCarpeta.setObjectName("btn_leerCarpeta")
        self.btn_guardaXlsx = QtWidgets.QPushButton(maxCopia)
        self.btn_guardaXlsx.setGeometry(QtCore.QRect(30, 120, 141, 23))
        self.btn_guardaXlsx.setObjectName("btn_guardaXlsx")
        self.btn_obtenerLista = QtWidgets.QPushButton(maxCopia)
        self.btn_obtenerLista.setGeometry(QtCore.QRect(30, 180, 411, 41))
        self.btn_obtenerLista.setObjectName("btn_obtenerLista")
        self.lbl_destino = QtWidgets.QLabel(maxCopia)
        self.lbl_destino.setGeometry(QtCore.QRect(30, 300, 411, 16))
        self.lbl_destino.setObjectName("lbl_destino")
        self.btn_indicaDestino = QtWidgets.QPushButton(maxCopia)
        self.btn_indicaDestino.setGeometry(QtCore.QRect(30, 260, 411, 41))
        self.btn_indicaDestino.setObjectName("btn_indicaDestino")
        self.btn_iniciaCopia = QtWidgets.QPushButton(maxCopia)
        self.btn_iniciaCopia.setGeometry(QtCore.QRect(30, 350, 411, 41))
        self.btn_iniciaCopia.setObjectName("btn_iniciaCopia")
        self.lbl_mensaje = QtWidgets.QLabel(maxCopia)
        self.lbl_mensaje.setGeometry(QtCore.QRect(30, 400, 411, 16))
        self.lbl_mensaje.setObjectName("lbl_mensaje")
        self.lbl_excel = QtWidgets.QLabel(maxCopia)
        self.lbl_excel.setGeometry(QtCore.QRect(30, 220, 411, 16))
        self.lbl_excel.setObjectName("lbl_excel")

        self.retranslateUi(maxCopia)
        QtCore.QMetaObject.connectSlotsByName(maxCopia)

    def retranslateUi(self, maxCopia):
        _translate = QtCore.QCoreApplication.translate
        maxCopia.setWindowTitle(_translate("maxCopia", "maxCopia"))
        self.lbl_lectura.setText(_translate("maxCopia", "INDICAR CARPETA DE LECTURA"))
        self.btn_leerCarpeta.setText(_translate("maxCopia", "LEER CARPTEA DE SOLICTUDES SUAC"))
        self.btn_guardaXlsx.setText(_translate("maxCopia", "GUARDAR EXCEL"))
        self.btn_obtenerLista.setText(_translate("maxCopia", "LISTA EXCEL PARA COPIAR"))
        self.lbl_destino.setText(_translate("maxCopia", "INDICAR CARPETA DE DESTINO"))
        self.btn_indicaDestino.setText(_translate("maxCopia", "INDICAR DESTINO"))
        self.btn_iniciaCopia.setText(_translate("maxCopia", "INICIAR COPIA"))
        self.lbl_mensaje.setText(_translate("maxCopia", "mensaje"))
        self.lbl_excel.setText(_translate("maxCopia", "INDICAR CARPETA DE LECTURA"))
