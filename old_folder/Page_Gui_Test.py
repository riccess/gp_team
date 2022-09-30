# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Page_Gui_Test.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(828, 857)
        MainWindow.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(290, 170, 121, 30))
        self.label_2.setStyleSheet("\n"
"font: 10pt \"Consolas\";\n"
"font: 75 9pt \"나눔고딕 ExtraBold\";\n"
"color: white;\n"
"    background-color: rgb(58, 134, 255);\n"
"    border-radius: 15px;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(290, 220, 121, 30))
        self.label_4.setStyleSheet("\n"
"font: 10pt \"Consolas\";\n"
"font: 75 9pt \"나눔고딕 ExtraBold\";\n"
"color: white;\n"
"    background-color: rgb(58, 134, 255);\n"
"    border-radius: 15px;")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.Store_Name = QtWidgets.QLineEdit(self.centralwidget)
        self.Store_Name.setGeometry(QtCore.QRect(420, 170, 113, 31))
        self.Store_Name.setStyleSheet("border-radius: 15px;\n"
"background-color: rgb(233, 245, 255);")
        self.Store_Name.setObjectName("Store_Name")
        self.Star_Total = QtWidgets.QLineEdit(self.centralwidget)
        self.Star_Total.setGeometry(QtCore.QRect(420, 220, 113, 31))
        self.Star_Total.setStyleSheet("border-radius: 15px;\n"
"\n"
"font: 10pt \"Consolas\";\n"
"font: 75 9pt \"나눔고딕 ExtraBold\";\n"
"color: black;")
        self.Star_Total.setObjectName("Star_Total")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(20, 80, 251, 231))
        self.graphicsView.setStyleSheet("border-radius: 20px;\n"
"background-color: rgb(233, 245, 255);")
        self.graphicsView.setObjectName("graphicsView")
        self.Review_Count_total = QtWidgets.QLineEdit(self.centralwidget)
        self.Review_Count_total.setGeometry(QtCore.QRect(700, 170, 111, 31))
        self.Review_Count_total.setStyleSheet("border-radius: 15px;\n"
"background-color: rgb(233, 245, 255);")
        self.Review_Count_total.setObjectName("Review_Count_total")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(560, 170, 131, 30))
        self.label_5.setStyleSheet("\n"
"font: 10pt \"Consolas\";\n"
"font: 75 9pt \"나눔고딕 ExtraBold\";\n"
"color: white;\n"
"    background-color: rgb(58, 134, 255);\n"
"    border-radius: 15px;")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(560, 270, 131, 30))
        self.label_6.setStyleSheet("\n"
"font: 10pt \"Consolas\";\n"
"font: 75 9pt \"나눔고딕 ExtraBold\";\n"
"color: white;\n"
"    background-color: rgb(58, 134, 255);\n"
"    border-radius: 15px;")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.Negative_Review = QtWidgets.QLineEdit(self.centralwidget)
        self.Negative_Review.setGeometry(QtCore.QRect(700, 220, 111, 31))
        self.Negative_Review.setStyleSheet("border-radius: 15px;\n"
"\n"
"\n"
"font: 10pt \"Consolas\";\n"
"font: 75 9pt \"나눔고딕 ExtraBold\";\n"
"color: green;")
        self.Negative_Review.setText("")
        self.Negative_Review.setObjectName("Negative_Review")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(560, 220, 131, 30))
        self.label_7.setStyleSheet("\n"
"font: 10pt \"Consolas\";\n"
"font: 75 9pt \"나눔고딕 ExtraBold\";\n"
"color: white;\n"
"    background-color: rgb(58, 134, 255);\n"
"    border-radius: 15px;")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.Positive_Review = QtWidgets.QLineEdit(self.centralwidget)
        self.Positive_Review.setGeometry(QtCore.QRect(700, 270, 111, 31))
        self.Positive_Review.setStyleSheet("border-radius: 15px;\n"
"\n"
"font: 10pt \"Consolas\";\n"
"font: 75 9pt \"나눔고딕 ExtraBold\";\n"
"color: red;\n"
"")
        self.Positive_Review.setText("")
        self.Positive_Review.setObjectName("Positive_Review")
        self.Find_Store_Btn = QtWidgets.QPushButton(self.centralwidget)
        self.Find_Store_Btn.setGeometry(QtCore.QRect(720, 80, 91, 31))
        font = QtGui.QFont()
        font.setFamily("나눔고딕 ExtraBold")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Find_Store_Btn.setFont(font)
        self.Find_Store_Btn.setStyleSheet("\n"
"font: 10pt \"Consolas\";\n"
"font: 75 9pt \"나눔고딕 ExtraBold\";\n"
"color: white;\n"
"    background-color: rgb(58, 134, 255);\n"
"    border-radius: 15px;")
        self.Find_Store_Btn.setObjectName("Find_Store_Btn")
        self.Input_Store = QtWidgets.QLineEdit(self.centralwidget)
        self.Input_Store.setGeometry(QtCore.QRect(420, 82, 291, 31))
        self.Input_Store.setStyleSheet("border-radius: 15px;\n"
"background-color: rgb(233, 245, 255);\n"
"font: 10pt \"Consolas\";\n"
"font: 75 9pt \"나눔고딕 ExtraBold\";\n"
"color: black;")
        self.Input_Store.setText("")
        self.Input_Store.setObjectName("Input_Store")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(290, 80, 121, 31))
        self.label_8.setStyleSheet("\n"
"font: 10pt \"Consolas\";\n"
"font: 75 9pt \"나눔고딕 ExtraBold\";\n"
"color: white;\n"
"    background-color: rgb(58, 134, 255);\n"
"    border-radius: 15px;")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(340, 130, 421, 23))
        self.progressBar.setStyleSheet("font: 75 9pt \"나눔고딕 ExtraBold\";\n"
"border-radius : 10px;\n"
"background-color: rgb(89, 255, 0);")
        self.progressBar.setMinimum(100)
        self.progressBar.setProperty("value", 100)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName("progressBar")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 320, 51, 31))
        self.pushButton.setStyleSheet("\n"
"font: 10pt \"Consolas\";\n"
"font: 75 9pt \"나눔고딕 ExtraBold\";\n"
"color: white;\n"
"    background-color: rgb(58, 134, 255);\n"
"    border-radius: 10px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 320, 51, 31))
        self.pushButton_2.setStyleSheet("\n"
"font: 10pt \"Consolas\";\n"
"font: 75 9pt \"나눔고딕 ExtraBold\";\n"
"color: white;\n"
"    background-color: rgb(58, 134, 255);\n"
"    border-radius: 10px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 380, 831, 421))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("color: black;\n"
"\n"
"font: 75 9pt \"나눔고딕 ExtraBold\";\n"
"\n"
"")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_11 = QtWidgets.QLabel(self.tab)
        self.label_11.setGeometry(QtCore.QRect(290, 10, 231, 31))
        self.label_11.setStyleSheet("color: black;\n"
"\n"
"font: 75 9pt \"나눔고딕 ExtraBold\";\n"
"\n"
"border-radius: 15px;\n"
"background-color: rgb(253, 237, 255);")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.graphicsView_8 = QtWidgets.QGraphicsView(self.tab)
        self.graphicsView_8.setGeometry(QtCore.QRect(20, 50, 381, 331))
        self.graphicsView_8.setStyleSheet("border-radius: 20px;\n"
"background-color: rgb(233, 245, 255);")
        self.graphicsView_8.setObjectName("graphicsView_8")
        self.graphicsView_9 = QtWidgets.QGraphicsView(self.tab)
        self.graphicsView_9.setGeometry(QtCore.QRect(420, 50, 381, 331))
        self.graphicsView_9.setStyleSheet("border-radius: 20px;\n"
"background-color: rgb(233, 245, 255);")
        self.graphicsView_9.setObjectName("graphicsView_9")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.graphicsView_4 = QtWidgets.QGraphicsView(self.tab_2)
        self.graphicsView_4.setGeometry(QtCore.QRect(20, 50, 381, 331))
        self.graphicsView_4.setStyleSheet("border-radius: 20px;\n"
"background-color: rgb(233, 245, 255);")
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.label_12 = QtWidgets.QLabel(self.tab_2)
        self.label_12.setGeometry(QtCore.QRect(140, 10, 141, 31))
        self.label_12.setStyleSheet("color: black;\n"
"\n"
"font: 75 9pt \"나눔고딕 ExtraBold\";\n"
"\n"
"border-radius: 15px;\n"
"background-color: rgb(253, 237, 255);")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.graphicsView_5 = QtWidgets.QGraphicsView(self.tab_2)
        self.graphicsView_5.setGeometry(QtCore.QRect(420, 50, 381, 331))
        self.graphicsView_5.setStyleSheet("border-radius: 20px;\n"
"background-color: rgb(233, 245, 255);")
        self.graphicsView_5.setObjectName("graphicsView_5")
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setGeometry(QtCore.QRect(540, 10, 141, 31))
        self.label_13.setStyleSheet("color: black;\n"
"\n"
"font: 75 9pt \"나눔고딕 ExtraBold\";\n"
"\n"
"border-radius: 15px;\n"
"background-color: rgb(253, 237, 255);")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_16 = QtWidgets.QLabel(self.tab_3)
        self.label_16.setGeometry(QtCore.QRect(140, 10, 141, 31))
        self.label_16.setStyleSheet("color: black;\n"
"\n"
"font: 75 9pt \"나눔고딕 ExtraBold\";\n"
"\n"
"border-radius: 15px;\n"
"background-color: rgb(253, 237, 255);")
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.tab_3)
        self.label_17.setGeometry(QtCore.QRect(540, 10, 141, 31))
        self.label_17.setStyleSheet("color: black;\n"
"\n"
"font: 75 9pt \"나눔고딕 ExtraBold\";\n"
"\n"
"border-radius: 15px;\n"
"background-color: rgb(253, 237, 255);")
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.graphicsView_6 = QtWidgets.QGraphicsView(self.tab_3)
        self.graphicsView_6.setGeometry(QtCore.QRect(20, 50, 381, 331))
        self.graphicsView_6.setStyleSheet("border-radius: 20px;\n"
"background-color: rgb(233, 245, 255);")
        self.graphicsView_6.setObjectName("graphicsView_6")
        self.graphicsView_7 = QtWidgets.QGraphicsView(self.tab_3)
        self.graphicsView_7.setGeometry(QtCore.QRect(420, 50, 381, 331))
        self.graphicsView_7.setStyleSheet("border-radius: 20px;\n"
"background-color: rgb(233, 245, 255);")
        self.graphicsView_7.setObjectName("graphicsView_7")
        self.tabWidget.addTab(self.tab_3, "")
        self.Star_Total_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.Star_Total_2.setGeometry(QtCore.QRect(420, 270, 113, 31))
        self.Star_Total_2.setStyleSheet("border-radius: 15px;\n"
"font: 10pt \"Consolas\";\n"
"font: 75 9pt \"나눔고딕 ExtraBold\";\n"
"color: black;")
        self.Star_Total_2.setText("")
        self.Star_Total_2.setObjectName("Star_Total_2")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(290, 270, 121, 30))
        self.label_9.setStyleSheet("\n"
"font: 10pt \"Consolas\";\n"
"font: 75 9pt \"나눔고딕 ExtraBold\";\n"
"color: white;\n"
"    background-color: rgb(58, 134, 255);\n"
"    border-radius: 15px;")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(420, 10, 271, 41))
        self.label_15.setStyleSheet("font: 75 16pt \"나눔고딕 ExtraBold\";\n"
"color: rgb(0, 0, 0);\n"
"    background-color: white;\n"
"    border: 2px solid rgb(0, 0, 0);\n"
"    border-radius: 20px;\n"
"")
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(280, 210, 261, 101))
        self.frame.setStyleSheet("border-radius: 15px;\n"
"background-color: rgb(231, 250, 255);\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(550, 210, 271, 101))
        self.frame_2.setStyleSheet("background-color: rgb(240, 255, 238);\n"
"border-radius:15px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.raise_()
        self.frame.raise_()
        self.label_2.raise_()
        self.label_4.raise_()
        self.Store_Name.raise_()
        self.Star_Total.raise_()
        self.graphicsView.raise_()
        self.Review_Count_total.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.Negative_Review.raise_()
        self.label_7.raise_()
        self.Positive_Review.raise_()
        self.Find_Store_Btn.raise_()
        self.Input_Store.raise_()
        self.label_8.raise_()
        self.progressBar.raise_()
        self.pushButton_2.raise_()
        self.tabWidget.raise_()
        self.Star_Total_2.raise_()
        self.label_9.raise_()
        self.label_15.raise_()
        self.pushButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 828, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionshow = QtWidgets.QAction(MainWindow)
        self.actionshow.setObjectName("actionshow")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        self.Find_Store_Btn.clicked.connect(MainWindow.start) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TEAM GP"))
        self.label_2.setText(_translate("MainWindow", "STORE NAME"))
        self.label_4.setText(_translate("MainWindow", "사이트 별점"))
        self.label_5.setText(_translate("MainWindow", "Total Comment"))
        self.label_6.setText(_translate("MainWindow", "부정 댓글 수"))
        self.label_7.setText(_translate("MainWindow", "긍정 댓글 수"))
        self.Find_Store_Btn.setText(_translate("MainWindow", "search"))
        self.label_8.setText(_translate("MainWindow", "STORE"))
        self.pushButton.setText(_translate("MainWindow", "◀"))
        self.pushButton_2.setText(_translate("MainWindow", "▶"))
        self.label_11.setText(_translate("MainWindow", "사이트 평점 Vs. 학습한 평점 비교"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.label_12.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>color: black;</p><p><br/></p><p>font: 75 9pt &quot;나눔고딕 ExtraBold&quot;;</p><p><br/></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "긍정 WordCloud"))
        self.label_13.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>color: black;</p><p><br/></p><p>font: 75 9pt &quot;나눔고딕 ExtraBold&quot;;</p><p><br/></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "부정 WordCloud"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.label_16.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>color: black;</p><p><br/></p><p>font: 75 9pt &quot;나눔고딕 ExtraBold&quot;;</p><p><br/></p></body></html>"))
        self.label_16.setText(_translate("MainWindow", "MENU TOP 5"))
        self.label_17.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>color: black;</p><p><br/></p><p>font: 75 9pt &quot;나눔고딕 ExtraBold&quot;;</p><p><br/></p></body></html>"))
        self.label_17.setText(_translate("MainWindow", "항목 별 점수"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Tab 3"))
        self.label_9.setText(_translate("MainWindow", "학습한 별점"))
        self.label_15.setText(_translate("MainWindow", "음식점 정보"))
        self.actionshow.setText(_translate("MainWindow", "show"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())