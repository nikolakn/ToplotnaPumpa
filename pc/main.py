#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
from PyQt4 import QtGui, QtCore
import time
import serial
import re
import csv

def pritisak(temp):
    return 0.00001*(temp*temp*temp)+0.002*(temp*temp)+0.161*temp+4.857
class Top(QtGui.QWidget):
    def __init__(self):
        super(Top, self).__init__()
        self.loadedImage = QtGui.QImage()
        self.loadedImage.load("sema2.png")
        self.loadedImage = self.loadedImage.scaledToHeight(500)
        self.t1=[]
        self.t2=[]
        self.t3=[]
        self.t4=[]
        self.t5=[]
        self.t6=[]
        self.c1 = self.c2 = self.c3 = self.c4 = self.c5 = self.c6 = True
    def paintEvent(self, QPaintEvent):
        paint = QtGui.QPainter(self)
        paint.setPen(QtCore.Qt.black);
        paint.setBrush(QtCore.Qt.white);
        #paint.drawRect(0, 0, 850, 650);
        paint.drawImage(QtCore.QPoint(50, 50),self.loadedImage)
        paint.drawLine(0,650,900,650)
        paint.drawText(710,684,"- 30")
        paint.drawText(710,674,"- 20")
        paint.drawText(710,664,"- 10")
        paint.drawText(710,654,"- 0")
        paint.drawText(710,644,"- 10")
        paint.drawText(710,634,"- 20")
        paint.drawText(710,624,"- 30")
        paint.drawText(710,614,"- 40")
        paint.drawText(710,604,"- 50")
        paint.drawText(710,594,"- 60")
        paint.drawText(710,584,"- 70")
        paint.drawText(710,574,"- 80")
        paint.drawText(710,564,"- 90")
        paint.drawText(710,554,"- 100")
        
        if self.c1:
            l = 699
            paint.setPen(QtCore.Qt.black);
            if len(self.t1)<=700:
                tp1=self.t1
                l = len(self.t1)-1 
            else:
                tp1=self.t1[-700:]
            for x in range(0,l,1):
                paint.drawLine(x,650-tp1[x],x+1,650-tp1[x+1])
        if self.c2:
            #s2##############
            l = 699
            paint.setPen(QtCore.Qt.black);
            if len(self.t2)<=700:
                tp2=self.t2
                l = len(self.t2)-1 
            else:
                tp2=self.t2[-700:]
            for x in range(0,l,1):
                paint.drawLine(x,650-tp2[x],x+1,650-tp2[x+1])
        if self.c3:
            #s3##############
            l = 699
            paint.setPen(QtCore.Qt.darkBlue);
            if len(self.t3)<=700:
                tp3=self.t3
                l = len(self.t3) -1
            else:
                tp3=self.t3[-700:]
            for x in range(0,l,1):
                paint.drawLine(x,650-tp3[x],x+1,650-tp3[x+1]) 
        if self.c4:        
            #s4##############
            l = 699
            paint.setPen(QtCore.Qt.red);
            if len(self.t4)<=700:
                tp4=self.t4
                l = len(self.t4) -1
            else:
                tp4=self.t4[-700:]
            for x in range(0,l,1):
                paint.drawLine(x,650-tp4[x],x+1,650-tp4[x+1]) 
        if self.c5:
            #s5##############
            l = 699
            paint.setPen(QtCore.Qt.cyan);
            if len(self.t5)<=700:
                tp5=self.t5
                l = len(self.t5) -1
            else:
                tp5=self.t5[-700:]
            for x in range(0,l,1):
                paint.drawLine(x,650-tp5[x],x+1,650-tp5[x+1])  
        if self.c6:        
            #s6##############
            paint.setPen(QtCore.Qt.red);
            l = 699
            if len(self.t6)<=700:
                tp6=self.t6
                l = len(self.t6) -1
            else:
                tp6=self.t6[-700:]
            for x in range(0,l,1):
                paint.drawLine(x,650-tp6[x],x+1,650-tp6[x+1])            
class Example(QtGui.QMainWindow):
    
    def __init__(self):
        super(Example, self).__init__()
        self.sl1 = False
        self.sl2 = False
        self.sr1 = False
        self.sr2 = False
        self.sr3 = False
        self.sr4 = False
        
        #with open('pritisak.csv', mode='r') as infile:
        #    reader = csv.reader(infile)
        #    self.pritisci = dict((rows[0],rows[1]) for rows in reader)
        self.initUI()
        
    def initUI(self):   
        self.ctimer = QtCore.QTimer()   
        self.ser = serial.Serial('COM4', 9600, timeout=1)
		
        self.wgore = Top()
        self.setCentralWidget(self.wgore)
        #self.addWidget(wgore)
        self.wgore.resize(850,700);
        self.wgore.move(0,0);
        
        self.texts1 =  QtGui.QLineEdit(self)
        self.texts1.resize(70,25);
        self.texts1.move(550,300);  
        self.ce1 = QtGui.QCheckBox(self)  
        self.ce1.setCheckState(QtCore.Qt.Checked)        
        self.ce1.move(550,270);
        self.ce1.stateChanged.connect(self.ce1_changed)
        
        self.texts2 =  QtGui.QLineEdit(self)
        self.texts2.resize(70,25);
        self.texts2.move(550,500);
        self.ce2 = QtGui.QCheckBox(self)  
        self.ce2.setCheckState(QtCore.Qt.Checked)        
        self.ce2.move(550,470);
        self.ce2.stateChanged.connect(self.ce2_changed)
        
        self.texts3 =  QtGui.QLineEdit(self)
        self.texts3.resize(70,25);
        self.texts3.move(680,300);
        self.ce3 = QtGui.QCheckBox(self)  
        self.ce3.setCheckState(QtCore.Qt.Checked)        
        self.ce3.move(680,270);
        self.ce3.stateChanged.connect(self.ce3_changed)
        
        self.texts4 =  QtGui.QLineEdit(self)
        self.texts4.resize(90,25);
        self.texts4.move(300,160); 
        self.ce4 = QtGui.QCheckBox(self)  
        self.ce4.setCheckState(QtCore.Qt.Checked)        
        self.ce4.move(300,130);
        self.ce4.stateChanged.connect(self.ce4_changed)
        
        
        self.texts5 =  QtGui.QLineEdit(self)
        self.texts5.resize(70,25);
        self.texts5.move(90,510);
        self.ce5 = QtGui.QCheckBox(self)  
        self.ce5.setCheckState(QtCore.Qt.Checked)        
        self.ce5.move(90,480);
        self.ce5.stateChanged.connect(self.ce5_changed)
        
        self.texts6 =  QtGui.QLineEdit(self)
        self.texts6.resize(80,25);
        self.texts6.move(430,340);
        self.ce6 = QtGui.QCheckBox(self)  
        self.ce6.setCheckState(QtCore.Qt.Checked)        
        self.ce6.move(430,310);
        self.ce6.stateChanged.connect(self.ce6_changed)
	
	
        btn1 = QtGui.QPushButton("kompresor", self)
        btn1.resize(60,30);
        btn1.move(394, 450)

        btn2 = QtGui.QPushButton("ventilator", self)
        btn2.resize(60,30);
        btn2.move(150, 120)
  
        btnr1 = QtGui.QPushButton("ventil", self)
        btnr1.resize(40,30);
        btnr1.move(220, 350)

        btnr2 = QtGui.QPushButton("pumpa", self)
        btnr2.resize(60,30);
        btnr2.move(800, 300)

        btnrs1 = QtGui.QPushButton("step otvori", self)
        btnrs1.resize(70,20);
        btnrs1.move(190, 400)
        btnrs1.clicked.connect(self.stepotvori)            
       
        
        btnrs2 = QtGui.QPushButton("step zatvori", self)
        btnrs2.resize(70,20);
        btnrs2.move(190, 460)
        btnrs2.clicked.connect(self.stepzatvori)
        btnrs2.setEnabled(False);
        
        self.step = QtGui.QSpinBox(self)
        self.step.setValue(30)
        self.setpi=30
        self.step.resize(50,30)
        self.step.move(185, 425)
        self.step.setMaximum (70)
        self.step.setMinimum (0)
        self.step.findChild(QtGui.QLineEdit).setReadOnly(True);
        QtCore.QObject.connect(self.step, QtCore.SIGNAL("valueChanged(int)"),self.steppromena)
        #btnr3 = QtGui.QPushButton("rele 5", self)
        #btnr3.move(150, 150)

        #btnr4 = QtGui.QPushButton("rele 6", self)
        #btnr4.move(300, 150) 

        btn1.setStyleSheet("background-color: #696969")
        btn2.setStyleSheet("background-color: #696969")
        btnr1.setStyleSheet("background-color: #696969")
        btnr2.setStyleSheet("background-color: #696969")
        #btnr3.setStyleSheet("background-color: #696969")
        #btnr4.setStyleSheet("background-color: #696969")

        btn1.clicked.connect(self.l1Clicked)            
        btn2.clicked.connect(self.l2Clicked)
        btnr1.clicked.connect(self.r1Clicked)  
        btnr2.clicked.connect(self.r2Clicked)  
        #btnr3.clicked.connect(self.r3Clicked)  
        #btnr4.clicked.connect(self.r4Clicked)  

        QtCore.QObject.connect(self.ctimer, QtCore.SIGNAL("timeout()"),     self.constantUpdate)
        #self.ctimer.start(300)
        self.ctimer.start(300)
        self.statusBar()
        
        self.setGeometry(50, 50, 900, 720)
        self.setWindowTitle('Event sender')
        self.show()
        
    def steppromena(self, i):
        #print(i)
        if(self.setpi<i):
            r = i - self.setpi
            st = str(r)
            if(len(st)==1):
                st = "0"+st
            self.ser.write("stepnapred"+st+"\n") 
        if(self.setpi>i):
            r = self.setpi-i
            st = str(r)
            if(len(st)==1):
                st = "0"+st
            self.ser.write("stepnazad"+st+"\n") 
        self.setpi = i
    def ce1_changed(self):   
        self.wgore.c1 = not self.wgore.c1
        self.repaint()
    def ce2_changed(self):   
        self.wgore.c2 = not self.wgore.c2
        self.repaint()
    def ce3_changed(self):   
        self.wgore.c3 = not self.wgore.c3
        self.repaint()
    def ce4_changed(self):   
        self.wgore.c4 = not self.wgore.c4
        self.repaint()
    def ce5_changed(self):   
        self.wgore.c5 = not self.wgore.c5
        self.repaint()
    def ce6_changed(self):   
        self.wgore.c6 = not self.wgore.c6
        self.repaint()        
    def stepotvori(self):
        self.ser.write("stepotvori\n") 
        self.setpi = 70
        self.step.setValue(70)
        
    def stepzatvori(self):  
        self.ser.write("stepzatvori\n")   
        self.setpi = 0
        self.step.setValue(0)        
    def constantUpdate(self):
        self.ser.flushInput()
        #time.sleep( 0.10 )
        #line="START;S2k7=10;S5k_1=15;S5k_2=20;S5k_3=25;S5k_4=30;S200k=60;STOP"
        line = self.ser.readline()
        matchObj1 = re.search( r'S2k7=.*?;', line)
        matchObj2 = re.search( r'S5k_1=.*?;', line)
        matchObj3 = re.search( r'S5k_2=.*?;', line)
        matchObj4 = re.search( r'S5k_3=.*?;', line)
        matchObj5 = re.search( r'S5k_4=.*?;', line)
        matchObj6 = re.search( r'S200k=.*?;', line)
        s1 = s2 = s3 = s4 = s5 = s6 = ""
        if matchObj1:
            s1 = matchObj1.group()[5:]
            s1 = s1[:-1]
            self.wgore.t1.append(int(s1))
            s1 = s1 + u"° "+'%.2fbar' % pritisak(int(s1))
        if matchObj2:
            s2 = matchObj2.group()[6:]
            s2 = s2[:-1]
            self.wgore.t2.append(int(s2))
            s2 = s2 + u"° "+'%.2fbar' % pritisak(int(s2))
        if matchObj3:
            s3 = matchObj3.group()[6:]
            s3 = s3[:-1]
            self.wgore.t3.append(int(s3))
        if matchObj4:
            s4 = matchObj4.group()[6:]
            s4 = s4[:-1]
            self.wgore.t4.append(int(s4))
            s4 = s4 + u"° "+'%.2fbar' % pritisak(int(s4))
        if matchObj5:
            s5 = matchObj5.group()[6:]
            s5 = s5[:-1]
            self.wgore.t5.append(int(s5))
            s5 = s5 + u"° "+'%.2fbar' % pritisak(int(s5))
        if matchObj6:
            s6 = matchObj6.group()[6:]
            s6 = s6[:-1]
            self.wgore.t6.append(int(s6))
            s6 = s6 + u"° "+'%.2fbar' % pritisak(int(s6))
            
        if (line[:5]=="START"):  
            self.texts1.setText(s1)
            self.texts2.setText(s2)
            self.texts3.setText(s3)
            self.texts4.setText(s4)
            self.texts5.setText(s5)
            self.texts6.setText(s6)   
        self.repaint()
            
    def l1Clicked(self):   
        sender = self.sender()
        if self.sl1== False:
            sender.setStyleSheet("background-color: green")
            self.ser.write("r1on\n")  
            self.sl1 = True
        else:
            sender.setStyleSheet("background-color: #696969")
            self.ser.write("r1off\n") 
            self.sl1 = False			
        
    def l2Clicked(self):  
        sender = self.sender()
        if self.sl2== False:
            self.ser.write("r2on\n") 
            sender.setStyleSheet("background-color: green")
            self.sl2 = True
        else:
            self.ser.write("r2off\n") 
            sender.setStyleSheet("background-color: #696969")
            self.sl2 = False

    def r1Clicked(self):  
        sender = self.sender()
        if self.sr1== False:
            self.ser.write("r3on\n") 
            sender.setStyleSheet("background-color: green")
            self.sr1 = True
        else:
            sender.setStyleSheet("background-color: #696969")
            self.ser.write("r3off\n") 
            self.sr1 = False
    def r2Clicked(self):  
        sender = self.sender()
        if self.sr2== False:
            self.ser.write("r4on\n") 
            sender.setStyleSheet("background-color: green")
            self.sr2 = True
        else:
            sender.setStyleSheet("background-color: #696969")
            self.ser.write("r4off\n") 
            self.sr2 = False
    def r3Clicked(self):  
        sender = self.sender()
        if self.sr3== False:
            sender.setStyleSheet("background-color: green")
            self.ser.write("r5on\n") 
            self.sr3 = True
        else:
            sender.setStyleSheet("background-color: #696969")
            self.ser.write("r5off\n") 
            self.sr3 = False
    def r4Clicked(self):  
        sender = self.sender()
        if self.sr4== False:
            sender.setStyleSheet("background-color: green")
            self.ser.write("r6on\n") 
            self.sr4 = True
        else:
            sender.setStyleSheet("background-color: #696969")
            self.ser.write("r6off\n") 
            self.sr4 = False

    def closeEvent(self, event):
        self.ser.close()
    

def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
