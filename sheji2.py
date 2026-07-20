import base64
from PyQt6 import QtCore, QtGui, QtWidgets
import sys

class key_locks:
    @staticmethod
    def text_to_binary(text):
        encoded_bytes = base64.b64encode(text.encode('utf-8'))
        return ''.join(format(byte, '08b') for byte in encoded_bytes).replace('0','☺').replace('1','✌')

    @staticmethod
    def binary_to_text(binary_string):
        try:
            byte_array = bytearray(int(binary_string.replace('☺','0').replace('✌','1')[i:i+8], 2) for i in range(0, len(binary_string), 8))        
            return base64.b64decode(byte_array).decode('utf-8')
        except:
            return "只能加表情"

class Ui_Form:
    def setupUi(self, Form):
        Form.setObjectName("Form")
     
        Form.resize(320, 480)
        Form.setMinimumSize(QtCore.QSize(320, 380))
    
        Form.setStyleSheet("""
QWidget#Form{
    image: url(:/him/him.png);
}
QLabel{
    color: #ffffff;
    background-color: rgba(0,0,0,70);
    border-radius: 8px;
    padding:4px;
}
QLineEdit{
    background-color: rgba(255,255,255,180);
    border:1px solid #666666;
    border-radius:6px;
    padding:4px 8px;
    font-size:11pt;
}
QLineEdit:focus{
    border:1px solid #4488ff;
}
QTextEdit{
    background-color: rgba(255,255,255,180);
    border:1px solid #666666;
    border-radius:6px;
    padding:6px;
    font-size:11pt;
}
QTextEdit:focus{
    border:1px solid #4488ff;
}
QPushButton{
    background-color: rgba(40,80,160,200);
    color:#fff;
    border:none;
    border-radius:6px;
    padding:4px;
    font-weight:bold;
}
QPushButton:hover{
    background-color: rgba(60,110,210,220);
}
QPushButton:pressed{
    background-color: rgba(20,50,120,200);
}
        """)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/him/him.ico"))
        Form.setWindowIcon(icon)

        # 加密标题label
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(15, 10, 290, 45))
        self.label.setObjectName("label")
        
        # 加密输入框
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(15, 60, 210, 28))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText("这是需要加密的文字")
        
        # 加密按钮
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(235, 60, 70, 28))
        self.pushButton.setObjectName("pushButton")
        
        # 加密输出框
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(15, 100, 290, 130))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setPlaceholderText("加密后的表情文本")

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(15, 240, 290, 45))
        self.label_2.setObjectName("label_2")

        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(15, 290, 210, 28))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setPlaceholderText("粘贴加密表情字符串")

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(235, 290, 70, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        
        
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(15, 330, 290, 130))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_2.setPlaceholderText("解密还原后的原始文字")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Him表情包加密神器"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:bold;\">文字 → Him表情加密</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "加密转换"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:bold;\">Him表情 → 文字解密</span></p></body></html>"))
        self.pushButton_2.setText(_translate("Form", "解密转换"))

        self.pushButton.clicked.connect(self.encryption)
        self.pushButton_2.clicked.connect(self.decryption)

    def encryption(self):
        text = self.lineEdit.text()
        self.textEdit.setText(key_locks.text_to_binary(text))

    def decryption(self):
        binary_string = self.lineEdit_2.text()
        text = key_locks.binary_to_text(binary_string)
        self.textEdit_2.setText(text)

import him_rc

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())

