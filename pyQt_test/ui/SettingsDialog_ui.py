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
        SettingsDialog.resize(450, 300)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SettingsDialog.sizePolicy().hasHeightForWidth())
        SettingsDialog.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Arial"])
        SettingsDialog.setFont(font)
        SettingsDialog.setAutoFillBackground(False)
        SettingsDialog.setStyleSheet(u"background:#DCDCDC;")
        self.buttonBox = QDialogButtonBox(SettingsDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(10, 260, 431, 32))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(12)
        self.buttonBox.setFont(font1)
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.label_start = QLabel(SettingsDialog)
        self.label_start.setObjectName(u"label_start")
        self.label_start.setGeometry(QRect(20, 50, 100, 32))
        self.label_start.setFont(font1)
        self.label_start.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.combo_run = QComboBox(SettingsDialog)
        self.combo_run.setObjectName(u"combo_run")
        self.combo_run.setGeometry(QRect(120, 50, 120, 32))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(12)
        font2.setItalic(False)
        font2.setKerning(False)
        self.combo_run.setFont(font2)
        self.combo_run.setStyleSheet(u"background:white;")
        self.check_ctrl1 = QCheckBox(SettingsDialog)
        self.check_ctrl1.setObjectName(u"check_ctrl1")
        self.check_ctrl1.setGeometry(QRect(250, 50, 50, 32))
        self.check_ctrl1.setFont(font1)
        self.check_ctrl1.setChecked(False)
        self.check_ctrl1.setTristate(False)
        self.check_shift1 = QCheckBox(SettingsDialog)
        self.check_shift1.setObjectName(u"check_shift1")
        self.check_shift1.setGeometry(QRect(300, 50, 55, 32))
        self.check_shift1.setFont(font1)
        self.check_shift1.setChecked(False)
        self.check_shift1.setTristate(False)
        self.check_alt1 = QCheckBox(SettingsDialog)
        self.check_alt1.setObjectName(u"check_alt1")
        self.check_alt1.setGeometry(QRect(355, 50, 50, 32))
        self.check_alt1.setFont(font1)
        self.check_alt1.setChecked(False)
        self.check_alt1.setTristate(False)
        self.label_stop = QLabel(SettingsDialog)
        self.label_stop.setObjectName(u"label_stop")
        self.label_stop.setGeometry(QRect(20, 110, 100, 32))
        self.label_stop.setFont(font1)
        self.label_stop.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.combo_stop = QComboBox(SettingsDialog)
        self.combo_stop.setObjectName(u"combo_stop")
        self.combo_stop.setGeometry(QRect(120, 110, 120, 32))
        self.combo_stop.setFont(font2)
        self.combo_stop.setStyleSheet(u"background:white;")
        self.check_alt2 = QCheckBox(SettingsDialog)
        self.check_alt2.setObjectName(u"check_alt2")
        self.check_alt2.setGeometry(QRect(355, 110, 50, 32))
        self.check_alt2.setFont(font1)
        self.check_alt2.setChecked(False)
        self.check_alt2.setTristate(False)
        self.check_ctrl2 = QCheckBox(SettingsDialog)
        self.check_ctrl2.setObjectName(u"check_ctrl2")
        self.check_ctrl2.setGeometry(QRect(250, 110, 50, 32))
        self.check_ctrl2.setFont(font1)
        self.check_ctrl2.setChecked(False)
        self.check_ctrl2.setTristate(False)
        self.check_shift2 = QCheckBox(SettingsDialog)
        self.check_shift2.setObjectName(u"check_shift2")
        self.check_shift2.setGeometry(QRect(300, 110, 55, 32))
        self.check_shift2.setFont(font1)
        self.check_shift2.setChecked(False)
        self.check_shift2.setTristate(False)

        self.retranslateUi(SettingsDialog)
        self.buttonBox.accepted.connect(SettingsDialog.accept)
        self.buttonBox.rejected.connect(SettingsDialog.reject)

        QMetaObject.connectSlotsByName(SettingsDialog)
    # setupUi

    def retranslateUi(self, SettingsDialog):
        SettingsDialog.setWindowTitle(QCoreApplication.translate("SettingsDialog", u"\uc124\uc815", None))
        self.label_start.setText(QCoreApplication.translate("SettingsDialog", u"\ub9e4\ud06c\ub85c \uc2dc\uc791 \ud0a4", None))
        self.combo_run.setCurrentText("")
        self.combo_run.setPlaceholderText(QCoreApplication.translate("SettingsDialog", u"\uc120\ud0dd\ud558\uc138\uc694", None))
        self.check_ctrl1.setText(QCoreApplication.translate("SettingsDialog", u"Ctrl", None))
        self.check_shift1.setText(QCoreApplication.translate("SettingsDialog", u"Shift", None))
        self.check_alt1.setText(QCoreApplication.translate("SettingsDialog", u"Alt", None))
        self.label_stop.setText(QCoreApplication.translate("SettingsDialog", u"\ub9e4\ud06c\ub85c \uc885\ub8cc \ud0a4", None))
        self.combo_stop.setCurrentText("")
        self.combo_stop.setPlaceholderText(QCoreApplication.translate("SettingsDialog", u"\uc120\ud0dd\ud558\uc138\uc694", None))
        self.check_alt2.setText(QCoreApplication.translate("SettingsDialog", u"Alt", None))
        self.check_ctrl2.setText(QCoreApplication.translate("SettingsDialog", u"Ctrl", None))
        self.check_shift2.setText(QCoreApplication.translate("SettingsDialog", u"Shift", None))
    # retranslateUi

