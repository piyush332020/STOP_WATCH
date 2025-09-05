import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel,QWidget,QPushButton,QVBoxLayout,QHBoxLayout
from PyQt5.QtCore import Qt,QTimer,QTime,Qt
class stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.timer=QTimer(self)
        self.time=QTime(0,0,0,0)
        self.timelabel=QLabel("00:00:00.00",self)
        self.startbutton=QPushButton("start",self)
        self.stopbutton=QPushButton("stop",self)
        self.resetbutton=QPushButton("reset",self)
        self.timer=QTimer(self)
        self.initui()
    def initui(self):
        self.setWindowTitle("stopwatch")
        
        vbox=QVBoxLayout()
        self.setLayout(vbox)
        vbox.addWidget(self.timelabel)
        vbox.addWidget(self.startbutton)
        vbox.addWidget(self.stopbutton)
        vbox.addWidget(self.resetbutton)
        self.timelabel.setAlignment(Qt.AlignCenter) 
        
        
        hbox=QHBoxLayout()
        hbox.addWidget(self.startbutton)
        hbox.addWidget(self.stopbutton)
        hbox.addWidget(self.resetbutton)
        
        vbox.addLayout(hbox) # Add the horizontal layout to the vertical layout to arrange buttons horizontally
        self.setStyleSheet("""
            QPushButton,QLabel{
            padding: 20px;
            font-weight: bold;
            font-family: calibri;}            
                        
            QPushButton{ 
                font-size: 20px;
                }
            QLabel{
                background-color: lightblue;
                font-size: 120px;
                border-radius: 10px;}
            """)
        self.startbutton.clicked.connect(self.start)
        self.stopbutton.clicked.connect(self.stop)  
        self.resetbutton.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_time)
        
        
    def start(self):
        self.timer.start(10)
        
    def stop(self):
        self.timer.stop()
    def reset(self):
        self.timer.stop()
        self.time=QTime(0,0,0,0)
        self.timelabel.setText("00:00:00.00")
    def format_time(self,time): # Format the time as hh:mm:ss.zzz and time is a QTime object
         # Extract hours, minutes, seconds, and milliseconds from the QTime object
         
        hours=time.hour()
        minutes=time.minute()
        seconds=time.second()
        milliseconds=time.msec() //10 # Convert milliseconds to two digits by integer division  
        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}" # Format time as hh:mm:ss.zzz with leading zeros
        
    def update_time(self): 
        self.time=self.time.addMSecs(10) # Increment time by 10 milliseconds .addMSecs(10) is used to add milliseconds to the current time
         # Update the label with the formatted time
        self.timelabel.setText(self.format_time(self.time)) # Format the time as hh:mm:ss.zzz  
        #self.time returns a QTime object which gives current time
        
if __name__=="__main__":
    app=QApplication(sys.argv)
    stopwatch=stopwatch()
    stopwatch.show()
    sys.exit(app.exec_())