# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLayout,
    QLineEdit, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(710, 491)
        font = QFont()
        font.setFamilies([u"Helvetica"])
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color: rgb(234, 238, 238)")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        font1 = QFont()
        font1.setBold(False)
        self.centralwidget.setFont(font1)
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(150, 75, 550, 392))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QSize(550, 388))
        self.scrollArea.setMaximumSize(QSize(550, 600))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        self.scrollArea.setFont(font2)
        self.scrollArea.setAutoFillBackground(False)
        self.scrollArea.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"color:rgb(0, 0, 0);\n"
"border: 1px solid black;")
        self.scrollArea.setFrameShape(QFrame.Shape.Box)
        self.scrollArea.setFrameShadow(QFrame.Shadow.Plain)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 590, 540))
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setMinimumSize(QSize(590, 540))
        self.scrollAreaWidgetContents.setMaximumSize(QSize(590, 540))
        self.scrollAreaWidgetContents.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"border: none;")
        self.Setting_frame = QFrame(self.scrollAreaWidgetContents)
        self.Setting_frame.setObjectName(u"Setting_frame")
        self.Setting_frame.setGeometry(QRect(43, 350, 461, 171))
        self.Setting_frame.setFont(font2)
        self.Setting_frame.setStyleSheet(u"border: 1px solid black;")
        self.Setting_frame.setFrameShape(QFrame.Shape.Box)
        self.Setting_frame.setFrameShadow(QFrame.Shadow.Plain)
        self.frame_timeset1 = QFrame(self.Setting_frame)
        self.frame_timeset1.setObjectName(u"frame_timeset1")
        self.frame_timeset1.setGeometry(QRect(5, 10, 453, 50))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_timeset1.sizePolicy().hasHeightForWidth())
        self.frame_timeset1.setSizePolicy(sizePolicy1)
        self.frame_timeset1.setFont(font2)
        self.frame_timeset1.setStyleSheet(u"border:none;")
        self.frame_timeset1.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_timeset1.setFrameShadow(QFrame.Shadow.Plain)
        self.label_timeset1 = QLabel(self.frame_timeset1)
        self.label_timeset1.setObjectName(u"label_timeset1")
        self.label_timeset1.setGeometry(QRect(10, 10, 131, 31))
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(9)
        self.label_timeset1.setFont(font3)
        self.verticalFrame_entry1 = QFrame(self.frame_timeset1)
        self.verticalFrame_entry1.setObjectName(u"verticalFrame_entry1")
        self.verticalFrame_entry1.setGeometry(QRect(190, 0, 51, 51))
        self.verticalFrame_entry1.setFont(font2)
        self.verticalLayout_7 = QVBoxLayout(self.verticalFrame_entry1)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_7.setContentsMargins(5, 5, 5, 5)
        self.verticalSpacer4 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer4)

        self.entry1 = QLineEdit(self.verticalFrame_entry1)
        self.entry1.setObjectName(u"entry1")
        self.entry1.setFont(font3)
        self.entry1.setStyleSheet(u"border: 1px solid black;")
        self.entry1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.entry1.setReadOnly(True)

        self.verticalLayout_7.addWidget(self.entry1)

        self.verticalSpacer3 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer3)

        self.verticalLayout_7.setStretch(1, 1)
        self.verticalFrame_plus1 = QFrame(self.frame_timeset1)
        self.verticalFrame_plus1.setObjectName(u"verticalFrame_plus1")
        self.verticalFrame_plus1.setGeometry(QRect(240, 0, 41, 51))
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.verticalFrame_plus1.sizePolicy().hasHeightForWidth())
        self.verticalFrame_plus1.setSizePolicy(sizePolicy2)
        self.verticalFrame_plus1.setFont(font2)
        self.verticalLayout_9 = QVBoxLayout(self.verticalFrame_plus1)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.verticalSpacer5 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer5)

        self.button_plus1 = QPushButton(self.verticalFrame_plus1)
        self.button_plus1.setObjectName(u"button_plus1")
        sizePolicy1.setHeightForWidth(self.button_plus1.sizePolicy().hasHeightForWidth())
        self.button_plus1.setSizePolicy(sizePolicy1)
        self.button_plus1.setMaximumSize(QSize(30, 20))
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setHintingPreference(QFont.PreferVerticalHinting)
        self.button_plus1.setFont(font4)
        self.button_plus1.setAutoFillBackground(False)
        self.button_plus1.setStyleSheet(u"QPushButton {\n"
"    border-radius: 5px;\n"
"    border: 1px solid #8f8f91;\n"
"    background-color: #f0f0f0;\n"
"    padding: 2px 4px;\n"
"}")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.InsertText))
        self.button_plus1.setIcon(icon)
        self.button_plus1.setAutoExclusive(False)
        self.button_plus1.setFlat(False)

        self.verticalLayout_9.addWidget(self.button_plus1)

        self.verticalSpacer6 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer6)

        self.verticalLayout_9.setStretch(1, 1)
        self.verticalFrame_minus1 = QFrame(self.frame_timeset1)
        self.verticalFrame_minus1.setObjectName(u"verticalFrame_minus1")
        self.verticalFrame_minus1.setGeometry(QRect(150, 0, 41, 51))
        sizePolicy2.setHeightForWidth(self.verticalFrame_minus1.sizePolicy().hasHeightForWidth())
        self.verticalFrame_minus1.setSizePolicy(sizePolicy2)
        self.verticalFrame_minus1.setFont(font2)
        self.verticalLayout_10 = QVBoxLayout(self.verticalFrame_minus1)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_10.setContentsMargins(5, 5, 5, 5)
        self.verticalSpacer1 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer1)

        self.button_minus1 = QPushButton(self.verticalFrame_minus1)
        self.button_minus1.setObjectName(u"button_minus1")
        sizePolicy1.setHeightForWidth(self.button_minus1.sizePolicy().hasHeightForWidth())
        self.button_minus1.setSizePolicy(sizePolicy1)
        self.button_minus1.setMaximumSize(QSize(30, 20))
        self.button_minus1.setFont(font4)
        self.button_minus1.setAutoFillBackground(False)
        self.button_minus1.setStyleSheet(u"QPushButton {\n"
"    border-radius: 5px;\n"
"    border: 1px solid #8f8f91;\n"
"    background-color: #f0f0f0;\n"
"    padding: 2px 4px;\n"
"}")
        self.button_minus1.setIcon(icon)
        self.button_minus1.setAutoExclusive(False)
        self.button_minus1.setFlat(False)

        self.verticalLayout_10.addWidget(self.button_minus1)

        self.verticalSpacer2 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer2)

        self.verticalLayout_10.setStretch(1, 1)
        self.frame_timeset2 = QFrame(self.Setting_frame)
        self.frame_timeset2.setObjectName(u"frame_timeset2")
        self.frame_timeset2.setGeometry(QRect(5, 65, 453, 50))
        self.frame_timeset2.setFont(font2)
        self.frame_timeset2.setStyleSheet(u"border:none;")
        self.frame_timeset2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_timeset2.setFrameShadow(QFrame.Shadow.Plain)
        self.label_timeset2 = QLabel(self.frame_timeset2)
        self.label_timeset2.setObjectName(u"label_timeset2")
        self.label_timeset2.setGeometry(QRect(10, 10, 131, 31))
        self.label_timeset2.setFont(font3)
        self.verticalFrame_plus2 = QFrame(self.frame_timeset2)
        self.verticalFrame_plus2.setObjectName(u"verticalFrame_plus2")
        self.verticalFrame_plus2.setGeometry(QRect(240, 0, 41, 51))
        sizePolicy2.setHeightForWidth(self.verticalFrame_plus2.sizePolicy().hasHeightForWidth())
        self.verticalFrame_plus2.setSizePolicy(sizePolicy2)
        self.verticalFrame_plus2.setFont(font2)
        self.verticalLayout_5 = QVBoxLayout(self.verticalFrame_plus2)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.verticalSpacer11 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer11)

        self.button_plus2 = QPushButton(self.verticalFrame_plus2)
        self.button_plus2.setObjectName(u"button_plus2")
        sizePolicy1.setHeightForWidth(self.button_plus2.sizePolicy().hasHeightForWidth())
        self.button_plus2.setSizePolicy(sizePolicy1)
        self.button_plus2.setMaximumSize(QSize(30, 20))
        self.button_plus2.setFont(font4)
        self.button_plus2.setAutoFillBackground(False)
        self.button_plus2.setStyleSheet(u"QPushButton {\n"
"    border-radius: 5px;\n"
"    border: 1px solid #8f8f91;\n"
"    background-color: #f0f0f0;\n"
"    padding: 2px 4px;\n"
"}")
        self.button_plus2.setIcon(icon)
        self.button_plus2.setAutoExclusive(False)
        self.button_plus2.setFlat(False)

        self.verticalLayout_5.addWidget(self.button_plus2)

        self.verticalSpacer12 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer12)

        self.verticalLayout_5.setStretch(1, 1)
        self.verticalFrame_entry2 = QFrame(self.frame_timeset2)
        self.verticalFrame_entry2.setObjectName(u"verticalFrame_entry2")
        self.verticalFrame_entry2.setGeometry(QRect(190, 0, 51, 51))
        self.verticalFrame_entry2.setFont(font2)
        self.verticalLayout_8 = QVBoxLayout(self.verticalFrame_entry2)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_8.setContentsMargins(5, 5, 5, 5)
        self.verticalSpacer9 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer9)

        self.entry2 = QLineEdit(self.verticalFrame_entry2)
        self.entry2.setObjectName(u"entry2")
        self.entry2.setFont(font3)
        self.entry2.setStyleSheet(u"border: 1px solid black;")
        self.entry2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.entry2.setReadOnly(True)

        self.verticalLayout_8.addWidget(self.entry2)

        self.verticalSpacer10 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer10)

        self.verticalLayout_8.setStretch(1, 1)
        self.verticalFrame_minus2 = QFrame(self.frame_timeset2)
        self.verticalFrame_minus2.setObjectName(u"verticalFrame_minus2")
        self.verticalFrame_minus2.setGeometry(QRect(150, 0, 41, 51))
        sizePolicy2.setHeightForWidth(self.verticalFrame_minus2.sizePolicy().hasHeightForWidth())
        self.verticalFrame_minus2.setSizePolicy(sizePolicy2)
        self.verticalFrame_minus2.setFont(font2)
        self.verticalLayout_11 = QVBoxLayout(self.verticalFrame_minus2)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_11.setContentsMargins(5, 5, 5, 5)
        self.verticalSpacer7 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer7)

        self.button_minus2 = QPushButton(self.verticalFrame_minus2)
        self.button_minus2.setObjectName(u"button_minus2")
        sizePolicy1.setHeightForWidth(self.button_minus2.sizePolicy().hasHeightForWidth())
        self.button_minus2.setSizePolicy(sizePolicy1)
        self.button_minus2.setMaximumSize(QSize(30, 20))
        self.button_minus2.setFont(font4)
        self.button_minus2.setAutoFillBackground(False)
        self.button_minus2.setStyleSheet(u"QPushButton {\n"
"    border-radius: 5px;\n"
"    border: 1px solid #8f8f91;\n"
"    background-color: #f0f0f0;\n"
"    padding: 2px 4px;\n"
"}")
        self.button_minus2.setIcon(icon)
        self.button_minus2.setAutoExclusive(False)
        self.button_minus2.setFlat(False)

        self.verticalLayout_11.addWidget(self.button_minus2)

        self.verticalSpacer8 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer8)

        self.verticalLayout_11.setStretch(1, 1)
        self.frame_timeset3 = QFrame(self.Setting_frame)
        self.frame_timeset3.setObjectName(u"frame_timeset3")
        self.frame_timeset3.setGeometry(QRect(5, 120, 453, 50))
        self.frame_timeset3.setFont(font2)
        self.frame_timeset3.setStyleSheet(u"border:none;")
        self.frame_timeset3.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_timeset3.setFrameShadow(QFrame.Shadow.Plain)
        self.label_timeset3 = QLabel(self.frame_timeset3)
        self.label_timeset3.setObjectName(u"label_timeset3")
        self.label_timeset3.setGeometry(QRect(10, 10, 91, 31))
        self.label_timeset3.setFont(font3)
        self.label_settings_icon = QLabel(self.frame_timeset3)
        self.label_settings_icon.setObjectName(u"label_settings_icon")
        self.label_settings_icon.setGeometry(QRect(150, 0, 30, 30))
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_settings_icon.sizePolicy().hasHeightForWidth())
        self.label_settings_icon.setSizePolicy(sizePolicy3)
        self.label_settings_icon.setMaximumSize(QSize(30, 30))
        self.label_settings_icon.setFont(font3)
        self.label_settings_icon.setPixmap(QPixmap(u"/img/settings.png"))
        self.label_settings_icon.setScaledContents(True)
        self.label_image5 = QLabel(self.scrollAreaWidgetContents)
        self.label_image5.setObjectName(u"label_image5")
        self.label_image5.setGeometry(QRect(213, 309, 120, 25))
        sizePolicy3.setHeightForWidth(self.label_image5.sizePolicy().hasHeightForWidth())
        self.label_image5.setSizePolicy(sizePolicy3)
        self.label_image5.setMinimumSize(QSize(120, 25))
        self.label_image5.setMaximumSize(QSize(120, 30))
        self.label_image5.setFont(font2)
        self.label_image5.setStyleSheet(u"color: black;\n"
"border: 1px solid black;")
        self.label_image5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_image1 = QLabel(self.scrollAreaWidgetContents)
        self.label_image1.setObjectName(u"label_image1")
        self.label_image1.setGeometry(QRect(43, 144, 120, 25))
        sizePolicy3.setHeightForWidth(self.label_image1.sizePolicy().hasHeightForWidth())
        self.label_image1.setSizePolicy(sizePolicy3)
        self.label_image1.setMinimumSize(QSize(120, 25))
        self.label_image1.setMaximumSize(QSize(120, 30))
        self.label_image1.setFont(font2)
        self.label_image1.setStyleSheet(u"color: black;\n"
"border: 1px solid black;")
        self.label_image1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_image6 = QLabel(self.scrollAreaWidgetContents)
        self.label_image6.setObjectName(u"label_image6")
        self.label_image6.setGeometry(QRect(383, 309, 120, 25))
        sizePolicy3.setHeightForWidth(self.label_image6.sizePolicy().hasHeightForWidth())
        self.label_image6.setSizePolicy(sizePolicy3)
        self.label_image6.setMinimumSize(QSize(120, 25))
        self.label_image6.setMaximumSize(QSize(120, 30))
        self.label_image6.setFont(font2)
        self.label_image6.setStyleSheet(u"color: black;\n"
"border: 1px solid black;")
        self.label_image6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_image2 = QLabel(self.scrollAreaWidgetContents)
        self.label_image2.setObjectName(u"label_image2")
        self.label_image2.setGeometry(QRect(213, 144, 120, 25))
        sizePolicy3.setHeightForWidth(self.label_image2.sizePolicy().hasHeightForWidth())
        self.label_image2.setSizePolicy(sizePolicy3)
        self.label_image2.setMinimumSize(QSize(120, 25))
        self.label_image2.setMaximumSize(QSize(120, 30))
        self.label_image2.setFont(font2)
        self.label_image2.setStyleSheet(u"color: black;\n"
"border: 1px solid black;")
        self.label_image2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_image4 = QLabel(self.scrollAreaWidgetContents)
        self.label_image4.setObjectName(u"label_image4")
        self.label_image4.setGeometry(QRect(43, 309, 120, 25))
        sizePolicy3.setHeightForWidth(self.label_image4.sizePolicy().hasHeightForWidth())
        self.label_image4.setSizePolicy(sizePolicy3)
        self.label_image4.setMinimumSize(QSize(120, 25))
        self.label_image4.setMaximumSize(QSize(120, 30))
        self.label_image4.setFont(font2)
        self.label_image4.setStyleSheet(u"color: black;\n"
"border: 1px solid black;")
        self.label_image4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_image3 = QLabel(self.scrollAreaWidgetContents)
        self.label_image3.setObjectName(u"label_image3")
        self.label_image3.setGeometry(QRect(383, 144, 120, 25))
        sizePolicy3.setHeightForWidth(self.label_image3.sizePolicy().hasHeightForWidth())
        self.label_image3.setSizePolicy(sizePolicy3)
        self.label_image3.setMinimumSize(QSize(120, 25))
        self.label_image3.setMaximumSize(QSize(120, 30))
        self.label_image3.setFont(font2)
        self.label_image3.setStyleSheet(u"color: black;\n"
"border: 1px solid black;")
        self.label_image3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.frame_image1 = QLabel(self.scrollAreaWidgetContents)
        self.frame_image1.setObjectName(u"frame_image1")
        self.frame_image1.setGeometry(QRect(43, 25, 120, 120))
        sizePolicy3.setHeightForWidth(self.frame_image1.sizePolicy().hasHeightForWidth())
        self.frame_image1.setSizePolicy(sizePolicy3)
        self.frame_image1.setMaximumSize(QSize(120, 120))
        self.frame_image1.setStyleSheet(u"background:rgb(206, 208, 208);\n"
"border:1px solid black;")
        self.frame_image1.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_image2 = QLabel(self.scrollAreaWidgetContents)
        self.frame_image2.setObjectName(u"frame_image2")
        self.frame_image2.setGeometry(QRect(213, 25, 120, 120))
        sizePolicy3.setHeightForWidth(self.frame_image2.sizePolicy().hasHeightForWidth())
        self.frame_image2.setSizePolicy(sizePolicy3)
        self.frame_image2.setMaximumSize(QSize(120, 120))
        self.frame_image2.setStyleSheet(u"background:rgb(206, 208, 208);\n"
"border:1px solid black;")
        self.frame_image2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_image3 = QLabel(self.scrollAreaWidgetContents)
        self.frame_image3.setObjectName(u"frame_image3")
        self.frame_image3.setGeometry(QRect(383, 25, 120, 120))
        sizePolicy3.setHeightForWidth(self.frame_image3.sizePolicy().hasHeightForWidth())
        self.frame_image3.setSizePolicy(sizePolicy3)
        self.frame_image3.setMaximumSize(QSize(120, 120))
        self.frame_image3.setStyleSheet(u"background:rgb(206, 208, 208);\n"
"border:1px solid black;")
        self.frame_image3.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_image4 = QLabel(self.scrollAreaWidgetContents)
        self.frame_image4.setObjectName(u"frame_image4")
        self.frame_image4.setGeometry(QRect(43, 190, 120, 120))
        sizePolicy3.setHeightForWidth(self.frame_image4.sizePolicy().hasHeightForWidth())
        self.frame_image4.setSizePolicy(sizePolicy3)
        self.frame_image4.setMaximumSize(QSize(120, 120))
        self.frame_image4.setStyleSheet(u"background:rgb(206, 208, 208);\n"
"border:1px solid black;")
        self.frame_image4.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_image5 = QLabel(self.scrollAreaWidgetContents)
        self.frame_image5.setObjectName(u"frame_image5")
        self.frame_image5.setGeometry(QRect(213, 190, 120, 120))
        sizePolicy3.setHeightForWidth(self.frame_image5.sizePolicy().hasHeightForWidth())
        self.frame_image5.setSizePolicy(sizePolicy3)
        self.frame_image5.setMaximumSize(QSize(120, 120))
        self.frame_image5.setStyleSheet(u"background:rgb(206, 208, 208);\n"
"border:1px solid black;")
        self.frame_image5.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_image6 = QLabel(self.scrollAreaWidgetContents)
        self.frame_image6.setObjectName(u"frame_image6")
        self.frame_image6.setGeometry(QRect(383, 190, 120, 120))
        sizePolicy3.setHeightForWidth(self.frame_image6.sizePolicy().hasHeightForWidth())
        self.frame_image6.setSizePolicy(sizePolicy3)
        self.frame_image6.setMaximumSize(QSize(120, 120))
        self.frame_image6.setStyleSheet(u"background:rgb(206, 208, 208);\n"
"border:1px solid black;")
        self.frame_image6.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.frame_title = QFrame(self.centralwidget)
        self.frame_title.setObjectName(u"frame_title")
        self.frame_title.setGeometry(QRect(150, 10, 550, 66))
        self.frame_title.setMinimumSize(QSize(550, 66))
        self.frame_title.setMaximumSize(QSize(550, 66))
        self.frame_title.setFont(font2)
        self.frame_title.setStyleSheet(u"background:rgb(206, 208, 208);\n"
"border: 1px solid black;")
        self.frame_title.setFrameShape(QFrame.Shape.Box)
        self.frame_title.setFrameShadow(QFrame.Shadow.Plain)
        self.label_title = QLabel(self.frame_title)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(1, 1, 548, 66))
        sizePolicy2.setHeightForWidth(self.label_title.sizePolicy().hasHeightForWidth())
        self.label_title.setSizePolicy(sizePolicy2)
        font5 = QFont()
        font5.setFamilies([u"Arial"])
        font5.setPointSize(30)
        font5.setBold(False)
        self.label_title.setFont(font5)
        self.label_title.setStyleSheet(u"color:rgb(0, 0, 0);\n"
"border: none;")
        self.label_title.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_title.setIndent(40)
        self.button_on = QPushButton(self.frame_title)
        self.button_on.setObjectName(u"button_on")
        self.button_on.setGeometry(QRect(465, 10, 70, 45))
        self.button_on.setFont(font2)
        self.button_on.setStyleSheet(u"background:rgb(219, 222, 222);\n"
"border:1px solid black;\n"
"border-radius:15px;")
        self.button_off = QPushButton(self.frame_title)
        self.button_off.setObjectName(u"button_off")
        self.button_off.setGeometry(QRect(465, 10, 70, 45))
        self.button_off.setFont(font2)
        self.button_off.setStyleSheet(u"background:rgb(219, 222, 222);\n"
"border:1px solid black;\n"
"border-radius:15px;")
        self.frame_menu = QFrame(self.centralwidget)
        self.frame_menu.setObjectName(u"frame_menu")
        self.frame_menu.setGeometry(QRect(10, 10, 130, 457))
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_menu.sizePolicy().hasHeightForWidth())
        self.frame_menu.setSizePolicy(sizePolicy4)
        self.frame_menu.setMinimumSize(QSize(130, 457))
        self.frame_menu.setMaximumSize(QSize(130, 457))
        self.frame_menu.setFont(font2)
        self.frame_menu.setAutoFillBackground(False)
        self.frame_menu.setStyleSheet(u"background: rgb(234, 238, 238);\n"
" border: 1px solid black; \n"
"")
        self.frame_menu.setFrameShape(QFrame.Shape.Box)
        self.frame_menu.setLineWidth(1)
        self.label_menu2 = QLabel(self.frame_menu)
        self.label_menu2.setObjectName(u"label_menu2")
        self.label_menu2.setGeometry(QRect(1, 66, 128, 65))
        sizePolicy2.setHeightForWidth(self.label_menu2.sizePolicy().hasHeightForWidth())
        self.label_menu2.setSizePolicy(sizePolicy2)
        self.label_menu2.setMinimumSize(QSize(128, 65))
        self.label_menu2.setMaximumSize(QSize(128, 65))
        font6 = QFont()
        font6.setFamilies([u"Arial"])
        font6.setPointSize(13)
        self.label_menu2.setFont(font6)
        self.label_menu2.setStyleSheet(u"background:rgb(206, 208, 208);\n"
"color: white;\n"
"border: none;")
        self.label_menu2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_menu6 = QLabel(self.frame_menu)
        self.label_menu6.setObjectName(u"label_menu6")
        self.label_menu6.setGeometry(QRect(1, 326, 128, 65))
        sizePolicy2.setHeightForWidth(self.label_menu6.sizePolicy().hasHeightForWidth())
        self.label_menu6.setSizePolicy(sizePolicy2)
        self.label_menu6.setMinimumSize(QSize(128, 65))
        self.label_menu6.setMaximumSize(QSize(128, 65))
        self.label_menu6.setFont(font6)
        self.label_menu6.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"color: black;\n"
"border: none;")
        self.label_menu6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_menu4 = QLabel(self.frame_menu)
        self.label_menu4.setObjectName(u"label_menu4")
        self.label_menu4.setGeometry(QRect(1, 196, 128, 65))
        sizePolicy2.setHeightForWidth(self.label_menu4.sizePolicy().hasHeightForWidth())
        self.label_menu4.setSizePolicy(sizePolicy2)
        self.label_menu4.setMinimumSize(QSize(128, 65))
        self.label_menu4.setMaximumSize(QSize(128, 65))
        self.label_menu4.setFont(font6)
        self.label_menu4.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"color: black;\n"
"border: none;")
        self.label_menu4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_menu5 = QLabel(self.frame_menu)
        self.label_menu5.setObjectName(u"label_menu5")
        self.label_menu5.setGeometry(QRect(1, 261, 128, 65))
        sizePolicy2.setHeightForWidth(self.label_menu5.sizePolicy().hasHeightForWidth())
        self.label_menu5.setSizePolicy(sizePolicy2)
        self.label_menu5.setMinimumSize(QSize(128, 65))
        self.label_menu5.setMaximumSize(QSize(128, 65))
        self.label_menu5.setFont(font6)
        self.label_menu5.setStyleSheet(u"background-color: rgb(148, 55, 255);\n"
"color:rgb(255, 255, 255);\n"
"border: none;")
        self.label_menu5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_menu7 = QLabel(self.frame_menu)
        self.label_menu7.setObjectName(u"label_menu7")
        self.label_menu7.setGeometry(QRect(1, 391, 128, 65))
        sizePolicy2.setHeightForWidth(self.label_menu7.sizePolicy().hasHeightForWidth())
        self.label_menu7.setSizePolicy(sizePolicy2)
        self.label_menu7.setMinimumSize(QSize(128, 65))
        self.label_menu7.setMaximumSize(QSize(128, 65))
        self.label_menu7.setFont(font6)
        self.label_menu7.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"color: black;\n"
"border: none;")
        self.label_menu7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_menu1 = QLabel(self.frame_menu)
        self.label_menu1.setObjectName(u"label_menu1")
        self.label_menu1.setGeometry(QRect(1, 1, 128, 65))
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(128)
        sizePolicy5.setVerticalStretch(60)
        sizePolicy5.setHeightForWidth(self.label_menu1.sizePolicy().hasHeightForWidth())
        self.label_menu1.setSizePolicy(sizePolicy5)
        self.label_menu1.setMinimumSize(QSize(128, 65))
        self.label_menu1.setMaximumSize(QSize(128, 65))
        self.label_menu1.setBaseSize(QSize(0, 0))
        self.label_menu1.setFont(font6)
        self.label_menu1.setStyleSheet(u"background-color: rgb(148, 55, 255);\n"
"color:rgb(255, 255, 255);\n"
"border: none;")
        self.label_menu1.setLineWidth(0)
        self.label_menu1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_menu3 = QLabel(self.frame_menu)
        self.label_menu3.setObjectName(u"label_menu3")
        self.label_menu3.setGeometry(QRect(1, 131, 128, 65))
        sizePolicy2.setHeightForWidth(self.label_menu3.sizePolicy().hasHeightForWidth())
        self.label_menu3.setSizePolicy(sizePolicy2)
        self.label_menu3.setMinimumSize(QSize(128, 65))
        self.label_menu3.setMaximumSize(QSize(128, 65))
        self.label_menu3.setFont(font6)
        self.label_menu3.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"color: black;\n"
"border: none;")
        self.label_menu3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_menu1.raise_()
        self.label_menu2.raise_()
        self.label_menu6.raise_()
        self.label_menu4.raise_()
        self.label_menu5.raise_()
        self.label_menu7.raise_()
        self.label_menu3.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.frame_title.raise_()
        self.frame_menu.raise_()
        self.scrollArea.raise_()
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.button_plus1.setDefault(False)
        self.button_minus1.setDefault(False)
        self.button_plus2.setDefault(False)
        self.button_minus2.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_timeset1.setText(QCoreApplication.translate("MainWindow", u"\ubc30\ub2ec \uae30\ubcf8 \uc811\uc218\uc2dc\uac04(\ubd84)", None))
        self.entry1.setText(QCoreApplication.translate("MainWindow", u"50", None))
        self.button_plus1.setText(QCoreApplication.translate("MainWindow", u"\u2227", None))
        self.button_minus1.setText(QCoreApplication.translate("MainWindow", u"\u2228", None))
        self.label_timeset2.setText(QCoreApplication.translate("MainWindow", u"\ud3ec\uc7a5 \uae30\ubcf8 \uc811\uc218\uc2dc\uac04(\ubd84)", None))
        self.button_plus2.setText(QCoreApplication.translate("MainWindow", u"\u2227", None))
        self.entry2.setText(QCoreApplication.translate("MainWindow", u"15", None))
        self.button_minus2.setText(QCoreApplication.translate("MainWindow", u"\u2228", None))
        self.label_timeset3.setText(QCoreApplication.translate("MainWindow", u"\ub9e4\ud06c\ub85c \ub3d9\uc791 \uc124\uc815", None))
        self.label_settings_icon.setText("")
        self.label_image5.setText(QCoreApplication.translate("MainWindow", u"\uc774\ubbf8\uc9c0 5", None))
        self.label_image1.setText(QCoreApplication.translate("MainWindow", u"\uc774\ubbf8\uc9c0 1", None))
        self.label_image6.setText(QCoreApplication.translate("MainWindow", u"\uc774\ubbf8\uc9c0 6", None))
        self.label_image2.setText(QCoreApplication.translate("MainWindow", u"\uc774\ubbf8\uc9c0 2", None))
        self.label_image4.setText(QCoreApplication.translate("MainWindow", u"\uc774\ubbf8\uc9c0 4", None))
        self.label_image3.setText(QCoreApplication.translate("MainWindow", u"\uc774\ubbf8\uc9c0 3", None))
        self.frame_image1.setText("")
        self.frame_image2.setText("")
        self.frame_image3.setText("")
        self.frame_image4.setText("")
        self.frame_image5.setText("")
        self.frame_image6.setText("")
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"Menu Name", None))
        self.button_on.setText(QCoreApplication.translate("MainWindow", u"ON", None))
        self.button_off.setText(QCoreApplication.translate("MainWindow", u"OFF", None))
        self.label_menu2.setText(QCoreApplication.translate("MainWindow", u"Menu2", None))
        self.label_menu6.setText(QCoreApplication.translate("MainWindow", u"Menu6", None))
        self.label_menu4.setText(QCoreApplication.translate("MainWindow", u"Menu4", None))
        self.label_menu5.setText(QCoreApplication.translate("MainWindow", u"Menu5", None))
        self.label_menu7.setText(QCoreApplication.translate("MainWindow", u"Menu7", None))
        self.label_menu1.setText(QCoreApplication.translate("MainWindow", u"Menu1", None))
        self.label_menu3.setText(QCoreApplication.translate("MainWindow", u"Menu3", None))
    # retranslateUi
