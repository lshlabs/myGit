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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGroupBox, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_ImageDialog(object):
    def setupUi(self, ImageDialog):
        if not ImageDialog.objectName():
            ImageDialog.setObjectName(u"ImageDialog")
        ImageDialog.resize(400, 550)
        font = QFont()
        font.setFamilies([u"Nanum Gothic"])
        ImageDialog.setFont(font)
        ImageDialog.setStyleSheet(u"QDialog{\n"
"	background-color: #EAEFEF;\n"
"}")
        ImageDialog.setSizeGripEnabled(False)
        ImageDialog.setModal(True)
        self.preview_label = QLabel(ImageDialog)
        self.preview_label.setObjectName(u"preview_label")
        self.preview_label.setGeometry(QRect(75, 10, 250, 150))
        self.preview_label.setMinimumSize(QSize(0, 0))
        font1 = QFont()
        font1.setFamilies([u"NanumGothic"])
        font1.setPointSize(12)
        self.preview_label.setFont(font1)
        self.preview_label.setStyleSheet(u"QLabel{\n"
"	color: rgb(0 ,0, 0);\n"
"	background:white;\n"
"	border: 1px solid black;\n"
"}")
        self.preview_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.reset_button = QPushButton(ImageDialog)
        self.reset_button.setObjectName(u"reset_button")
        self.reset_button.setGeometry(QRect(300, 135, 20, 20))
        self.reset_button.setMinimumSize(QSize(0, 0))
        self.reset_button.setMaximumSize(QSize(88, 16777215))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(12)
        self.reset_button.setFont(font2)
        self.reset_button.setStyleSheet(u"background: white;\n"
"border: 1px solid black;\n"
"border-radius: 10px;")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ViewRefresh))
        self.reset_button.setIcon(icon)
        self.groupBox = QGroupBox(ImageDialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(25, 210, 350, 280))
        font3 = QFont()
        font3.setFamilies([u"Nanum Gothic"])
        font3.setPointSize(12)
        font3.setKerning(True)
        self.groupBox.setFont(font3)
        self.groupBox.setStyleSheet(u"")
        self.button_record1 = QPushButton(self.groupBox)
        self.button_record1.setObjectName(u"button_record1")
        self.button_record1.setGeometry(QRect(250, 100, 70, 30))
        font4 = QFont()
        font4.setFamilies([u"NanumGothic"])
        font4.setPointSize(10)
        self.button_record1.setFont(font4)
        self.button_record1.setStyleSheet(u"")
        self.button_record1.setAutoDefault(False)
        self.button_record1.setFlat(False)
        self.label_X1 = QLabel(self.groupBox)
        self.label_X1.setObjectName(u"label_X1")
        self.label_X1.setGeometry(QRect(50, 105, 20, 20))
        font5 = QFont()
        font5.setFamilies([u"NanumGothic"])
        font5.setPointSize(11)
        self.label_X1.setFont(font5)
        self.label_X1.setStyleSheet(u"QLabel{\n"
"	color: rgb(0 ,0, 0);\n"
"	background-color: transparent;\n"
"}")
        self.textEdit_X1 = QLineEdit(self.groupBox)
        self.textEdit_X1.setObjectName(u"textEdit_X1")
        self.textEdit_X1.setGeometry(QRect(70, 105, 60, 20))
        font6 = QFont()
        font6.setFamilies([u"Nanum Gothic"])
        font6.setPointSize(10)
        self.textEdit_X1.setFont(font6)
        self.textEdit_X1.setAutoFillBackground(False)
        self.textEdit_X1.setStyleSheet(u"background:white;\n"
"border: 1px solid black;")
        self.label_Y1 = QLabel(self.groupBox)
        self.label_Y1.setObjectName(u"label_Y1")
        self.label_Y1.setGeometry(QRect(140, 105, 20, 20))
        self.label_Y1.setFont(font5)
        self.label_Y1.setStyleSheet(u"QLabel{\n"
"	color: rgb(0 ,0, 0);\n"
"	background-color: transparent;\n"
"}")
        self.textEdit_Y1 = QLineEdit(self.groupBox)
        self.textEdit_Y1.setObjectName(u"textEdit_Y1")
        self.textEdit_Y1.setGeometry(QRect(160, 105, 60, 20))
        self.textEdit_Y1.setFont(font6)
        self.textEdit_Y1.setAutoFillBackground(False)
        self.textEdit_Y1.setStyleSheet(u"background:white;\n"
"border: 1px solid black;")
        self.tooltip_1 = QLabel(self.groupBox)
        self.tooltip_1.setObjectName(u"tooltip_1")
        self.tooltip_1.setGeometry(QRect(220, 32, 15, 15))
        font7 = QFont()
        font7.setFamilies([u"Nanum Gothic"])
        font7.setPointSize(8)
        self.tooltip_1.setFont(font7)
        self.tooltip_1.setStyleSheet(u"QLabel{\n"
"	background-color: #9437FF;\n"
"	color:#FFFFFF;\n"
"	border: none;\n"
"	border-radius: 6px;\n"
"	border-width : 1px\n"
"\n"
"}")
        self.tooltip_1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_1 = QLabel(self.groupBox)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setGeometry(QRect(20, 30, 200, 20))
        font8 = QFont()
        font8.setFamilies([u"NanumGothic"])
        font8.setPointSize(12)
        font8.setItalic(False)
        font8.setUnderline(False)
        self.label_1.setFont(font8)
        self.label_1.setStyleSheet(u"QLabel{\n"
"	color: rgb(0 ,0, 0);\n"
"	background-color: transparent;\n"
"}")
        self.label_1.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 80, 60, 20))
        self.label_3.setFont(font5)
        self.label_3.setStyleSheet(u"QLabel{\n"
"	color: rgb(0 ,0, 0);\n"
"	background-color: transparent;\n"
"}")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.button_record2 = QPushButton(self.groupBox)
        self.button_record2.setObjectName(u"button_record2")
        self.button_record2.setGeometry(QRect(250, 160, 70, 30))
        self.button_record2.setFont(font4)
        self.button_record2.setStyleSheet(u"")
        self.button_record2.setAutoDefault(False)
        self.button_record2.setFlat(False)
        self.label_Y2 = QLabel(self.groupBox)
        self.label_Y2.setObjectName(u"label_Y2")
        self.label_Y2.setGeometry(QRect(140, 165, 20, 20))
        self.label_Y2.setFont(font5)
        self.label_Y2.setStyleSheet(u"QLabel{\n"
"	color: rgb(0 ,0, 0);\n"
"	background-color: transparent;\n"
"}")
        self.textEdit_Y2 = QLineEdit(self.groupBox)
        self.textEdit_Y2.setObjectName(u"textEdit_Y2")
        self.textEdit_Y2.setGeometry(QRect(160, 165, 60, 20))
        self.textEdit_Y2.setFont(font6)
        self.textEdit_Y2.setAutoFillBackground(False)
        self.textEdit_Y2.setStyleSheet(u"background:white;\n"
"border: 1px solid black;")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 140, 60, 20))
        self.label_4.setFont(font5)
        self.label_4.setStyleSheet(u"QLabel{\n"
"	color: rgb(0 ,0, 0);\n"
"	background-color: transparent;\n"
"}")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.textEdit_X2 = QLineEdit(self.groupBox)
        self.textEdit_X2.setObjectName(u"textEdit_X2")
        self.textEdit_X2.setGeometry(QRect(70, 165, 60, 20))
        self.textEdit_X2.setFont(font6)
        self.textEdit_X2.setAutoFillBackground(False)
        self.textEdit_X2.setStyleSheet(u"background:white;\n"
"border: 1px solid black;")
        self.label_X2 = QLabel(self.groupBox)
        self.label_X2.setObjectName(u"label_X2")
        self.label_X2.setGeometry(QRect(50, 165, 20, 20))
        self.label_X2.setFont(font5)
        self.label_X2.setStyleSheet(u"QLabel{\n"
"	color: rgb(0 ,0, 0);\n"
"	background-color: transparent;\n"
"}")
        self.textEdit_Y3 = QLineEdit(self.groupBox)
        self.textEdit_Y3.setObjectName(u"textEdit_Y3")
        self.textEdit_Y3.setGeometry(QRect(160, 238, 60, 20))
        self.textEdit_Y3.setFont(font6)
        self.textEdit_Y3.setAutoFillBackground(False)
        self.textEdit_Y3.setStyleSheet(u"background:white;\n"
"border: 1px solid black;")
        self.label_Y3 = QLabel(self.groupBox)
        self.label_Y3.setObjectName(u"label_Y3")
        self.label_Y3.setGeometry(QRect(140, 238, 20, 20))
        self.label_Y3.setFont(font5)
        self.label_Y3.setStyleSheet(u"QLabel{\n"
"	color: rgb(0 ,0, 0);\n"
"	background-color: transparent;\n"
"}")
        self.textEdit_X3 = QLineEdit(self.groupBox)
        self.textEdit_X3.setObjectName(u"textEdit_X3")
        self.textEdit_X3.setGeometry(QRect(70, 238, 60, 20))
        self.textEdit_X3.setFont(font6)
        self.textEdit_X3.setAutoFillBackground(False)
        self.textEdit_X3.setStyleSheet(u"background:white;\n"
"border: 1px solid black;")
        self.label_X3 = QLabel(self.groupBox)
        self.label_X3.setObjectName(u"label_X3")
        self.label_X3.setGeometry(QRect(50, 238, 20, 20))
        self.label_X3.setFont(font5)
        self.label_X3.setStyleSheet(u"QLabel{\n"
"	color: rgb(0 ,0, 0);\n"
"	background-color: transparent;\n"
"}")
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 208, 190, 20))
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"QLabel{\n"
"	color: rgb(0 ,0, 0);\n"
"	background-color: transparent;\n"
"}")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.tooltip_2 = QLabel(self.groupBox)
        self.tooltip_2.setObjectName(u"tooltip_2")
        self.tooltip_2.setGeometry(QRect(215, 210, 15, 15))
        self.tooltip_2.setFont(font7)
        self.tooltip_2.setStyleSheet(u"QLabel{\n"
"	background-color: #9437FF;\n"
"	color:#FFFFFF;\n"
"	border: none;\n"
"	border-radius: 6px;\n"
"	border-width : 1px\n"
"\n"
"}")
        self.tooltip_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 55, 290, 20))
        self.label_2.setFont(font8)
        self.label_2.setStyleSheet(u"QLabel{\n"
"	color: rgb(0 ,0, 0);\n"
"	background-color: transparent;\n"
"}")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.buttonBox = QDialogButtonBox(ImageDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(25, 510, 350, 35))
        self.buttonBox.setFont(font1)
        self.buttonBox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.buttonBox.setAutoFillBackground(False)
        self.buttonBox.setStyleSheet(u"")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setCenterButtons(False)
        self.textEdit_img_name = QLineEdit(ImageDialog)
        self.textEdit_img_name.setObjectName(u"textEdit_img_name")
        self.textEdit_img_name.setGeometry(QRect(110, 180, 180, 20))
        self.textEdit_img_name.setFont(font6)
        self.textEdit_img_name.setStyleSheet(u"background:white;\n"
"border: 1px solid black;")
        self.textEdit_img_name.setMaxLength(20)

        self.retranslateUi(ImageDialog)

        self.button_record1.setDefault(False)
        self.button_record2.setDefault(False)


        QMetaObject.connectSlotsByName(ImageDialog)
    # setupUi

    def retranslateUi(self, ImageDialog):
        ImageDialog.setWindowTitle(QCoreApplication.translate("ImageDialog", u"\uc774\ubbf8\uc9c0 \ucca8\ubd80", None))
        self.preview_label.setText(QCoreApplication.translate("ImageDialog", u"\uc774\uacf3\uc744 \ud074\ub9ad\ud558\uc5ec\n"
"\uc774\ubbf8\uc9c0\ub97c \uc120\ud0dd\ud558\uc138\uc694", None))
        self.reset_button.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("ImageDialog", u" \uc88c\ud45c \uc124\uc815 ", None))
        self.button_record1.setText(QCoreApplication.translate("ImageDialog", u"\uae30\ub85d \uc2dc\uc791", None))
        self.label_X1.setText(QCoreApplication.translate("ImageDialog", u"X :", None))
        self.label_Y1.setText(QCoreApplication.translate("ImageDialog", u"Y :", None))
        self.tooltip_1.setText(QCoreApplication.translate("ImageDialog", u"?", None))
        self.label_1.setText(QCoreApplication.translate("ImageDialog", u"\ud574\ub2f9 \uc774\ubbf8\uc9c0\ub97c \uc778\uc2dd\ud560 \ubc94\uc704\ub97c \uc124\uc815\ud558\uc138\uc694", None))
        self.label_3.setText(QCoreApplication.translate("ImageDialog", u"\uc2dc\uc791\uc810 \uc88c\ud45c", None))
        self.button_record2.setText(QCoreApplication.translate("ImageDialog", u"\uae30\ub85d \uc2dc\uc791", None))
        self.label_Y2.setText(QCoreApplication.translate("ImageDialog", u"Y :", None))
        self.label_4.setText(QCoreApplication.translate("ImageDialog", u"\ub05d\uc810 \uc88c\ud45c", None))
        self.label_X2.setText(QCoreApplication.translate("ImageDialog", u"X :", None))
        self.label_Y3.setText(QCoreApplication.translate("ImageDialog", u"Y :", None))
        self.label_X3.setText(QCoreApplication.translate("ImageDialog", u"X :", None))
        self.label_5.setText(QCoreApplication.translate("ImageDialog", u"\ud074\ub9ad \uc88c\ud45c \uc870\uc815 (\u203b\uccab \uc2e4\ud589\uc2dc \uc218\uc815 \uae08\uc9c0)", None))
        self.tooltip_2.setText(QCoreApplication.translate("ImageDialog", u"?", None))
        self.label_2.setText(QCoreApplication.translate("ImageDialog", u"\uae30\ub85d \uc2dc\uc791 \ubc84\ud2bc\uc744 \ub204\ub978 \ud6c4 F10\uc744 \ub204\ub974\uba74 \uc88c\ud45c\ub97c \ud655\uc815\ud569\ub2c8\ub2e4", None))
        self.textEdit_img_name.setInputMask("")
        self.textEdit_img_name.setPlaceholderText(QCoreApplication.translate("ImageDialog", u"\uc774\ubbf8\uc9c0\uc758 \uc774\ub984\uc744 \uc785\ub825\ud558\uc138\uc694", None))
    # retranslateUi

