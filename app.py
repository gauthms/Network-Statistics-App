import os
import sys 
from PyQt4.QtCore import * 
from PyQt4.QtGui import *  
 
def main(): 
    app = QApplication(sys.argv) 
    w = MyWindow() 
    w.setWindowTitle("Network Statistics")
    w.setGeometry(720,320,500,500)
    w.show() 
    sys.exit(app.exec_()) 
 
class MyWindow(QWidget): 
    def __init__(self, *args): 
        QWidget.__init__(self, *args) 
        label = QLabel(self.tr("press Enter to display network statistics"))
        self.le = QLineEdit()
        self.te = QTextEdit()
	self.btn = QPushButton("Exit")
        layout = QVBoxLayout(self)
        layout.addWidget(label)
        layout.addWidget(self.le)
        layout.addWidget(self.te)
	layout.addWidget(self.btn)
        self.setLayout(layout) 
	self.le.setText('location of information : /proc/net/netstat')
        self.connect(self.le,SIGNAL("returnPressed(void)"),
                     self.run_command)
	self.btn.clicked.connect(quit)
	
	

    def run_command(self):
        cmd = '''cat /proc/net/netstat |awk '(f==0) { i=1; while ( i<=NF) {n[i] = $i; i++ }; f=1; 	next}(f==1){ i=2; while ( i<=NF){ printf "%s = %d\\n", n[i], $i; i++}; f=0} ' '''
        stdouterr = os.popen4(cmd)[1].read()
        self.te.setText(stdouterr)
  
if __name__ == "__main__": 
    main()
