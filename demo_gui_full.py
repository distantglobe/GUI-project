# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\demo_gui_full.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(842, 654)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab.sizePolicy().hasHeightForWidth())
        self.tab.setSizePolicy(sizePolicy)
        self.tab.setObjectName("tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.mes_3 = QtWidgets.QLabel(self.tab)
        self.mes_3.setText("")
        self.mes_3.setAlignment(QtCore.Qt.AlignCenter)
        self.mes_3.setObjectName("mes_3")
        self.gridLayout_4.addWidget(self.mes_3, 2, 2, 1, 1)
        self.dissconect_can_message = QtWidgets.QLabel(self.tab)
        self.dissconect_can_message.setText("")
        self.dissconect_can_message.setObjectName("dissconect_can_message")
        self.gridLayout_4.addWidget(self.dissconect_can_message, 1, 1, 1, 1)
        self.read_calbration_file_text = QtWidgets.QLineEdit(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.read_calbration_file_text.sizePolicy().hasHeightForWidth())
        self.read_calbration_file_text.setSizePolicy(sizePolicy)
        self.read_calbration_file_text.setObjectName("read_calbration_file_text")
        self.gridLayout_4.addWidget(self.read_calbration_file_text, 9, 1, 1, 1)
        self.read_sensor_file_text = QtWidgets.QLineEdit(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.read_sensor_file_text.sizePolicy().hasHeightForWidth())
        self.read_sensor_file_text.setSizePolicy(sizePolicy)
        self.read_sensor_file_text.setObjectName("read_sensor_file_text")
        self.gridLayout_4.addWidget(self.read_sensor_file_text, 7, 1, 1, 1)
        self.dissconect_can = QtWidgets.QPushButton(self.tab)
        self.dissconect_can.setEnabled(False)
        self.dissconect_can.setObjectName("dissconect_can")
        self.gridLayout_4.addWidget(self.dissconect_can, 1, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.tab)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_4.addWidget(self.line_2, 6, 1, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.tab)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_4.addWidget(self.line_3, 6, 2, 1, 1)
        self.read_sensor_file_message = QtWidgets.QLabel(self.tab)
        self.read_sensor_file_message.setText("")
        self.read_sensor_file_message.setObjectName("read_sensor_file_message")
        self.gridLayout_4.addWidget(self.read_sensor_file_message, 5, 1, 1, 1)
        self.browse_2 = QtWidgets.QPushButton(self.tab)
        self.browse_2.setObjectName("browse_2")
        self.gridLayout_4.addWidget(self.browse_2, 8, 2, 1, 1)
        self.interrogate_and_get_temperature = QtWidgets.QPushButton(self.tab)
        self.interrogate_and_get_temperature.setEnabled(False)
        self.interrogate_and_get_temperature.setObjectName("interrogate_and_get_temperature")
        self.gridLayout_4.addWidget(self.interrogate_and_get_temperature, 5, 0, 1, 1)
        self.interrogate_text = QtWidgets.QLineEdit(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.interrogate_text.sizePolicy().hasHeightForWidth())
        self.interrogate_text.setSizePolicy(sizePolicy)
        self.interrogate_text.setObjectName("interrogate_text")
        self.gridLayout_4.addWidget(self.interrogate_text, 2, 1, 1, 1)
        self.connect_can = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.connect_can.sizePolicy().hasHeightForWidth())
        self.connect_can.setSizePolicy(sizePolicy)
        self.connect_can.setObjectName("connect_can")
        self.gridLayout_4.addWidget(self.connect_can, 0, 0, 1, 1)
        self.read_band_file_text = QtWidgets.QLineEdit(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.read_band_file_text.sizePolicy().hasHeightForWidth())
        self.read_band_file_text.setSizePolicy(sizePolicy)
        self.read_band_file_text.setObjectName("read_band_file_text")
        self.gridLayout_4.addWidget(self.read_band_file_text, 8, 1, 1, 1)
        self.get_version_message = QtWidgets.QLabel(self.tab)
        self.get_version_message.setText("")
        self.get_version_message.setObjectName("get_version_message")
        self.gridLayout_4.addWidget(self.get_version_message, 4, 1, 1, 1)
        self.get_temperature_message = QtWidgets.QLabel(self.tab)
        self.get_temperature_message.setText("")
        self.get_temperature_message.setObjectName("get_temperature_message")
        self.gridLayout_4.addWidget(self.get_temperature_message, 3, 1, 1, 1)
        self.read_sensor_file = QtWidgets.QPushButton(self.tab)
        self.read_sensor_file.setEnabled(True)
        self.read_sensor_file.setFlat(False)
        self.read_sensor_file.setObjectName("read_sensor_file")
        self.gridLayout_4.addWidget(self.read_sensor_file, 7, 0, 1, 1)
        self.browse_3 = QtWidgets.QPushButton(self.tab)
        self.browse_3.setObjectName("browse_3")
        self.gridLayout_4.addWidget(self.browse_3, 9, 2, 1, 1)
        self.get_version = QtWidgets.QPushButton(self.tab)
        self.get_version.setEnabled(False)
        self.get_version.setObjectName("get_version")
        self.gridLayout_4.addWidget(self.get_version, 4, 0, 1, 1)
        self.browse_1 = QtWidgets.QPushButton(self.tab)
        self.browse_1.setObjectName("browse_1")
        self.gridLayout_4.addWidget(self.browse_1, 7, 2, 1, 1)
        self.mes_1 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.mes_1.setFont(font)
        self.mes_1.setAlignment(QtCore.Qt.AlignCenter)
        self.mes_1.setObjectName("mes_1")
        self.gridLayout_4.addWidget(self.mes_1, 0, 2, 1, 1)
        self.read_calibration_file = QtWidgets.QPushButton(self.tab)
        self.read_calibration_file.setEnabled(False)
        self.read_calibration_file.setObjectName("read_calibration_file")
        self.gridLayout_4.addWidget(self.read_calibration_file, 9, 0, 1, 1)
        self.mes_2 = QtWidgets.QLabel(self.tab)
        self.mes_2.setText("")
        self.mes_2.setAlignment(QtCore.Qt.AlignCenter)
        self.mes_2.setObjectName("mes_2")
        self.gridLayout_4.addWidget(self.mes_2, 1, 2, 1, 1)
        self.connect_can_message = QtWidgets.QLabel(self.tab)
        self.connect_can_message.setText("")
        self.connect_can_message.setObjectName("connect_can_message")
        self.gridLayout_4.addWidget(self.connect_can_message, 0, 1, 1, 1)
        self.interrogate = QtWidgets.QPushButton(self.tab)
        self.interrogate.setEnabled(False)
        self.interrogate.setObjectName("interrogate")
        self.gridLayout_4.addWidget(self.interrogate, 2, 0, 1, 1)
        self.get_temperature = QtWidgets.QPushButton(self.tab)
        self.get_temperature.setEnabled(False)
        self.get_temperature.setObjectName("get_temperature")
        self.gridLayout_4.addWidget(self.get_temperature, 3, 0, 1, 1)
        self.mes_4 = QtWidgets.QLabel(self.tab)
        self.mes_4.setText("")
        self.mes_4.setAlignment(QtCore.Qt.AlignCenter)
        self.mes_4.setObjectName("mes_4")
        self.gridLayout_4.addWidget(self.mes_4, 3, 2, 1, 1)
        self.mes_6 = QtWidgets.QLabel(self.tab)
        self.mes_6.setText("")
        self.mes_6.setAlignment(QtCore.Qt.AlignCenter)
        self.mes_6.setObjectName("mes_6")
        self.gridLayout_4.addWidget(self.mes_6, 5, 2, 1, 1)
        self.read_band_file = QtWidgets.QPushButton(self.tab)
        self.read_band_file.setEnabled(False)
        self.read_band_file.setObjectName("read_band_file")
        self.gridLayout_4.addWidget(self.read_band_file, 8, 0, 1, 1)
        self.mes_5 = QtWidgets.QLabel(self.tab)
        self.mes_5.setText("")
        self.mes_5.setAlignment(QtCore.Qt.AlignCenter)
        self.mes_5.setObjectName("mes_5")
        self.gridLayout_4.addWidget(self.mes_5, 4, 2, 1, 1)
        self.line = QtWidgets.QFrame(self.tab)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_4.addWidget(self.line, 6, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_4, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.gridLayout_3.addItem(spacerItem1, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_2.sizePolicy().hasHeightForWidth())
        self.tab_2.setSizePolicy(sizePolicy)
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.measure_tableWidget = QtWidgets.QTableWidget(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.measure_tableWidget.sizePolicy().hasHeightForWidth())
        self.measure_tableWidget.setSizePolicy(sizePolicy)
        self.measure_tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.measure_tableWidget.setObjectName("measure_tableWidget")
        self.measure_tableWidget.setColumnCount(5)
        self.measure_tableWidget.setRowCount(14)
        item = QtWidgets.QTableWidgetItem()
        self.measure_tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.measure_tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.measure_tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.measure_tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.measure_tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.measure_tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.measure_tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.measure_tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.measure_tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.measure_tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.measure_tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.measure_tableWidget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.measure_tableWidget.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.measure_tableWidget.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        item.setFont(font)
        self.measure_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.measure_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.measure_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.measure_tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.measure_tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.measure_tableWidget.setItem(1, 0, item)
        self.horizontalLayout_2.addWidget(self.measure_tableWidget)
        self.interrogate_all = QtWidgets.QPushButton(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.interrogate_all.sizePolicy().hasHeightForWidth())
        self.interrogate_all.setSizePolicy(sizePolicy)
        self.interrogate_all.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.interrogate_all.setObjectName("interrogate_all")
        self.horizontalLayout_2.addWidget(self.interrogate_all)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.monitor = QtWidgets.QPushButton(self.tab_3)
        self.monitor.setGeometry(QtCore.QRect(490, 490, 151, 23))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 212, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 113, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 212, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 212, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 113, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 212, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 212, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 113, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.monitor.setPalette(palette)
        self.monitor.setAutoFillBackground(True)
        self.monitor.setCheckable(True)
        self.monitor.setObjectName("monitor")
        self.label = QtWidgets.QLabel(self.tab_3)
        self.label.setGeometry(QtCore.QRect(320, 80, 491, 371))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab_3)
        self.label_2.setGeometry(QtCore.QRect(30, 30, 291, 471))
        self.label_2.setObjectName("label_2")
        self.tabWidget.addTab(self.tab_3, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 842, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.dissconect_can.setText(_translate("MainWindow", "Disconnect Can"))
        self.browse_2.setText(_translate("MainWindow", "Browse"))
        self.interrogate_and_get_temperature.setText(_translate("MainWindow", "Interrogate and Get Temperature"))
        self.connect_can.setText(_translate("MainWindow", "Connect Can"))
        self.read_sensor_file.setText(_translate("MainWindow", "Read Sensor File"))
        self.browse_3.setText(_translate("MainWindow", "Browse"))
        self.get_version.setText(_translate("MainWindow", "Get Version"))
        self.browse_1.setText(_translate("MainWindow", "Browse"))
        self.mes_1.setText(_translate("MainWindow", "Sensor:"))
        self.read_calibration_file.setText(_translate("MainWindow", "Read Calibration File"))
        self.interrogate.setText(_translate("MainWindow", "Interrogate"))
        self.get_temperature.setText(_translate("MainWindow", "Get Temperature"))
        self.read_band_file.setText(_translate("MainWindow", "Read Band File"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Connect"))
        item = self.measure_tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "B06"))
        item = self.measure_tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "C06"))
        item = self.measure_tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "A06"))
        item = self.measure_tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "S06"))
        item = self.measure_tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "E06"))
        item = self.measure_tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "F06"))
        item = self.measure_tableWidget.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "D06"))
        item = self.measure_tableWidget.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "H07"))
        item = self.measure_tableWidget.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "S07"))
        item = self.measure_tableWidget.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "A07"))
        item = self.measure_tableWidget.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "C07"))
        item = self.measure_tableWidget.verticalHeaderItem(11)
        item.setText(_translate("MainWindow", "E07"))
        item = self.measure_tableWidget.verticalHeaderItem(12)
        item.setText(_translate("MainWindow", "F07"))
        item = self.measure_tableWidget.verticalHeaderItem(13)
        item.setText(_translate("MainWindow", "G07"))
        item = self.measure_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Temperature"))
        item = self.measure_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "F0"))
        item = self.measure_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "F1"))
        item = self.measure_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Mag0"))
        item = self.measure_tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Mag1"))
        __sortingEnabled = self.measure_tableWidget.isSortingEnabled()
        self.measure_tableWidget.setSortingEnabled(False)
        self.measure_tableWidget.setSortingEnabled(__sortingEnabled)
        self.interrogate_all.setText(_translate("MainWindow", "Interrogate All Sensors"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Measurements"))
        self.monitor.setText(_translate("MainWindow", "Monitor"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/cmap4/Map_exmple.png\"/></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/barel1/barel.jpg\"/></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Map"))
import barel_rc
import map4_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
