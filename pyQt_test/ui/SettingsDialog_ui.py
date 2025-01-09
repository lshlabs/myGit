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
    QDialog, QDialogButtonBox, QGroupBox, QLabel,
    QSizePolicy, QWidget)

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
        font.setFamilies([u"\ub098\ub214\uace0\ub515"])
        SettingsDialog.setFont(font)
        SettingsDialog.setAutoFillBackground(False)
        SettingsDialog.setStyleSheet(u"QDialog{\n"
"	background-color: #EAEFEF;\n"
"}")
        SettingsDialog.setSizeGripEnabled(False)
        self.buttonBox = QDialogButtonBox(SettingsDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(10, 260, 430, 35))
        self.buttonBox.setMinimumSize(QSize(430, 35))
        font1 = QFont()
        font1.setFamilies([u"\ub098\ub214\uace0\ub515"])
        font1.setPointSize(12)
        self.buttonBox.setFont(font1)
        self.buttonBox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.buttonBox.setAutoFillBackground(False)
        self.buttonBox.setStyleSheet(u"")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.groupBox = QGroupBox(SettingsDialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 20, 410, 150))
        font2 = QFont()
        font2.setPointSize(10)
        self.groupBox.setFont(font2)
        self.check_shift1 = QCheckBox(self.groupBox)
        self.check_shift1.setObjectName(u"check_shift1")
        self.check_shift1.setGeometry(QRect(290, 30, 55, 32))
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(10)
        self.check_shift1.setFont(font3)
        self.check_shift1.setStyleSheet(u"QCheckBox{\n"
"	color: rgb(0 ,0, 0);\n"
"}")
        self.check_shift1.setChecked(False)
        self.check_shift1.setTristate(False)
        self.combo_stop = QComboBox(self.groupBox)
        self.combo_stop.setObjectName(u"combo_stop")
        self.combo_stop.setGeometry(QRect(90, 90, 120, 32))
        font4 = QFont()
        font4.setFamilies([u"\ub098\ub214\uace0\ub515"])
        font4.setPointSize(10)
        font4.setItalic(False)
        font4.setKerning(False)
        self.combo_stop.setFont(font4)
        self.combo_stop.setStyleSheet(u"QComboBox{\n"
"	color: rgb(0 ,0, 0);\n"
"	background-color:  rgb(255 ,255, 255);\n"
"}")
        self.check_shift2 = QCheckBox(self.groupBox)
        self.check_shift2.setObjectName(u"check_shift2")
        self.check_shift2.setGeometry(QRect(290, 90, 55, 32))
        self.check_shift2.setFont(font3)
        self.check_shift2.setStyleSheet(u"QCheckBox{\n"
"	color: rgb(0 ,0, 0);\n"
"}")
        self.check_shift2.setChecked(False)
        self.check_shift2.setTristate(False)
        self.label_start = QLabel(self.groupBox)
        self.label_start.setObjectName(u"label_start")
        self.label_start.setGeometry(QRect(10, 30, 70, 32))
        font5 = QFont()
        font5.setFamilies([u"\ub098\ub214\uace0\ub515"])
        font5.setPointSize(10)
        self.label_start.setFont(font5)
        self.label_start.setStyleSheet(u"QLabel{\n"
"	color: rgb(0 ,0, 0);\n"
"}")
        self.label_start.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.check_ctrl2 = QCheckBox(self.groupBox)
        self.check_ctrl2.setObjectName(u"check_ctrl2")
        self.check_ctrl2.setGeometry(QRect(230, 90, 50, 32))
        self.check_ctrl2.setFont(font3)
        self.check_ctrl2.setStyleSheet(u"QCheckBox{\n"
"	color: rgb(0 ,0, 0);\n"
"}")
        self.check_ctrl2.setChecked(False)
        self.check_ctrl2.setTristate(False)
        self.check_alt2 = QCheckBox(self.groupBox)
        self.check_alt2.setObjectName(u"check_alt2")
        self.check_alt2.setGeometry(QRect(350, 90, 50, 32))
        self.check_alt2.setFont(font3)
        self.check_alt2.setStyleSheet(u"QCheckBox{\n"
"	color: rgb(0 ,0, 0);\n"
"}")
        self.check_alt2.setChecked(False)
        self.check_alt2.setTristate(False)
        self.label_stop = QLabel(self.groupBox)
        self.label_stop.setObjectName(u"label_stop")
        self.label_stop.setGeometry(QRect(10, 90, 70, 32))
        self.label_stop.setFont(font5)
        self.label_stop.setStyleSheet(u"QLabel{\n"
"	color: rgb(0 ,0, 0);\n"
"}")
        self.label_stop.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.check_ctrl1 = QCheckBox(self.groupBox)
        self.check_ctrl1.setObjectName(u"check_ctrl1")
        self.check_ctrl1.setGeometry(QRect(230, 30, 50, 32))
        self.check_ctrl1.setFont(font3)
        self.check_ctrl1.setStyleSheet(u"QCheckBox{\n"
"	color: rgb(0 ,0, 0);\n"
"}")
        self.check_ctrl1.setIconSize(QSize(16, 16))
        self.check_ctrl1.setChecked(False)
        self.check_ctrl1.setTristate(False)
        self.check_alt1 = QCheckBox(self.groupBox)
        self.check_alt1.setObjectName(u"check_alt1")
        self.check_alt1.setGeometry(QRect(350, 30, 50, 32))
        self.check_alt1.setFont(font3)
        self.check_alt1.setStyleSheet(u"QCheckBox{\n"
"	color: rgb(0 ,0, 0);\n"
"}")
        self.check_alt1.setChecked(False)
        self.check_alt1.setTristate(False)
        self.combo_run = QComboBox(self.groupBox)
        self.combo_run.setObjectName(u"combo_run")
        self.combo_run.setGeometry(QRect(90, 30, 120, 32))
        self.combo_run.setFont(font4)
        self.combo_run.setStyleSheet(u"QComboBox{\n"
"	color: rgb(0 ,0, 0);\n"
"	background-color:  rgb(255 ,255, 255);\n"
"}")

        self.retranslateUi(SettingsDialog)
        self.buttonBox.accepted.connect(SettingsDialog.accept)
        self.buttonBox.rejected.connect(SettingsDialog.reject)

        QMetaObject.connectSlotsByName(SettingsDialog)
    # setupUi

    def retranslateUi(self, SettingsDialog):
        SettingsDialog.setWindowTitle(QCoreApplication.translate("SettingsDialog", u"\uc124\uc815", None))
        self.groupBox.setTitle(QCoreApplication.translate("SettingsDialog", u" \ub9e4\ud06c\ub85c \uc2dc\uc791 / \uc911\uc9c0 \ud0a4 \uc124\uc815 ", None))
        self.check_shift1.setText(QCoreApplication.translate("SettingsDialog", u"Shift", None))
        self.combo_stop.setCurrentText("")
        self.combo_stop.setPlaceholderText(QCoreApplication.translate("SettingsDialog", u"\uc120\ud0dd\ud558\uc138\uc694", None))
        self.check_shift2.setText(QCoreApplication.translate("SettingsDialog", u"Shift", None))
        self.label_start.setText(QCoreApplication.translate("SettingsDialog", u"\uc2dc\uc791 \ud0a4", None))
        self.check_ctrl2.setText(QCoreApplication.translate("SettingsDialog", u"Ctrl", None))
        self.check_alt2.setText(QCoreApplication.translate("SettingsDialog", u"Alt", None))
        self.label_stop.setText(QCoreApplication.translate("SettingsDialog", u"\uc885\ub8cc \ud0a4", None))
        self.check_ctrl1.setText(QCoreApplication.translate("SettingsDialog", u"Ctrl", None))
        self.check_alt1.setText(QCoreApplication.translate("SettingsDialog", u"Alt", None))
        self.combo_run.setCurrentText("")
        self.combo_run.setPlaceholderText(QCoreApplication.translate("SettingsDialog", u"\uc120\ud0dd\ud558\uc138\uc694", None))
    # retranslateUi

