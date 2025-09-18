import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5 import QtGui

class FenPrincipale(QMainWindow):
    def __init__(self):
        super(FenPrincipale, self).__init__()
        self.setWindowIcon(QtGui.QIcon('logo.ico'))
        self.navigateur = QWebEngineView()
        self.navigateur.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.navigateur)
        self.showMaximized()


        #navbar :
        navbar = QToolBar()
        self.addToolBar(navbar)
       
        retour_btn = QAction('<--retour<--', self)
        retour_btn.triggered.connect(self.navigateur.back)
        navbar.addAction(retour_btn)

        
        rafraichire_btn = QAction('rafraîchire', self)
        rafraichire_btn.triggered.connect(self.navigateur.reload)
        navbar.addAction(rafraichire_btn)

        avancer_btn = QAction('-->avancer-->', self)
        avancer_btn.triggered.connect(self.navigateur.forward)
        navbar.addAction(avancer_btn)

        acceuil_btn = QAction('<acceuil>', self)
        acceuil_btn.triggered.connect(self.url_acceuil)
        navbar.addAction(acceuil_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigation)
        navbar.addWidget(self.url_bar)

        self.navigateur.urlChanged.connect(self.udate_url)

    def url_acceuil(self):
        self.navigateur.setUrl(QUrl('http://google.com'))

    def navigation(self):
        url = self.url_bar.text()
        self.navigateur.setUrl(QUrl(url))

    def udate_url(self, url):
        self.url_bar.setText(url.toString())



app = QApplication(sys.argv)
QApplication.setApplicationName('jingembre')
fenetre = FenPrincipale()
app.exec()