# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QComboBox, QDoubleSpinBox, QFrame, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QSpinBox, QStatusBar, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1050, 800)
        MainWindow.setMaximumSize(QSize(1050, 800))
        font = QFont()
        font.setFamilies([u"Arial"])
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"QMainWindow{\n"
"	background-color: #EFEFEF;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"QTabWidget::pane {\n"
"  border: 1px solid #C2C2C2;\n"
"  background-color: #EFEFEF;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"  background-color: #EFEFEF;\n"
"  color: #212121;\n"
"  padding: 10px 20px;\n"
"  border: 1px solid #C2C2C2;\n"
"  border-bottom: none;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"  background-color: #212121;\n"
"  color: white;\n"
"}")
        self.tab_trading = QWidget()
        self.tab_trading.setObjectName(u"tab_trading")
        self.right_panel = QGroupBox(self.tab_trading)
        self.right_panel.setObjectName(u"right_panel")
        self.right_panel.setGeometry(QRect(660, 20, 355, 618))
        font1 = QFont()
        font1.setFamilies([u"\ub9d1\uc740 \uace0\ub515"])
        font1.setPointSize(11)
        font1.setBold(True)
        self.right_panel.setFont(font1)
        self.right_panel.setStyleSheet(u"QGroupBox {\n"
"  background-color: white;\n"
"  border: 1px solid #C2C2C2;\n"
"  margin-top: 20px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"  subcontrol-origin: margin;\n"
"  subcontrol-position: top left;\n"
"  padding: 0px 5px 5px 5px;\n"
"}")
        self.verticalLayout_8 = QVBoxLayout(self.right_panel)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.coin_table = QTableWidget(self.right_panel)
        if (self.coin_table.columnCount() < 5):
            self.coin_table.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.coin_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.coin_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.coin_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.coin_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.coin_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        if (self.coin_table.rowCount() < 10):
            self.coin_table.setRowCount(10)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.coin_table.setItem(0, 0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.coin_table.setItem(0, 1, __qtablewidgetitem6)
        brush = QBrush(QColor(255, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setForeground(brush);
        self.coin_table.setItem(0, 2, __qtablewidgetitem7)
        brush1 = QBrush(QColor(255, 38, 0, 255))
        brush1.setStyle(Qt.NoBrush)
        brush2 = QBrush(QColor(255, 38, 0, 255))
        brush2.setStyle(Qt.NoBrush)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setBackground(brush2);
        __qtablewidgetitem8.setForeground(brush1);
        self.coin_table.setItem(0, 3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.coin_table.setItem(0, 4, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.coin_table.setItem(1, 0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.coin_table.setItem(1, 1, __qtablewidgetitem11)
        brush3 = QBrush(QColor(0, 0, 255, 255))
        brush3.setStyle(Qt.SolidPattern)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setForeground(brush3);
        self.coin_table.setItem(1, 2, __qtablewidgetitem12)
        brush4 = QBrush(QColor(19, 49, 245, 255))
        brush4.setStyle(Qt.NoBrush)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setForeground(brush4);
        self.coin_table.setItem(1, 3, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.coin_table.setItem(1, 4, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.coin_table.setItem(2, 0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.coin_table.setItem(2, 1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setForeground(brush);
        self.coin_table.setItem(2, 2, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.coin_table.setItem(2, 3, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.coin_table.setItem(2, 4, __qtablewidgetitem19)
        self.coin_table.setObjectName(u"coin_table")
        self.coin_table.setStyleSheet(u"QTableWidget {\n"
"  border: 1px solid #C2C2C2;\n"
"  background-color: white;\n"
"  color: #212121;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"  background-color: #E0E0E0;\n"
"}\n"
"\n"
"QTableWidget::item {\n"
" alignment: center;\n"
"}")
        self.coin_table.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.coin_table.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.coin_table.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.coin_table.setAutoScroll(False)
        self.coin_table.setTextElideMode(Qt.TextElideMode.ElideMiddle)
        self.coin_table.setRowCount(10)
        self.coin_table.setColumnCount(5)
        self.coin_table.horizontalHeader().setCascadingSectionResizes(True)
        self.coin_table.horizontalHeader().setMinimumSectionSize(19)
        self.coin_table.horizontalHeader().setDefaultSectionSize(54)
        self.coin_table.verticalHeader().setMinimumSectionSize(20)
        self.coin_table.verticalHeader().setDefaultSectionSize(30)

        self.verticalLayout_8.addWidget(self.coin_table)

        self.middle_panel = QGroupBox(self.tab_trading)
        self.middle_panel.setObjectName(u"middle_panel")
        self.middle_panel.setGeometry(QRect(330, 20, 321, 618))
        self.middle_panel.setMinimumSize(QSize(300, 0))
        font2 = QFont()
        font2.setFamilies([u"\ub9d1\uc740 \uace0\ub515"])
        font2.setPointSize(11)
        font2.setBold(False)
        self.middle_panel.setFont(font2)
        self.middle_panel.setStyleSheet(u"QGroupBox {\n"
"  background-color: white;\n"
"  border: 1px solid #C2C2C2;\n"
"  margin-top: 20px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"  subcontrol-origin: margin;\n"
"  subcontrol-position: top left;\n"
"  padding: 0px 5px 5px 5px;\n"
"}")
        self.verticalLayout_7 = QVBoxLayout(self.middle_panel)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(10, -1, -1, 10)
        self.scrollArea_log = QScrollArea(self.middle_panel)
        self.scrollArea_log.setObjectName(u"scrollArea_log")
        self.scrollArea_log.setWidgetResizable(True)
        self.scrollAreaWidgetContents2 = QWidget()
        self.scrollAreaWidgetContents2.setObjectName(u"scrollAreaWidgetContents2")
        self.scrollAreaWidgetContents2.setGeometry(QRect(0, 0, 295, 530))
        self.scrollArea_log.setWidget(self.scrollAreaWidgetContents2)

        self.verticalLayout_7.addWidget(self.scrollArea_log)

        self.log_clear = QPushButton(self.middle_panel)
        self.log_clear.setObjectName(u"log_clear")
        self.log_clear.setStyleSheet(u"QPushButton {\n"
"  background-color: #E0E0E0;\n"
"  border: 1px solid #C2C2C2;\n"
"  color: #212121;\n"
"  font-weight: bold;\n"
"  padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #D0D0D0;\n"
"}")

        self.verticalLayout_7.addWidget(self.log_clear)

        self.left_panel = QWidget(self.tab_trading)
        self.left_panel.setObjectName(u"left_panel")
        self.left_panel.setGeometry(QRect(0, 20, 330, 618))
        self.left_panel.setMinimumSize(QSize(330, 0))
        self.left_panel.setMaximumSize(QSize(330, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.left_panel)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 0, 10, 0)
        self.groupBox = QGroupBox(self.left_panel)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFont(font1)
        self.groupBox.setStyleSheet(u"QGroupBox {\n"
"  background-color: white;\n"
"  border: 1px solid #C2C2C2;\n"
"  margin-top: 20px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"  subcontrol-origin: margin;\n"
"  subcontrol-position: top left;\n"
"  padding: 0px 5px 5px 5px;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.scrollArea_setting = QScrollArea(self.groupBox)
        self.scrollArea_setting.setObjectName(u"scrollArea_setting")
        self.scrollArea_setting.setEnabled(True)
        self.scrollArea_setting.setWidgetResizable(True)
        self.scrollAreaWidgetContents1 = QWidget()
        self.scrollAreaWidgetContents1.setObjectName(u"scrollAreaWidgetContents1")
        self.scrollAreaWidgetContents1.setGeometry(QRect(0, 0, 282, 442))
        self.scrollArea_setting.setWidget(self.scrollAreaWidgetContents1)

        self.verticalLayout_3.addWidget(self.scrollArea_setting)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.start_button = QPushButton(self.left_panel)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setMinimumSize(QSize(0, 50))
        self.start_button.setStyleSheet(u"QPushButton {\n"
"  background-color: #E0E0E0;\n"
"  border: 1px solid #C2C2C2;\n"
"  color: #212121;\n"
"  font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #D0D0D0;\n"
"}")

        self.verticalLayout_2.addWidget(self.start_button)

        self.stop_button = QPushButton(self.left_panel)
        self.stop_button.setObjectName(u"stop_button")
        self.stop_button.setMinimumSize(QSize(0, 50))
        self.stop_button.setStyleSheet(u"QPushButton {\n"
"  background-color: #E0E0E0;\n"
"  border: 1px solid #C2C2C2;\n"
"  color: #212121;\n"
"  font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #D0D0D0;\n"
"}")

        self.verticalLayout_2.addWidget(self.stop_button)

        self.tabWidget.addTab(self.tab_trading, "")
        self.tab_settings_long = QWidget()
        self.tab_settings_long.setObjectName(u"tab_settings_long")
        self.verticalLayout_settings_long = QVBoxLayout(self.tab_settings_long)
        self.verticalLayout_settings_long.setObjectName(u"verticalLayout_settings_long")
        self.Layout_long_coin_selection = QGroupBox(self.tab_settings_long)
        self.Layout_long_coin_selection.setObjectName(u"Layout_long_coin_selection")
        font3 = QFont()
        font3.setFamilies([u"\ub9d1\uc740 \uace0\ub515"])
        font3.setPointSize(10)
        font3.setBold(True)
        self.Layout_long_coin_selection.setFont(font3)
        self.Layout_long_coin_selection.setStyleSheet(u"QGroupBox {\n"
"  background-color: #FAFAFA;\n"
"  border: 1px solid #E0E0E0;\n"
"  border-radius: 4px;\n"
"  margin-top: 15px;\n"
"  padding-top: 10px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"  subcontrol-origin: margin;\n"
"  subcontrol-position: top left;\n"
"  padding: 0 5px;\n"
"  color: #4CAF50;\n"
"}")
        self.verticalLayout_coin_selection_long = QVBoxLayout(self.Layout_long_coin_selection)
        self.verticalLayout_coin_selection_long.setObjectName(u"verticalLayout_coin_selection_long")
        self.comboBox_coin_selection_long = QComboBox(self.Layout_long_coin_selection)
        self.comboBox_coin_selection_long.addItem("")
        self.comboBox_coin_selection_long.addItem("")
        self.comboBox_coin_selection_long.setObjectName(u"comboBox_coin_selection_long")
        self.comboBox_coin_selection_long.setMinimumSize(QSize(0, 30))
        font4 = QFont()
        font4.setFamilies([u"\ub9d1\uc740 \uace0\ub515"])
        font4.setPointSize(9)
        font4.setBold(False)
        self.comboBox_coin_selection_long.setFont(font4)

        self.verticalLayout_coin_selection_long.addWidget(self.comboBox_coin_selection_long)


        self.verticalLayout_settings_long.addWidget(self.Layout_long_coin_selection)

        self.Layout_long_buy_settings = QGroupBox(self.tab_settings_long)
        self.Layout_long_buy_settings.setObjectName(u"Layout_long_buy_settings")
        self.Layout_long_buy_settings.setFont(font3)
        self.Layout_long_buy_settings.setStyleSheet(u"QGroupBox {\n"
"  background-color: #FAFAFA;\n"
"  border: 1px solid #E0E0E0;\n"
"  border-radius: 4px;\n"
"  margin-top: 15px;\n"
"  padding-top: 10px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"  subcontrol-origin: margin;\n"
"  subcontrol-position: top left;\n"
"  padding: 0 5px;\n"
"  color: #4CAF50;\n"
"}")
        self.verticalLayout_buy_settings_long = QVBoxLayout(self.Layout_long_buy_settings)
        self.verticalLayout_buy_settings_long.setObjectName(u"verticalLayout_buy_settings_long")
        self.buy_signal1_long = QHBoxLayout()
        self.buy_signal1_long.setObjectName(u"buy_signal1_long")
        self.label_signal1_long = QLabel(self.Layout_long_buy_settings)
        self.label_signal1_long.setObjectName(u"label_signal1_long")
        self.label_signal1_long.setMinimumSize(QSize(100, 0))
        self.label_signal1_long.setFont(font4)

        self.buy_signal1_long.addWidget(self.label_signal1_long)

        self.comboBox_signal1_long = QComboBox(self.Layout_long_buy_settings)
        self.comboBox_signal1_long.addItem("")
        self.comboBox_signal1_long.addItem("")
        self.comboBox_signal1_long.addItem("")
        self.comboBox_signal1_long.addItem("")
        self.comboBox_signal1_long.setObjectName(u"comboBox_signal1_long")
        self.comboBox_signal1_long.setMinimumSize(QSize(0, 30))
        self.comboBox_signal1_long.setFont(font4)

        self.buy_signal1_long.addWidget(self.comboBox_signal1_long)

        self.comboBox_timeframe1_long = QComboBox(self.Layout_long_buy_settings)
        self.comboBox_timeframe1_long.addItem("")
        self.comboBox_timeframe1_long.addItem("")
        self.comboBox_timeframe1_long.addItem("")
        self.comboBox_timeframe1_long.addItem("")
        self.comboBox_timeframe1_long.setObjectName(u"comboBox_timeframe1_long")
        self.comboBox_timeframe1_long.setMinimumSize(QSize(0, 30))
        self.comboBox_timeframe1_long.setFont(font4)

        self.buy_signal1_long.addWidget(self.comboBox_timeframe1_long)

        self.btn_detail_signal1_long = QPushButton(self.Layout_long_buy_settings)
        self.btn_detail_signal1_long.setObjectName(u"btn_detail_signal1_long")
        self.btn_detail_signal1_long.setMinimumSize(QSize(0, 30))
        self.btn_detail_signal1_long.setFont(font4)
        self.btn_detail_signal1_long.setStyleSheet(u"QPushButton {\n"
"  background-color: #4CAF50;\n"
"  color: white;\n"
"  border: none;\n"
"  border-radius: 2px;\n"
"}\n"
"QPushButton:hover {\n"
"  background-color: #45a049;\n"
"}")

        self.buy_signal1_long.addWidget(self.btn_detail_signal1_long)


        self.verticalLayout_buy_settings_long.addLayout(self.buy_signal1_long)

        self.buy_signal2_long = QHBoxLayout()
        self.buy_signal2_long.setObjectName(u"buy_signal2_long")
        self.label_signal2_long = QLabel(self.Layout_long_buy_settings)
        self.label_signal2_long.setObjectName(u"label_signal2_long")
        self.label_signal2_long.setMinimumSize(QSize(100, 0))
        self.label_signal2_long.setFont(font4)

        self.buy_signal2_long.addWidget(self.label_signal2_long)

        self.comboBox_signal2_long = QComboBox(self.Layout_long_buy_settings)
        self.comboBox_signal2_long.addItem("")
        self.comboBox_signal2_long.addItem("")
        self.comboBox_signal2_long.addItem("")
        self.comboBox_signal2_long.addItem("")
        self.comboBox_signal2_long.setObjectName(u"comboBox_signal2_long")
        self.comboBox_signal2_long.setMinimumSize(QSize(0, 30))
        self.comboBox_signal2_long.setFont(font4)

        self.buy_signal2_long.addWidget(self.comboBox_signal2_long)

        self.comboBox_timeframe2_long = QComboBox(self.Layout_long_buy_settings)
        self.comboBox_timeframe2_long.addItem("")
        self.comboBox_timeframe2_long.addItem("")
        self.comboBox_timeframe2_long.addItem("")
        self.comboBox_timeframe2_long.addItem("")
        self.comboBox_timeframe2_long.setObjectName(u"comboBox_timeframe2_long")
        self.comboBox_timeframe2_long.setMinimumSize(QSize(0, 30))
        self.comboBox_timeframe2_long.setFont(font4)

        self.buy_signal2_long.addWidget(self.comboBox_timeframe2_long)

        self.btn_detail_signal2_long = QPushButton(self.Layout_long_buy_settings)
        self.btn_detail_signal2_long.setObjectName(u"btn_detail_signal2_long")
        self.btn_detail_signal2_long.setMinimumSize(QSize(0, 30))
        self.btn_detail_signal2_long.setFont(font4)
        self.btn_detail_signal2_long.setStyleSheet(u"QPushButton {\n"
"  background-color: #4CAF50;\n"
"  color: white;\n"
"  border: none;\n"
"  border-radius: 2px;\n"
"}\n"
"QPushButton:hover {\n"
"  background-color: #45a049;\n"
"}")

        self.buy_signal2_long.addWidget(self.btn_detail_signal2_long)


        self.verticalLayout_buy_settings_long.addLayout(self.buy_signal2_long)

        self.line = QFrame(self.Layout_long_buy_settings)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_buy_settings_long.addWidget(self.line)

        self.buy_long_amount = QHBoxLayout()
        self.buy_long_amount.setObjectName(u"buy_long_amount")
        self.label_buy_amount_long = QLabel(self.Layout_long_buy_settings)
        self.label_buy_amount_long.setObjectName(u"label_buy_amount_long")
        self.label_buy_amount_long.setMinimumSize(QSize(100, 0))
        self.label_buy_amount_long.setFont(font4)

        self.buy_long_amount.addWidget(self.label_buy_amount_long)

        self.spinBox_buy_amount_long = QSpinBox(self.Layout_long_buy_settings)
        self.spinBox_buy_amount_long.setObjectName(u"spinBox_buy_amount_long")
        self.spinBox_buy_amount_long.setMinimumSize(QSize(120, 30))
        self.spinBox_buy_amount_long.setFont(font4)
        self.spinBox_buy_amount_long.setMaximum(10000000)
        self.spinBox_buy_amount_long.setSingleStep(1)
        self.spinBox_buy_amount_long.setValue(100)

        self.buy_long_amount.addWidget(self.spinBox_buy_amount_long)

        self.spinBox_additional_long = QSpinBox(self.Layout_long_buy_settings)
        self.spinBox_additional_long.setObjectName(u"spinBox_additional_long")
        self.spinBox_additional_long.setMinimumSize(QSize(120, 30))
        self.spinBox_additional_long.setFont(font4)
        self.spinBox_additional_long.setMaximum(100)
        self.spinBox_additional_long.setValue(50)

        self.buy_long_amount.addWidget(self.spinBox_additional_long)

        self.checkBox_split_buy_long = QCheckBox(self.Layout_long_buy_settings)
        self.checkBox_split_buy_long.setObjectName(u"checkBox_split_buy_long")
        self.checkBox_split_buy_long.setFont(font4)

        self.buy_long_amount.addWidget(self.checkBox_split_buy_long)


        self.verticalLayout_buy_settings_long.addLayout(self.buy_long_amount)

        self.buy_split1_long = QHBoxLayout()
        self.buy_split1_long.setObjectName(u"buy_split1_long")
        self.checkBox1_split_long = QCheckBox(self.Layout_long_buy_settings)
        self.checkBox1_split_long.setObjectName(u"checkBox1_split_long")
        self.checkBox1_split_long.setFont(font4)

        self.buy_split1_long.addWidget(self.checkBox1_split_long)

        self.spinBox1_split1_long = QSpinBox(self.Layout_long_buy_settings)
        self.spinBox1_split1_long.setObjectName(u"spinBox1_split1_long")
        self.spinBox1_split1_long.setMinimumSize(QSize(120, 30))
        self.spinBox1_split1_long.setFont(font4)
        self.spinBox1_split1_long.setMaximum(10000000)
        self.spinBox1_split1_long.setSingleStep(1)
        self.spinBox1_split1_long.setValue(5)

        self.buy_split1_long.addWidget(self.spinBox1_split1_long)

        self.label1_split1_long = QLabel(self.Layout_long_buy_settings)
        self.label1_split1_long.setObjectName(u"label1_split1_long")
        self.label1_split1_long.setFont(font4)

        self.buy_split1_long.addWidget(self.label1_split1_long)

        self.spinBox2_split1_long = QSpinBox(self.Layout_long_buy_settings)
        self.spinBox2_split1_long.setObjectName(u"spinBox2_split1_long")
        self.spinBox2_split1_long.setMinimumSize(QSize(120, 30))
        self.spinBox2_split1_long.setFont(font4)
        self.spinBox2_split1_long.setMaximum(10000000)
        self.spinBox2_split1_long.setSingleStep(1)
        self.spinBox2_split1_long.setValue(10)

        self.buy_split1_long.addWidget(self.spinBox2_split1_long)

        self.spinBox3_split1_long = QSpinBox(self.Layout_long_buy_settings)
        self.spinBox3_split1_long.setObjectName(u"spinBox3_split1_long")
        self.spinBox3_split1_long.setMinimumSize(QSize(120, 30))
        self.spinBox3_split1_long.setFont(font4)
        self.spinBox3_split1_long.setMaximum(10000000)
        self.spinBox3_split1_long.setSingleStep(1)
        self.spinBox3_split1_long.setValue(10)

        self.buy_split1_long.addWidget(self.spinBox3_split1_long)

        self.label2_split1_long = QLabel(self.Layout_long_buy_settings)
        self.label2_split1_long.setObjectName(u"label2_split1_long")
        self.label2_split1_long.setFont(font4)

        self.buy_split1_long.addWidget(self.label2_split1_long)


        self.verticalLayout_buy_settings_long.addLayout(self.buy_split1_long)

        self.buy_split2_long = QHBoxLayout()
        self.buy_split2_long.setObjectName(u"buy_split2_long")
        self.checkBox2_split_long = QCheckBox(self.Layout_long_buy_settings)
        self.checkBox2_split_long.setObjectName(u"checkBox2_split_long")
        self.checkBox2_split_long.setFont(font4)

        self.buy_split2_long.addWidget(self.checkBox2_split_long)

        self.spinBox1_split2_long = QSpinBox(self.Layout_long_buy_settings)
        self.spinBox1_split2_long.setObjectName(u"spinBox1_split2_long")
        self.spinBox1_split2_long.setMinimumSize(QSize(120, 30))
        self.spinBox1_split2_long.setFont(font4)
        self.spinBox1_split2_long.setMaximum(10000000)
        self.spinBox1_split2_long.setSingleStep(1)
        self.spinBox1_split2_long.setValue(200)

        self.buy_split2_long.addWidget(self.spinBox1_split2_long)

        self.label1_split2_long = QLabel(self.Layout_long_buy_settings)
        self.label1_split2_long.setObjectName(u"label1_split2_long")
        self.label1_split2_long.setFont(font4)

        self.buy_split2_long.addWidget(self.label1_split2_long)

        self.spinBox2_split2_long = QSpinBox(self.Layout_long_buy_settings)
        self.spinBox2_split2_long.setObjectName(u"spinBox2_split2_long")
        self.spinBox2_split2_long.setMinimumSize(QSize(120, 30))
        self.spinBox2_split2_long.setFont(font4)
        self.spinBox2_split2_long.setMaximum(10000000)
        self.spinBox2_split2_long.setSingleStep(1)
        self.spinBox2_split2_long.setValue(10)

        self.buy_split2_long.addWidget(self.spinBox2_split2_long)

        self.spinBox3_split2_long = QSpinBox(self.Layout_long_buy_settings)
        self.spinBox3_split2_long.setObjectName(u"spinBox3_split2_long")
        self.spinBox3_split2_long.setMinimumSize(QSize(120, 30))
        self.spinBox3_split2_long.setFont(font4)
        self.spinBox3_split2_long.setMaximum(10000000)
        self.spinBox3_split2_long.setSingleStep(1)
        self.spinBox3_split2_long.setValue(10)

        self.buy_split2_long.addWidget(self.spinBox3_split2_long)

        self.label2_split2_long = QLabel(self.Layout_long_buy_settings)
        self.label2_split2_long.setObjectName(u"label2_split2_long")
        self.label2_split2_long.setFont(font4)

        self.buy_split2_long.addWidget(self.label2_split2_long)


        self.verticalLayout_buy_settings_long.addLayout(self.buy_split2_long)


        self.verticalLayout_settings_long.addWidget(self.Layout_long_buy_settings)

        self.Layout_long_sell_settings = QGroupBox(self.tab_settings_long)
        self.Layout_long_sell_settings.setObjectName(u"Layout_long_sell_settings")
        self.Layout_long_sell_settings.setFont(font3)
        self.Layout_long_sell_settings.setStyleSheet(u"QGroupBox {\n"
"  background-color: #FAFAFA;\n"
"  border: 1px solid #E0E0E0;\n"
"  border-radius: 4px;\n"
"  margin-top: 15px;\n"
"  padding-top: 10px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"  subcontrol-origin: margin;\n"
"  subcontrol-position: top left;\n"
"  padding: 0 5px;\n"
"  color: #2196F3;\n"
"}")
        self.verticalLayout_sell_settings_long = QVBoxLayout(self.Layout_long_sell_settings)
        self.verticalLayout_sell_settings_long.setObjectName(u"verticalLayout_sell_settings_long")
        self.Layout_long_sell1 = QHBoxLayout()
        self.Layout_long_sell1.setObjectName(u"Layout_long_sell1")
        self.label_profit_cut_long = QLabel(self.Layout_long_sell_settings)
        self.label_profit_cut_long.setObjectName(u"label_profit_cut_long")
        self.label_profit_cut_long.setMinimumSize(QSize(50, 0))
        self.label_profit_cut_long.setFont(font4)

        self.Layout_long_sell1.addWidget(self.label_profit_cut_long)

        self.checkBox_takeprofit1_long = QCheckBox(self.Layout_long_sell_settings)
        self.checkBox_takeprofit1_long.setObjectName(u"checkBox_takeprofit1_long")
        self.checkBox_takeprofit1_long.setFont(font4)

        self.Layout_long_sell1.addWidget(self.checkBox_takeprofit1_long)

        self.doubleSpinBox_profit_rate_long = QDoubleSpinBox(self.Layout_long_sell_settings)
        self.doubleSpinBox_profit_rate_long.setObjectName(u"doubleSpinBox_profit_rate_long")
        self.doubleSpinBox_profit_rate_long.setMinimumSize(QSize(100, 30))
        self.doubleSpinBox_profit_rate_long.setFont(font4)
        self.doubleSpinBox_profit_rate_long.setDecimals(1)
        self.doubleSpinBox_profit_rate_long.setMaximum(100.000000000000000)
        self.doubleSpinBox_profit_rate_long.setSingleStep(0.100000000000000)
        self.doubleSpinBox_profit_rate_long.setValue(30.000000000000000)

        self.Layout_long_sell1.addWidget(self.doubleSpinBox_profit_rate_long)

        self.label_profit_condition_long = QLabel(self.Layout_long_sell_settings)
        self.label_profit_condition_long.setObjectName(u"label_profit_condition_long")
        self.label_profit_condition_long.setFont(font4)

        self.Layout_long_sell1.addWidget(self.label_profit_condition_long)

        self.checkBox_takeprofit2_long = QCheckBox(self.Layout_long_sell_settings)
        self.checkBox_takeprofit2_long.setObjectName(u"checkBox_takeprofit2_long")
        self.checkBox_takeprofit2_long.setFont(font4)

        self.Layout_long_sell1.addWidget(self.checkBox_takeprofit2_long)

        self.spinBox_takeprofit1_long = QSpinBox(self.Layout_long_sell_settings)
        self.spinBox_takeprofit1_long.setObjectName(u"spinBox_takeprofit1_long")
        self.spinBox_takeprofit1_long.setMinimumSize(QSize(120, 30))
        self.spinBox_takeprofit1_long.setFont(font4)
        self.spinBox_takeprofit1_long.setMaximum(10000000)
        self.spinBox_takeprofit1_long.setSingleStep(1)
        self.spinBox_takeprofit1_long.setValue(200)

        self.Layout_long_sell1.addWidget(self.spinBox_takeprofit1_long)

        self.label_profit_condition_2_long = QLabel(self.Layout_long_sell_settings)
        self.label_profit_condition_2_long.setObjectName(u"label_profit_condition_2_long")
        self.label_profit_condition_2_long.setFont(font4)

        self.Layout_long_sell1.addWidget(self.label_profit_condition_2_long)

        self.Layout_long_sell1.setStretch(0, 1)
        self.Layout_long_sell1.setStretch(2, 1)
        self.Layout_long_sell1.setStretch(3, 1)
        self.Layout_long_sell1.setStretch(5, 1)
        self.Layout_long_sell1.setStretch(6, 1)

        self.verticalLayout_sell_settings_long.addLayout(self.Layout_long_sell1)

        self.Layout_long_sell2 = QHBoxLayout()
        self.Layout_long_sell2.setObjectName(u"Layout_long_sell2")
        self.label_loss_cut_long = QLabel(self.Layout_long_sell_settings)
        self.label_loss_cut_long.setObjectName(u"label_loss_cut_long")
        self.label_loss_cut_long.setMinimumSize(QSize(50, 0))
        self.label_loss_cut_long.setFont(font4)

        self.Layout_long_sell2.addWidget(self.label_loss_cut_long)

        self.checkBox_stoploss1_long = QCheckBox(self.Layout_long_sell_settings)
        self.checkBox_stoploss1_long.setObjectName(u"checkBox_stoploss1_long")
        self.checkBox_stoploss1_long.setFont(font4)

        self.Layout_long_sell2.addWidget(self.checkBox_stoploss1_long)

        self.doubleSpinBox_loss_rate_long = QDoubleSpinBox(self.Layout_long_sell_settings)
        self.doubleSpinBox_loss_rate_long.setObjectName(u"doubleSpinBox_loss_rate_long")
        self.doubleSpinBox_loss_rate_long.setMinimumSize(QSize(100, 30))
        self.doubleSpinBox_loss_rate_long.setFont(font4)
        self.doubleSpinBox_loss_rate_long.setDecimals(1)
        self.doubleSpinBox_loss_rate_long.setMaximum(100.000000000000000)
        self.doubleSpinBox_loss_rate_long.setSingleStep(0.100000000000000)
        self.doubleSpinBox_loss_rate_long.setValue(20.000000000000000)

        self.Layout_long_sell2.addWidget(self.doubleSpinBox_loss_rate_long)

        self.label_loss_condition_long = QLabel(self.Layout_long_sell_settings)
        self.label_loss_condition_long.setObjectName(u"label_loss_condition_long")
        self.label_loss_condition_long.setFont(font4)

        self.Layout_long_sell2.addWidget(self.label_loss_condition_long)

        self.checkBox_stoploss2_long = QCheckBox(self.Layout_long_sell_settings)
        self.checkBox_stoploss2_long.setObjectName(u"checkBox_stoploss2_long")
        self.checkBox_stoploss2_long.setFont(font4)

        self.Layout_long_sell2.addWidget(self.checkBox_stoploss2_long)

        self.spinBox_stoploss1_long = QSpinBox(self.Layout_long_sell_settings)
        self.spinBox_stoploss1_long.setObjectName(u"spinBox_stoploss1_long")
        self.spinBox_stoploss1_long.setMinimumSize(QSize(120, 30))
        self.spinBox_stoploss1_long.setFont(font4)
        self.spinBox_stoploss1_long.setMaximum(10000000)
        self.spinBox_stoploss1_long.setSingleStep(1)
        self.spinBox_stoploss1_long.setValue(200)

        self.Layout_long_sell2.addWidget(self.spinBox_stoploss1_long)

        self.label_profit_condition_3_long = QLabel(self.Layout_long_sell_settings)
        self.label_profit_condition_3_long.setObjectName(u"label_profit_condition_3_long")
        self.label_profit_condition_3_long.setFont(font4)

        self.Layout_long_sell2.addWidget(self.label_profit_condition_3_long)

        self.Layout_long_sell2.setStretch(0, 1)
        self.Layout_long_sell2.setStretch(2, 1)
        self.Layout_long_sell2.setStretch(3, 1)
        self.Layout_long_sell2.setStretch(5, 1)
        self.Layout_long_sell2.setStretch(6, 1)

        self.verticalLayout_sell_settings_long.addLayout(self.Layout_long_sell2)


        self.verticalLayout_settings_long.addWidget(self.Layout_long_sell_settings)

        self.button_save_long = QPushButton(self.tab_settings_long)
        self.button_save_long.setObjectName(u"button_save_long")

        self.verticalLayout_settings_long.addWidget(self.button_save_long)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_settings_long.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.tab_settings_long, "")
        self.tab_settings_short = QWidget()
        self.tab_settings_short.setObjectName(u"tab_settings_short")
        font5 = QFont()
        font5.setPointSize(13)
        self.tab_settings_short.setFont(font5)
        self.verticalLayout_settings_short = QVBoxLayout(self.tab_settings_short)
        self.verticalLayout_settings_short.setObjectName(u"verticalLayout_settings_short")
        self.Layout_short_coin_selection = QGroupBox(self.tab_settings_short)
        self.Layout_short_coin_selection.setObjectName(u"Layout_short_coin_selection")
        self.Layout_short_coin_selection.setFont(font3)
        self.Layout_short_coin_selection.setStyleSheet(u"QGroupBox {\n"
"  background-color: #FAFAFA;\n"
"  border: 1px solid #E0E0E0;\n"
"  border-radius: 4px;\n"
"  margin-top: 15px;\n"
"  padding-top: 10px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"  subcontrol-origin: margin;\n"
"  subcontrol-position: top left;\n"
"  padding: 0 5px;\n"
"  color: #4CAF50;\n"
"}")
        self.verticalLayout_coin_selection_short = QVBoxLayout(self.Layout_short_coin_selection)
        self.verticalLayout_coin_selection_short.setObjectName(u"verticalLayout_coin_selection_short")
        self.comboBox_coin_selection_short = QComboBox(self.Layout_short_coin_selection)
        self.comboBox_coin_selection_short.addItem("")
        self.comboBox_coin_selection_short.addItem("")
        self.comboBox_coin_selection_short.setObjectName(u"comboBox_coin_selection_short")
        self.comboBox_coin_selection_short.setMinimumSize(QSize(0, 30))
        self.comboBox_coin_selection_short.setFont(font4)

        self.verticalLayout_coin_selection_short.addWidget(self.comboBox_coin_selection_short)


        self.verticalLayout_settings_short.addWidget(self.Layout_short_coin_selection)

        self.Layout_short_buy_settings = QGroupBox(self.tab_settings_short)
        self.Layout_short_buy_settings.setObjectName(u"Layout_short_buy_settings")
        self.Layout_short_buy_settings.setFont(font3)
        self.Layout_short_buy_settings.setStyleSheet(u"QGroupBox {\n"
"  background-color: #FAFAFA;\n"
"  border: 1px solid #E0E0E0;\n"
"  border-radius: 4px;\n"
"  margin-top: 15px;\n"
"  padding-top: 10px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"  subcontrol-origin: margin;\n"
"  subcontrol-position: top left;\n"
"  padding: 0 5px;\n"
"  color: #4CAF50;\n"
"}")
        self.verticalLayout_buy_settings_short = QVBoxLayout(self.Layout_short_buy_settings)
        self.verticalLayout_buy_settings_short.setObjectName(u"verticalLayout_buy_settings_short")
        self.buy_signal1_short = QHBoxLayout()
        self.buy_signal1_short.setObjectName(u"buy_signal1_short")
        self.label_signal1_short = QLabel(self.Layout_short_buy_settings)
        self.label_signal1_short.setObjectName(u"label_signal1_short")
        self.label_signal1_short.setMinimumSize(QSize(100, 0))
        self.label_signal1_short.setFont(font4)

        self.buy_signal1_short.addWidget(self.label_signal1_short)

        self.comboBox_signal1_short = QComboBox(self.Layout_short_buy_settings)
        self.comboBox_signal1_short.addItem("")
        self.comboBox_signal1_short.addItem("")
        self.comboBox_signal1_short.addItem("")
        self.comboBox_signal1_short.addItem("")
        self.comboBox_signal1_short.setObjectName(u"comboBox_signal1_short")
        self.comboBox_signal1_short.setMinimumSize(QSize(0, 30))
        self.comboBox_signal1_short.setFont(font4)

        self.buy_signal1_short.addWidget(self.comboBox_signal1_short)

        self.comboBox_timeframe1_short = QComboBox(self.Layout_short_buy_settings)
        self.comboBox_timeframe1_short.addItem("")
        self.comboBox_timeframe1_short.addItem("")
        self.comboBox_timeframe1_short.addItem("")
        self.comboBox_timeframe1_short.addItem("")
        self.comboBox_timeframe1_short.setObjectName(u"comboBox_timeframe1_short")
        self.comboBox_timeframe1_short.setMinimumSize(QSize(0, 30))
        self.comboBox_timeframe1_short.setFont(font4)

        self.buy_signal1_short.addWidget(self.comboBox_timeframe1_short)

        self.btn_detail_signal1_short = QPushButton(self.Layout_short_buy_settings)
        self.btn_detail_signal1_short.setObjectName(u"btn_detail_signal1_short")
        self.btn_detail_signal1_short.setMinimumSize(QSize(0, 30))
        self.btn_detail_signal1_short.setFont(font4)
        self.btn_detail_signal1_short.setStyleSheet(u"QPushButton {\n"
"  background-color: #4CAF50;\n"
"  color: white;\n"
"  border: none;\n"
"  border-radius: 2px;\n"
"}\n"
"QPushButton:hover {\n"
"  background-color: #45a049;\n"
"}")

        self.buy_signal1_short.addWidget(self.btn_detail_signal1_short)


        self.verticalLayout_buy_settings_short.addLayout(self.buy_signal1_short)

        self.buy_signal2_short = QHBoxLayout()
        self.buy_signal2_short.setObjectName(u"buy_signal2_short")
        self.label_signal2_short = QLabel(self.Layout_short_buy_settings)
        self.label_signal2_short.setObjectName(u"label_signal2_short")
        self.label_signal2_short.setMinimumSize(QSize(100, 0))
        self.label_signal2_short.setFont(font4)

        self.buy_signal2_short.addWidget(self.label_signal2_short)

        self.comboBox_signal2_short = QComboBox(self.Layout_short_buy_settings)
        self.comboBox_signal2_short.addItem("")
        self.comboBox_signal2_short.addItem("")
        self.comboBox_signal2_short.addItem("")
        self.comboBox_signal2_short.addItem("")
        self.comboBox_signal2_short.setObjectName(u"comboBox_signal2_short")
        self.comboBox_signal2_short.setMinimumSize(QSize(0, 30))
        self.comboBox_signal2_short.setFont(font4)

        self.buy_signal2_short.addWidget(self.comboBox_signal2_short)

        self.comboBox_timeframe2_short = QComboBox(self.Layout_short_buy_settings)
        self.comboBox_timeframe2_short.addItem("")
        self.comboBox_timeframe2_short.addItem("")
        self.comboBox_timeframe2_short.addItem("")
        self.comboBox_timeframe2_short.addItem("")
        self.comboBox_timeframe2_short.setObjectName(u"comboBox_timeframe2_short")
        self.comboBox_timeframe2_short.setMinimumSize(QSize(0, 30))
        self.comboBox_timeframe2_short.setFont(font4)

        self.buy_signal2_short.addWidget(self.comboBox_timeframe2_short)

        self.btn_detail_signal2_short = QPushButton(self.Layout_short_buy_settings)
        self.btn_detail_signal2_short.setObjectName(u"btn_detail_signal2_short")
        self.btn_detail_signal2_short.setMinimumSize(QSize(0, 30))
        self.btn_detail_signal2_short.setFont(font4)
        self.btn_detail_signal2_short.setStyleSheet(u"QPushButton {\n"
"  background-color: #4CAF50;\n"
"  color: white;\n"
"  border: none;\n"
"  border-radius: 2px;\n"
"}\n"
"QPushButton:hover {\n"
"  background-color: #45a049;\n"
"}")

        self.buy_signal2_short.addWidget(self.btn_detail_signal2_short)


        self.verticalLayout_buy_settings_short.addLayout(self.buy_signal2_short)

        self.line1 = QFrame(self.Layout_short_buy_settings)
        self.line1.setObjectName(u"line1")
        self.line1.setFrameShape(QFrame.Shape.HLine)
        self.line1.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_buy_settings_short.addWidget(self.line1)

        self.buy_short_amount = QHBoxLayout()
        self.buy_short_amount.setObjectName(u"buy_short_amount")
        self.label_buy_amount_short = QLabel(self.Layout_short_buy_settings)
        self.label_buy_amount_short.setObjectName(u"label_buy_amount_short")
        self.label_buy_amount_short.setMinimumSize(QSize(100, 0))
        self.label_buy_amount_short.setFont(font4)

        self.buy_short_amount.addWidget(self.label_buy_amount_short)

        self.spinBox_buy_amount_short = QSpinBox(self.Layout_short_buy_settings)
        self.spinBox_buy_amount_short.setObjectName(u"spinBox_buy_amount_short")
        self.spinBox_buy_amount_short.setMinimumSize(QSize(120, 30))
        self.spinBox_buy_amount_short.setFont(font4)
        self.spinBox_buy_amount_short.setMaximum(10000000)
        self.spinBox_buy_amount_short.setSingleStep(1)
        self.spinBox_buy_amount_short.setValue(100)

        self.buy_short_amount.addWidget(self.spinBox_buy_amount_short)

        self.spinBox_additional_short = QSpinBox(self.Layout_short_buy_settings)
        self.spinBox_additional_short.setObjectName(u"spinBox_additional_short")
        self.spinBox_additional_short.setMinimumSize(QSize(120, 30))
        self.spinBox_additional_short.setFont(font4)
        self.spinBox_additional_short.setMaximum(100)
        self.spinBox_additional_short.setValue(50)

        self.buy_short_amount.addWidget(self.spinBox_additional_short)

        self.checkBox_split_buy_short = QCheckBox(self.Layout_short_buy_settings)
        self.checkBox_split_buy_short.setObjectName(u"checkBox_split_buy_short")
        self.checkBox_split_buy_short.setFont(font4)

        self.buy_short_amount.addWidget(self.checkBox_split_buy_short)


        self.verticalLayout_buy_settings_short.addLayout(self.buy_short_amount)

        self.buy_split1_short = QHBoxLayout()
        self.buy_split1_short.setObjectName(u"buy_split1_short")
        self.checkBox1_split_short = QCheckBox(self.Layout_short_buy_settings)
        self.checkBox1_split_short.setObjectName(u"checkBox1_split_short")
        self.checkBox1_split_short.setFont(font4)

        self.buy_split1_short.addWidget(self.checkBox1_split_short)

        self.spinBox1_split1_short = QSpinBox(self.Layout_short_buy_settings)
        self.spinBox1_split1_short.setObjectName(u"spinBox1_split1_short")
        self.spinBox1_split1_short.setMinimumSize(QSize(120, 30))
        self.spinBox1_split1_short.setFont(font4)
        self.spinBox1_split1_short.setMaximum(10000000)
        self.spinBox1_split1_short.setSingleStep(1)
        self.spinBox1_split1_short.setValue(5)

        self.buy_split1_short.addWidget(self.spinBox1_split1_short)

        self.label1_split1_short = QLabel(self.Layout_short_buy_settings)
        self.label1_split1_short.setObjectName(u"label1_split1_short")
        self.label1_split1_short.setFont(font4)

        self.buy_split1_short.addWidget(self.label1_split1_short)

        self.spinBox2_split1_short = QSpinBox(self.Layout_short_buy_settings)
        self.spinBox2_split1_short.setObjectName(u"spinBox2_split1_short")
        self.spinBox2_split1_short.setMinimumSize(QSize(120, 30))
        self.spinBox2_split1_short.setFont(font4)
        self.spinBox2_split1_short.setMaximum(10000000)
        self.spinBox2_split1_short.setSingleStep(1)
        self.spinBox2_split1_short.setValue(10)

        self.buy_split1_short.addWidget(self.spinBox2_split1_short)

        self.spinBox3_split1_short = QSpinBox(self.Layout_short_buy_settings)
        self.spinBox3_split1_short.setObjectName(u"spinBox3_split1_short")
        self.spinBox3_split1_short.setMinimumSize(QSize(120, 30))
        self.spinBox3_split1_short.setFont(font4)
        self.spinBox3_split1_short.setMaximum(10000000)
        self.spinBox3_split1_short.setSingleStep(1)
        self.spinBox3_split1_short.setValue(10)

        self.buy_split1_short.addWidget(self.spinBox3_split1_short)

        self.label2_split1_short = QLabel(self.Layout_short_buy_settings)
        self.label2_split1_short.setObjectName(u"label2_split1_short")
        self.label2_split1_short.setFont(font4)

        self.buy_split1_short.addWidget(self.label2_split1_short)


        self.verticalLayout_buy_settings_short.addLayout(self.buy_split1_short)

        self.buy_split2_short = QHBoxLayout()
        self.buy_split2_short.setObjectName(u"buy_split2_short")
        self.checkBox2_split_short = QCheckBox(self.Layout_short_buy_settings)
        self.checkBox2_split_short.setObjectName(u"checkBox2_split_short")
        self.checkBox2_split_short.setFont(font4)

        self.buy_split2_short.addWidget(self.checkBox2_split_short)

        self.spinBox1_split2_short = QSpinBox(self.Layout_short_buy_settings)
        self.spinBox1_split2_short.setObjectName(u"spinBox1_split2_short")
        self.spinBox1_split2_short.setMinimumSize(QSize(120, 30))
        self.spinBox1_split2_short.setFont(font4)
        self.spinBox1_split2_short.setMaximum(10000000)
        self.spinBox1_split2_short.setSingleStep(1)
        self.spinBox1_split2_short.setValue(200)

        self.buy_split2_short.addWidget(self.spinBox1_split2_short)

        self.label1_split2_short = QLabel(self.Layout_short_buy_settings)
        self.label1_split2_short.setObjectName(u"label1_split2_short")
        self.label1_split2_short.setFont(font4)

        self.buy_split2_short.addWidget(self.label1_split2_short)

        self.spinBox2_split2_short = QSpinBox(self.Layout_short_buy_settings)
        self.spinBox2_split2_short.setObjectName(u"spinBox2_split2_short")
        self.spinBox2_split2_short.setMinimumSize(QSize(120, 30))
        self.spinBox2_split2_short.setFont(font4)
        self.spinBox2_split2_short.setMaximum(10000000)
        self.spinBox2_split2_short.setSingleStep(1)
        self.spinBox2_split2_short.setValue(10)

        self.buy_split2_short.addWidget(self.spinBox2_split2_short)

        self.spinBox3_split2_short = QSpinBox(self.Layout_short_buy_settings)
        self.spinBox3_split2_short.setObjectName(u"spinBox3_split2_short")
        self.spinBox3_split2_short.setMinimumSize(QSize(120, 30))
        self.spinBox3_split2_short.setFont(font4)
        self.spinBox3_split2_short.setMaximum(10000000)
        self.spinBox3_split2_short.setSingleStep(1)
        self.spinBox3_split2_short.setValue(10)

        self.buy_split2_short.addWidget(self.spinBox3_split2_short)

        self.label2_split2_short = QLabel(self.Layout_short_buy_settings)
        self.label2_split2_short.setObjectName(u"label2_split2_short")
        self.label2_split2_short.setFont(font4)

        self.buy_split2_short.addWidget(self.label2_split2_short)


        self.verticalLayout_buy_settings_short.addLayout(self.buy_split2_short)


        self.verticalLayout_settings_short.addWidget(self.Layout_short_buy_settings)

        self.Layout_short_sell_settings = QGroupBox(self.tab_settings_short)
        self.Layout_short_sell_settings.setObjectName(u"Layout_short_sell_settings")
        self.Layout_short_sell_settings.setFont(font3)
        self.Layout_short_sell_settings.setStyleSheet(u"QGroupBox {\n"
"  background-color: #FAFAFA;\n"
"  border: 1px solid #E0E0E0;\n"
"  border-radius: 4px;\n"
"  margin-top: 15px;\n"
"  padding-top: 10px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"  subcontrol-origin: margin;\n"
"  subcontrol-position: top left;\n"
"  padding: 0 5px;\n"
"  color: #2196F3;\n"
"}")
        self.verticalLayout_sell_settings_short = QVBoxLayout(self.Layout_short_sell_settings)
        self.verticalLayout_sell_settings_short.setObjectName(u"verticalLayout_sell_settings_short")
        self.Layout_short_sell1 = QHBoxLayout()
        self.Layout_short_sell1.setObjectName(u"Layout_short_sell1")
        self.label_profit_cut_short = QLabel(self.Layout_short_sell_settings)
        self.label_profit_cut_short.setObjectName(u"label_profit_cut_short")
        self.label_profit_cut_short.setMinimumSize(QSize(50, 0))
        self.label_profit_cut_short.setFont(font4)

        self.Layout_short_sell1.addWidget(self.label_profit_cut_short)

        self.checkBox_takeprofit1_short = QCheckBox(self.Layout_short_sell_settings)
        self.checkBox_takeprofit1_short.setObjectName(u"checkBox_takeprofit1_short")
        self.checkBox_takeprofit1_short.setFont(font4)

        self.Layout_short_sell1.addWidget(self.checkBox_takeprofit1_short)

        self.doubleSpinBox_profit_rate_short = QDoubleSpinBox(self.Layout_short_sell_settings)
        self.doubleSpinBox_profit_rate_short.setObjectName(u"doubleSpinBox_profit_rate_short")
        self.doubleSpinBox_profit_rate_short.setMinimumSize(QSize(100, 30))
        self.doubleSpinBox_profit_rate_short.setFont(font4)
        self.doubleSpinBox_profit_rate_short.setDecimals(1)
        self.doubleSpinBox_profit_rate_short.setMaximum(100.000000000000000)
        self.doubleSpinBox_profit_rate_short.setSingleStep(0.100000000000000)
        self.doubleSpinBox_profit_rate_short.setValue(30.000000000000000)

        self.Layout_short_sell1.addWidget(self.doubleSpinBox_profit_rate_short)

        self.label_profit_condition_short = QLabel(self.Layout_short_sell_settings)
        self.label_profit_condition_short.setObjectName(u"label_profit_condition_short")
        self.label_profit_condition_short.setFont(font4)

        self.Layout_short_sell1.addWidget(self.label_profit_condition_short)

        self.checkBox_takeprofit2_short = QCheckBox(self.Layout_short_sell_settings)
        self.checkBox_takeprofit2_short.setObjectName(u"checkBox_takeprofit2_short")
        self.checkBox_takeprofit2_short.setFont(font4)

        self.Layout_short_sell1.addWidget(self.checkBox_takeprofit2_short)

        self.spinBox_takeprofit1_short = QSpinBox(self.Layout_short_sell_settings)
        self.spinBox_takeprofit1_short.setObjectName(u"spinBox_takeprofit1_short")
        self.spinBox_takeprofit1_short.setMinimumSize(QSize(120, 30))
        self.spinBox_takeprofit1_short.setFont(font4)
        self.spinBox_takeprofit1_short.setMaximum(10000000)
        self.spinBox_takeprofit1_short.setSingleStep(1)
        self.spinBox_takeprofit1_short.setValue(200)

        self.Layout_short_sell1.addWidget(self.spinBox_takeprofit1_short)

        self.label_profit_condition_2_short = QLabel(self.Layout_short_sell_settings)
        self.label_profit_condition_2_short.setObjectName(u"label_profit_condition_2_short")
        self.label_profit_condition_2_short.setFont(font4)

        self.Layout_short_sell1.addWidget(self.label_profit_condition_2_short)

        self.Layout_short_sell1.setStretch(0, 1)
        self.Layout_short_sell1.setStretch(2, 1)
        self.Layout_short_sell1.setStretch(3, 1)
        self.Layout_short_sell1.setStretch(5, 1)
        self.Layout_short_sell1.setStretch(6, 1)

        self.verticalLayout_sell_settings_short.addLayout(self.Layout_short_sell1)

        self.Layout_short_sell2 = QHBoxLayout()
        self.Layout_short_sell2.setObjectName(u"Layout_short_sell2")
        self.label_loss_cut_short = QLabel(self.Layout_short_sell_settings)
        self.label_loss_cut_short.setObjectName(u"label_loss_cut_short")
        self.label_loss_cut_short.setMinimumSize(QSize(50, 0))
        self.label_loss_cut_short.setFont(font4)

        self.Layout_short_sell2.addWidget(self.label_loss_cut_short)

        self.checkBox_stoploss1_short = QCheckBox(self.Layout_short_sell_settings)
        self.checkBox_stoploss1_short.setObjectName(u"checkBox_stoploss1_short")
        self.checkBox_stoploss1_short.setFont(font4)

        self.Layout_short_sell2.addWidget(self.checkBox_stoploss1_short)

        self.doubleSpinBox_loss_rate_short = QDoubleSpinBox(self.Layout_short_sell_settings)
        self.doubleSpinBox_loss_rate_short.setObjectName(u"doubleSpinBox_loss_rate_short")
        self.doubleSpinBox_loss_rate_short.setMinimumSize(QSize(100, 30))
        self.doubleSpinBox_loss_rate_short.setFont(font4)
        self.doubleSpinBox_loss_rate_short.setDecimals(1)
        self.doubleSpinBox_loss_rate_short.setMaximum(100.000000000000000)
        self.doubleSpinBox_loss_rate_short.setSingleStep(0.100000000000000)
        self.doubleSpinBox_loss_rate_short.setValue(20.000000000000000)

        self.Layout_short_sell2.addWidget(self.doubleSpinBox_loss_rate_short)

        self.label_loss_condition_short = QLabel(self.Layout_short_sell_settings)
        self.label_loss_condition_short.setObjectName(u"label_loss_condition_short")
        self.label_loss_condition_short.setFont(font4)

        self.Layout_short_sell2.addWidget(self.label_loss_condition_short)

        self.checkBox_stoploss2_short = QCheckBox(self.Layout_short_sell_settings)
        self.checkBox_stoploss2_short.setObjectName(u"checkBox_stoploss2_short")
        self.checkBox_stoploss2_short.setFont(font4)

        self.Layout_short_sell2.addWidget(self.checkBox_stoploss2_short)

        self.spinBox_stoploss1_short = QSpinBox(self.Layout_short_sell_settings)
        self.spinBox_stoploss1_short.setObjectName(u"spinBox_stoploss1_short")
        self.spinBox_stoploss1_short.setMinimumSize(QSize(120, 30))
        self.spinBox_stoploss1_short.setFont(font4)
        self.spinBox_stoploss1_short.setMaximum(10000000)
        self.spinBox_stoploss1_short.setSingleStep(1)
        self.spinBox_stoploss1_short.setValue(200)

        self.Layout_short_sell2.addWidget(self.spinBox_stoploss1_short)

        self.label_profit_condition_3_short = QLabel(self.Layout_short_sell_settings)
        self.label_profit_condition_3_short.setObjectName(u"label_profit_condition_3_short")
        self.label_profit_condition_3_short.setFont(font4)

        self.Layout_short_sell2.addWidget(self.label_profit_condition_3_short)

        self.Layout_short_sell2.setStretch(0, 1)
        self.Layout_short_sell2.setStretch(2, 1)
        self.Layout_short_sell2.setStretch(3, 1)
        self.Layout_short_sell2.setStretch(5, 1)
        self.Layout_short_sell2.setStretch(6, 1)

        self.verticalLayout_sell_settings_short.addLayout(self.Layout_short_sell2)


        self.verticalLayout_settings_short.addWidget(self.Layout_short_sell_settings)

        self.button_save_short = QPushButton(self.tab_settings_short)
        self.button_save_short.setObjectName(u"button_save_short")

        self.verticalLayout_settings_short.addWidget(self.button_save_short)

        self.verticalSpacer1 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_settings_short.addItem(self.verticalSpacer1)

        self.tabWidget.addTab(self.tab_settings_short, "")
        self.tab_profits = QWidget()
        self.tab_profits.setObjectName(u"tab_profits")
        self.verticalLayout_9 = QVBoxLayout(self.tab_profits)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.tab_profits)
        self.label.setObjectName(u"label")
        self.label.setFont(font3)

        self.horizontalLayout_3.addWidget(self.label)

        self.period_combo = QComboBox(self.tab_profits)
        self.period_combo.addItem("")
        self.period_combo.addItem("")
        self.period_combo.addItem("")
        self.period_combo.addItem("")
        self.period_combo.addItem("")
        self.period_combo.addItem("")
        self.period_combo.setObjectName(u"period_combo")
        self.period_combo.setMinimumSize(QSize(200, 25))
        self.period_combo.setMaximumSize(QSize(200, 25))
        font6 = QFont()
        font6.setFamilies([u"\ub9d1\uc740 \uace0\ub515"])
        self.period_combo.setFont(font6)

        self.horizontalLayout_3.addWidget(self.period_combo)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.excel_download_btn = QPushButton(self.tab_profits)
        self.excel_download_btn.setObjectName(u"excel_download_btn")
        self.excel_download_btn.setMinimumSize(QSize(120, 28))
        font7 = QFont()
        font7.setFamilies([u"\ub9d1\uc740 \uace0\ub515"])
        font7.setPointSize(9)
        self.excel_download_btn.setFont(font7)
        self.excel_download_btn.setStyleSheet(u"QPushButton {\n"
"  background-color: #E0E0E0;\n"
"  border: 1px solid #C2C2C2;\n"
"  border-radius: 3px;\n"
"  color: #212121;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #D0D0D0;\n"
"}")

        self.horizontalLayout_3.addWidget(self.excel_download_btn)


        self.verticalLayout_9.addLayout(self.horizontalLayout_3)

        self.label_2 = QLabel(self.tab_profits)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font7)

        self.verticalLayout_9.addWidget(self.label_2)

        self.label_3 = QLabel(self.tab_profits)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font7)

        self.verticalLayout_9.addWidget(self.label_3)

        self.profit_table = QTableWidget(self.tab_profits)
        if (self.profit_table.columnCount() < 9):
            self.profit_table.setColumnCount(9)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.profit_table.setHorizontalHeaderItem(0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.profit_table.setHorizontalHeaderItem(1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.profit_table.setHorizontalHeaderItem(2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.profit_table.setHorizontalHeaderItem(3, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.profit_table.setHorizontalHeaderItem(4, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.profit_table.setHorizontalHeaderItem(5, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.profit_table.setHorizontalHeaderItem(6, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.profit_table.setHorizontalHeaderItem(7, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.profit_table.setHorizontalHeaderItem(8, __qtablewidgetitem28)
        self.profit_table.setObjectName(u"profit_table")
        self.profit_table.setFont(font7)
        self.profit_table.setStyleSheet(u"QTableWidget {\n"
"  border: 1px solid #C2C2C2;\n"
"  background-color: white;\n"
"  color: #212121;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"  background-color: #E0E0E0;\n"
"}")
        self.profit_table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.profit_table.setAlternatingRowColors(True)
        self.profit_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.profit_table.setSortingEnabled(True)
        self.profit_table.horizontalHeader().setDefaultSectionSize(120)
        self.profit_table.horizontalHeader().setStretchLastSection(True)
        self.profit_table.verticalHeader().setDefaultSectionSize(30)

        self.verticalLayout_9.addWidget(self.profit_table)

        self.tabWidget.addTab(self.tab_profits, "")
        self.tab_coordin = QWidget()
        self.tab_coordin.setObjectName(u"tab_coordin")
        self.verticalLayoutWidget = QWidget(self.tab_coordin)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 1001, 631))
        self.verticalLayout_6 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout1 = QHBoxLayout()
        self.horizontalLayout1.setObjectName(u"horizontalLayout1")
        self.label_limit = QLabel(self.verticalLayoutWidget)
        self.label_limit.setObjectName(u"label_limit")
        self.label_limit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout1.addWidget(self.label_limit)

        self.lineEdit_limit_x = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_limit_x.setObjectName(u"lineEdit_limit_x")

        self.horizontalLayout1.addWidget(self.lineEdit_limit_x)

        self.lineEdit_limit_y = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_limit_y.setObjectName(u"lineEdit_limit_y")

        self.horizontalLayout1.addWidget(self.lineEdit_limit_y)

        self.button_record1 = QPushButton(self.verticalLayoutWidget)
        self.button_record1.setObjectName(u"button_record1")

        self.horizontalLayout1.addWidget(self.button_record1)

        self.horizontalSpacer1 = QSpacerItem(80, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout1.addItem(self.horizontalSpacer1)

        self.label_market = QLabel(self.verticalLayoutWidget)
        self.label_market.setObjectName(u"label_market")
        self.label_market.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout1.addWidget(self.label_market)

        self.lineEdit_market_x = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_market_x.setObjectName(u"lineEdit_market_x")

        self.horizontalLayout1.addWidget(self.lineEdit_market_x)

        self.lineEdit_market_y = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_market_y.setObjectName(u"lineEdit_market_y")

        self.horizontalLayout1.addWidget(self.lineEdit_market_y)

        self.button_record2 = QPushButton(self.verticalLayoutWidget)
        self.button_record2.setObjectName(u"button_record2")

        self.horizontalLayout1.addWidget(self.button_record2)

        self.horizontalLayout1.setStretch(0, 1)
        self.horizontalLayout1.setStretch(1, 1)
        self.horizontalLayout1.setStretch(2, 1)
        self.horizontalLayout1.setStretch(3, 1)
        self.horizontalLayout1.setStretch(4, 2)
        self.horizontalLayout1.setStretch(5, 1)
        self.horizontalLayout1.setStretch(6, 1)
        self.horizontalLayout1.setStretch(7, 1)
        self.horizontalLayout1.setStretch(8, 1)

        self.verticalLayout_6.addLayout(self.horizontalLayout1)

        self.horizontalLayout2 = QHBoxLayout()
        self.horizontalLayout2.setObjectName(u"horizontalLayout2")
        self.label_buy = QLabel(self.verticalLayoutWidget)
        self.label_buy.setObjectName(u"label_buy")
        self.label_buy.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout2.addWidget(self.label_buy)

        self.lineEdit_buy_x = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_buy_x.setObjectName(u"lineEdit_buy_x")

        self.horizontalLayout2.addWidget(self.lineEdit_buy_x)

        self.lineEdit_buy_y = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_buy_y.setObjectName(u"lineEdit_buy_y")

        self.horizontalLayout2.addWidget(self.lineEdit_buy_y)

        self.button_record3 = QPushButton(self.verticalLayoutWidget)
        self.button_record3.setObjectName(u"button_record3")

        self.horizontalLayout2.addWidget(self.button_record3)

        self.horizontalSpacer2 = QSpacerItem(80, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout2.addItem(self.horizontalSpacer2)

        self.label_sell = QLabel(self.verticalLayoutWidget)
        self.label_sell.setObjectName(u"label_sell")
        self.label_sell.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout2.addWidget(self.label_sell)

        self.lineEdit_sell_x = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_sell_x.setObjectName(u"lineEdit_sell_x")

        self.horizontalLayout2.addWidget(self.lineEdit_sell_x)

        self.lineEdit_sell_y = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_sell_y.setObjectName(u"lineEdit_sell_y")

        self.horizontalLayout2.addWidget(self.lineEdit_sell_y)

        self.button_record4 = QPushButton(self.verticalLayoutWidget)
        self.button_record4.setObjectName(u"button_record4")

        self.horizontalLayout2.addWidget(self.button_record4)

        self.horizontalLayout2.setStretch(0, 1)
        self.horizontalLayout2.setStretch(1, 1)
        self.horizontalLayout2.setStretch(2, 1)
        self.horizontalLayout2.setStretch(3, 1)
        self.horizontalLayout2.setStretch(4, 2)
        self.horizontalLayout2.setStretch(5, 1)
        self.horizontalLayout2.setStretch(6, 1)
        self.horizontalLayout2.setStretch(7, 1)
        self.horizontalLayout2.setStretch(8, 1)

        self.verticalLayout_6.addLayout(self.horizontalLayout2)

        self.horizontalLayout3 = QHBoxLayout()
        self.horizontalLayout3.setObjectName(u"horizontalLayout3")
        self.label_buyprice = QLabel(self.verticalLayoutWidget)
        self.label_buyprice.setObjectName(u"label_buyprice")
        self.label_buyprice.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout3.addWidget(self.label_buyprice)

        self.lineEdit_buyprice_x = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_buyprice_x.setObjectName(u"lineEdit_buyprice_x")

        self.horizontalLayout3.addWidget(self.lineEdit_buyprice_x)

        self.lineEdit_buyprice_y = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_buyprice_y.setObjectName(u"lineEdit_buyprice_y")

        self.horizontalLayout3.addWidget(self.lineEdit_buyprice_y)

        self.button_record5 = QPushButton(self.verticalLayoutWidget)
        self.button_record5.setObjectName(u"button_record5")

        self.horizontalLayout3.addWidget(self.button_record5)

        self.horizontalSpacer3 = QSpacerItem(80, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout3.addItem(self.horizontalSpacer3)

        self.label_nowprice = QLabel(self.verticalLayoutWidget)
        self.label_nowprice.setObjectName(u"label_nowprice")
        self.label_nowprice.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout3.addWidget(self.label_nowprice)

        self.lineEdit_nowprice_x = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_nowprice_x.setObjectName(u"lineEdit_nowprice_x")

        self.horizontalLayout3.addWidget(self.lineEdit_nowprice_x)

        self.lineEdit_nowprice_y = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_nowprice_y.setObjectName(u"lineEdit_nowprice_y")

        self.horizontalLayout3.addWidget(self.lineEdit_nowprice_y)

        self.button_record6 = QPushButton(self.verticalLayoutWidget)
        self.button_record6.setObjectName(u"button_record6")

        self.horizontalLayout3.addWidget(self.button_record6)

        self.horizontalLayout3.setStretch(0, 1)
        self.horizontalLayout3.setStretch(1, 1)
        self.horizontalLayout3.setStretch(2, 1)
        self.horizontalLayout3.setStretch(3, 1)
        self.horizontalLayout3.setStretch(4, 2)
        self.horizontalLayout3.setStretch(5, 1)
        self.horizontalLayout3.setStretch(6, 1)
        self.horizontalLayout3.setStretch(7, 1)
        self.horizontalLayout3.setStretch(8, 1)

        self.verticalLayout_6.addLayout(self.horizontalLayout3)

        self.horizontalLayout4 = QHBoxLayout()
        self.horizontalLayout4.setObjectName(u"horizontalLayout4")
        self.label_quantity = QLabel(self.verticalLayoutWidget)
        self.label_quantity.setObjectName(u"label_quantity")
        self.label_quantity.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout4.addWidget(self.label_quantity)

        self.lineEdit_quantity_x = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_quantity_x.setObjectName(u"lineEdit_quantity_x")

        self.horizontalLayout4.addWidget(self.lineEdit_quantity_x)

        self.lineEdit_quantity_y = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_quantity_y.setObjectName(u"lineEdit_quantity_y")

        self.horizontalLayout4.addWidget(self.lineEdit_quantity_y)

        self.button_record7 = QPushButton(self.verticalLayoutWidget)
        self.button_record7.setObjectName(u"button_record7")

        self.horizontalLayout4.addWidget(self.button_record7)

        self.horizontalSpacer4 = QSpacerItem(80, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout4.addItem(self.horizontalSpacer4)

        self.label_leverage = QLabel(self.verticalLayoutWidget)
        self.label_leverage.setObjectName(u"label_leverage")
        self.label_leverage.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout4.addWidget(self.label_leverage)

        self.lineEdit_leverage_x = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_leverage_x.setObjectName(u"lineEdit_leverage_x")

        self.horizontalLayout4.addWidget(self.lineEdit_leverage_x)

        self.lineEdit_leverage_y = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_leverage_y.setObjectName(u"lineEdit_leverage_y")

        self.horizontalLayout4.addWidget(self.lineEdit_leverage_y)

        self.button_record8 = QPushButton(self.verticalLayoutWidget)
        self.button_record8.setObjectName(u"button_record8")

        self.horizontalLayout4.addWidget(self.button_record8)

        self.horizontalLayout4.setStretch(0, 1)
        self.horizontalLayout4.setStretch(1, 1)
        self.horizontalLayout4.setStretch(2, 1)
        self.horizontalLayout4.setStretch(3, 1)
        self.horizontalLayout4.setStretch(4, 2)
        self.horizontalLayout4.setStretch(5, 1)
        self.horizontalLayout4.setStretch(6, 1)
        self.horizontalLayout4.setStretch(7, 1)
        self.horizontalLayout4.setStretch(8, 1)

        self.verticalLayout_6.addLayout(self.horizontalLayout4)

        self.horizontalLayout5 = QHBoxLayout()
        self.horizontalLayout5.setObjectName(u"horizontalLayout5")
        self.label_position = QLabel(self.verticalLayoutWidget)
        self.label_position.setObjectName(u"label_position")
        self.label_position.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout5.addWidget(self.label_position)

        self.lineEdit_position_x = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_position_x.setObjectName(u"lineEdit_position_x")

        self.horizontalLayout5.addWidget(self.lineEdit_position_x)

        self.lineEdit_position_y = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_position_y.setObjectName(u"lineEdit_position_y")

        self.horizontalLayout5.addWidget(self.lineEdit_position_y)

        self.button_record9 = QPushButton(self.verticalLayoutWidget)
        self.button_record9.setObjectName(u"button_record9")

        self.horizontalLayout5.addWidget(self.button_record9)

        self.horizontalSpacer5 = QSpacerItem(80, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout5.addItem(self.horizontalSpacer5)

        self.label_oi = QLabel(self.verticalLayoutWidget)
        self.label_oi.setObjectName(u"label_oi")
        self.label_oi.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout5.addWidget(self.label_oi)

        self.lineEdit_oi_x = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_oi_x.setObjectName(u"lineEdit_oi_x")

        self.horizontalLayout5.addWidget(self.lineEdit_oi_x)

        self.lineEdit_oi_y = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_oi_y.setObjectName(u"lineEdit_oi_y")

        self.horizontalLayout5.addWidget(self.lineEdit_oi_y)

        self.button_record10 = QPushButton(self.verticalLayoutWidget)
        self.button_record10.setObjectName(u"button_record10")

        self.horizontalLayout5.addWidget(self.button_record10)

        self.horizontalLayout5.setStretch(0, 1)
        self.horizontalLayout5.setStretch(1, 1)
        self.horizontalLayout5.setStretch(2, 1)
        self.horizontalLayout5.setStretch(3, 1)
        self.horizontalLayout5.setStretch(4, 2)
        self.horizontalLayout5.setStretch(5, 1)
        self.horizontalLayout5.setStretch(6, 1)
        self.horizontalLayout5.setStretch(7, 1)
        self.horizontalLayout5.setStretch(8, 1)

        self.verticalLayout_6.addLayout(self.horizontalLayout5)

        self.horizontalLayout6 = QHBoxLayout()
        self.horizontalLayout6.setObjectName(u"horizontalLayout6")
        self.label_details = QLabel(self.verticalLayoutWidget)
        self.label_details.setObjectName(u"label_details")
        self.label_details.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout6.addWidget(self.label_details)

        self.lineEdit_details_x = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_details_x.setObjectName(u"lineEdit_details_x")

        self.horizontalLayout6.addWidget(self.lineEdit_details_x)

        self.lineEdit_details_y = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_details_y.setObjectName(u"lineEdit_details_y")

        self.horizontalLayout6.addWidget(self.lineEdit_details_y)

        self.button_record11 = QPushButton(self.verticalLayoutWidget)
        self.button_record11.setObjectName(u"button_record11")

        self.horizontalLayout6.addWidget(self.button_record11)

        self.horizontalSpacer6 = QSpacerItem(80, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout6.addItem(self.horizontalSpacer6)

        self.label_pnl = QLabel(self.verticalLayoutWidget)
        self.label_pnl.setObjectName(u"label_pnl")
        self.label_pnl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout6.addWidget(self.label_pnl)

        self.lineEdit_pnl_x = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_pnl_x.setObjectName(u"lineEdit_pnl_x")

        self.horizontalLayout6.addWidget(self.lineEdit_pnl_x)

        self.lineEdit_pnl_y = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_pnl_y.setObjectName(u"lineEdit_pnl_y")

        self.horizontalLayout6.addWidget(self.lineEdit_pnl_y)

        self.button_record12 = QPushButton(self.verticalLayoutWidget)
        self.button_record12.setObjectName(u"button_record12")

        self.horizontalLayout6.addWidget(self.button_record12)

        self.horizontalLayout6.setStretch(0, 1)
        self.horizontalLayout6.setStretch(1, 1)
        self.horizontalLayout6.setStretch(2, 1)
        self.horizontalLayout6.setStretch(3, 1)
        self.horizontalLayout6.setStretch(4, 2)
        self.horizontalLayout6.setStretch(5, 1)
        self.horizontalLayout6.setStretch(6, 1)
        self.horizontalLayout6.setStretch(7, 1)
        self.horizontalLayout6.setStretch(8, 1)

        self.verticalLayout_6.addLayout(self.horizontalLayout6)

        self.horizontalLayout7 = QHBoxLayout()
        self.horizontalLayout7.setObjectName(u"horizontalLayout7")
        self.label_allsell = QLabel(self.verticalLayoutWidget)
        self.label_allsell.setObjectName(u"label_allsell")
        self.label_allsell.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout7.addWidget(self.label_allsell)

        self.lineEdit_allsell_x = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_allsell_x.setObjectName(u"lineEdit_allsell_x")

        self.horizontalLayout7.addWidget(self.lineEdit_allsell_x)

        self.lineEdit_allsell_y = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_allsell_y.setObjectName(u"lineEdit_allsell_y")

        self.horizontalLayout7.addWidget(self.lineEdit_allsell_y)

        self.button_record13 = QPushButton(self.verticalLayoutWidget)
        self.button_record13.setObjectName(u"button_record13")

        self.horizontalLayout7.addWidget(self.button_record13)

        self.horizontalSpacer7 = QSpacerItem(80, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout7.addItem(self.horizontalSpacer7)

        self.label_allcancel = QLabel(self.verticalLayoutWidget)
        self.label_allcancel.setObjectName(u"label_allcancel")
        self.label_allcancel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout7.addWidget(self.label_allcancel)

        self.lineEdit_allcancel_x = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_allcancel_x.setObjectName(u"lineEdit_allcancel_x")

        self.horizontalLayout7.addWidget(self.lineEdit_allcancel_x)

        self.lineEdit_allcancel_y = QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_allcancel_y.setObjectName(u"lineEdit_allcancel_y")

        self.horizontalLayout7.addWidget(self.lineEdit_allcancel_y)

        self.button_record14 = QPushButton(self.verticalLayoutWidget)
        self.button_record14.setObjectName(u"button_record14")

        self.horizontalLayout7.addWidget(self.button_record14)

        self.horizontalLayout7.setStretch(0, 1)
        self.horizontalLayout7.setStretch(1, 1)
        self.horizontalLayout7.setStretch(2, 1)
        self.horizontalLayout7.setStretch(3, 1)
        self.horizontalLayout7.setStretch(4, 2)
        self.horizontalLayout7.setStretch(5, 1)
        self.horizontalLayout7.setStretch(6, 1)
        self.horizontalLayout7.setStretch(7, 1)
        self.horizontalLayout7.setStretch(8, 1)

        self.verticalLayout_6.addLayout(self.horizontalLayout7)

        self.tabWidget.addTab(self.tab_coordin, "")
        self.tab_api = QWidget()
        self.tab_api.setObjectName(u"tab_api")
        self.tabWidget.addTab(self.tab_api, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.bottom_frame = QFrame(self.centralwidget)
        self.bottom_frame.setObjectName(u"bottom_frame")
        self.bottom_frame.setMinimumSize(QSize(0, 50))
        self.bottom_frame.setMaximumSize(QSize(16777215, 50))
        self.bottom_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.bottom_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.bottom_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.btn_all_coins = QPushButton(self.bottom_frame)
        self.btn_all_coins.setObjectName(u"btn_all_coins")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_all_coins.sizePolicy().hasHeightForWidth())
        self.btn_all_coins.setSizePolicy(sizePolicy)
        self.btn_all_coins.setMinimumSize(QSize(150, 35))
        self.btn_all_coins.setStyleSheet(u"QPushButton {\n"
"  background-color: #E0E0E0;\n"
"  border: 1px solid #C2C2C2;\n"
"  color: #212121;\n"
"  font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #D0D0D0;\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_all_coins)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.status_label = QLabel(self.bottom_frame)
        self.status_label.setObjectName(u"status_label")

        self.horizontalLayout_2.addWidget(self.status_label)


        self.verticalLayout.addWidget(self.bottom_frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"NewOrder_prototype", None))
        self.right_panel.setTitle(QCoreApplication.translate("MainWindow", u"\ud604\uc7ac \ucf54\uc778 \uc2dc\uc138", None))
        ___qtablewidgetitem = self.coin_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\ucf54\uc778", None));
        ___qtablewidgetitem1 = self.coin_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\ud69f\uc218", None));
        ___qtablewidgetitem2 = self.coin_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\ud3c9\uac00\uc190\uc775", None));
        ___qtablewidgetitem3 = self.coin_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\uc218\uc775\ub960", None));
        ___qtablewidgetitem4 = self.coin_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\ud604\uc7ac\uac00", None));

        __sortingEnabled = self.coin_table.isSortingEnabled()
        self.coin_table.setSortingEnabled(False)
        ___qtablewidgetitem5 = self.coin_table.item(0, 0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"BTC", None));
        ___qtablewidgetitem6 = self.coin_table.item(0, 1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem7 = self.coin_table.item(0, 2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"5,922", None));
        ___qtablewidgetitem8 = self.coin_table.item(0, 3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"0.99", None));
        ___qtablewidgetitem9 = self.coin_table.item(0, 4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"89,100", None));
        ___qtablewidgetitem10 = self.coin_table.item(1, 0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"ETH", None));
        ___qtablewidgetitem11 = self.coin_table.item(1, 1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem12 = self.coin_table.item(1, 2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"-1,652", None));
        ___qtablewidgetitem13 = self.coin_table.item(1, 3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"-0.28", None));
        ___qtablewidgetitem14 = self.coin_table.item(1, 4)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"1,980", None));
        self.coin_table.setSortingEnabled(__sortingEnabled)

        self.middle_panel.setTitle(QCoreApplication.translate("MainWindow", u"Trading Log", None))
        self.log_clear.setText(QCoreApplication.translate("MainWindow", u"\ub85c\uadf8\uc0ad\uc81c", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\ub098\uc758 \ub9e4\ub9e4 \uc124\uc815", None))
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"\ub9e4\ub9e4 \uc2dc\uc791", None))
        self.stop_button.setText(QCoreApplication.translate("MainWindow", u"\ub9e4\ub9e4 \uc911\uc9c0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_trading), QCoreApplication.translate("MainWindow", u"\ud2b8\ub808\uc774\ub529", None))
        self.Layout_long_coin_selection.setTitle(QCoreApplication.translate("MainWindow", u"\ucf54\uc778\uc120\ud0dd", None))
        self.comboBox_coin_selection_long.setItemText(0, QCoreApplication.translate("MainWindow", u"\ube44\ud2b8\ucf54\uc778", None))
        self.comboBox_coin_selection_long.setItemText(1, QCoreApplication.translate("MainWindow", u"\uc774\ub354\ub9ac\uc6c0", None))

        self.comboBox_coin_selection_long.setCurrentText(QCoreApplication.translate("MainWindow", u"\ube44\ud2b8\ucf54\uc778", None))
        self.Layout_long_buy_settings.setTitle(QCoreApplication.translate("MainWindow", u"\ub871 \ud3ec\uc9c0\uc158 \uc9c4\uc785 \uc124\uc815", None))
        self.label_signal1_long.setText(QCoreApplication.translate("MainWindow", u"\uc9c4\uc785 \uc2dc\uadf8\ub110 1", None))
        self.comboBox_signal1_long.setItemText(0, QCoreApplication.translate("MainWindow", u"RSI", None))
        self.comboBox_signal1_long.setItemText(1, QCoreApplication.translate("MainWindow", u"\uc774\ub3d9\ud3c9\uade0\uc120", None))
        self.comboBox_signal1_long.setItemText(2, QCoreApplication.translate("MainWindow", u"MACD", None))
        self.comboBox_signal1_long.setItemText(3, QCoreApplication.translate("MainWindow", u"\ubcfc\ub9b0\uc800\ubc34\ub4dc", None))

        self.comboBox_signal1_long.setCurrentText(QCoreApplication.translate("MainWindow", u"RSI", None))
        self.comboBox_timeframe1_long.setItemText(0, QCoreApplication.translate("MainWindow", u"5\ubd84\ubd09", None))
        self.comboBox_timeframe1_long.setItemText(1, QCoreApplication.translate("MainWindow", u"15\ubd84\ubd09", None))
        self.comboBox_timeframe1_long.setItemText(2, QCoreApplication.translate("MainWindow", u"30\ubd84\ubd09", None))
        self.comboBox_timeframe1_long.setItemText(3, QCoreApplication.translate("MainWindow", u"1\uc2dc\uac04\ubd09", None))

        self.comboBox_timeframe1_long.setCurrentText(QCoreApplication.translate("MainWindow", u"5\ubd84\ubd09", None))
        self.btn_detail_signal1_long.setText(QCoreApplication.translate("MainWindow", u"\uc0c1\uc138\uc124\uc815", None))
        self.label_signal2_long.setText(QCoreApplication.translate("MainWindow", u"\uc9c4\uc785 \uc2dc\uadf8\ub110 2", None))
        self.comboBox_signal2_long.setItemText(0, QCoreApplication.translate("MainWindow", u"RSI", None))
        self.comboBox_signal2_long.setItemText(1, QCoreApplication.translate("MainWindow", u"\uc774\ub3d9\ud3c9\uade0\uc120", None))
        self.comboBox_signal2_long.setItemText(2, QCoreApplication.translate("MainWindow", u"\ubcfc\ub9b0\uc800\ubc34\ub4dc", None))
        self.comboBox_signal2_long.setItemText(3, QCoreApplication.translate("MainWindow", u"MACD", None))

        self.comboBox_signal2_long.setCurrentText(QCoreApplication.translate("MainWindow", u"RSI", None))
        self.comboBox_timeframe2_long.setItemText(0, QCoreApplication.translate("MainWindow", u"5\ubd84\ubd09", None))
        self.comboBox_timeframe2_long.setItemText(1, QCoreApplication.translate("MainWindow", u"15\ubd84\ubd09", None))
        self.comboBox_timeframe2_long.setItemText(2, QCoreApplication.translate("MainWindow", u"30\ubd84\ubd09", None))
        self.comboBox_timeframe2_long.setItemText(3, QCoreApplication.translate("MainWindow", u"1\uc2dc\uac04\ubd09", None))

        self.comboBox_timeframe2_long.setCurrentText(QCoreApplication.translate("MainWindow", u"5\ubd84\ubd09", None))
        self.btn_detail_signal2_long.setText(QCoreApplication.translate("MainWindow", u"\uc0c1\uc138\uc124\uc815", None))
        self.label_buy_amount_long.setText(QCoreApplication.translate("MainWindow", u"\uc9c4\uc785 \uac1c\uc218", None))
        self.spinBox_buy_amount_long.setSuffix(QCoreApplication.translate("MainWindow", u" \uac1c", None))
        self.spinBox_additional_long.setSuffix(QCoreApplication.translate("MainWindow", u" \ubc30", None))
        self.checkBox_split_buy_long.setText(QCoreApplication.translate("MainWindow", u"\ubd84\ud560\ub9e4\uc218", None))
        self.checkBox1_split_long.setText(QCoreApplication.translate("MainWindow", u"RSI", None))
        self.spinBox1_split1_long.setSuffix(QCoreApplication.translate("MainWindow", u" \ud3ec\uc778\ud2b8", None))
        self.label1_split1_long.setText(QCoreApplication.translate("MainWindow", u"\ud558\ub77d \uc2dc", None))
        self.spinBox2_split1_long.setSuffix(QCoreApplication.translate("MainWindow", u" \uac1c", None))
        self.spinBox3_split1_long.setSuffix(QCoreApplication.translate("MainWindow", u" \ubc88", None))
        self.spinBox3_split1_long.setPrefix(QCoreApplication.translate("MainWindow", u"\ucd5c\ub300 ", None))
        self.label2_split1_long.setText(QCoreApplication.translate("MainWindow", u"\ub9e4\uc218", None))
        self.checkBox2_split_long.setText(QCoreApplication.translate("MainWindow", u"\uac00\uaca9", None))
        self.spinBox1_split2_long.setSuffix(QCoreApplication.translate("MainWindow", u" USDT", None))
        self.label1_split2_long.setText(QCoreApplication.translate("MainWindow", u"\ud558\ub77d \uc2dc", None))
        self.spinBox2_split2_long.setSuffix(QCoreApplication.translate("MainWindow", u" \uac1c", None))
        self.spinBox3_split2_long.setSuffix(QCoreApplication.translate("MainWindow", u" \ubc88", None))
        self.spinBox3_split2_long.setPrefix(QCoreApplication.translate("MainWindow", u"\ucd5c\ub300 ", None))
        self.label2_split2_long.setText(QCoreApplication.translate("MainWindow", u"\ub9e4\uc218", None))
        self.Layout_long_sell_settings.setTitle(QCoreApplication.translate("MainWindow", u"\ub871 \ud3ec\uc9c0\uc158 \uccad\uc0b0 \uc124\uc815", None))
        self.label_profit_cut_long.setText(QCoreApplication.translate("MainWindow", u"\uc775\uc808", None))
        self.checkBox_takeprofit1_long.setText(QCoreApplication.translate("MainWindow", u"\uc218\uc775\ub960", None))
        self.doubleSpinBox_profit_rate_long.setPrefix(QCoreApplication.translate("MainWindow", u"+ ", None))
        self.doubleSpinBox_profit_rate_long.setSuffix(QCoreApplication.translate("MainWindow", u"%", None))
        self.label_profit_condition_long.setText(QCoreApplication.translate("MainWindow", u"\ub2ec\uc131 \uc2dc \ub9e4\ub3c4", None))
        self.checkBox_takeprofit2_long.setText(QCoreApplication.translate("MainWindow", u"\ud3ec\uc9c0\uc158  \ub300\ube44", None))
        self.spinBox_takeprofit1_long.setSuffix(QCoreApplication.translate("MainWindow", u" USDT", None))
        self.label_profit_condition_2_long.setText(QCoreApplication.translate("MainWindow", u"\uc0c1\uc2b9 \uc2dc \ub9e4\ub3c4", None))
        self.label_loss_cut_long.setText(QCoreApplication.translate("MainWindow", u"\uc190\uc808", None))
        self.checkBox_stoploss1_long.setText(QCoreApplication.translate("MainWindow", u"\uc218\uc775\ub960", None))
        self.doubleSpinBox_loss_rate_long.setPrefix(QCoreApplication.translate("MainWindow", u"- ", None))
        self.doubleSpinBox_loss_rate_long.setSuffix(QCoreApplication.translate("MainWindow", u"%", None))
        self.label_loss_condition_long.setText(QCoreApplication.translate("MainWindow", u"\ub2ec\uc131 \uc2dc \ub9e4\ub3c4", None))
        self.checkBox_stoploss2_long.setText(QCoreApplication.translate("MainWindow", u"\ud3ec\uc9c0\uc158 \ub300\ube44", None))
        self.spinBox_stoploss1_long.setSuffix(QCoreApplication.translate("MainWindow", u" USDT", None))
        self.label_profit_condition_3_long.setText(QCoreApplication.translate("MainWindow", u"\ud558\ub77d \uc2dc \ub9e4\ub3c4", None))
        self.button_save_long.setText(QCoreApplication.translate("MainWindow", u"\uc124\uc815 \uc800\uc7a5", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_settings_long), QCoreApplication.translate("MainWindow", u"\ub9e4\ub9e4\uc124\uc815(\ub871)", None))
        self.Layout_short_coin_selection.setTitle(QCoreApplication.translate("MainWindow", u"\ucf54\uc778\uc120\ud0dd", None))
        self.comboBox_coin_selection_short.setItemText(0, QCoreApplication.translate("MainWindow", u"\ube44\ud2b8\ucf54\uc778", None))
        self.comboBox_coin_selection_short.setItemText(1, QCoreApplication.translate("MainWindow", u"\uc774\ub354\ub9ac\uc6c0", None))

        self.comboBox_coin_selection_short.setCurrentText(QCoreApplication.translate("MainWindow", u"\ube44\ud2b8\ucf54\uc778", None))
        self.Layout_short_buy_settings.setTitle(QCoreApplication.translate("MainWindow", u"\uc20f \ud3ec\uc9c0\uc158 \uc9c4\uc785 \uc124\uc815", None))
        self.label_signal1_short.setText(QCoreApplication.translate("MainWindow", u"\uc9c4\uc785 \uc2dc\uadf8\ub110 1", None))
        self.comboBox_signal1_short.setItemText(0, QCoreApplication.translate("MainWindow", u"RSI", None))
        self.comboBox_signal1_short.setItemText(1, QCoreApplication.translate("MainWindow", u"\uc774\ub3d9\ud3c9\uade0\uc120", None))
        self.comboBox_signal1_short.setItemText(2, QCoreApplication.translate("MainWindow", u"MACD", None))
        self.comboBox_signal1_short.setItemText(3, QCoreApplication.translate("MainWindow", u"\ubcfc\ub9b0\uc800\ubc34\ub4dc", None))

        self.comboBox_signal1_short.setCurrentText(QCoreApplication.translate("MainWindow", u"RSI", None))
        self.comboBox_timeframe1_short.setItemText(0, QCoreApplication.translate("MainWindow", u"5\ubd84\ubd09", None))
        self.comboBox_timeframe1_short.setItemText(1, QCoreApplication.translate("MainWindow", u"15\ubd84\ubd09", None))
        self.comboBox_timeframe1_short.setItemText(2, QCoreApplication.translate("MainWindow", u"30\ubd84\ubd09", None))
        self.comboBox_timeframe1_short.setItemText(3, QCoreApplication.translate("MainWindow", u"1\uc2dc\uac04\ubd09", None))

        self.comboBox_timeframe1_short.setCurrentText(QCoreApplication.translate("MainWindow", u"5\ubd84\ubd09", None))
        self.btn_detail_signal1_short.setText(QCoreApplication.translate("MainWindow", u"\uc0c1\uc138\uc124\uc815", None))
        self.label_signal2_short.setText(QCoreApplication.translate("MainWindow", u"\uc9c4\uc785 \uc2dc\uadf8\ub110 2", None))
        self.comboBox_signal2_short.setItemText(0, QCoreApplication.translate("MainWindow", u"RSI", None))
        self.comboBox_signal2_short.setItemText(1, QCoreApplication.translate("MainWindow", u"\uc774\ub3d9\ud3c9\uade0\uc120", None))
        self.comboBox_signal2_short.setItemText(2, QCoreApplication.translate("MainWindow", u"\ubcfc\ub9b0\uc800\ubc34\ub4dc", None))
        self.comboBox_signal2_short.setItemText(3, QCoreApplication.translate("MainWindow", u"MACD", None))

        self.comboBox_signal2_short.setCurrentText(QCoreApplication.translate("MainWindow", u"RSI", None))
        self.comboBox_timeframe2_short.setItemText(0, QCoreApplication.translate("MainWindow", u"5\ubd84\ubd09", None))
        self.comboBox_timeframe2_short.setItemText(1, QCoreApplication.translate("MainWindow", u"15\ubd84\ubd09", None))
        self.comboBox_timeframe2_short.setItemText(2, QCoreApplication.translate("MainWindow", u"30\ubd84\ubd09", None))
        self.comboBox_timeframe2_short.setItemText(3, QCoreApplication.translate("MainWindow", u"1\uc2dc\uac04\ubd09", None))

        self.comboBox_timeframe2_short.setCurrentText(QCoreApplication.translate("MainWindow", u"5\ubd84\ubd09", None))
        self.btn_detail_signal2_short.setText(QCoreApplication.translate("MainWindow", u"\uc0c1\uc138\uc124\uc815", None))
        self.label_buy_amount_short.setText(QCoreApplication.translate("MainWindow", u"\uc9c4\uc785 \uac1c\uc218", None))
        self.spinBox_buy_amount_short.setSuffix(QCoreApplication.translate("MainWindow", u" \uac1c", None))
        self.spinBox_additional_short.setSuffix(QCoreApplication.translate("MainWindow", u" \ubc30", None))
        self.checkBox_split_buy_short.setText(QCoreApplication.translate("MainWindow", u"\ubd84\ud560\ub9e4\uc218", None))
        self.checkBox1_split_short.setText(QCoreApplication.translate("MainWindow", u"RSI", None))
        self.spinBox1_split1_short.setSuffix(QCoreApplication.translate("MainWindow", u" \ud3ec\uc778\ud2b8", None))
        self.label1_split1_short.setText(QCoreApplication.translate("MainWindow", u"\uc0c1\uc2b9 \uc2dc", None))
        self.spinBox2_split1_short.setSuffix(QCoreApplication.translate("MainWindow", u" \uac1c", None))
        self.spinBox3_split1_short.setSuffix(QCoreApplication.translate("MainWindow", u" \ubc88", None))
        self.spinBox3_split1_short.setPrefix(QCoreApplication.translate("MainWindow", u"\ucd5c\ub300 ", None))
        self.label2_split1_short.setText(QCoreApplication.translate("MainWindow", u"\ub9e4\uc218", None))
        self.checkBox2_split_short.setText(QCoreApplication.translate("MainWindow", u"\uac00\uaca9", None))
        self.spinBox1_split2_short.setSuffix(QCoreApplication.translate("MainWindow", u" USDT", None))
        self.label1_split2_short.setText(QCoreApplication.translate("MainWindow", u"\uc0c1\uc2b9 \uc2dc", None))
        self.spinBox2_split2_short.setSuffix(QCoreApplication.translate("MainWindow", u" \uac1c", None))
        self.spinBox3_split2_short.setSuffix(QCoreApplication.translate("MainWindow", u" \ubc88", None))
        self.spinBox3_split2_short.setPrefix(QCoreApplication.translate("MainWindow", u"\ucd5c\ub300 ", None))
        self.label2_split2_short.setText(QCoreApplication.translate("MainWindow", u"\ub9e4\uc218", None))
        self.Layout_short_sell_settings.setTitle(QCoreApplication.translate("MainWindow", u"\uc20f \ud3ec\uc9c0\uc158 \uccad\uc0b0 \uc124\uc815", None))
        self.label_profit_cut_short.setText(QCoreApplication.translate("MainWindow", u"\uc775\uc808", None))
        self.checkBox_takeprofit1_short.setText(QCoreApplication.translate("MainWindow", u"\uc218\uc775\ub960", None))
        self.doubleSpinBox_profit_rate_short.setPrefix(QCoreApplication.translate("MainWindow", u"+ ", None))
        self.doubleSpinBox_profit_rate_short.setSuffix(QCoreApplication.translate("MainWindow", u"%", None))
        self.label_profit_condition_short.setText(QCoreApplication.translate("MainWindow", u"\ub2ec\uc131 \uc2dc \ub9e4\ub3c4", None))
        self.checkBox_takeprofit2_short.setText(QCoreApplication.translate("MainWindow", u"\ud604\uc7ac\uac00 \ub300\ube44", None))
        self.spinBox_takeprofit1_short.setSuffix(QCoreApplication.translate("MainWindow", u" USDT", None))
        self.label_profit_condition_2_short.setText(QCoreApplication.translate("MainWindow", u"\ud558\ub77d \uc2dc \ub9e4\ub3c4", None))
        self.label_loss_cut_short.setText(QCoreApplication.translate("MainWindow", u"\uc190\uc808", None))
        self.checkBox_stoploss1_short.setText(QCoreApplication.translate("MainWindow", u"\uc218\uc775\ub960", None))
        self.doubleSpinBox_loss_rate_short.setPrefix(QCoreApplication.translate("MainWindow", u"- ", None))
        self.doubleSpinBox_loss_rate_short.setSuffix(QCoreApplication.translate("MainWindow", u"%", None))
        self.label_loss_condition_short.setText(QCoreApplication.translate("MainWindow", u"\ub2ec\uc131 \uc2dc \ub9e4\ub3c4", None))
        self.checkBox_stoploss2_short.setText(QCoreApplication.translate("MainWindow", u"\ud604\uc7ac\uac00 \ub300\ube44", None))
        self.spinBox_stoploss1_short.setSuffix(QCoreApplication.translate("MainWindow", u" USDT", None))
        self.label_profit_condition_3_short.setText(QCoreApplication.translate("MainWindow", u"\uc0c1\uc2b9 \uc2dc \ub9e4\ub3c4", None))
        self.button_save_short.setText(QCoreApplication.translate("MainWindow", u"\uc124\uc815 \uc800\uc7a5", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_settings_short), QCoreApplication.translate("MainWindow", u"\ub9e4\ub9e4\uc124\uc815(\uc20f)", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\ub9e4\ub9e4 \uae30\uac04\ubcc4 \ubcf4\uae30", None))
        self.period_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"\uc804\uccb4", None))
        self.period_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"\uc624\ub298", None))
        self.period_combo.setItemText(2, QCoreApplication.translate("MainWindow", u"\uc5b4\uc81c", None))
        self.period_combo.setItemText(3, QCoreApplication.translate("MainWindow", u"3\uc77c", None))
        self.period_combo.setItemText(4, QCoreApplication.translate("MainWindow", u"7\uc77c", None))
        self.period_combo.setItemText(5, QCoreApplication.translate("MainWindow", u"30\uc77c", None))

        self.excel_download_btn.setText(QCoreApplication.translate("MainWindow", u"\uc5d1\uc140\ub2e4\uc6b4\ub85c\ub4dc", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"* \uc218\uc775 \ubc0f \uc218\uc775\ub960\uc740 \uac70\ub798 \uc218\uc218\ub8cc\ub97c \uc801\uc6a9\ud558\uc5ec \uacc4\uc0b0\ub429\ub2c8\ub2e4. \uc218\ub3d9\uc73c\ub85c \ub9e4\ub3c4\ud55c \ucf54\uc778\uc740 \ubc18\uc601\ub418\uc9c0 \uc54a\uc2b5\ub2c8\ub2e4.", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"* \ub354\ube14\ud074\ub9ad\uc2dc \uc2dc\uadf8\ub110 \uc124\uc815 \uac12\uc744 \ud655\uc778\ud558\uc2e4 \uc218 \uc788\uc2b5\ub2c8\ub2e4.", None))
        ___qtablewidgetitem15 = self.profit_table.horizontalHeaderItem(1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"\ub9e4\ub3c4\uc77c\uc2dc", None));
        ___qtablewidgetitem16 = self.profit_table.horizontalHeaderItem(2)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"\uc2dc\uadf8\ub110", None));
        ___qtablewidgetitem17 = self.profit_table.horizontalHeaderItem(3)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"\uc2ec\ubcfc", None));
        ___qtablewidgetitem18 = self.profit_table.horizontalHeaderItem(4)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"\ub9e4\ub3c4\uc218\ub7c9", None));
        ___qtablewidgetitem19 = self.profit_table.horizontalHeaderItem(5)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"\ub9e4\uc218\ud3c9\uade0\uac00", None));
        ___qtablewidgetitem20 = self.profit_table.horizontalHeaderItem(6)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"\ub9e4\ub3c4\ub2e8\uac00", None));
        ___qtablewidgetitem21 = self.profit_table.horizontalHeaderItem(7)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"\uc218\uc775", None));
        ___qtablewidgetitem22 = self.profit_table.horizontalHeaderItem(8)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"\uc218\uc775\ub960", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_profits), QCoreApplication.translate("MainWindow", u"\uc218\uc775\uae30\ub85d", None))
        self.label_limit.setText(QCoreApplication.translate("MainWindow", u"\uc9c0\uc815\uac00", None))
        self.lineEdit_limit_x.setInputMask("")
        self.lineEdit_limit_x.setText("")
        self.button_record1.setText(QCoreApplication.translate("MainWindow", u"\ub179\ud654 \uc2dc\uc791", None))
        self.label_market.setText(QCoreApplication.translate("MainWindow", u"\uc2dc\uc7a5\uac00", None))
        self.button_record2.setText(QCoreApplication.translate("MainWindow", u"\ub179\ud654 \uc2dc\uc791", None))
        self.label_buy.setText(QCoreApplication.translate("MainWindow", u"\ub9e4\uc218", None))
        self.button_record3.setText(QCoreApplication.translate("MainWindow", u"\ub179\ud654 \uc2dc\uc791", None))
        self.label_sell.setText(QCoreApplication.translate("MainWindow", u"\ub9e4\ub3c4", None))
        self.button_record4.setText(QCoreApplication.translate("MainWindow", u"\ub179\ud654 \uc2dc\uc791", None))
        self.label_buyprice.setText(QCoreApplication.translate("MainWindow", u"\uc8fc\ubb38\uac00\uaca9", None))
        self.button_record5.setText(QCoreApplication.translate("MainWindow", u"\ub179\ud654 \uc2dc\uc791", None))
        self.label_nowprice.setText(QCoreApplication.translate("MainWindow", u"\ud604\uc7ac\uac00", None))
        self.button_record6.setText(QCoreApplication.translate("MainWindow", u"\ub179\ud654 \uc2dc\uc791", None))
        self.label_quantity.setText(QCoreApplication.translate("MainWindow", u"\uc8fc\ubb38\uc218\ub7c9", None))
        self.button_record7.setText(QCoreApplication.translate("MainWindow", u"\ub179\ud654 \uc2dc\uc791", None))
        self.label_leverage.setText(QCoreApplication.translate("MainWindow", u"\ubc30\uc728\uc124\uc815", None))
        self.button_record8.setText(QCoreApplication.translate("MainWindow", u"\ub179\ud654 \uc2dc\uc791", None))
        self.label_position.setText(QCoreApplication.translate("MainWindow", u"\ud3ec\uc9c0\uc158", None))
        self.button_record9.setText(QCoreApplication.translate("MainWindow", u"\ub179\ud654 \uc2dc\uc791", None))
        self.label_oi.setText(QCoreApplication.translate("MainWindow", u"\ubbf8\uccb4\uacb0 \uc8fc\ubb38", None))
        self.button_record10.setText(QCoreApplication.translate("MainWindow", u"\ub179\ud654 \uc2dc\uc791", None))
        self.label_details.setText(QCoreApplication.translate("MainWindow", u"\uc8fc\ubb38\ub0b4\uc5ed", None))
        self.button_record11.setText(QCoreApplication.translate("MainWindow", u"\ub179\ud654 \uc2dc\uc791", None))
        self.label_pnl.setText(QCoreApplication.translate("MainWindow", u"\ub9c8\uac10\uc190\uc775", None))
        self.button_record12.setText(QCoreApplication.translate("MainWindow", u"\ub179\ud654 \uc2dc\uc791", None))
        self.label_allsell.setText(QCoreApplication.translate("MainWindow", u"\uc77c\uad04\uccad\uc0b0", None))
        self.button_record13.setText(QCoreApplication.translate("MainWindow", u"\ub179\ud654 \uc2dc\uc791", None))
        self.label_allcancel.setText(QCoreApplication.translate("MainWindow", u"\uc77c\uad04\ucde8\uc18c", None))
        self.button_record14.setText(QCoreApplication.translate("MainWindow", u"\ub179\ud654 \uc2dc\uc791", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_coordin), QCoreApplication.translate("MainWindow", u"\uc88c\ud45c\uc124\uc815", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_api), QCoreApplication.translate("MainWindow", u"\uae30\ud0c0\uc124\uc815", None))
        self.btn_all_coins.setText(QCoreApplication.translate("MainWindow", u"\ubcf4\uc720\ud3ec\uc9c0\uc158 \uc77c\uad04 \uccad\uc0b0", None))
        self.status_label.setText(QCoreApplication.translate("MainWindow", u"\uc2e4\ud589 \ub300\uae30 \uc911...", None))
    # retranslateUi

