import Ui_main
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMessageBox, QFileDialog
import sys
import os
import shutil
import pandas as pd

class MainUiClass (QtWidgets.QMainWindow, Ui_main.Ui_maxCopia):
    def __init__(self, parent=None):
        super (MainUiClass, self).__init__(parent)
        self.setupUi(self)

class Aplicacion (object):
    def __init__(self, ui):
        self.ui = ui
    
    def btn_leerCarpeta(self):
        self.ui.lbl_lectura.setText('Z:\TramitesWEB\Banco de la Gente\linea 2')
        contenido = os.listdir(r'Z:\TramitesWEB\Banco de la Gente\linea 2')
        self.df_contenido = pd.DataFrame(contenido)
        self.df_contenido['carpeta'] = self.df_contenido[0]
        self.df_contenido[0]= self.df_contenido[0].str.split(" ", n = 1, expand = True)
        print (self.df_contenido)
        self.df_contenido.columns = ['Sticker', 'Carpeta']
        self.df_contenido.to_excel('separado.xlsx')

    def btn_indicaDestino(self):
        fileName = QtWidgets.QFileDialog.getExistingDirectory()
        if fileName != "":
            self.ui.lbl_destino.setText(fileName)
    
    def btn_guardaXlsx(self):
        pass        

    def btn_obtenerLista(self):
        self.ui.lbl_excel.setText("")
        filename = QtWidgets.QFileDialog.getOpenFileName(filter = "Excel (*.xlsx)")
        if filename[0]:
            self.ui.lbl_excel.setText(filename[0])
            self.df_stickers = pd.read_excel(filename[0], usecols=['Sticker'], converters={'Sticker':str})
            self.df_merge = self.df_contenido.merge(self.df_stickers)
            #self.df_merge.to_excel('merge.xlsx')

    def btn_iniciaCopia(self):
        # COPIAR CARPTAS
        directorio_origen = r'Z:\TramitesWEB\Banco de la Gente\linea 2\\'
        directorio_destino = r'E:\linea 2\\'
        for index, row in self.df_merge.iterrows():
            shutil.copytree(directorio_origen + row['Carpeta'], directorio_destino + row['Carpeta'])
            self.ui.lbl_mensaje.setText(str(index) + "-" + row['Carpeta']) 
            print(str(index) + "-" + row['Carpeta'])


def main():
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
        ui = MainUiClass()
        apli = Aplicacion(ui)
        ui.show()

        ui.btn_leerCarpeta.clicked.connect(apli.btn_leerCarpeta)
        ui.btn_obtenerLista.clicked.connect(apli.btn_obtenerLista)
        ui.btn_iniciaCopia.clicked.connect(apli.btn_iniciaCopia)
        ui.btn_indicaDestino.clicked.connect(apli.btn_indicaDestino)

        app.exec_()

if __name__ == "__main__":
    main()
