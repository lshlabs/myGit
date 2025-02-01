# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ActionsettingWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QFrame, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_ActionSettingWindow(object):
    def setupUi(self, ActionSettingWindow):
        if not ActionSettingWindow.objectName():
            ActionSettingWindow.setObjectName(u"ActionSettingWindow")
        ActionSettingWindow.resize(360, 320)
        font = QFont()
        font.setFamilies([u"Nanum Gothic"])
        ActionSettingWindow.setFont(font)
        ActionSettingWindow.setStyleSheet(u"background-color: #EAEFEF;\n"
"")
        ActionSettingWindow.setSizeGripEnabled(False)
        ActionSettingWindow.setModal(True)
        self.frame_main = QFrame(ActionSettingWindow)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setGeometry(QRect(10, 10, 340, 300))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        self.frame_main.setFont(font1)
        self.frame_main.setStyleSheet(u"background: white;\n"
"border:1px solid black;\n"
"border-radius: 5px;\n"
"")
        self.frame_main.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_main.setFrameShadow(QFrame.Shadow.Raised)
        self.button_save = QPushButton(self.frame_main)
        self.button_save.setObjectName(u"button_save")
        self.button_save.setGeometry(QRect(160, 260, 80, 30))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_save.sizePolicy().hasHeightForWidth())
        self.button_save.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setHintingPreference(QFont.PreferVerticalHinting)
        self.button_save.setFont(font2)
        self.button_save.setAutoFillBackground(False)
        self.button_save.setStyleSheet(u"QPushButton {\n"
"    border-radius: 5px;\n"
"	color:black;\n"
"    border: 1px solid #8f8f91;\n"
"    background-color: #f0f0f0;\n"
"    padding: 2px 4px;\n"
"}")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.InsertText))
        self.button_save.setIcon(icon)
        self.button_save.setAutoExclusive(False)
        self.button_save.setFlat(False)
        self.button_cancel = QPushButton(self.frame_main)
        self.button_cancel.setObjectName(u"button_cancel")
        self.button_cancel.setGeometry(QRect(250, 260, 80, 30))
        sizePolicy.setHeightForWidth(self.button_cancel.sizePolicy().hasHeightForWidth())
        self.button_cancel.setSizePolicy(sizePolicy)
        self.button_cancel.setFont(font2)
        self.button_cancel.setAutoFillBackground(False)
        self.button_cancel.setStyleSheet(u"QPushButton {\n"
"    border-radius: 5px;\n"
"	color:black;\n"
"    border: 1px solid #8f8f91;\n"
"    background-color: #f0f0f0;\n"
"    padding: 2px 4px;\n"
"}")
        self.button_cancel.setIcon(icon)
        self.button_cancel.setAutoExclusive(False)
        self.button_cancel.setFlat(False)
        self.label_tip = QLabel(self.frame_main)
        self.label_tip.setObjectName(u"label_tip")
        self.label_tip.setGeometry(QRect(20, 20, 300, 20))
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(9)
        self.label_tip.setFont(font3)
        self.label_tip.setStyleSheet(u"border:none;\n"
"color:black;")
        self.label_tip.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.comboBox_run = QComboBox(self.frame_main)
        self.comboBox_run.setObjectName(u"comboBox_run")
        self.comboBox_run.setGeometry(QRect(30, 100, 110, 25))
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(10)
        self.comboBox_run.setFont(font4)
        self.comboBox_run.setStyleSheet(u"")
        self.comboBox_stop = QComboBox(self.frame_main)
        self.comboBox_stop.setObjectName(u"comboBox_stop")
        self.comboBox_stop.setGeometry(QRect(30, 190, 110, 25))
        self.comboBox_stop.setFont(font4)
        self.comboBox_stop.setStyleSheet(u"")
        self.checkBox_ctrl1 = QCheckBox(self.frame_main)
        self.checkBox_ctrl1.setObjectName(u"checkBox_ctrl1")
        self.checkBox_ctrl1.setGeometry(QRect(160, 100, 50, 25))
        self.checkBox_ctrl1.setStyleSheet(u"border: none;")
        self.checkBox_ctrl2 = QCheckBox(self.frame_main)
        self.checkBox_ctrl2.setObjectName(u"checkBox_ctrl2")
        self.checkBox_ctrl2.setGeometry(QRect(160, 190, 50, 25))
        self.checkBox_ctrl2.setStyleSheet(u"border: none;")
        self.checkBox_shift2 = QCheckBox(self.frame_main)
        self.checkBox_shift2.setObjectName(u"checkBox_shift2")
        self.checkBox_shift2.setGeometry(QRect(260, 190, 50, 25))
        self.checkBox_shift2.setStyleSheet(u"border: none;")
        self.checkBox_shift1 = QCheckBox(self.frame_main)
        self.checkBox_shift1.setObjectName(u"checkBox_shift1")
        self.checkBox_shift1.setGeometry(QRect(260, 100, 50, 25))
        self.checkBox_shift1.setStyleSheet(u"border: none;")
        self.checkBox_alt1 = QCheckBox(self.frame_main)
        self.checkBox_alt1.setObjectName(u"checkBox_alt1")
        self.checkBox_alt1.setGeometry(QRect(210, 100, 50, 25))
        self.checkBox_alt1.setStyleSheet(u"border: none;")
        self.checkBox_alt2 = QCheckBox(self.frame_main)
        self.checkBox_alt2.setObjectName(u"checkBox_alt2")
        self.checkBox_alt2.setGeometry(QRect(210, 190, 50, 25))
        self.checkBox_alt2.setStyleSheet(u"border: none;")
        self.label_run = QLabel(self.frame_main)
        self.label_run.setObjectName(u"label_run")
        self.label_run.setGeometry(QRect(30, 70, 100, 20))
        self.label_run.setFont(font4)
        self.label_run.setStyleSheet(u"border:none;\n"
"color:black;")
        self.label_run.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_stop = QLabel(self.frame_main)
        self.label_stop.setObjectName(u"label_stop")
        self.label_stop.setGeometry(QRect(30, 160, 100, 20))
        self.label_stop.setFont(font4)
        self.label_stop.setStyleSheet(u"border:none;\n"
"color:black;")
        self.label_stop.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.retranslateUi(ActionSettingWindow)

        self.button_save.setDefault(False)
        self.button_cancel.setDefault(False)


        QMetaObject.connectSlotsByName(ActionSettingWindow)
    # setupUi

    def retranslateUi(self, ActionSettingWindow):
        ActionSettingWindow.setWindowTitle(QCoreApplication.translate("ActionSettingWindow", u"\ub3d9\uc791 \uc124\uc815", None))
        self.button_save.setText(QCoreApplication.translate("ActionSettingWindow", u"\uc800\uc7a5", None))
        self.button_cancel.setText(QCoreApplication.translate("ActionSettingWindow", u"\ucde8\uc18c", None))
        self.label_tip.setText(QCoreApplication.translate("ActionSettingWindow", u"\ub3d9\uc791\uc758 \uc2dc\uc791/\uc911\uc9c0 \ub2e8\ucd95\ud0a4\ub97c \uc124\uc815\ud558\uc138\uc694", None))
        self.comboBox_run.setPlaceholderText(QCoreApplication.translate("ActionSettingWindow", u"\uc120\ud0dd\ud558\uc138\uc694", None))
        self.comboBox_stop.setPlaceholderText(QCoreApplication.translate("ActionSettingWindow", u"\uc120\ud0dd\ud558\uc138\uc694", None))
        self.checkBox_ctrl1.setText(QCoreApplication.translate("ActionSettingWindow", u"Ctrl", None))
        self.checkBox_ctrl2.setText(QCoreApplication.translate("ActionSettingWindow", u"Ctrl", None))
        self.checkBox_shift2.setText(QCoreApplication.translate("ActionSettingWindow", u"Shift", None))
        self.checkBox_shift1.setText(QCoreApplication.translate("ActionSettingWindow", u"Shift", None))
        self.checkBox_alt1.setText(QCoreApplication.translate("ActionSettingWindow", u"Alt", None))
        self.checkBox_alt2.setText(QCoreApplication.translate("ActionSettingWindow", u"Alt", None))
        self.label_run.setText(QCoreApplication.translate("ActionSettingWindow", u"\u25cf \uc2dc\uc791 \ub2e8\ucd95\ud0a4", None))
        self.label_stop.setText(QCoreApplication.translate("ActionSettingWindow", u"\u25cf \uc911\uc9c0 \ub2e8\ucd95\ud0a4", None))
    # retranslateUi

