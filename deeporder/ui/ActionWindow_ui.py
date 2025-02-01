# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ActionWindow.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QLabel,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QSizePolicy, QWidget)

class Ui_ActionWindow(object):
    def setupUi(self, ActionWindow):
        if not ActionWindow.objectName():
            ActionWindow.setObjectName(u"ActionWindow")
        ActionWindow.resize(500, 570)
        ActionWindow.setMaximumSize(QSize(500, 700))
        font = QFont()
        font.setFamilies([u"Arial"])
        ActionWindow.setFont(font)
        ActionWindow.setAutoFillBackground(False)
        ActionWindow.setStyleSheet(u"background-color: #EAEFEF;")
        self.actionwindow = QWidget(ActionWindow)
        self.actionwindow.setObjectName(u"actionwindow")
        font1 = QFont()
        font1.setBold(False)
        self.actionwindow.setFont(font1)
        self.frame_main = QFrame(self.actionwindow)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setGeometry(QRect(10, 10, 480, 550))
        self.frame_main.setFont(font)
        self.frame_main.setStyleSheet(u"background: white;\n"
"border:1px solid black;\n"
"border-radius: 5px;\n"
"")
        self.frame_main.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_main.setFrameShadow(QFrame.Shadow.Raised)
        self.listWidget = QListWidget(self.frame_main)
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(12)
        font2.setStyleStrategy(QFont.PreferDefault)
        __qlistwidgetitem = QListWidgetItem(self.listWidget)
        __qlistwidgetitem.setFont(font2);
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(12)
        __qlistwidgetitem1 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem1.setFont(font3);
        __qlistwidgetitem2 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem2.setFont(font3);
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(20, 80, 340, 340))
        self.listWidget.setFont(font3)
        self.listWidget.setStyleSheet(u"color:black;\n"
"border-radius: 5px;")
        self.listWidget.setFrameShadow(QFrame.Shadow.Plain)
        self.listWidget.setDragEnabled(True)
        self.listWidget.setDragDropMode(QAbstractItemView.DragDropMode.DragOnly)
        self.listWidget.setDefaultDropAction(Qt.DropAction.IgnoreAction)
        self.listWidget.setSpacing(3)
        self.listWidget.setSortingEnabled(False)
        self.button_add = QPushButton(self.frame_main)
        self.button_add.setObjectName(u"button_add")
        self.button_add.setGeometry(QRect(375, 80, 90, 40))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_add.sizePolicy().hasHeightForWidth())
        self.button_add.setSizePolicy(sizePolicy)
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setHintingPreference(QFont.PreferVerticalHinting)
        self.button_add.setFont(font4)
        self.button_add.setAutoFillBackground(False)
        self.button_add.setStyleSheet(u"QPushButton {\n"
"    border-radius: 5px;\n"
"	color:black;\n"
"    border: 1px solid #8f8f91;\n"
"    background-color :#f0f0f0;;\n"
"    padding: 2px 4px;\n"
"}")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.InsertText))
        self.button_add.setIcon(icon)
        self.button_add.setAutoExclusive(False)
        self.button_add.setFlat(False)
        self.button_delete = QPushButton(self.frame_main)
        self.button_delete.setObjectName(u"button_delete")
        self.button_delete.setGeometry(QRect(375, 320, 90, 40))
        sizePolicy.setHeightForWidth(self.button_delete.sizePolicy().hasHeightForWidth())
        self.button_delete.setSizePolicy(sizePolicy)
        self.button_delete.setFont(font4)
        self.button_delete.setAutoFillBackground(False)
        self.button_delete.setStyleSheet(u"QPushButton {\n"
"    border-radius: 5px;\n"
"	color:black;\n"
"    border: 1px solid #8f8f91;\n"
"    background-color: #f0f0f0;\n"
"    padding: 2px 4px;\n"
"}")
        self.button_delete.setIcon(icon)
        self.button_delete.setAutoExclusive(False)
        self.button_delete.setFlat(False)
        self.button_edit = QPushButton(self.frame_main)
        self.button_edit.setObjectName(u"button_edit")
        self.button_edit.setGeometry(QRect(375, 140, 90, 40))
        sizePolicy.setHeightForWidth(self.button_edit.sizePolicy().hasHeightForWidth())
        self.button_edit.setSizePolicy(sizePolicy)
        self.button_edit.setFont(font4)
        self.button_edit.setAutoFillBackground(False)
        self.button_edit.setStyleSheet(u"QPushButton {\n"
"    border-radius: 5px;\n"
"	color:black;\n"
"    border: 1px solid #8f8f91;\n"
"    background-color: #f0f0f0;\n"
"    padding: 2px 4px;\n"
"}")
        self.button_edit.setIcon(icon)
        self.button_edit.setAutoExclusive(False)
        self.button_edit.setFlat(False)
        self.button_copy = QPushButton(self.frame_main)
        self.button_copy.setObjectName(u"button_copy")
        self.button_copy.setGeometry(QRect(375, 200, 90, 40))
        sizePolicy.setHeightForWidth(self.button_copy.sizePolicy().hasHeightForWidth())
        self.button_copy.setSizePolicy(sizePolicy)
        self.button_copy.setFont(font4)
        self.button_copy.setAutoFillBackground(False)
        self.button_copy.setStyleSheet(u"QPushButton {\n"
"    border-radius: 5px;\n"
"	color:black;\n"
"    border: 1px solid #8f8f91;\n"
"    background-color: #f0f0f0;\n"
"    padding: 2px 4px;\n"
"}")
        self.button_copy.setIcon(icon)
        self.button_copy.setAutoExclusive(False)
        self.button_copy.setFlat(False)
        self.button_save = QPushButton(self.frame_main)
        self.button_save.setObjectName(u"button_save")
        self.button_save.setGeometry(QRect(300, 510, 80, 30))
        sizePolicy.setHeightForWidth(self.button_save.sizePolicy().hasHeightForWidth())
        self.button_save.setSizePolicy(sizePolicy)
        self.button_save.setFont(font4)
        self.button_save.setAutoFillBackground(False)
        self.button_save.setStyleSheet(u"QPushButton {\n"
"    border-radius: 5px;\n"
"	color:black;\n"
"    border: 1px solid #8f8f91;\n"
"    background-color: #f0f0f0;\n"
"    padding: 2px 4px;\n"
"}")
        self.button_save.setIcon(icon)
        self.button_save.setAutoExclusive(False)
        self.button_save.setFlat(False)
        self.button_cancel = QPushButton(self.frame_main)
        self.button_cancel.setObjectName(u"button_cancel")
        self.button_cancel.setGeometry(QRect(390, 510, 80, 30))
        sizePolicy.setHeightForWidth(self.button_cancel.sizePolicy().hasHeightForWidth())
        self.button_cancel.setSizePolicy(sizePolicy)
        self.button_cancel.setFont(font4)
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
        self.label_tip.setGeometry(QRect(22, 440, 281, 20))
        font5 = QFont()
        font5.setFamilies([u"Arial"])
        font5.setPointSize(9)
        self.label_tip.setFont(font5)
        self.label_tip.setStyleSheet(u"border:none;\n"
"color:black;")
        self.label_tip.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.button_down = QPushButton(self.frame_main)
        self.button_down.setObjectName(u"button_down")
        self.button_down.setGeometry(QRect(335, 440, 25, 20))
        sizePolicy.setHeightForWidth(self.button_down.sizePolicy().hasHeightForWidth())
        self.button_down.setSizePolicy(sizePolicy)
        font6 = QFont()
        font6.setFamilies([u"NanumGothic"])
        font6.setPointSize(10)
        font6.setBold(False)
        font6.setHintingPreference(QFont.PreferVerticalHinting)
        self.button_down.setFont(font6)
        self.button_down.setAutoFillBackground(False)
        self.button_down.setStyleSheet(u"border-radius: 5px;\n"
"border: 1px solid #8f8f91;\n"
"background-color: #f0f0f0;\n"
"color:black;\n"
"padding: 2px 4px;")
        self.button_down.setIcon(icon)
        self.button_down.setAutoExclusive(False)
        self.button_down.setFlat(False)
        self.button_up = QPushButton(self.frame_main)
        self.button_up.setObjectName(u"button_up")
        self.button_up.setGeometry(QRect(305, 440, 25, 20))
        sizePolicy.setHeightForWidth(self.button_up.sizePolicy().hasHeightForWidth())
        self.button_up.setSizePolicy(sizePolicy)
        self.button_up.setFont(font6)
        self.button_up.setAutoFillBackground(False)
        self.button_up.setStyleSheet(u"border-radius: 5px;\n"
"border: 1px solid #8f8f91;\n"
"background-color: #f0f0f0;\n"
"color:black;\n"
"padding: 2px 4px;")
        self.button_up.setIcon(icon)
        self.button_up.setAutoExclusive(False)
        self.button_up.setFlat(False)
        self.label_title = QLabel(self.frame_main)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(1, 1, 478, 60))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(128)
        sizePolicy1.setVerticalStretch(60)
        sizePolicy1.setHeightForWidth(self.label_title.sizePolicy().hasHeightForWidth())
        self.label_title.setSizePolicy(sizePolicy1)
        self.label_title.setBaseSize(QSize(0, 0))
        font7 = QFont()
        font7.setFamilies([u"Arial"])
        font7.setPointSize(20)
        font7.setBold(True)
        self.label_title.setFont(font7)
        self.label_title.setStyleSheet(u"background-color: deepskyblue;\n"
"color: white;\n"
"border: none;\n"
"border-top-left-radius :5px;\n"
"border-top-right-radius : 5px;\n"
"border-bottom-left-radius : 0px;\n"
"border-bottom-right-radius : 0px;")
        self.label_title.setLineWidth(0)
        self.label_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.button_setting = QPushButton(self.frame_main)
        self.button_setting.setObjectName(u"button_setting")
        self.button_setting.setGeometry(QRect(375, 260, 90, 40))
        sizePolicy.setHeightForWidth(self.button_setting.sizePolicy().hasHeightForWidth())
        self.button_setting.setSizePolicy(sizePolicy)
        self.button_setting.setFont(font4)
        self.button_setting.setAutoFillBackground(False)
        self.button_setting.setStyleSheet(u"QPushButton {\n"
"    border-radius: 5px;\n"
"	color:black;\n"
"    border: 1px solid #8f8f91;\n"
"    background-color: #f0f0f0;\n"
"    padding: 2px 4px;\n"
"}")
        self.button_setting.setIcon(icon)
        self.button_setting.setAutoExclusive(False)
        self.button_setting.setFlat(False)
        self.button_priority = QPushButton(self.frame_main)
        self.button_priority.setObjectName(u"button_priority")
        self.button_priority.setGeometry(QRect(375, 380, 90, 40))
        sizePolicy.setHeightForWidth(self.button_priority.sizePolicy().hasHeightForWidth())
        self.button_priority.setSizePolicy(sizePolicy)
        self.button_priority.setFont(font4)
        self.button_priority.setAutoFillBackground(False)
        self.button_priority.setStyleSheet(u"QPushButton {\n"
"    border-radius: 5px;\n"
"	color:black;\n"
"    border: 1px solid #8f8f91;\n"
"    background-color: #f0f0f0;\n"
"    padding: 2px 4px;\n"
"}")
        self.button_priority.setIcon(icon)
        self.button_priority.setAutoExclusive(False)
        self.button_priority.setFlat(False)
        ActionWindow.setCentralWidget(self.actionwindow)

        self.retranslateUi(ActionWindow)

        self.button_add.setDefault(False)
        self.button_delete.setDefault(False)
        self.button_edit.setDefault(False)
        self.button_copy.setDefault(False)
        self.button_save.setDefault(False)
        self.button_cancel.setDefault(False)
        self.button_down.setDefault(False)
        self.button_up.setDefault(False)
        self.button_setting.setDefault(False)
        self.button_priority.setDefault(False)


        QMetaObject.connectSlotsByName(ActionWindow)
    # setupUi

    def retranslateUi(self, ActionWindow):
        ActionWindow.setWindowTitle(QCoreApplication.translate("ActionWindow", u"\ub3d9\uc791 \ud3b8\uc9d1", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("ActionWindow", u"\uc2dc\uac04 \uc870\uc815", None));
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("ActionWindow", u"\uc811\uc218\ubc84\ud2bc \ud074\ub9ad", None));
        ___qlistwidgetitem2 = self.listWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("ActionWindow", u"\uc9c0\uc5f0 0.5 ms", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.button_add.setText(QCoreApplication.translate("ActionWindow", u"\uc774\ubbf8\uc9c0 \ucd94\uac00", None))
        self.button_delete.setText(QCoreApplication.translate("ActionWindow", u"\uc0ad\uc81c", None))
        self.button_edit.setText(QCoreApplication.translate("ActionWindow", u"\uc774\ubbf8\uc9c0 \uc218\uc815", None))
        self.button_copy.setText(QCoreApplication.translate("ActionWindow", u"\ub300\uae30\uc2dc\uac04 \ucd94\uac00", None))
        self.button_save.setText(QCoreApplication.translate("ActionWindow", u"\uc800\uc7a5", None))
        self.button_cancel.setText(QCoreApplication.translate("ActionWindow", u"\ucde8\uc18c", None))
        self.label_tip.setText(QCoreApplication.translate("ActionWindow", u"[ \uc774\ubbf8\uc9c0 \ucd94\uac00 ] \ubc84\ud2bc\uc744 \ub20c\ub7ec \uc774\ubbf8\uc9c0\ub97c \uc120\ud0dd\ud558\uc138\uc694", None))
        self.button_down.setText(QCoreApplication.translate("ActionWindow", u"\u2228", None))
        self.button_up.setText(QCoreApplication.translate("ActionWindow", u"\u2227", None))
        self.label_title.setText(QCoreApplication.translate("ActionWindow", u"macro name", None))
        self.button_setting.setText(QCoreApplication.translate("ActionWindow", u"\uc6b0\uc120\uc21c\uc704 \uc9c0\uc815", None))
        self.button_priority.setText(QCoreApplication.translate("ActionWindow", u"\uc124\uc815", None))
    # retranslateUi

