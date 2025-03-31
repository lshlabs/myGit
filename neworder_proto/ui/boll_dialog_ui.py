# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'boll_dialog.ui'
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
        Dialog.resize(385, 300)
        Dialog.setStyleSheet(u"")
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(12, 10, 361, 111))
        font = QFont()
        font.setPointSize(20)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(u"")
        self.label1 = QLabel(self.groupBox)
        self.label1.setObjectName(u"label1")
        self.label1.setGeometry(QRect(10, 40, 100, 25))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label1.sizePolicy().hasHeightForWidth())
        self.label1.setSizePolicy(sizePolicy)
        self.label1.setMinimumSize(QSize(0, 25))
        font1 = QFont()
        font1.setPointSize(13)
        self.label1.setFont(font1)
        self.label1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.boll_length = QSpinBox(self.groupBox)
        self.boll_length.setObjectName(u"boll_length")
        self.boll_length.setGeometry(QRect(130, 40, 200, 25))
        self.boll_length.setMinimumSize(QSize(200, 25))
        self.boll_length.setFont(font1)
        self.boll_length.setMinimum(1)
        self.boll_length.setMaximum(100)
        self.boll_length.setValue(20)
        self.boll_deviation = QSpinBox(self.groupBox)
        self.boll_deviation.setObjectName(u"boll_deviation")
        self.boll_deviation.setGeometry(QRect(130, 70, 200, 25))
        self.boll_deviation.setMinimumSize(QSize(200, 25))
        self.boll_deviation.setFont(font1)
        self.boll_deviation.setMinimum(1)
        self.boll_deviation.setMaximum(10)
        self.boll_deviation.setValue(2)
        self.label2 = QLabel(self.groupBox)
        self.label2.setObjectName(u"label2")
        self.label2.setGeometry(QRect(10, 70, 100, 25))
        self.label2.setMinimumSize(QSize(0, 25))
        self.label2.setFont(font1)
        self.label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(12, 130, 361, 16))
        self.frame.setFrameShape(QFrame.Shape.HLine)
        self.frame.setFrameShadow(QFrame.Shadow.Sunken)
        self.label4 = QLabel(Dialog)
        self.label4.setObjectName(u"label4")
        self.label4.setGeometry(QRect(12, 150, 71, 16))
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(True)
        self.label4.setFont(font2)
        self.label4.setStyleSheet(u"color: #FF0000; font-weight: bold;")
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(60, 250, 271, 37))
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

        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 180, 383, 52))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(20, -1, -1, -1)
        self.radio_option1 = QRadioButton(self.widget)
        self.radio_option1.setObjectName(u"radio_option1")
        self.radio_option1.setChecked(True)

        self.horizontalLayout.addWidget(self.radio_option1)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout2 = QHBoxLayout()
        self.horizontalLayout2.setObjectName(u"horizontalLayout2")
        self.horizontalLayout2.setContentsMargins(20, -1, -1, -1)
        self.radio_option2 = QRadioButton(self.widget)
        self.radio_option2.setObjectName(u"radio_option2")
        self.radio_option2.setChecked(True)

        self.horizontalLayout2.addWidget(self.radio_option2)


        self.verticalLayout.addLayout(self.horizontalLayout2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\ubcfc\ub9b0\uc800\ubc34\ub4dc \uc124\uc815", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"RSI \uc124\uc815", None))
        self.label1.setText(QCoreApplication.translate("Dialog", u"\ubcfc\ub9b0\uc800\ubc34\ub4dc \uae38\uc774", None))
        self.label2.setText(QCoreApplication.translate("Dialog", u"\ud45c\uc900\ud3b8\ucc28", None))
        self.label4.setText(QCoreApplication.translate("Dialog", u"\uc2dc\uadf8\ub110 \uc120\ud0dd", None))
        self.reset_btn.setText(QCoreApplication.translate("Dialog", u"\ucd08\uae30\ud654", None))
        self.save_btn.setText(QCoreApplication.translate("Dialog", u"\uc800\uc7a5", None))
        self.radio_option1.setText(QCoreApplication.translate("Dialog", u"\ud558\ub2e8\ubc34\ub4dc \ud130\uce58 \ud6c4 \ubc18\ub4f1 \uc2dc \ub871 \ud3ec\uc9c0\uc158 \uc9c4\uc785 (\uc5ed\ucd94\uc138)", None))
        self.radio_option2.setText(QCoreApplication.translate("Dialog", u"\uc0c1\ub2e8\ubc34\ub4dc \ub3cc\ud30c \ud6c4 \ubbf8\ub4e4\ubc34\ub4dc\ub85c \uc870\uc815 \uc2dc \ub871 \ud3ec\uc9c0\uc158 \uc9c4\uc785 (\ucd94\uc138\ucd94\uc885)", None))
    # retranslateUi

