import googletrans
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QTimer
from googletrans import LANGUAGES
from gtts.lang import tts_langs
from gtts import gTTS
from os import remove
from playsound import playsound
from datetime import datetime
from PyQt6.QtWidgets import QMessageBox
from subprocess import check_output


class Ui_Window(object):
    def setupUi(self, Window):
        Window.setObjectName("Window")
        Window.resize(650, 550)
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(21)
        Window.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Window.setWindowIcon(icon)
        Window.setStyleSheet("*{\n"
                             "    background-color: rgb(255, 255, 255);\n"
                             "}\n"
                             "#Swap {\n"
                             "    background-color: rgb(255, 255, 255);\n"
                             "    border: none;\n"
                             "}\n"
                             "#Swap::hover{\n"
                             "    background-color:rgb(235, 235, 235);\n"
                             "}\n"
                             "#destLang, #srcLang{\n"
                             "    background-color: rgb(25, 103, 210);\n"
                             "    color: rgb(255, 255, 255);\n"
                             "    border: 2px solid rgb(18, 53, 168)\n"
                             "}\n"
                             "\n"
                             "#destLang::hover{\n"
                             "    background-color: rgb(22, 97, 194);\n"
                             "}\n"
                             "#srcLang::hover{\n"
                             "    background-color: rgb(22, 97, 194);\n"
                             "}\n"
                             "#translateLabel, #translateLabel_2{\n"
                             "    color: rgb(21, 89, 179);\n"
                             "    background-color: rgb(255, 255, 255);\n"
                             "}\n"
                             "#srcPlay, #destPlay{\n"
                             "    border: 2px solid rgb(18, 53, 168);\n"
                             "    background-color: rgb(255, 255, 255);\n"
                             "    padding:1px;\n"
                             "}\n"
                             "#srcPlay::hover, #destPlay::hover{\n"
                             "    background-color: rgb(235, 235, 235);\n"
                             "}\n"
                             "#destText, #srcText{\n"
                             "    border: 1px solid rgb(18, 53, 168);\n"
                             "    background-color:rgb(201, 255, 252);\n"
                             "\n"
                             "}\n"
                             "#srcText::focus{\n"
                             "    border: 2px solid rgb(13, 17, 125);\n"
                             "}\n"
                             "#translateB{\n"
                             "    background-color: rgb(25, 103, 210);\n"
                             "    color: rgb(255, 255, 255);\n"
                             "    border: 2px solid rgb(18, 53, 168);\n"
                             "    padding: 3px\n"
                             "}\n"
                             "#translateB::hover{\n"
                             "    background-color: rgb(22, 97, 194);}")
        self.centralwidget = QtWidgets.QWidget(Window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.translationPage = QtWidgets.QWidget()
        self.translationPage.setObjectName("translationPage")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.translationPage)
        self.verticalLayout.setObjectName("verticalLayout")
        self.translateLabel = QtWidgets.QLabel(self.translationPage)
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(50)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.translateLabel.setFont(font)
        self.translateLabel.setScaledContents(False)
        self.translateLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.translateLabel.setObjectName("translateLabel")
        self.verticalLayout.addWidget(self.translateLabel)
        spacerItem = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Policy.Minimum,
                                           QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.srcLang = QtWidgets.QComboBox(self.translationPage)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(16)
        self.srcLang.setFont(font)
        self.srcLang.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.srcLang.setMaxVisibleItems(6)
        self.srcLang.setInsertPolicy(QtWidgets.QComboBox.InsertPolicy.InsertAlphabetically)
        self.srcLang.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContents)
        self.srcLang.setFrame(True)
        self.srcLang.setObjectName("srcLang")
        self.horizontalLayout.addWidget(self.srcLang)
        self.Swap = QtWidgets.QPushButton(self.translationPage)
        self.Swap.setMaximumSize(QtCore.QSize(100, 16777215))
        self.Swap.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.Swap.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.Swap.setStyleSheet("")
        self.Swap.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("swap.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Swap.setIcon(icon1)
        self.Swap.setIconSize(QtCore.QSize(35, 35))
        self.Swap.setFlat(False)
        self.Swap.setObjectName("Swap")
        self.horizontalLayout.addWidget(self.Swap)
        self.destLang = QtWidgets.QComboBox(self.translationPage)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(16)
        self.destLang.setFont(font)
        self.destLang.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.destLang.setMaxVisibleItems(6)
        self.destLang.setInsertPolicy(QtWidgets.QComboBox.InsertPolicy.InsertAlphabetically)
        self.destLang.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContents)
        self.destLang.setMinimumContentsLength(0)
        self.destLang.setDuplicatesEnabled(False)
        self.destLang.setFrame(True)
        self.destLang.setObjectName("destLang")
        self.horizontalLayout.addWidget(self.destLang)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.destText = QtWidgets.QPlainTextEdit(self.translationPage)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(15)
        self.destText.setFont(font)
        self.destText.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CursorShape.IBeamCursor))
        self.destText.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.destText.setReadOnly(True)
        self.destText.setPlainText("")
        self.destText.setObjectName("destText")
        self.gridLayout.addWidget(self.destText, 0, 1, 1, 1)
        self.srcText = QtWidgets.QPlainTextEdit(self.translationPage)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(15)
        self.srcText.setFont(font)
        self.srcText.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CursorShape.IBeamCursor))
        self.srcText.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.srcText.setPlainText("")
        self.srcText.setObjectName("srcText")
        self.gridLayout.addWidget(self.srcText, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.srcPlay = QtWidgets.QPushButton(self.translationPage)
        self.srcPlay.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.srcPlay.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.srcPlay.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("high-volume.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.srcPlay.setIcon(icon2)
        self.srcPlay.setIconSize(QtCore.QSize(30, 30))
        self.srcPlay.setDefault(False)
        self.srcPlay.setFlat(False)
        self.srcPlay.setObjectName("srcPlay")
        self.horizontalLayout_2.addWidget(self.srcPlay)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.destPlay = QtWidgets.QPushButton(self.translationPage)
        self.destPlay.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.destPlay.setText("")
        self.destPlay.setIcon(icon2)
        self.destPlay.setIconSize(QtCore.QSize(30, 30))
        self.destPlay.setFlat(False)
        self.destPlay.setObjectName("destPlay")
        self.horizontalLayout_4.addWidget(self.destPlay)
        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout.addItem(spacerItem1)
        self.translateB = QtWidgets.QPushButton(self.translationPage)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(20)
        self.translateB.setFont(font)
        self.translateB.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.translateB.setIconSize(QtCore.QSize(16, 16))
        self.translateB.setObjectName("translateB")
        self.verticalLayout.addWidget(self.translateB)
        self.stackedWidget.addWidget(self.translationPage)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.WaitCursor))
        self.page_2.setObjectName("page_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.translateLabel_2 = QtWidgets.QLabel(self.page_2)
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(60)
        self.translateLabel_2.setFont(font)
        self.translateLabel_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.WaitCursor))
        self.translateLabel_2.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.translateLabel_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.translateLabel_2.setObjectName("translateLabel_2")
        self.verticalLayout_4.addWidget(self.translateLabel_2)
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        Window.setCentralWidget(self.centralwidget)
        self.retranslateUi(Window)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Window)

        self.destText.clear()
        self.timer = QTimer()
        self.timer.timeout.connect(self.stopTimer)
        self.timer.start(1500)
        for lang in LANGUAGES:
            self.srcLang.addItem(str(LANGUAGES[lang]).title())
            self.destLang.addItem(str(LANGUAGES[lang]).title())
        self.srcLang.setCurrentText("English")
        self.destLang.setCurrentText("German")
        self.srcLang.currentIndexChanged.connect(self.changedIndex)
        self.destLang.currentIndexChanged.connect(self.changedIndex)
        self.Swap.clicked.connect(self.swapF)
        self.srcPlay.clicked.connect(self.srcPlaySoundF)
        self.destPlay.clicked.connect(self.destPlaySoundF)
        self.translateB.clicked.connect(self.translateF)
        self.translator = googletrans.Translator()
        self.srcText.textChanged.connect(self.destText.clear)

    def translateF(self):
        srctxt = self.srcText.toPlainText()
        if srctxt.strip() != "":
            dest = self.destLang.currentText()
            src = self.srcLang.currentText()
            try:
                SRC = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(src.lower())]
                DEST = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(dest.lower())]
                desttxt = self.translator.translate(text=srctxt, src=SRC, dest=DEST)
                self.destText.setPlainText(str(desttxt.text))
            except:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Icon.Critical)
                msg.setText("Something went wrong!\nCheck your Internet connection.")
                msg.setWindowTitle("Connection Error")
                msg.setStandardButtons(QMessageBox.StandardButton.Ok)
                msg.exec()
                self.deleteALLFILES()
                exit()

    def deleteALLFILES(self):
        try:
            cmd = check_output(["dir", "/b", "*.mp3"], shell=True).decode().split()
            for file in cmd:
                if "TranslateTTS" in file:
                    remove(file)
        except:
            pass

    def srcPlaySoundF(self):
        now = datetime.now()
        f_name = f"TranslateTTS{now.year}{now.month}{now.day}{now.hour}{now.minute}{now.second}S.mp3"
        text = str(self.srcText.toPlainText())
        if text.strip() != "":
            lang = self.srcLang.currentText()
            try:
                selLang = list(tts_langs().keys())[list(tts_langs().values()).index(lang.title())]
                sound = gTTS(text=text, lang=selLang)
                sound.save(f_name)
                playsound(f_name)
                try:
                    remove(f_name)
                except FileNotFoundError:
                    pass
            except:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Icon.Critical)
                msg.setText("Something went wrong!\nCheck your Internet connection.")
                msg.setWindowTitle("Connection Error")
                msg.setStandardButtons(QMessageBox.StandardButton.Ok)
                msg.exec()
                self.deleteALLFILES()
                exit()

    def destPlaySoundF(self):
        now = datetime.now()
        f_name = f"TranslateTTS{now.year}{now.month}{now.day}{now.hour}{now.minute}{now.second}D.mp3"
        text = str(self.destText.toPlainText())
        if text.strip() != "":
            lang = self.destLang.currentText()
            try:
                selLang = list(tts_langs().keys())[list(tts_langs().values()).index(lang.title())]
                sound = gTTS(text=text, lang=selLang)
                sound.save(f_name)
                playsound(f_name)
                try:
                    remove(f_name)
                except FileNotFoundError:
                    pass
            except:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Icon.Critical)
                msg.setText("Something went wrong!\nCheck your Internet connection.")
                msg.setWindowTitle("Connection Error")
                msg.setStandardButtons(QMessageBox.StandardButton.Ok)
                msg.exec()
                self.deleteALLFILES()
                exit()

    def swapF(self):
        c1 = str(self.srcLang.currentText())
        c2 = str(self.destLang.currentText())
        self.srcLang.setCurrentText(c2)
        self.destLang.setCurrentText(c1)

    def changedIndex(self):
        c1 = str(self.srcLang.currentText())
        c2 = str(self.destLang.currentText())
        langs = tts_langs()
        if c1.upper() not in [str(l).upper() for l in langs.values()]:
            self.srcPlay.setDisabled(True)
        else:
            self.srcPlay.setDisabled(False)
        if c2.upper() not in [str(l).upper() for l in langs.values()]:
            self.destPlay.setDisabled(True)
        else:
            self.destPlay.setDisabled(False)
        self.destText.clear()

    def stopTimer(self):
        self.timer.stop()
        self.stackedWidget.setCurrentIndex(0)

    def retranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "Translate"))
        self.translateLabel.setText(_translate("Window", "Translate"))
        self.Swap.setToolTip(_translate("Window", "<html><head/><body><p>Swap</p></body></html>"))
        self.Swap.setShortcut(_translate("Window", "Ctrl+Shift+S"))
        self.destText.setPlaceholderText(_translate("Window", "Translation"))
        self.srcPlay.setToolTip(_translate("Window", "<html><head/><body><p>Listen</p></body></html>"))
        self.destPlay.setToolTip(_translate("Window", "<html><head/><body><p>Listen</p></body></html>"))
        self.translateB.setToolTip(_translate("Window", "<html><head/><body><p>Translate</p></body></html>"))
        self.translateB.setText(_translate("Window", "Translate"))
        self.translateLabel_2.setText(_translate("Window", "Translate"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Window = QtWidgets.QMainWindow()
    ui = Ui_Window()
    ui.setupUi(Window)
    Window.show()
    sys.exit(app.exec())
