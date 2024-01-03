from PyQt5 import QMainWindow,QMessageBox
from PyQt5.uic import loadUi

class LoginWindow(QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        loadUi('C:\Users\Admin\Desktop\HARSHIT\weapon_detection\client_side\ui\login_window.ui',self)
        
        self.register_button.clicked.connect(self.go_to_register_page)
        self.login_button.clicked.connect(self.open_setting_window)
        
        self.show()
        
    def go_to_register_page(self):
        print ("Go to Register Page")
        
    def open_setting_window(self):
        print ("Open Settings Window")         