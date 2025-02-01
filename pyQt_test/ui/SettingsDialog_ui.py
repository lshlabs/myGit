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
    QDialog, QDialogButtonBox, QFrame, QGroupBox,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTabWidget, QTextEdit, QWidget)

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        if not SettingsDialog.objectName():
            SettingsDialog.setObjectName(u"SettingsDialog")
        SettingsDialog.setWindowModality(Qt.WindowModality.NonModal)
        SettingsDialog.resize(450, 580)
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
        self.buttonBox.setGeometry(QRect(10, 540, 430, 35))
        font1 = QFont()
        font1.setFamilies([u"NanumGothic"])
        font1.setPointSize(12)
        self.buttonBox.setFont(font1)
        self.buttonBox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.buttonBox.setAutoFillBackground(False)
        self.buttonBox.setStyleSheet(u"")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.tabWidget = QTabWidget(SettingsDialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 10, 430, 520))
        self.tabWidget.setStyleSheet(u"QTabWidget{\n"
"	background-color: #EAEFEF;\n"
"}")
        self.keyset_tab = QWidget()
        self.keyset_tab.setObjectName(u"keyset_tab")
        self.groupBox_active = QGroupBox(self.keyset_tab)
        self.groupBox_active.setObjectName(u"groupBox_active")
        self.groupBox_active.setGeometry(QRect(10, 10, 405, 130))
        self.groupBox_active.setFont(font1)
        self.check_shift1 = QCheckBox(self.groupBox_active)
        self.check_shift1.setObjectName(u"check_shift1")
        self.check_shift1.setGeometry(QRect(290, 30, 55, 32))
        font2 = QFont()
        font2.setFamilies([u"NanumGothic"])
        font2.setPointSize(10)
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
        self.groupBox_passive = QGroupBox(self.keyset_tab)
        self.groupBox_passive.setObjectName(u"groupBox_passive")
        self.groupBox_passive.setGeometry(QRect(10, 150, 405, 330))
        self.groupBox_passive.setFont(font1)
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
        self.label_img1 = QLabel(self.groupBox_passive)
        self.label_img1.setObjectName(u"label_img1")
        self.label_img1.setGeometry(QRect(10, 30, 70, 32))
        self.label_img1.setFont(font2)
        self.label_img1.setStyleSheet(u"QLabel{\n"
"	color: rgb(0 ,0, 0);\n"
"	background-color: transparent;\n"
"}")
        self.label_img1.setAlignment(Qt.AlignmentFlag.AlignCenter)
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
        self.label_img2 = QLabel(self.groupBox_passive)
        self.label_img2.setObjectName(u"label_img2")
        self.label_img2.setGeometry(QRect(10, 80, 70, 32))
        self.label_img2.setFont(font2)
        self.label_img2.setStyleSheet(u"QLabel{\n"
"	color: rgb(0 ,0, 0);\n"
"	background-color: transparent;\n"
"}")
        self.label_img2.setAlignment(Qt.AlignmentFlag.AlignCenter)
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
        self.label_img4 = QLabel(self.groupBox_passive)
        self.label_img4.setObjectName(u"label_img4")
        self.label_img4.setGeometry(QRect(10, 180, 70, 32))
        self.label_img4.setFont(font2)
        self.label_img4.setStyleSheet(u"QLabel{\n"
"	color: rgb(0 ,0, 0);\n"
"	background-color: transparent;\n"
"}")
        self.label_img4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.check_ctrl6 = QCheckBox(self.groupBox_passive)
        self.check_ctrl6.setObjectName(u"check_ctrl6")
        self.check_ctrl6.setGeometry(QRect(230, 180, 50, 32))
        self.check_ctrl6.setFont(font2)
        self.check_ctrl6.setStyleSheet(u"QCheckBox{\n"
"	color: rgb(0 ,0, 0);\n"
"}")
        self.check_ctrl6.setChecked(False)
        self.check_ctrl6.setTristate(False)
        self.label_img3 = QLabel(self.groupBox_passive)
        self.label_img3.setObjectName(u"label_img3")
        self.label_img3.setGeometry(QRect(10, 130, 70, 32))
        self.label_img3.setFont(font2)
        self.label_img3.setStyleSheet(u"QLabel{\n"
"	color: rgb(0 ,0, 0);\n"
"	background-color: transparent;\n"
"}")
        self.label_img3.setAlignment(Qt.AlignmentFlag.AlignCenter)
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
        self.label_img5 = QLabel(self.groupBox_passive)
        self.label_img5.setObjectName(u"label_img5")
        self.label_img5.setGeometry(QRect(10, 230, 70, 32))
        self.label_img5.setFont(font2)
        self.label_img5.setStyleSheet(u"QLabel{\n"
"	color: rgb(0 ,0, 0);\n"
"	background-color: transparent;\n"
"}")
        self.label_img5.setAlignment(Qt.AlignmentFlag.AlignCenter)
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
        self.label_img6 = QLabel(self.groupBox_passive)
        self.label_img6.setObjectName(u"label_img6")
        self.label_img6.setGeometry(QRect(10, 280, 70, 32))
        self.label_img6.setFont(font2)
        self.label_img6.setStyleSheet(u"QLabel{\n"
"	color: rgb(0 ,0, 0);\n"
"	background-color: transparent;\n"
"}")
        self.label_img6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tabWidget.addTab(self.keyset_tab, "")
        self.passiveset_tab = QWidget()
        self.passiveset_tab.setObjectName(u"passiveset_tab")
        self.groupBox_coordinate = QGroupBox(self.passiveset_tab)
        self.groupBox_coordinate.setObjectName(u"groupBox_coordinate")
        self.groupBox_coordinate.setGeometry(QRect(10, 10, 405, 410))
        self.groupBox_coordinate.setFont(font1)
        self.textEdit_X1 = QTextEdit(self.groupBox_coordinate)
        self.textEdit_X1.setObjectName(u"textEdit_X1")
        self.textEdit_X1.setGeometry(QRect(140, 100, 60, 20))
        font4 = QFont()
        font4.setFamilies([u"Nanum Gothic"])
        font4.setPointSize(10)
        self.textEdit_X1.setFont(font4)
        self.textEdit_X1.setAutoFillBackground(False)
        self.textEdit_X1.setStyleSheet(u"background:white;\n"
"border: 1px solid black;")
        self.textEdit_X1.setFrameShape(QFrame.Shape.Box)
        self.textEdit_X1.setFrameShadow(QFrame.Shadow.Plain)
        self.textEdit_X1.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textEdit_X1.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.label_Y1 = QLabel(self.groupBox_coordinate)
        self.label_Y1.setObjectName(u"label_Y1")
        self.label_Y1.setGeometry(QRect(210, 100, 20, 20))
        self.label_Y1.setFont(font2)
        self.label_Y1.setStyleSheet(u"QLabel{\n"
"	color: rgb(0 ,0, 0);\n"
"	background-color: transparent;\n"
"}")
        self.textEdit_Y1 = QTextEdit(self.groupBox_coordinate)
        self.textEdit_Y1.setObjectName(u"textEdit_Y1")
        self.textEdit_Y1.setGeometry(QRect(230, 100, 60, 20))
        self.textEdit_Y1.setFont(font4)
        self.textEdit_Y1.setAutoFillBackground(False)
        self.textEdit_Y1.setStyleSheet(u"background:white;\n"
"border: 1px solid black;")
        self.textEdit_Y1.setFrameShape(QFrame.Shape.Box)
        self.textEdit_Y1.setFrameShadow(QFrame.Shadow.Plain)
        self.textEdit_Y1.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textEdit_Y1.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.label_X1 = QLabel(self.groupBox_coordinate)
        self.label_X1.setObjectName(u"label_X1")
        self.label_X1.setGeometry(QRect(120, 100, 20, 20))
        self.label_X1.setFont(font2)
        self.label_X1.setStyleSheet(u"QLabel{\n"
"	color: rgb(0 ,0, 0);\n"
"	background-color: transparent;\n"
"}")
        self.button_record1 = QPushButton(self.groupBox_coordinate)
        self.button_record1.setObjectName(u"button_record1")
        self.button_record1.setGeometry(QRect(310, 95, 70, 30))
        self.button_record1.setFont(font2)
        self.button_record1.setStyleSheet(u"")
        self.button_record1.setAutoDefault(False)
        self.button_record1.setFlat(False)
        self.button_record2 = QPushButton(self.groupBox_coordinate)
        self.button_record2.setObjectName(u"button_record2")
        self.button_record2.setGeometry(QRect(310, 145, 70, 30))
        self.button_record2.setFont(font2)
        self.button_record2.setStyleSheet(u"")
        self.button_record2.setAutoDefault(False)
        self.button_record2.setFlat(False)
        self.textEdit_Y2 = QTextEdit(self.groupBox_coordinate)
        self.textEdit_Y2.setObjectName(u"textEdit_Y2")
        self.textEdit_Y2.setGeometry(QRect(230, 150, 60, 20))
        self.textEdit_Y2.setFont(font4)
        self.textEdit_Y2.setAutoFillBackground(False)
        self.textEdit_Y2.setStyleSheet(u"background:white;\n"
"border: 1px solid black;")
        self.textEdit_Y2.setFrameShape(QFrame.Shape.Box)
        self.textEdit_Y2.setFrameShadow(QFrame.Shadow.Plain)
        self.textEdit_Y2.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textEdit_Y2.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.label_Y2 = QLabel(self.groupBox_coordinate)
        self.label_Y2.setObjectName(u"label_Y2")
        self.label_Y2.setGeometry(QRect(210, 150, 20, 20))
        self.label_Y2.setFont(font2)
        self.label_Y2.setStyleSheet(u"QLabel{\n"
"	color: rgb(0 ,0, 0);\n"
"	background-color: transparent;\n"
"}")
        self.textEdit_X2 = QTextEdit(self.groupBox_coordinate)
        self.textEdit_X2.setObjectName(u"textEdit_X2")
        self.textEdit_X2.setGeometry(QRect(140, 150, 60, 20))
        self.textEdit_X2.setFont(font4)
        self.textEdit_X2.setAutoFillBackground(False)
        self.textEdit_X2.setStyleSheet(u"background:white;\n"
"border: 1px solid black;")
        self.textEdit_X2.setFrameShape(QFrame.Shape.Box)
        self.textEdit_X2.setFrameShadow(QFrame.Shadow.Plain)
        self.textEdit_X2.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textEdit_X2.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.label_X2 = QLabel(self.groupBox_coordinate)
        self.label_X2.setObjectName(u"label_X2")
        self.label_X2.setGeometry(QRect(120, 150, 20, 20))
        self.label_X2.setFont(font2)
        self.label_X2.setStyleSheet(u"QLabel{\n"
"	color: rgb(0 ,0, 0);\n"
"	background-color: transparent;\n"
"}")
        self.textEdit_Y3 = QTextEdit(self.groupBox_coordinate)
        self.textEdit_Y3.setObjectName(u"textEdit_Y3")
        self.textEdit_Y3.setGeometry(QRect(230, 200, 60, 20))
        self.textEdit_Y3.setFont(font4)
        self.textEdit_Y3.setAutoFillBackground(False)
        self.textEdit_Y3.setStyleSheet(u"background:white;\n"
"border: 1px solid black;")
        self.textEdit_Y3.setFrameShape(QFrame.Shape.Box)
        self.textEdit_Y3.setFrameShadow(QFrame.Shadow.Plain)
        self.textEdit_Y3.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textEdit_Y3.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.label_Y3 = QLabel(self.groupBox_coordinate)
        self.label_Y3.setObjectName(u"label_Y3")
        self.label_Y3.setGeometry(QRect(210, 200, 20, 20))
        self.label_Y3.setFont(font2)
        self.label_Y3.setStyleSheet(u"QLabel{\n"
"	color: rgb(0 ,0, 0);\n"
"	background-color: transparent;\n"
"}")
        self.label_X3 = QLabel(self.groupBox_coordinate)
        self.label_X3.setObjectName(u"label_X3")
        self.label_X3.setGeometry(QRect(120, 200, 20, 20))
        self.label_X3.setFont(font2)
        self.label_X3.setStyleSheet(u"QLabel{\n"
"	color: rgb(0 ,0, 0);\n"
"	background-color: transparent;\n"
"}")
        self.button_record3 = QPushButton(self.groupBox_coordinate)
        self.button_record3.setObjectName(u"button_record3")
        self.button_record3.setGeometry(QRect(310, 195, 70, 30))
        self.button_record3.setFont(font2)
        self.button_record3.setStyleSheet(u"")
        self.button_record3.setAutoDefault(False)
        self.button_record3.setFlat(False)
        self.textEdit_X3 = QTextEdit(self.groupBox_coordinate)
        self.textEdit_X3.setObjectName(u"textEdit_X3")
        self.textEdit_X3.setGeometry(QRect(140, 200, 60, 20))
        self.textEdit_X3.setFont(font4)
        self.textEdit_X3.setAutoFillBackground(False)
        self.textEdit_X3.setStyleSheet(u"background:white;\n"
"border: 1px solid black;")
        self.textEdit_X3.setFrameShape(QFrame.Shape.Box)
        self.textEdit_X3.setFrameShadow(QFrame.Shadow.Plain)
        self.textEdit_X3.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textEdit_X3.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.button_record4 = QPushButton(self.groupBox_coordinate)
        self.button_record4.setObjectName(u"button_record4")
        self.button_record4.setGeometry(QRect(310, 245, 70, 30))
        self.button_record4.setFont(font2)
        self.button_record4.setStyleSheet(u"")
        self.button_record4.setAutoDefault(False)
        self.button_record4.setFlat(False)
        self.textEdit_Y4 = QTextEdit(self.groupBox_coordinate)
        self.textEdit_Y4.setObjectName(u"textEdit_Y4")
        self.textEdit_Y4.setGeometry(QRect(230, 250, 60, 20))
        self.textEdit_Y4.setFont(font4)
        self.textEdit_Y4.setAutoFillBackground(False)
        self.textEdit_Y4.setStyleSheet(u"background:white;\n"
"border: 1px solid black;")
        self.textEdit_Y4.setFrameShape(QFrame.Shape.Box)
        self.textEdit_Y4.setFrameShadow(QFrame.Shadow.Plain)
        self.textEdit_Y4.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textEdit_Y4.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.label_Y4 = QLabel(self.groupBox_coordinate)
        self.label_Y4.setObjectName(u"label_Y4")
        self.label_Y4.setGeometry(QRect(210, 250, 20, 20))
        self.label_Y4.setFont(font2)
        self.label_Y4.setStyleSheet(u"QLabel{\n"
"	color: rgb(0 ,0, 0);\n"
"	background-color: transparent;\n"
"}")
        self.textEdit_Y5 = QTextEdit(self.groupBox_coordinate)
        self.textEdit_Y5.setObjectName(u"textEdit_Y5")
        self.textEdit_Y5.setGeometry(QRect(230, 300, 60, 20))
        self.textEdit_Y5.setFont(font4)
        self.textEdit_Y5.setAutoFillBackground(False)
        self.textEdit_Y5.setStyleSheet(u"background:white;\n"
"border: 1px solid black;")
        self.textEdit_Y5.setFrameShape(QFrame.Shape.Box)
        self.textEdit_Y5.setFrameShadow(QFrame.Shadow.Plain)
        self.textEdit_Y5.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textEdit_Y5.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.label_Y5 = QLabel(self.groupBox_coordinate)
        self.label_Y5.setObjectName(u"label_Y5")
        self.label_Y5.setGeometry(QRect(210, 300, 20, 20))
        self.label_Y5.setFont(font2)
        self.label_Y5.setStyleSheet(u"QLabel{\n"
"	color: rgb(0 ,0, 0);\n"
"	background-color: transparent;\n"
"}")
        self.label_X5 = QLabel(self.groupBox_coordinate)
        self.label_X5.setObjectName(u"label_X5")
        self.label_X5.setGeometry(QRect(120, 300, 20, 20))
        self.label_X5.setFont(font2)
        self.label_X5.setStyleSheet(u"QLabel{\n"
"	color: rgb(0 ,0, 0);\n"
"	background-color: transparent;\n"
"}")
        self.button_record5 = QPushButton(self.groupBox_coordinate)
        self.button_record5.setObjectName(u"button_record5")
        self.button_record5.setGeometry(QRect(310, 295, 70, 30))
        self.button_record5.setFont(font2)
        self.button_record5.setStyleSheet(u"")
        self.button_record5.setAutoDefault(False)
        self.button_record5.setFlat(False)
        self.button_record6 = QPushButton(self.groupBox_coordinate)
        self.button_record6.setObjectName(u"button_record6")
        self.button_record6.setGeometry(QRect(310, 345, 70, 30))
        self.button_record6.setFont(font2)
        self.button_record6.setStyleSheet(u"")
        self.button_record6.setAutoDefault(False)
        self.button_record6.setFlat(False)
        self.textEdit_X5 = QTextEdit(self.groupBox_coordinate)
        self.textEdit_X5.setObjectName(u"textEdit_X5")
        self.textEdit_X5.setGeometry(QRect(140, 300, 60, 20))
        self.textEdit_X5.setFont(font4)
        self.textEdit_X5.setAutoFillBackground(False)
        self.textEdit_X5.setStyleSheet(u"background:white;\n"
"border: 1px solid black;")
        self.textEdit_X5.setFrameShape(QFrame.Shape.Box)
        self.textEdit_X5.setFrameShadow(QFrame.Shadow.Plain)
        self.textEdit_X5.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textEdit_X5.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.label_Y6 = QLabel(self.groupBox_coordinate)
        self.label_Y6.setObjectName(u"label_Y6")
        self.label_Y6.setGeometry(QRect(210, 350, 20, 20))
        self.label_Y6.setFont(font2)
        self.label_Y6.setStyleSheet(u"QLabel{\n"
"	color: rgb(0 ,0, 0);\n"
"	background-color: transparent;\n"
"}")
        self.textEdit_X6 = QTextEdit(self.groupBox_coordinate)
        self.textEdit_X6.setObjectName(u"textEdit_X6")
        self.textEdit_X6.setGeometry(QRect(140, 350, 60, 20))
        self.textEdit_X6.setFont(font4)
        self.textEdit_X6.setAutoFillBackground(False)
        self.textEdit_X6.setStyleSheet(u"background:white;\n"
"border: 1px solid black;")
        self.textEdit_X6.setFrameShape(QFrame.Shape.Box)
        self.textEdit_X6.setFrameShadow(QFrame.Shadow.Plain)
        self.textEdit_X6.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textEdit_X6.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textEdit_X4 = QTextEdit(self.groupBox_coordinate)
        self.textEdit_X4.setObjectName(u"textEdit_X4")
        self.textEdit_X4.setGeometry(QRect(140, 250, 60, 20))
        self.textEdit_X4.setFont(font4)
        self.textEdit_X4.setAutoFillBackground(False)
        self.textEdit_X4.setStyleSheet(u"background:white;\n"
"border: 1px solid black;")
        self.textEdit_X4.setFrameShape(QFrame.Shape.Box)
        self.textEdit_X4.setFrameShadow(QFrame.Shadow.Plain)
        self.textEdit_X4.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textEdit_X4.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.label_X4 = QLabel(self.groupBox_coordinate)
        self.label_X4.setObjectName(u"label_X4")
        self.label_X4.setGeometry(QRect(120, 250, 20, 20))
        self.label_X4.setFont(font2)
        self.label_X4.setStyleSheet(u"QLabel{\n"
"	color: rgb(0 ,0, 0);\n"
"	background-color: transparent;\n"
"}")
        self.textEdit_Y6 = QTextEdit(self.groupBox_coordinate)
        self.textEdit_Y6.setObjectName(u"textEdit_Y6")
        self.textEdit_Y6.setGeometry(QRect(230, 350, 60, 20))
        self.textEdit_Y6.setFont(font4)
        self.textEdit_Y6.setAutoFillBackground(False)
        self.textEdit_Y6.setStyleSheet(u"background:white;\n"
"border: 1px solid black;")
        self.textEdit_Y6.setFrameShape(QFrame.Shape.Box)
        self.textEdit_Y6.setFrameShadow(QFrame.Shadow.Plain)
        self.textEdit_Y6.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textEdit_Y6.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.label_X6 = QLabel(self.groupBox_coordinate)
        self.label_X6.setObjectName(u"label_X6")
        self.label_X6.setGeometry(QRect(120, 350, 20, 20))
        self.label_X6.setFont(font2)
        self.label_X6.setStyleSheet(u"QLabel{\n"
"	color: rgb(0 ,0, 0);\n"
"	background-color: transparent;\n"
"}")
        self.label_1 = QLabel(self.groupBox_coordinate)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setGeometry(QRect(20, 35, 250, 20))
        font5 = QFont()
        font5.setFamilies([u"NanumGothic"])
        font5.setPointSize(10)
        font5.setItalic(False)
        font5.setUnderline(False)
        self.label_1.setFont(font5)
        self.label_1.setStyleSheet(u"QLabel{\n"
"	color: rgb(0 ,0, 0);\n"
"	background-color: transparent;\n"
"}")
        self.label_1.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_2 = QLabel(self.groupBox_coordinate)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 60, 320, 20))
        self.label_2.setFont(font5)
        self.label_2.setStyleSheet(u"QLabel{\n"
"	color: rgb(0 ,0, 0);\n"
"	background-color: transparent;\n"
"}")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.LineEdit_img_name1 = QLineEdit(self.groupBox_coordinate)
        self.LineEdit_img_name1.setObjectName(u"LineEdit_img_name1")
        self.LineEdit_img_name1.setGeometry(QRect(30, 100, 70, 20))
        self.LineEdit_img_name1.setFont(font4)
        self.LineEdit_img_name1.setStyleSheet(u"background:white;\n"
"border: 1px solid black;")
        self.LineEdit_img_name1.setMaxLength(32767)
        self.LineEdit_img_name2 = QLineEdit(self.groupBox_coordinate)
        self.LineEdit_img_name2.setObjectName(u"LineEdit_img_name2")
        self.LineEdit_img_name2.setGeometry(QRect(30, 150, 70, 20))
        self.LineEdit_img_name2.setFont(font4)
        self.LineEdit_img_name2.setStyleSheet(u"background:white;\n"
"border: 1px solid black;")
        self.LineEdit_img_name2.setMaxLength(32767)
        self.LineEdit_img_name2.setClearButtonEnabled(False)
        self.LineEdit_img_name3 = QLineEdit(self.groupBox_coordinate)
        self.LineEdit_img_name3.setObjectName(u"LineEdit_img_name3")
        self.LineEdit_img_name3.setGeometry(QRect(30, 200, 70, 20))
        self.LineEdit_img_name3.setFont(font4)
        self.LineEdit_img_name3.setStyleSheet(u"background:white;\n"
"border: 1px solid black;")
        self.LineEdit_img_name3.setMaxLength(32767)
        self.LineEdit_img_name4 = QLineEdit(self.groupBox_coordinate)
        self.LineEdit_img_name4.setObjectName(u"LineEdit_img_name4")
        self.LineEdit_img_name4.setGeometry(QRect(30, 250, 70, 20))
        self.LineEdit_img_name4.setFont(font4)
        self.LineEdit_img_name4.setStyleSheet(u"background:white;\n"
"border: 1px solid black;")
        self.LineEdit_img_name4.setMaxLength(32767)
        self.LineEdit_img_name5 = QLineEdit(self.groupBox_coordinate)
        self.LineEdit_img_name5.setObjectName(u"LineEdit_img_name5")
        self.LineEdit_img_name5.setGeometry(QRect(30, 300, 70, 20))
        self.LineEdit_img_name5.setFont(font4)
        self.LineEdit_img_name5.setStyleSheet(u"background:white;\n"
"border: 1px solid black;")
        self.LineEdit_img_name5.setMaxLength(32767)
        self.LineEdit_img_name6 = QLineEdit(self.groupBox_coordinate)
        self.LineEdit_img_name6.setObjectName(u"LineEdit_img_name6")
        self.LineEdit_img_name6.setGeometry(QRect(30, 350, 70, 20))
        self.LineEdit_img_name6.setFont(font4)
        self.LineEdit_img_name6.setStyleSheet(u"background:white;\n"
"border: 1px solid black;")
        self.LineEdit_img_name6.setMaxLength(32767)
        self.tabWidget.addTab(self.passiveset_tab, "")

        self.retranslateUi(SettingsDialog)
        self.buttonBox.accepted.connect(SettingsDialog.accept)
        self.buttonBox.rejected.connect(SettingsDialog.reject)

        self.tabWidget.setCurrentIndex(1)
        self.button_record1.setDefault(False)
        self.button_record2.setDefault(False)
        self.button_record3.setDefault(False)
        self.button_record4.setDefault(False)
        self.button_record5.setDefault(False)
        self.button_record6.setDefault(False)


        QMetaObject.connectSlotsByName(SettingsDialog)
    # setupUi

    def retranslateUi(self, SettingsDialog):
        SettingsDialog.setWindowTitle(QCoreApplication.translate("SettingsDialog", u"\uc124\uc815", None))
        self.groupBox_active.setTitle(QCoreApplication.translate("SettingsDialog", u" \uc790\ub3d9\ubaa8\ub4dc \uc2dc\uc791 / \uc885\ub8cc \ud0a4 \uc124\uc815 ", None))
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
        self.groupBox_passive.setTitle(QCoreApplication.translate("SettingsDialog", u"\uc218\ub3d9\ubaa8\ub4dc \ub3d9\uc791 \ud0a4 \uc124\uc815", None))
        self.check_shift3.setText(QCoreApplication.translate("SettingsDialog", u"Shift", None))
        self.combo_ps2.setCurrentText("")
        self.combo_ps2.setPlaceholderText(QCoreApplication.translate("SettingsDialog", u"\uc120\ud0dd\ud558\uc138\uc694", None))
        self.check_shift4.setText(QCoreApplication.translate("SettingsDialog", u"Shift", None))
        self.label_img1.setText(QCoreApplication.translate("SettingsDialog", u"\uc774\ubbf8\uc9c01", None))
        self.check_ctrl4.setText(QCoreApplication.translate("SettingsDialog", u"Ctrl", None))
        self.check_alt4.setText(QCoreApplication.translate("SettingsDialog", u"Alt", None))
        self.label_img2.setText(QCoreApplication.translate("SettingsDialog", u"\uc774\ubbf8\uc9c02", None))
        self.check_ctrl3.setText(QCoreApplication.translate("SettingsDialog", u"Ctrl", None))
        self.check_alt3.setText(QCoreApplication.translate("SettingsDialog", u"Alt", None))
        self.combo_ps1.setCurrentText("")
        self.combo_ps1.setPlaceholderText(QCoreApplication.translate("SettingsDialog", u"\uc120\ud0dd\ud558\uc138\uc694", None))
        self.combo_ps3.setCurrentText("")
        self.combo_ps3.setPlaceholderText(QCoreApplication.translate("SettingsDialog", u"\uc120\ud0dd\ud558\uc138\uc694", None))
        self.combo_ps4.setCurrentText("")
        self.combo_ps4.setPlaceholderText(QCoreApplication.translate("SettingsDialog", u"\uc120\ud0dd\ud558\uc138\uc694", None))
        self.check_alt6.setText(QCoreApplication.translate("SettingsDialog", u"Alt", None))
        self.label_img4.setText(QCoreApplication.translate("SettingsDialog", u"\uc774\ubbf8\uc9c04", None))
        self.check_ctrl6.setText(QCoreApplication.translate("SettingsDialog", u"Ctrl", None))
        self.label_img3.setText(QCoreApplication.translate("SettingsDialog", u"\uc774\ubbf8\uc9c03", None))
        self.check_alt5.setText(QCoreApplication.translate("SettingsDialog", u"Alt", None))
        self.check_ctrl5.setText(QCoreApplication.translate("SettingsDialog", u"Ctrl", None))
        self.check_shift5.setText(QCoreApplication.translate("SettingsDialog", u"Shift", None))
        self.check_shift6.setText(QCoreApplication.translate("SettingsDialog", u"Shift", None))
        self.check_ctrl7.setText(QCoreApplication.translate("SettingsDialog", u"Ctrl", None))
        self.combo_ps5.setCurrentText("")
        self.combo_ps5.setPlaceholderText(QCoreApplication.translate("SettingsDialog", u"\uc120\ud0dd\ud558\uc138\uc694", None))
        self.check_shift7.setText(QCoreApplication.translate("SettingsDialog", u"Shift", None))
        self.check_alt7.setText(QCoreApplication.translate("SettingsDialog", u"Alt", None))
        self.label_img5.setText(QCoreApplication.translate("SettingsDialog", u"\uc774\ubbf8\uc9c05", None))
        self.check_ctrl8.setText(QCoreApplication.translate("SettingsDialog", u"Ctrl", None))
        self.combo_ps6.setCurrentText("")
        self.combo_ps6.setPlaceholderText(QCoreApplication.translate("SettingsDialog", u"\uc120\ud0dd\ud558\uc138\uc694", None))
        self.check_shift8.setText(QCoreApplication.translate("SettingsDialog", u"Shift", None))
        self.check_alt8.setText(QCoreApplication.translate("SettingsDialog", u"Alt", None))
        self.label_img6.setText(QCoreApplication.translate("SettingsDialog", u"\uc774\ubbf8\uc9c06", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.keyset_tab), QCoreApplication.translate("SettingsDialog", u"\ud0a4 \uc124\uc815", None))
        self.groupBox_coordinate.setTitle(QCoreApplication.translate("SettingsDialog", u"\uc88c\ud45c \uc124\uc815", None))
        self.label_Y1.setText(QCoreApplication.translate("SettingsDialog", u"Y :", None))
        self.label_X1.setText(QCoreApplication.translate("SettingsDialog", u"X :", None))
        self.button_record1.setText(QCoreApplication.translate("SettingsDialog", u"\uae30\ub85d \uc2dc\uc791", None))
        self.button_record2.setText(QCoreApplication.translate("SettingsDialog", u"\uae30\ub85d \uc2dc\uc791", None))
        self.label_Y2.setText(QCoreApplication.translate("SettingsDialog", u"Y :", None))
        self.label_X2.setText(QCoreApplication.translate("SettingsDialog", u"X :", None))
        self.label_Y3.setText(QCoreApplication.translate("SettingsDialog", u"Y :", None))
        self.label_X3.setText(QCoreApplication.translate("SettingsDialog", u"X :", None))
        self.button_record3.setText(QCoreApplication.translate("SettingsDialog", u"\uae30\ub85d \uc2dc\uc791", None))
        self.button_record4.setText(QCoreApplication.translate("SettingsDialog", u"\uae30\ub85d \uc2dc\uc791", None))
        self.label_Y4.setText(QCoreApplication.translate("SettingsDialog", u"Y :", None))
        self.label_Y5.setText(QCoreApplication.translate("SettingsDialog", u"Y :", None))
        self.label_X5.setText(QCoreApplication.translate("SettingsDialog", u"X :", None))
        self.button_record5.setText(QCoreApplication.translate("SettingsDialog", u"\uae30\ub85d \uc2dc\uc791", None))
        self.button_record6.setText(QCoreApplication.translate("SettingsDialog", u"\uae30\ub85d \uc2dc\uc791", None))
        self.label_Y6.setText(QCoreApplication.translate("SettingsDialog", u"Y :", None))
        self.label_X4.setText(QCoreApplication.translate("SettingsDialog", u"X :", None))
        self.label_X6.setText(QCoreApplication.translate("SettingsDialog", u"X :", None))
        self.label_1.setText(QCoreApplication.translate("SettingsDialog", u"\uc218\ub3d9\ubaa8\ub4dc\uc5d0\uc11c \ud074\ub9ad\ud560 \uc88c\ud45c\ub97c \uc124\uc815\ud558\uc138\uc694", None))
        self.label_2.setText(QCoreApplication.translate("SettingsDialog", u"\uae30\ub85d \uc2dc\uc791 \ubc84\ud2bc\uc744 \ub204\ub978 \ud6c4 F10\uc744 \ub204\ub974\uba74 \uc88c\ud45c\ub97c \uc800\uc7a5\ud569\ub2c8\ub2e4", None))
        self.LineEdit_img_name1.setInputMask("")
        self.LineEdit_img_name1.setPlaceholderText("")
        self.LineEdit_img_name2.setInputMask("")
        self.LineEdit_img_name2.setPlaceholderText("")
        self.LineEdit_img_name3.setInputMask("")
        self.LineEdit_img_name3.setPlaceholderText("")
        self.LineEdit_img_name4.setInputMask("")
        self.LineEdit_img_name4.setPlaceholderText("")
        self.LineEdit_img_name5.setInputMask("")
        self.LineEdit_img_name5.setPlaceholderText("")
        self.LineEdit_img_name6.setInputMask("")
        self.LineEdit_img_name6.setPlaceholderText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.passiveset_tab), QCoreApplication.translate("SettingsDialog", u"\uc218\ub3d9\ubaa8\ub4dc", None))
    # retranslateUi

