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
        SettingsDialog.resize(450, 560)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SettingsDialog.sizePolicy().hasHeightForWidth())
        SettingsDialog.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Nanum Gothic"])
        SettingsDialog.setFont(font)
        SettingsDialog.setAutoFillBackground(False)
        SettingsDialog.setStyleSheet(u"QDialog{\n"
"	background-color: #EAEFEF;\n"
"}")
        SettingsDialog.setSizeGripEnabled(False)
        self.buttonBox = QDialogButtonBox(SettingsDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(10, 520, 430, 35))
        font1 = QFont()
        font1.setFamilies([u"NanumGothic"])
        font1.setPointSize(12)
        self.buttonBox.setFont(font1)
        self.buttonBox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.buttonBox.setAutoFillBackground(False)
        self.buttonBox.setStyleSheet(u"")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.groupBox_active = QGroupBox(SettingsDialog)
        self.groupBox_active.setObjectName(u"groupBox_active")
        self.groupBox_active.setGeometry(QRect(20, 20, 410, 130))
        font2 = QFont()
        font2.setFamilies([u"NanumGothic"])
        font2.setPointSize(10)
        self.groupBox_active.setFont(font2)
        self.check_shift1 = QCheckBox(self.groupBox_active)
        self.check_shift1.setObjectName(u"check_shift1")
        self.check_shift1.setGeometry(QRect(290, 30, 55, 32))
        self.check_shift1.setFont(font2)
        self.check_shift1.setStyleSheet(u"QCheckBox{\n"
"	color: rgb(0 ,0, 0);\n"
"}")
        self.check_shift1.setChecked(False)
        self.check_shift1.setTristate(False)
        self.combo_stop = QComboBox(self.groupBox_active)
        self.combo_stop.setObjectName(u"combo_stop")
        self.combo_stop.setGeometry(QRect(90, 80, 120, 32))
        font3 = QFont()
        font3.setFamilies([u"NanumGothic"])
        font3.setPointSize(10)
        font3.setItalic(False)
        font3.setKerning(False)
        self.combo_stop.setFont(font3)
        self.combo_stop.setStyleSheet(u"QComboBox{\n"
"	color: rgb(0 ,0, 0);\n"
"	background-color:  rgb(255 ,255, 255);\n"
"}")
        self.check_shift2 = QCheckBox(self.groupBox_active)
        self.check_shift2.setObjectName(u"check_shift2")
        self.check_shift2.setGeometry(QRect(290, 80, 55, 32))
        self.check_shift2.setFont(font2)
        self.check_shift2.setStyleSheet(u"QCheckBox{\n"
"	color: rgb(0 ,0, 0);\n"
"}")
        self.check_shift2.setChecked(False)
        self.check_shift2.setTristate(False)
        self.label_start = QLabel(self.groupBox_active)
        self.label_start.setObjectName(u"label_start")
        self.label_start.setGeometry(QRect(10, 30, 70, 32))
        self.label_start.setFont(font2)
        self.label_start.setStyleSheet(u"QLabel{\n"
"	color: rgb(0 ,0, 0);\n"
"	background-color: transparent;\n"
"}")
        self.label_start.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.check_ctrl2 = QCheckBox(self.groupBox_active)
        self.check_ctrl2.setObjectName(u"check_ctrl2")
        self.check_ctrl2.setGeometry(QRect(230, 80, 50, 32))
        self.check_ctrl2.setFont(font2)
        self.check_ctrl2.setStyleSheet(u"QCheckBox{\n"
"	color: rgb(0 ,0, 0);\n"
"}")
        self.check_ctrl2.setChecked(False)
        self.check_ctrl2.setTristate(False)
        self.check_alt2 = QCheckBox(self.groupBox_active)
        self.check_alt2.setObjectName(u"check_alt2")
        self.check_alt2.setGeometry(QRect(350, 80, 50, 32))
        self.check_alt2.setFont(font2)
        self.check_alt2.setStyleSheet(u"QCheckBox{\n"
"	color: rgb(0 ,0, 0);\n"
"}")
        self.check_alt2.setChecked(False)
        self.check_alt2.setTristate(False)
        self.label_stop = QLabel(self.groupBox_active)
        self.label_stop.setObjectName(u"label_stop")
        self.label_stop.setGeometry(QRect(10, 80, 70, 32))
        self.label_stop.setFont(font2)
        self.label_stop.setStyleSheet(u"QLabel{\n"
"	color: rgb(0 ,0, 0);\n"
"	background-color: transparent;\n"
"}")
        self.label_stop.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.check_ctrl1 = QCheckBox(self.groupBox_active)
        self.check_ctrl1.setObjectName(u"check_ctrl1")
        self.check_ctrl1.setGeometry(QRect(230, 30, 50, 32))
        self.check_ctrl1.setFont(font2)
        self.check_ctrl1.setStyleSheet(u"QCheckBox{\n"
"	color: rgb(0 ,0, 0);\n"
"}")
        self.check_ctrl1.setIconSize(QSize(16, 16))
        self.check_ctrl1.setChecked(False)
        self.check_ctrl1.setTristate(False)
        self.check_alt1 = QCheckBox(self.groupBox_active)
        self.check_alt1.setObjectName(u"check_alt1")
        self.check_alt1.setGeometry(QRect(350, 30, 50, 32))
        self.check_alt1.setFont(font2)
        self.check_alt1.setStyleSheet(u"QCheckBox{\n"
"	color: rgb(0 ,0, 0);\n"
"}")
        self.check_alt1.setChecked(False)
        self.check_alt1.setTristate(False)
        self.combo_run = QComboBox(self.groupBox_active)
        self.combo_run.setObjectName(u"combo_run")
        self.combo_run.setGeometry(QRect(90, 30, 120, 32))
        self.combo_run.setFont(font3)
        self.combo_run.setStyleSheet(u"QComboBox{\n"
"	color: rgb(0 ,0, 0);\n"
"	background-color:  rgb(255 ,255, 255);\n"
"}")
        self.groupBox_passive = QGroupBox(SettingsDialog)
        self.groupBox_passive.setObjectName(u"groupBox_passive")
        self.groupBox_passive.setGeometry(QRect(20, 170, 410, 330))
        self.groupBox_passive.setFont(font2)
        self.check_shift3 = QCheckBox(self.groupBox_passive)
        self.check_shift3.setObjectName(u"check_shift3")
        self.check_shift3.setGeometry(QRect(290, 30, 55, 32))
        self.check_shift3.setFont(font2)
        self.check_shift3.setStyleSheet(u"QCheckBox{\n"
"	color: rgb(0 ,0, 0);\n"
"}")
        self.check_shift3.setChecked(False)
        self.check_shift3.setTristate(False)
        self.combo_ps2 = QComboBox(self.groupBox_passive)
        self.combo_ps2.setObjectName(u"combo_ps2")
        self.combo_ps2.setGeometry(QRect(90, 80, 120, 32))
        self.combo_ps2.setFont(font3)
        self.combo_ps2.setStyleSheet(u"QComboBox{\n"
"	color: rgb(0 ,0, 0);\n"
"	background-color:  rgb(255 ,255, 255);\n"
"}")
        self.check_shift4 = QCheckBox(self.groupBox_passive)
        self.check_shift4.setObjectName(u"check_shift4")
        self.check_shift4.setGeometry(QRect(290, 80, 55, 32))
        self.check_shift4.setFont(font2)
        self.check_shift4.setStyleSheet(u"QCheckBox{\n"
"	color: rgb(0 ,0, 0);\n"
"}")
        self.check_shift4.setChecked(False)
        self.check_shift4.setTristate(False)
        self.label_img_name1 = QLabel(self.groupBox_passive)
        self.label_img_name1.setObjectName(u"label_img_name1")
        self.label_img_name1.setGeometry(QRect(10, 30, 70, 32))
        self.label_img_name1.setFont(font2)
        self.label_img_name1.setStyleSheet(u"QLabel{\n"
"	color: rgb(0 ,0, 0);\n"
"	background-color: transparent;\n"
"}")
        self.label_img_name1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.check_ctrl4 = QCheckBox(self.groupBox_passive)
        self.check_ctrl4.setObjectName(u"check_ctrl4")
        self.check_ctrl4.setGeometry(QRect(230, 80, 50, 32))
        self.check_ctrl4.setFont(font2)
        self.check_ctrl4.setStyleSheet(u"QCheckBox{\n"
"	color: rgb(0 ,0, 0);\n"
"}")
        self.check_ctrl4.setChecked(False)
        self.check_ctrl4.setTristate(False)
        self.check_alt4 = QCheckBox(self.groupBox_passive)
        self.check_alt4.setObjectName(u"check_alt4")
        self.check_alt4.setGeometry(QRect(350, 80, 50, 32))
        self.check_alt4.setFont(font2)
        self.check_alt4.setStyleSheet(u"QCheckBox{\n"
"	color: rgb(0 ,0, 0);\n"
"}")
        self.check_alt4.setChecked(False)
        self.check_alt4.setTristate(False)
        self.label_img_name2 = QLabel(self.groupBox_passive)
        self.label_img_name2.setObjectName(u"label_img_name2")
        self.label_img_name2.setGeometry(QRect(10, 80, 70, 32))
        self.label_img_name2.setFont(font2)
        self.label_img_name2.setStyleSheet(u"QLabel{\n"
"	color: rgb(0 ,0, 0);\n"
"	background-color: transparent;\n"
"}")
        self.label_img_name2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.check_ctrl3 = QCheckBox(self.groupBox_passive)
        self.check_ctrl3.setObjectName(u"check_ctrl3")
        self.check_ctrl3.setGeometry(QRect(230, 30, 50, 32))
        self.check_ctrl3.setFont(font2)
        self.check_ctrl3.setStyleSheet(u"QCheckBox{\n"
"	color: rgb(0 ,0, 0);\n"
"}")
        self.check_ctrl3.setIconSize(QSize(16, 16))
        self.check_ctrl3.setChecked(False)
        self.check_ctrl3.setTristate(False)
        self.check_alt3 = QCheckBox(self.groupBox_passive)
        self.check_alt3.setObjectName(u"check_alt3")
        self.check_alt3.setGeometry(QRect(350, 30, 50, 32))
        self.check_alt3.setFont(font2)
        self.check_alt3.setStyleSheet(u"QCheckBox{\n"
"	color: rgb(0 ,0, 0);\n"
"}")
        self.check_alt3.setChecked(False)
        self.check_alt3.setTristate(False)
        self.combo_ps1 = QComboBox(self.groupBox_passive)
        self.combo_ps1.setObjectName(u"combo_ps1")
        self.combo_ps1.setGeometry(QRect(90, 30, 120, 32))
        self.combo_ps1.setFont(font3)
        self.combo_ps1.setStyleSheet(u"QComboBox{\n"
"	color: rgb(0 ,0, 0);\n"
"	background-color:  rgb(255 ,255, 255);\n"
"}")
        self.combo_ps3 = QComboBox(self.groupBox_passive)
        self.combo_ps3.setObjectName(u"combo_ps3")
        self.combo_ps3.setGeometry(QRect(90, 130, 120, 32))
        self.combo_ps3.setFont(font3)
        self.combo_ps3.setStyleSheet(u"QComboBox{\n"
"	color: rgb(0 ,0, 0);\n"
"	background-color:  rgb(255 ,255, 255);\n"
"}")
        self.combo_ps4 = QComboBox(self.groupBox_passive)
        self.combo_ps4.setObjectName(u"combo_ps4")
        self.combo_ps4.setGeometry(QRect(90, 180, 120, 32))
        self.combo_ps4.setFont(font3)
        self.combo_ps4.setStyleSheet(u"QComboBox{\n"
"	color: rgb(0 ,0, 0);\n"
"	background-color:  rgb(255 ,255, 255);\n"
"}")
        self.check_alt6 = QCheckBox(self.groupBox_passive)
        self.check_alt6.setObjectName(u"check_alt6")
        self.check_alt6.setGeometry(QRect(350, 180, 50, 32))
        self.check_alt6.setFont(font2)
        self.check_alt6.setStyleSheet(u"QCheckBox{\n"
"	color: rgb(0 ,0, 0);\n"
"}")
        self.check_alt6.setChecked(False)
        self.check_alt6.setTristate(False)
        self.label_img_name4 = QLabel(self.groupBox_passive)
        self.label_img_name4.setObjectName(u"label_img_name4")
        self.label_img_name4.setGeometry(QRect(10, 180, 70, 32))
        self.label_img_name4.setFont(font2)
        self.label_img_name4.setStyleSheet(u"QLabel{\n"
"	color: rgb(0 ,0, 0);\n"
"	background-color: transparent;\n"
"}")
        self.label_img_name4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.check_ctrl6 = QCheckBox(self.groupBox_passive)
        self.check_ctrl6.setObjectName(u"check_ctrl6")
        self.check_ctrl6.setGeometry(QRect(230, 180, 50, 32))
        self.check_ctrl6.setFont(font2)
        self.check_ctrl6.setStyleSheet(u"QCheckBox{\n"
"	color: rgb(0 ,0, 0);\n"
"}")
        self.check_ctrl6.setChecked(False)
        self.check_ctrl6.setTristate(False)
        self.label_img_name3 = QLabel(self.groupBox_passive)
        self.label_img_name3.setObjectName(u"label_img_name3")
        self.label_img_name3.setGeometry(QRect(10, 130, 70, 32))
        self.label_img_name3.setFont(font2)
        self.label_img_name3.setStyleSheet(u"QLabel{\n"
"	color: rgb(0 ,0, 0);\n"
"	background-color: transparent;\n"
"}")
        self.label_img_name3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.check_alt5 = QCheckBox(self.groupBox_passive)
        self.check_alt5.setObjectName(u"check_alt5")
        self.check_alt5.setGeometry(QRect(350, 130, 50, 32))
        self.check_alt5.setFont(font2)
        self.check_alt5.setStyleSheet(u"QCheckBox{\n"
"	color: rgb(0 ,0, 0);\n"
"}")
        self.check_alt5.setChecked(False)
        self.check_alt5.setTristate(False)
        self.check_ctrl5 = QCheckBox(self.groupBox_passive)
        self.check_ctrl5.setObjectName(u"check_ctrl5")
        self.check_ctrl5.setGeometry(QRect(230, 130, 50, 32))
        self.check_ctrl5.setFont(font2)
        self.check_ctrl5.setStyleSheet(u"QCheckBox{\n"
"	color: rgb(0 ,0, 0);\n"
"}")
        self.check_ctrl5.setIconSize(QSize(16, 16))
        self.check_ctrl5.setChecked(False)
        self.check_ctrl5.setTristate(False)
        self.check_shift5 = QCheckBox(self.groupBox_passive)
        self.check_shift5.setObjectName(u"check_shift5")
        self.check_shift5.setGeometry(QRect(290, 130, 55, 32))
        self.check_shift5.setFont(font2)
        self.check_shift5.setStyleSheet(u"QCheckBox{\n"
"	color: rgb(0 ,0, 0);\n"
"}")
        self.check_shift5.setChecked(False)
        self.check_shift5.setTristate(False)
        self.check_shift6 = QCheckBox(self.groupBox_passive)
        self.check_shift6.setObjectName(u"check_shift6")
        self.check_shift6.setGeometry(QRect(290, 180, 55, 32))
        self.check_shift6.setFont(font2)
        self.check_shift6.setStyleSheet(u"QCheckBox{\n"
"	color: rgb(0 ,0, 0);\n"
"}")
        self.check_shift6.setChecked(False)
        self.check_shift6.setTristate(False)
        self.check_ctrl7 = QCheckBox(self.groupBox_passive)
        self.check_ctrl7.setObjectName(u"check_ctrl7")
        self.check_ctrl7.setGeometry(QRect(230, 230, 50, 32))
        self.check_ctrl7.setFont(font2)
        self.check_ctrl7.setStyleSheet(u"QCheckBox{\n"
"	color: rgb(0 ,0, 0);\n"
"}")
        self.check_ctrl7.setChecked(False)
        self.check_ctrl7.setTristate(False)
        self.combo_ps5 = QComboBox(self.groupBox_passive)
        self.combo_ps5.setObjectName(u"combo_ps5")
        self.combo_ps5.setGeometry(QRect(90, 230, 120, 32))
        self.combo_ps5.setFont(font3)
        self.combo_ps5.setStyleSheet(u"QComboBox{\n"
"	color: rgb(0 ,0, 0);\n"
"	background-color:  rgb(255 ,255, 255);\n"
"}")
        self.check_shift7 = QCheckBox(self.groupBox_passive)
        self.check_shift7.setObjectName(u"check_shift7")
        self.check_shift7.setGeometry(QRect(290, 230, 55, 32))
        self.check_shift7.setFont(font2)
        self.check_shift7.setStyleSheet(u"QCheckBox{\n"
"	color: rgb(0 ,0, 0);\n"
"}")
        self.check_shift7.setChecked(False)
        self.check_shift7.setTristate(False)
        self.check_alt7 = QCheckBox(self.groupBox_passive)
        self.check_alt7.setObjectName(u"check_alt7")
        self.check_alt7.setGeometry(QRect(350, 230, 50, 32))
        self.check_alt7.setFont(font2)
        self.check_alt7.setStyleSheet(u"QCheckBox{\n"
"	color: rgb(0 ,0, 0);\n"
"}")
        self.check_alt7.setChecked(False)
        self.check_alt7.setTristate(False)
        self.label_img_name5 = QLabel(self.groupBox_passive)
        self.label_img_name5.setObjectName(u"label_img_name5")
        self.label_img_name5.setGeometry(QRect(10, 230, 70, 32))
        self.label_img_name5.setFont(font2)
        self.label_img_name5.setStyleSheet(u"QLabel{\n"
"	color: rgb(0 ,0, 0);\n"
"	background-color: transparent;\n"
"}")
        self.label_img_name5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.check_ctrl8 = QCheckBox(self.groupBox_passive)
        self.check_ctrl8.setObjectName(u"check_ctrl8")
        self.check_ctrl8.setGeometry(QRect(230, 280, 50, 32))
        self.check_ctrl8.setFont(font2)
        self.check_ctrl8.setStyleSheet(u"QCheckBox{\n"
"	color: rgb(0 ,0, 0);\n"
"}")
        self.check_ctrl8.setChecked(False)
        self.check_ctrl8.setTristate(False)
        self.combo_ps6 = QComboBox(self.groupBox_passive)
        self.combo_ps6.setObjectName(u"combo_ps6")
        self.combo_ps6.setGeometry(QRect(90, 280, 120, 32))
        self.combo_ps6.setFont(font3)
        self.combo_ps6.setStyleSheet(u"QComboBox{\n"
"	color: rgb(0 ,0, 0);\n"
"	background-color:  rgb(255 ,255, 255);\n"
"}")
        self.check_shift8 = QCheckBox(self.groupBox_passive)
        self.check_shift8.setObjectName(u"check_shift8")
        self.check_shift8.setGeometry(QRect(290, 280, 55, 32))
        self.check_shift8.setFont(font2)
        self.check_shift8.setStyleSheet(u"QCheckBox{\n"
"	color: rgb(0 ,0, 0);\n"
"}")
        self.check_shift8.setChecked(False)
        self.check_shift8.setTristate(False)
        self.check_alt8 = QCheckBox(self.groupBox_passive)
        self.check_alt8.setObjectName(u"check_alt8")
        self.check_alt8.setGeometry(QRect(350, 280, 50, 32))
        self.check_alt8.setFont(font2)
        self.check_alt8.setStyleSheet(u"QCheckBox{\n"
"	color: rgb(0 ,0, 0);\n"
"}")
        self.check_alt8.setChecked(False)
        self.check_alt8.setTristate(False)
        self.label_img_name6 = QLabel(self.groupBox_passive)
        self.label_img_name6.setObjectName(u"label_img_name6")
        self.label_img_name6.setGeometry(QRect(10, 280, 70, 32))
        self.label_img_name6.setFont(font2)
        self.label_img_name6.setStyleSheet(u"QLabel{\n"
"	color: rgb(0 ,0, 0);\n"
"	background-color: transparent;\n"
"}")
        self.label_img_name6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.retranslateUi(SettingsDialog)
        self.buttonBox.accepted.connect(SettingsDialog.accept)
        self.buttonBox.rejected.connect(SettingsDialog.reject)

        QMetaObject.connectSlotsByName(SettingsDialog)
    # setupUi

    def retranslateUi(self, SettingsDialog):
        SettingsDialog.setWindowTitle(QCoreApplication.translate("SettingsDialog", u"\uc124\uc815", None))
        self.groupBox_active.setTitle(QCoreApplication.translate("SettingsDialog", u" \uc790\ub3d9\ubaa8\ub4dc \uc2dc\uc791 / \uc911\uc9c0 \ud0a4 \uc124\uc815 ", None))
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
        self.groupBox_passive.setTitle(QCoreApplication.translate("SettingsDialog", u"\uc218\ub3d9\ubaa8\ub4dc \ud074\ub9ad \ud0a4 \uc124\uc815", None))
        self.check_shift3.setText(QCoreApplication.translate("SettingsDialog", u"Shift", None))
        self.combo_ps2.setCurrentText("")
        self.combo_ps2.setPlaceholderText(QCoreApplication.translate("SettingsDialog", u"\uc120\ud0dd\ud558\uc138\uc694", None))
        self.check_shift4.setText(QCoreApplication.translate("SettingsDialog", u"Shift", None))
        self.label_img_name1.setText(QCoreApplication.translate("SettingsDialog", u"\uc774\ubbf8\uc9c01", None))
        self.check_ctrl4.setText(QCoreApplication.translate("SettingsDialog", u"Ctrl", None))
        self.check_alt4.setText(QCoreApplication.translate("SettingsDialog", u"Alt", None))
        self.label_img_name2.setText(QCoreApplication.translate("SettingsDialog", u"\uc774\ubbf8\uc9c02", None))
        self.check_ctrl3.setText(QCoreApplication.translate("SettingsDialog", u"Ctrl", None))
        self.check_alt3.setText(QCoreApplication.translate("SettingsDialog", u"Alt", None))
        self.combo_ps1.setCurrentText("")
        self.combo_ps1.setPlaceholderText(QCoreApplication.translate("SettingsDialog", u"\uc120\ud0dd\ud558\uc138\uc694", None))
        self.combo_ps3.setCurrentText("")
        self.combo_ps3.setPlaceholderText(QCoreApplication.translate("SettingsDialog", u"\uc120\ud0dd\ud558\uc138\uc694", None))
        self.combo_ps4.setCurrentText("")
        self.combo_ps4.setPlaceholderText(QCoreApplication.translate("SettingsDialog", u"\uc120\ud0dd\ud558\uc138\uc694", None))
        self.check_alt6.setText(QCoreApplication.translate("SettingsDialog", u"Alt", None))
        self.label_img_name4.setText(QCoreApplication.translate("SettingsDialog", u"\uc774\ubbf8\uc9c04", None))
        self.check_ctrl6.setText(QCoreApplication.translate("SettingsDialog", u"Ctrl", None))
        self.label_img_name3.setText(QCoreApplication.translate("SettingsDialog", u"\uc774\ubbf8\uc9c03", None))
        self.check_alt5.setText(QCoreApplication.translate("SettingsDialog", u"Alt", None))
        self.check_ctrl5.setText(QCoreApplication.translate("SettingsDialog", u"Ctrl", None))
        self.check_shift5.setText(QCoreApplication.translate("SettingsDialog", u"Shift", None))
        self.check_shift6.setText(QCoreApplication.translate("SettingsDialog", u"Shift", None))
        self.check_ctrl7.setText(QCoreApplication.translate("SettingsDialog", u"Ctrl", None))
        self.combo_ps5.setCurrentText("")
        self.combo_ps5.setPlaceholderText(QCoreApplication.translate("SettingsDialog", u"\uc120\ud0dd\ud558\uc138\uc694", None))
        self.check_shift7.setText(QCoreApplication.translate("SettingsDialog", u"Shift", None))
        self.check_alt7.setText(QCoreApplication.translate("SettingsDialog", u"Alt", None))
        self.label_img_name5.setText(QCoreApplication.translate("SettingsDialog", u"\uc774\ubbf8\uc9c05", None))
        self.check_ctrl8.setText(QCoreApplication.translate("SettingsDialog", u"Ctrl", None))
        self.combo_ps6.setCurrentText("")
        self.combo_ps6.setPlaceholderText(QCoreApplication.translate("SettingsDialog", u"\uc120\ud0dd\ud558\uc138\uc694", None))
        self.check_shift8.setText(QCoreApplication.translate("SettingsDialog", u"Shift", None))
        self.check_alt8.setText(QCoreApplication.translate("SettingsDialog", u"Alt", None))
        self.label_img_name6.setText(QCoreApplication.translate("SettingsDialog", u"\uc774\ubbf8\uc9c06", None))
    # retranslateUi

