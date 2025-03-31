# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ma_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFormLayout,
    QFrame, QGroupBox, QHBoxLayout, QLabel,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(385, 350)
        Dialog.setStyleSheet(u"")
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(12, 10, 361, 161))
        font = QFont()
        font.setPointSize(20)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(u"")
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label1 = QLabel(self.groupBox)
        self.label1.setObjectName(u"label1")
        self.label1.setMinimumSize(QSize(0, 25))
        font1 = QFont()
        font1.setPointSize(13)
        self.label1.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label1)

        self.short_ma = QSpinBox(self.groupBox)
        self.short_ma.setObjectName(u"short_ma")
        self.short_ma.setMinimumSize(QSize(300, 25))
        self.short_ma.setFont(font1)
        self.short_ma.setMinimum(1)
        self.short_ma.setMaximum(200)
        self.short_ma.setValue(20)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.short_ma)

        self.label2 = QLabel(self.groupBox)
        self.label2.setObjectName(u"label2")
        self.label2.setMinimumSize(QSize(0, 25))
        self.label2.setFont(font1)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label2)

        self.mid_ma = QSpinBox(self.groupBox)
        self.mid_ma.setObjectName(u"mid_ma")
        self.mid_ma.setMinimumSize(QSize(300, 25))
        self.mid_ma.setFont(font1)
        self.mid_ma.setMinimum(1)
        self.mid_ma.setMaximum(200)
        self.mid_ma.setValue(60)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.mid_ma)

        self.label3 = QLabel(self.groupBox)
        self.label3.setObjectName(u"label3")
        self.label3.setMinimumSize(QSize(0, 25))
        self.label3.setFont(font1)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label3)

        self.long_ma = QSpinBox(self.groupBox)
        self.long_ma.setObjectName(u"long_ma")
        self.long_ma.setMinimumSize(QSize(300, 25))
        self.long_ma.setFont(font1)
        self.long_ma.setMinimum(1)
        self.long_ma.setMaximum(200)
        self.long_ma.setValue(120)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.long_ma)

        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(12, 180, 361, 16))
        self.frame.setFrameShape(QFrame.Shape.HLine)
        self.frame.setFrameShadow(QFrame.Shadow.Sunken)
        self.label4 = QLabel(Dialog)
        self.label4.setObjectName(u"label4")
        self.label4.setGeometry(QRect(12, 195, 71, 16))
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(True)
        self.label4.setFont(font2)
        self.label4.setStyleSheet(u"color: #FF0000; font-weight: bold;")
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(60, 300, 271, 37))
        self.horizontalLayout3 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout3.setObjectName(u"horizontalLayout3")
        self.horizontalLayout3.setContentsMargins(0, 0, 0, 0)
        self.reset_btn = QPushButton(self.layoutWidget)
        self.reset_btn.setObjectName(u"reset_btn")
        self.reset_btn.setMinimumSize(QSize(100, 35))
        self.reset_btn.setMaximumSize(QSize(100, 35))
        self.reset_btn.setStyleSheet(u"background-color: #EFEFEF; border: 1px solid #C2C2C2;")

        self.horizontalLayout3.addWidget(self.reset_btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout3.addItem(self.horizontalSpacer)

        self.save_btn = QPushButton(self.layoutWidget)
        self.save_btn.setObjectName(u"save_btn")
        self.save_btn.setMinimumSize(QSize(100, 35))
        self.save_btn.setMaximumSize(QSize(100, 35))
        self.save_btn.setStyleSheet(u"background-color: #212121; color: white; border: none;")

        self.horizontalLayout3.addWidget(self.save_btn)

        self.layoutWidget1 = QWidget(Dialog)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 220, 361, 64))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout1 = QHBoxLayout()
        self.horizontalLayout1.setObjectName(u"horizontalLayout1")
        self.horizontalLayout1.setContentsMargins(20, -1, -1, -1)
        self.radio_option1 = QRadioButton(self.layoutWidget1)
        self.radio_option1.setObjectName(u"radio_option1")
        self.radio_option1.setChecked(True)

        self.horizontalLayout1.addWidget(self.radio_option1)

        self.combo1 = QComboBox(self.layoutWidget1)
        self.combo1.addItem("")
        self.combo1.addItem("")
        self.combo1.addItem("")
        self.combo1.setObjectName(u"combo1")
        self.combo1.setMinimumSize(QSize(80, 0))
        self.combo1.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout1.addWidget(self.combo1)

        self.combo2 = QComboBox(self.layoutWidget1)
        self.combo2.addItem("")
        self.combo2.addItem("")
        self.combo2.addItem("")
        self.combo2.setObjectName(u"combo2")
        self.combo2.setMinimumSize(QSize(60, 0))
        self.combo2.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout1.addWidget(self.combo2)

        self.label5 = QLabel(self.layoutWidget1)
        self.label5.setObjectName(u"label5")

        self.horizontalLayout1.addWidget(self.label5)

        self.horizontalLayout1.setStretch(1, 1)
        self.horizontalLayout1.setStretch(2, 1)
        self.horizontalLayout1.setStretch(3, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout1)

        self.horizontalLayout2 = QHBoxLayout()
        self.horizontalLayout2.setObjectName(u"horizontalLayout2")
        self.horizontalLayout2.setContentsMargins(20, -1, -1, -1)
        self.radio_option2 = QRadioButton(self.layoutWidget1)
        self.radio_option2.setObjectName(u"radio_option2")
        self.radio_option2.setChecked(True)

        self.horizontalLayout2.addWidget(self.radio_option2)


        self.verticalLayout_2.addLayout(self.horizontalLayout2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\uc774\ub3d9\ud3c9\uade0\uc120 \uc124\uc815", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"\uc774\ub3d9\ud3c9\uade0\uc120 \uc124\uc815", None))
        self.label1.setText(QCoreApplication.translate("Dialog", u"\ub2e8\uae30", None))
        self.label2.setText(QCoreApplication.translate("Dialog", u"\uc911\uae30", None))
        self.label3.setText(QCoreApplication.translate("Dialog", u"\uc7a5\uae30", None))
        self.label4.setText(QCoreApplication.translate("Dialog", u"\uc2dc\uadf8\ub110 \uc120\ud0dd", None))
        self.reset_btn.setText(QCoreApplication.translate("Dialog", u"\ucd08\uae30\ud654", None))
        self.save_btn.setText(QCoreApplication.translate("Dialog", u"\uc800\uc7a5", None))
        self.radio_option1.setText("")
        self.combo1.setItemText(0, QCoreApplication.translate("Dialog", u"\ub2e8\uae30", None))
        self.combo1.setItemText(1, QCoreApplication.translate("Dialog", u"\uc911\uae30", None))
        self.combo1.setItemText(2, QCoreApplication.translate("Dialog", u"\uc7a5\uae30", None))

        self.combo2.setItemText(0, QCoreApplication.translate("Dialog", u"\ub2e8\uae30", None))
        self.combo2.setItemText(1, QCoreApplication.translate("Dialog", u"\uc911\uae30", None))
        self.combo2.setItemText(2, QCoreApplication.translate("Dialog", u"\uc7a5\uae30", None))

        self.label5.setText(QCoreApplication.translate("Dialog", u"\uace8\ub4e0 \ud06c\ub85c\uc2a4 \ubc1c\uc0dd \uc2dc", None))
        self.radio_option2.setText(QCoreApplication.translate("Dialog", u"   \ub2e8\uae30, \uc911\uae30, \uc7a5\uae30 \uc815\ubc30\uc5f4 \uc644\uc131 \uc2dc", None))
    # retranslateUi

