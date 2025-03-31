# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'macd_dialog.ui'
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
    QHBoxLayout, QLabel, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(385, 350)
        Dialog.setStyleSheet(u"")
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(12, 10, 361, 140))
        font = QFont()
        font.setPointSize(20)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(u"")
        self.label1 = QLabel(self.groupBox)
        self.label1.setObjectName(u"label1")
        self.label1.setGeometry(QRect(10, 40, 100, 25))
        self.label1.setMinimumSize(QSize(0, 25))
        font1 = QFont()
        font1.setPointSize(13)
        self.label1.setFont(font1)
        self.label1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.macd_fast = QSpinBox(self.groupBox)
        self.macd_fast.setObjectName(u"macd_fast")
        self.macd_fast.setGeometry(QRect(130, 40, 200, 25))
        self.macd_fast.setMinimumSize(QSize(200, 25))
        self.macd_fast.setFont(font1)
        self.macd_fast.setMinimum(1)
        self.macd_fast.setMaximum(200)
        self.macd_fast.setValue(12)
        self.macd_slow = QSpinBox(self.groupBox)
        self.macd_slow.setObjectName(u"macd_slow")
        self.macd_slow.setGeometry(QRect(130, 70, 200, 25))
        self.macd_slow.setMinimumSize(QSize(200, 25))
        self.macd_slow.setFont(font1)
        self.macd_slow.setMinimum(1)
        self.macd_slow.setMaximum(100)
        self.macd_slow.setValue(26)
        self.label2 = QLabel(self.groupBox)
        self.label2.setObjectName(u"label2")
        self.label2.setGeometry(QRect(10, 70, 100, 25))
        self.label2.setMinimumSize(QSize(0, 25))
        self.label2.setFont(font1)
        self.label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.macd_signal = QSpinBox(self.groupBox)
        self.macd_signal.setObjectName(u"macd_signal")
        self.macd_signal.setGeometry(QRect(130, 100, 200, 25))
        self.macd_signal.setMinimumSize(QSize(200, 25))
        self.macd_signal.setFont(font1)
        self.macd_signal.setMinimum(1)
        self.macd_signal.setMaximum(100)
        self.macd_signal.setValue(9)
        self.label3 = QLabel(self.groupBox)
        self.label3.setObjectName(u"label3")
        self.label3.setGeometry(QRect(10, 100, 100, 25))
        self.label3.setMinimumSize(QSize(0, 25))
        self.label3.setFont(font1)
        self.label3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(12, 160, 361, 16))
        self.frame.setFrameShape(QFrame.Shape.HLine)
        self.frame.setFrameShadow(QFrame.Shadow.Sunken)
        self.label4 = QLabel(Dialog)
        self.label4.setObjectName(u"label4")
        self.label4.setGeometry(QRect(12, 180, 71, 16))
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(True)
        self.label4.setFont(font2)
        self.label4.setStyleSheet(u"color: #FF0000; font-weight: bold;")
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(60, 300, 271, 37))
        self.horizontalLayout1 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout1.setObjectName(u"horizontalLayout1")
        self.horizontalLayout1.setContentsMargins(0, 0, 0, 0)
        self.reset_btn = QPushButton(self.layoutWidget)
        self.reset_btn.setObjectName(u"reset_btn")
        self.reset_btn.setMinimumSize(QSize(100, 35))
        self.reset_btn.setMaximumSize(QSize(100, 35))
        self.reset_btn.setStyleSheet(u"background-color: #EFEFEF; border: 1px solid #C2C2C2;")

        self.horizontalLayout1.addWidget(self.reset_btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout1.addItem(self.horizontalSpacer)

        self.save_btn = QPushButton(self.layoutWidget)
        self.save_btn.setObjectName(u"save_btn")
        self.save_btn.setMinimumSize(QSize(100, 35))
        self.save_btn.setMaximumSize(QSize(100, 35))
        self.save_btn.setStyleSheet(u"background-color: #212121; color: white; border: none;")

        self.horizontalLayout1.addWidget(self.save_btn)

        self.layoutWidget1 = QWidget(Dialog)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 211, 370, 52))
        self.verticalLayout = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(20, -1, -1, -1)
        self.radio_option1 = QRadioButton(self.layoutWidget1)
        self.radio_option1.setObjectName(u"radio_option1")
        self.radio_option1.setChecked(True)

        self.horizontalLayout.addWidget(self.radio_option1)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout2 = QHBoxLayout()
        self.horizontalLayout2.setObjectName(u"horizontalLayout2")
        self.horizontalLayout2.setContentsMargins(20, -1, -1, -1)
        self.radio_option2 = QRadioButton(self.layoutWidget1)
        self.radio_option2.setObjectName(u"radio_option2")
        self.radio_option2.setChecked(True)

        self.horizontalLayout2.addWidget(self.radio_option2)


        self.verticalLayout.addLayout(self.horizontalLayout2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"MACD \uc124\uc815", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"MACD \uc124\uc815", None))
        self.label1.setText(QCoreApplication.translate("Dialog", u"\ub2e8\uae30 \uc120", None))
        self.label2.setText(QCoreApplication.translate("Dialog", u"\uc7a5\uae30 \uc120", None))
        self.label3.setText(QCoreApplication.translate("Dialog", u"\uc2dc\uadf8\ub110 \uc120", None))
        self.label4.setText(QCoreApplication.translate("Dialog", u"\uc2dc\uadf8\ub110 \uc120\ud0dd", None))
        self.reset_btn.setText(QCoreApplication.translate("Dialog", u"\ucd08\uae30\ud654", None))
        self.save_btn.setText(QCoreApplication.translate("Dialog", u"\uc800\uc7a5", None))
        self.radio_option1.setText(QCoreApplication.translate("Dialog", u"MACD\uc120\uc774 0\uc120\uc744 \uc0c1\ud5a5 \ub3cc\ud30c\ud560 \ub54c \ub871 \ud3ec\uc9c0\uc158 \uc9c4\uc785", None))
        self.radio_option2.setText(QCoreApplication.translate("Dialog", u"MACD\uc120\uc774 \uc2dc\uadf8\ub110\uc120\uc744 \uc0c1\ud5a5 \ub3cc\ud30c\ud560 \ub54c \ub871 \ud3ec\uc9c0\uc158 \uc9c4\uc785", None))
    # retranslateUi

