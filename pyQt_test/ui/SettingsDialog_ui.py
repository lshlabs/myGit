# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SettingsDialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QComboBox,
    QDialog, QDialogButtonBox, QLabel, QSizePolicy,
    QWidget)

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        if not SettingsDialog.objectName():
            SettingsDialog.setObjectName(u"SettingsDialog")
        SettingsDialog.setWindowModality(Qt.WindowModality.NonModal)
        SettingsDialog.resize(450, 480)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SettingsDialog.sizePolicy().hasHeightForWidth())
        SettingsDialog.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Arial"])
        SettingsDialog.setFont(font)
        SettingsDialog.setAutoFillBackground(False)
        SettingsDialog.setStyleSheet(u"background:gainsboro;")
        self.buttonBox = QDialogButtonBox(SettingsDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(10, 440, 431, 32))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(12)
        self.buttonBox.setFont(font1)
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.label = QLabel(SettingsDialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 50, 100, 32))
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.comboBox = QComboBox(SettingsDialog)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(120, 50, 120, 32))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(12)
        font2.setItalic(False)
        font2.setKerning(False)
        self.comboBox.setFont(font2)
        self.comboBox.setStyleSheet(u"background:white;")
        self.checkBox = QCheckBox(SettingsDialog)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(250, 50, 50, 32))
        self.checkBox.setFont(font1)
        self.checkBox.setChecked(False)
        self.checkBox.setTristate(False)
        self.checkBox_2 = QCheckBox(SettingsDialog)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(300, 50, 55, 32))
        self.checkBox_2.setFont(font1)
        self.checkBox_2.setChecked(False)
        self.checkBox_2.setTristate(False)
        self.checkBox_3 = QCheckBox(SettingsDialog)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setGeometry(QRect(355, 50, 50, 32))
        self.checkBox_3.setFont(font1)
        self.checkBox_3.setChecked(False)
        self.checkBox_3.setTristate(False)

        self.retranslateUi(SettingsDialog)
        self.buttonBox.accepted.connect(SettingsDialog.accept)
        self.buttonBox.rejected.connect(SettingsDialog.reject)

        QMetaObject.connectSlotsByName(SettingsDialog)
    # setupUi

    def retranslateUi(self, SettingsDialog):
        SettingsDialog.setWindowTitle(QCoreApplication.translate("SettingsDialog", u"\uc124\uc815", None))
        self.label.setText(QCoreApplication.translate("SettingsDialog", u"\ud0a4 \uc124\uc815", None))
        self.comboBox.setCurrentText("")
        self.comboBox.setPlaceholderText(QCoreApplication.translate("SettingsDialog", u"\uc120\ud0dd\ud558\uc138\uc694", None))
        self.checkBox.setText(QCoreApplication.translate("SettingsDialog", u"Ctrl", None))
        self.checkBox_2.setText(QCoreApplication.translate("SettingsDialog", u"Shift", None))
        self.checkBox_3.setText(QCoreApplication.translate("SettingsDialog", u"Alt", None))
    # retranslateUi

