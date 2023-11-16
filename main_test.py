from PyQt5 import QtCore, QtWidgets, QtGui
from demo_gui import Ui_MainWindow
from ctypes import *
from array import *
import sys
import os
import time



#dll import and functions
mydll=cdll.LoadLibrary(os.path.join("LLOYDSSENSORDLL.dll"))

global st1
global st2
global st3

st1 = 0
st2 = 0
st3 = 0
outdata=(c_long*5)() #ctypes handles data types from dlls commands

mydll.get_Version.restype=c_char_p # get_version functions return type is char *
mydll.get_Temp.restype=c_float # get_Temp function returns float value
mydll.get_Temp_Freq_Mag.restype=c_float # get_Temp_Freq_Mag function returns float value

class MonitorThread(QtCore.QThread):

    measured = pyqtSignal([float])

    def __init__(self, parent=None):
        super(MonitorThread, self).__init__(parent)
        self.threadRunning = False

    def run(self):
        if self.threadRunning:
            return
        self.threadRunning = True
        while self.threadRunning:

            #data = []
            #self.measured.emit(data)
            pass # insert here

    def stop(self):
        self.threadRunning = False


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):


    def __init__(self, parent=None):
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)
        self.monitorThread = None
        #button actions
        self.connect_can.clicked.connect(self.canconn)
        self.dissconect_can.clicked.connect(self.candisconn)
        self.interrogate.clicked.connect(self.inter)
        self.get_temperature.clicked.connect(self.temp)
        self.get_version.clicked.connect(self.getvers)
        self.interrogate_and_get_temperature.clicked.connect(self.getall)
        self.read_sensor_file.clicked.connect(self.readsens)
        self.read_band_file.clicked.connect(self.readband)
        self.read_calibration_file.clicked.connect(self.readcal)
        self.browse_1.clicked.connect(self.sensor_file_open)
        self.browse_2.clicked.connect(self.band_file_open)
        self.browse_3.clicked.connect(self.cal_file_open)
        self.interrogate_all.clicked.connect(self.interall)
        self.monitor.clicked.connect(self.mntr)
        self.stop.clicked.connect(self.paint)





    #methods
    def sensor_file_open(self):
        name = QtWidgets.QFileDialog.getOpenFileName(self, 'Choose file')
        self.read_sensor_file_text.setText(name[0])


    def band_file_open(self):
        name = QtWidgets.QFileDialog.getOpenFileName(self, 'Choose file')
        self.read_band_file_text.setText(name[0])

    def cal_file_open(self):
        name = QtWidgets.QFileDialog.getOpenFileName(self, 'Choose file')
        self.read_calbration_file_text.setText(name[0])


    #dll methods
    def readsens(self):
        global st1
        sensorfilename = self.read_sensor_file_text.text()
        sensorfilename_ok = mydll.Sensors_from_file_read(sensorfilename.encode()) # function returns 1 on success
        st1=sensorfilename_ok
        if (sensorfilename_ok==1):
            self.chktempon()
            self.read_band_file.setEnabled(True)
            self.read_calibration_file.setEnabled(True)
            self.connect_can_message.setText("Sensor file read successfully ")
        else:
            self.connect_can_message.setText("Could not read sensor file ")

    def readband(self):
        bandfilename = self.read_band_file_text.text()
        bandfilename_ok = mydll.Bands_from_file_read(bandfilename.encode())
        st3=bandfilename_ok
        if (bandfilename_ok==1):
            self.chktempon()
            self.interrogate.setEnabled(True)
            self.connect_can_message.setText("Band file read successfully ")
        else:
            self.connect_can_message.setText("Could not read band file ")

    def readcal(self):
        global st2
        calibfilename = self.read_calbration_file_text.text()
        calibfilename_ok=mydll.Read_calib_data(calibfilename.encode())
        st2=calibfilename_ok
        if (calibfilename_ok==1):
            self.chktempon()
            self.connect_can_message.setText("Caliberation file read successfully ")
        else:
            self.connect_can_message.setText("Could not read calibration file ")

    def chktempon(self):
        if st1==1 and st2==1 :
            self.get_temperature.setEnabled(True)
            self.interrogate_and_get_temperature.setEnabled(True)

    #connect to can
    def canconn(self):
        stat_ver= mydll.Can_Connect(2)
        if stat_ver==1:
            self.connect_can_message.setText("Device Connected")
            self.connect_can.setEnabled(False)
            self.dissconect_can.setEnabled(True)
            self.get_version.setEnabled(True)
        else:
            self.connect_can_message.setText("Device not Connected")

    def candisconn(self):
        stat_ver=mydll.Can_Disconnect()
        if stat_ver==1:
            self.connect_can_message.setText("Device disconnected")
            self.dissconect_can.setEnabled(False)
            self.connect_can.setEnabled(True)
            self.get_version.setEnabled(False)
        else:
            self.connect_can_message.setText("Device failed to disconnect")

    def getvers(self):
        vers = mydll.get_Version()
        vers = str(vers)
        self.get_version_message.setText(vers)

    def chkinterron(self):
        if st1==1 and st3==1:
            self.interrogate.setEnabled(True)
    #interrogate sensor
    def inter(self):
        sensorname = self.interrogate_text.text()
        mydll.Interrogate_sensor(sensorname.encode(),outdata)

        self.mes_1.setText('Sensor: ' + sensorname)
        self.mes_2.setText("F1: " + str(outdata[0] + 424000000))
        self.mes_3.setText("F2: " + str(outdata[1] + 424000000))
        self.mes_4.setText("")
        self.mes_5.setText("")
    #get temperature
    def temp(self):
        sensorname = self.interrogate_text.text()
        temp = "%.2f" % mydll.get_Temp(sensorname.encode())
        self.mes_1.setText('Sensor: ' + sensorname)
        self.mes_2.setText('Tmp: ' + temp)
        self.mes_3.setText("")
        self.mes_4.setText("")
        self.mes_5.setText("")

    #get all parameters from sensor
    def getall(self):
        sensorname = self.interrogate_text.text()
        self.mes_1.setText('Sensor: ' + sensorname)
        self.mes_2.setText("Tmp: " + "%.2f" % mydll.get_Temp_Freq_Mag(sensorname.encode(),outdata))
        self.mes_3.setText("")
        self.mes_4.setText("")
        self.mes_5.setText("")


    #populate measurments table with items and then change the items
    def interall(self):
        for i in range(4):
            for j in range(5):
                item = QtWidgets.QTableWidgetItem()
                self.measure_tableWidget.setItem(j,i,item)

        sensors = ["S06", "C06", "A06", "B06"]

        j=0
        for sensorname in sensors:
            mydll.Interrogate_sensor(sensorname.encode(),outdata)
            print(sensorname)
            time.sleep(1)

            self.measure_tableWidget.item(0,j).setText("%.2f" % mydll.get_Temp(sensorname.encode()))
            self.measure_tableWidget.item(1,j).setText(str(outdata[0]+424000000))
            self.measure_tableWidget.item(2,j).setText(str(outdata[1]+424000000))
            self.measure_tableWidget.item(3,j).setText(str(outdata[2]))
            self.measure_tableWidget.item(4,j).setText(str(outdata[3]))
            self.measure_tableWidget.repaint()
            j+=1


    def populate_rows(self, data):
        #pass

    def mntr(self):
        if self.monitorThread is not None:
            self.monitorThread.stop()
            self.monitorThread.wait()
            self.monitorThread = None
            return

        self.monitorThread = MonitorThread(self)
        self.monitorThread.measured.connect(self.populate_rows)
        self.monitorThread.start()

        #if self.monitor.isChecked():
            #self.mstatus.setAutoFillBackground(False) change colour?
        #    print("measuring")
        #    self.mstatus.setText("online")
        #    #self.interall()
        #    time.sleep(2)

        #print("off")
        #self.mstatus.setText("offline")

    def paint(self):
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        #brush.setStyle(QtCore.Qt.SolidPattern)
        painter = QtGui.QPalette()
        painter.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.label.setPalette(painter)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec())
