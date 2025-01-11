# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ImageDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFrame, QGroupBox, QLabel, QPushButton,
    QSizePolicy, QTextEdit, QWidget)

class Ui_ImageDialog(object):
    def setupUi(self, ImageDialog):
        if not ImageDialog.objectName():
            ImageDialog.setObjectName(u"ImageDialog")
        ImageDialog.resize(300, 350)
        font = QFont()
        font.setFamilies([u"Arial"])
        ImageDialog.setFont(font)
        ImageDialog.setStyleSheet(u"QDialog{\n"
"	background-color: #EAEFEF;\n"
"}")
        ImageDialog.setSizeGripEnabled(False)
        ImageDialog.setModal(True)
        self.preview_label = QLabel(ImageDialog)
        self.preview_label.setObjectName(u"preview_label")
        self.preview_label.setGeometry(QRect(50, 10, 200, 150))
        self.preview_label.setMinimumSize(QSize(0, 0))
        self.preview_label.setMaximumSize(QSize(200, 160))
        font1 = QFont()
        font1.setFamilies([u"Nanum Gothic"])
        font1.setPointSize(12)
        self.preview_label.setFont(font1)
        self.preview_label.setStyleSheet(u"QLabel{\n"
"	color: rgb(0 ,0, 0);\n"
"	background:white;\n"
"	border: 1px solid black;\n"
"}")
        self.preview_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.reset_button = QPushButton(ImageDialog)
        self.reset_button.setObjectName(u"reset_button")
        self.reset_button.setGeometry(QRect(225, 135, 20, 20))
        self.reset_button.setMinimumSize(QSize(0, 0))
        self.reset_button.setMaximumSize(QSize(88, 16777215))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(12)
        self.reset_button.setFont(font2)
        self.reset_button.setStyleSheet(u"background: white;\n"
"border: 1px solid black;\n"
"border-radius: 10px;")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ViewRefresh))
        self.reset_button.setIcon(icon)
        self.groupBox = QGroupBox(ImageDialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(25, 170, 250, 120))
        font3 = QFont()
        font3.setFamilies([u"Nanum Gothic"])
        font3.setPointSize(10)
        font3.setKerning(True)
        self.groupBox.setFont(font3)
        self.groupBox.setStyleSheet(u"")
        self.button_record = QPushButton(self.groupBox)
        self.button_record.setObjectName(u"button_record")
        self.button_record.setGeometry(QRect(80, 80, 80, 25))
        font4 = QFont()
        font4.setPointSize(10)
        self.button_record.setFont(font4)
        self.button_record.setStyleSheet(u"")
        self.button_record.setFlat(False)
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 50, 20, 20))
        font5 = QFont()
        font5.setFamilies([u"Arial"])
        font5.setPointSize(11)
        self.label_2.setFont(font5)
        self.label_2.setStyleSheet(u"QLabel{\n"
"	color: rgb(0 ,0, 0);\n"
"	background-color: transparent;\n"
"}")
        self.textEdit_X = QTextEdit(self.groupBox)
        self.textEdit_X.setObjectName(u"textEdit_X")
        self.textEdit_X.setGeometry(QRect(50, 50, 60, 20))
        font6 = QFont()
        font6.setFamilies([u"Nanum Gothic"])
        font6.setPointSize(10)
        self.textEdit_X.setFont(font6)
        self.textEdit_X.setAutoFillBackground(False)
        self.textEdit_X.setStyleSheet(u"background:white;\n"
"border: 1px solid black;")
        self.textEdit_X.setFrameShape(QFrame.Shape.Box)
        self.textEdit_X.setFrameShadow(QFrame.Shadow.Plain)
        self.textEdit_X.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textEdit_X.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(130, 50, 20, 20))
        self.label_3.setFont(font5)
        self.label_3.setStyleSheet(u"QLabel{\n"
"	color: rgb(0 ,0, 0);\n"
"	background-color: transparent;\n"
"}")
        self.textEdit_Y = QTextEdit(self.groupBox)
        self.textEdit_Y.setObjectName(u"textEdit_Y")
        self.textEdit_Y.setGeometry(QRect(150, 50, 60, 20))
        self.textEdit_Y.setFont(font6)
        self.textEdit_Y.setAutoFillBackground(False)
        self.textEdit_Y.setStyleSheet(u"background:white;\n"
"border: 1px solid black;")
        self.textEdit_Y.setFrameShape(QFrame.Shape.Box)
        self.textEdit_Y.setFrameShadow(QFrame.Shadow.Plain)
        self.textEdit_Y.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textEdit_Y.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tool_tip = QLabel(self.groupBox)
        self.tool_tip.setObjectName(u"tool_tip")
        self.tool_tip.setGeometry(QRect(223, 25, 15, 15))
        font7 = QFont()
        font7.setFamilies([u"Nanum Gothic"])
        font7.setPointSize(8)
        self.tool_tip.setFont(font7)
        self.tool_tip.setStyleSheet(u"QLabel{\n"
"	background-color: #9437FF;\n"
"	color:#FFFFFF;\n"
"	border: none;\n"
"	border-radius: 6px;\n"
"	border-width : 1px\n"
"\n"
"}")
        self.tool_tip.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 25, 210, 15))
        font8 = QFont()
        font8.setFamilies([u"Nanum Gothic"])
        font8.setPointSize(8)
        font8.setItalic(False)
        font8.setUnderline(False)
        self.label_4.setFont(font8)
        self.label_4.setStyleSheet(u"QLabel{\n"
"	color: rgb(0 ,0, 0);\n"
"	background-color: transparent;\n"
"}")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.buttonBox = QDialogButtonBox(ImageDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(50, 310, 201, 35))
        self.buttonBox.setFont(font1)
        self.buttonBox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.buttonBox.setAutoFillBackground(False)
        self.buttonBox.setStyleSheet(u"")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setCenterButtons(True)

        self.retranslateUi(ImageDialog)

        self.button_record.setDefault(True)


        QMetaObject.connectSlotsByName(ImageDialog)
    # setupUi

    def retranslateUi(self, ImageDialog):
        ImageDialog.setWindowTitle(QCoreApplication.translate("ImageDialog", u"\uc774\ubbf8\uc9c0 \ucca8\ubd80", None))
        self.preview_label.setText(QCoreApplication.translate("ImageDialog", u"\uc774\uacf3\uc744 \ud074\ub9ad\ud558\uc5ec\n"
"\uc774\ubbf8\uc9c0\ub97c \uc120\ud0dd\ud558\uc138\uc694", None))
        self.reset_button.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("ImageDialog", u" \uc88c\ud45c \uc124\uc815 ", None))
        self.button_record.setText(QCoreApplication.translate("ImageDialog", u"\uae30\ub85d", None))
        self.label_2.setText(QCoreApplication.translate("ImageDialog", u"X :", None))
        self.label_3.setText(QCoreApplication.translate("ImageDialog", u"Y :", None))
        self.tool_tip.setText(QCoreApplication.translate("ImageDialog", u"?", None))
        self.label_4.setText(QCoreApplication.translate("ImageDialog", u"\uc218\ub3d9\ubaa8\ub4dc \uc0ac\uc6a9 \uc2dc \uc774\ubbf8\uc9c0\uc758 \uc88c\ud45c\ub97c \uc124\uc815\ud558\uc138\uc694", None))
    # retranslateUi

