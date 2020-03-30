import os
import sys 
from PyQt4.QtCore import * 
from PyQt4.QtGui import * 
 
def main(): 
    app = QApplication(sys.argv) 
    w = MyWindow() 
    w.show() 
    sys.exit(app.exec_()) 
 
class MyWindow(QWidget): 
    def __init__(self, *args): 
        QWidget.__init__(self, *args) 
 
  
        label = QLabel(self.tr("press Enter to display network statistics"))
        self.le = QLineEdit()
        self.te = QTextEdit()

 
        layout = QVBoxLayout(self)
        layout.addWidget(label)
        layout.addWidget(self.le)
        layout.addWidget(self.te)
        self.setLayout(layout) 


        self.connect(self.le,SIGNAL("returnPressed(void)"),
                     self.run_command)

    def run_command(self):
        cmd = '''cat /proc/net/netstat |awk '(f==0) { i=1; while ( i<=NF) {n[i] = $i; i++ }; f=1; 	next}(f==1){ i=2; while ( i<=NF){ printf "%s = %d\\n", n[i], $i; i++}; f=0} ' '''
        stdouterr = os.popen4(cmd)[1].read()
        self.te.setText(stdouterr)
  
if __name__ == "__main__": 
    main()
