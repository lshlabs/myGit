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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGroupBox,
    QLabel, QPushButton, QSizePolicy, QTextEdit,
    QWidget)

class Ui_ImageDialog(object):
    def setupUi(self, ImageDialog):
        if not ImageDialog.objectName():
            ImageDialog.setObjectName(u"ImageDialog")
        ImageDialog.resize(300, 320)
        font = QFont()
        font.setFamilies([u"Arial"])
        ImageDialog.setFont(font)
        ImageDialog.setStyleSheet(u"background-color: rgb(234, 238, 238)")
        self.preview_label = QLabel(ImageDialog)
        self.preview_label.setObjectName(u"preview_label")
        self.preview_label.setGeometry(QRect(50, 10, 200, 150))
        self.preview_label.setMinimumSize(QSize(0, 0))
        self.preview_label.setMaximumSize(QSize(200, 160))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(12)
        self.preview_label.setFont(font1)
        self.preview_label.setStyleSheet(u"background:white;\n"
"border: 1px solid black;")
        self.preview_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.cancel_button = QPushButton(ImageDialog)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setGeometry(QRect(163, 270, 88, 32))
        self.cancel_button.setMinimumSize(QSize(0, 0))
        self.cancel_button.setMaximumSize(QSize(88, 16777215))
        self.cancel_button.setFont(font1)
        self.cancel_button.setStyleSheet(u"background-color: rgb(234, 238, 238)")
        self.apply_button = QPushButton(ImageDialog)
        self.apply_button.setObjectName(u"apply_button")
        self.apply_button.setGeometry(QRect(50, 270, 88, 32))
        self.apply_button.setMinimumSize(QSize(0, 0))
        self.apply_button.setMaximumSize(QSize(88, 16777215))
        self.apply_button.setFont(font1)
        self.apply_button.setStyleSheet(u"background-color: rgb(234, 238, 238)")
        self.reset_button = QPushButton(ImageDialog)
        self.reset_button.setObjectName(u"reset_button")
        self.reset_button.setGeometry(QRect(225, 135, 20, 20))
        self.reset_button.setMinimumSize(QSize(0, 0))
        self.reset_button.setMaximumSize(QSize(88, 16777215))
        self.reset_button.setFont(font1)
        self.reset_button.setStyleSheet(u"background: white;\n"
"border: 1px solid black;\n"
"border-radius: 10px;")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ViewRefresh))
        self.reset_button.setIcon(icon)
        self.groupBox = QGroupBox(ImageDialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(50, 170, 201, 91))
        self.button_record = QPushButton(self.groupBox)
        self.button_record.setObjectName(u"button_record")
        self.button_record.setGeometry(QRect(80, 60, 40, 20))
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 30, 20, 20))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(11)
        self.label_2.setFont(font2)
        self.textEdit = QTextEdit(self.groupBox)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(40, 30, 50, 20))
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(10)
        self.textEdit.setFont(font3)
        self.textEdit.setAutoFillBackground(False)
        self.textEdit.setStyleSheet(u"background:white;\n"
"border: 1px solid black;")
        self.textEdit.setFrameShape(QFrame.Shape.Box)
        self.textEdit.setFrameShadow(QFrame.Shadow.Plain)
        self.textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(110, 30, 20, 20))
        self.label_3.setFont(font2)
        self.textEdit_2 = QTextEdit(self.groupBox)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(130, 30, 50, 20))
        self.textEdit_2.setFont(font3)
        self.textEdit_2.setAutoFillBackground(False)
        self.textEdit_2.setStyleSheet(u"background:white;\n"
"border: 1px solid black;")
        self.textEdit_2.setFrameShape(QFrame.Shape.Box)
        self.textEdit_2.setFrameShadow(QFrame.Shadow.Plain)
        self.textEdit_2.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textEdit_2.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tool_tip = QLabel(self.groupBox)
        self.tool_tip.setObjectName(u"tool_tip")
        self.tool_tip.setGeometry(QRect(103, 2, 20, 20))
        self.tool_tip.setTextFormat(Qt.TextFormat.PlainText)
        self.tool_tip.setPixmap(QPixmap(u"../img/tooltips.png"))
        self.tool_tip.setScaledContents(True)
        self.tool_tip.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.retranslateUi(ImageDialog)

        QMetaObject.connectSlotsByName(ImageDialog)
    # setupUi

    def retranslateUi(self, ImageDialog):
        ImageDialog.setWindowTitle(QCoreApplication.translate("ImageDialog", u"\uc774\ubbf8\uc9c0 \ucca8\ubd80", None))
        self.preview_label.setText(QCoreApplication.translate("ImageDialog", u"\uc774\uacf3\uc744 \ud074\ub9ad\ud558\uc5ec\n"
"\uc774\ubbf8\uc9c0\ub97c \uc120\ud0dd\ud558\uc138\uc694", None))
        self.cancel_button.setText(QCoreApplication.translate("ImageDialog", u"\ucde8\uc18c", None))
        self.apply_button.setText(QCoreApplication.translate("ImageDialog", u"\uc801\uc6a9", None))
        self.reset_button.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("ImageDialog", u"\uc218\ub3d9\ubaa8\ub4dc \uc88c\ud45c\uc124\uc815", None))
        self.button_record.setText(QCoreApplication.translate("ImageDialog", u"\ub179\ud654", None))
        self.label_2.setText(QCoreApplication.translate("ImageDialog", u"X :", None))
        self.label_3.setText(QCoreApplication.translate("ImageDialog", u"Y :", None))
        self.tool_tip.setText("")
    # retranslateUi

