import base64
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

line_1 = 'None'
line_2 = 'None'

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
        Form.setFixedSize(287, 462)
        Form.resize(287, 462)
        Form.setMinimumSize(QtCore.QSize(287, 315))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/him/him.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 0, 271, 41))
        self.label.setObjectName("label")
        
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(190, 70, 75, 23))
        self.pushButton.setObjectName("pushButton")
        
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(20, 40, 251, 20))
        self.lineEdit.setObjectName("lineEdit")
        
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 220, 271, 41))
        self.label_2.setObjectName("label_2")
        
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 260, 251, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 290, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(20, 110, 241, 121))
        self.textEdit.setObjectName("textEdit")
        
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(20, 330, 241, 121))
        self.textEdit_2.setObjectName("textEdit_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "him表情包加密神器"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; vertical-align:sub;\">请输入要加密成表情的文字</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "转换"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; vertical-align:sub;\">请输入要解密的表情</span></p></body></html>"))
        self.pushButton_2.setText(_translate("Form", "转换"))

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
    sys.exit(app.exec_())

