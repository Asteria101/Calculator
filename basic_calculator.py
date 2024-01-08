from math import sqrt
import PyQt5.QtWidgets as qtw
from PyQt5 import uic, QtCore, QtWidgets
from PyQt5.QtGui import *
import sys

# Colors
# celadon: #BDE4A8
# tea green: #D7F2BA
# lavander pink: #F44174
# pink: #DB2763
# bright pink: #F44174
# ♥

# self.face.setText("(*ᴗ͈ˬᴗ͈)ꕤ*.ﾟ")

CALCULATOR_VERSION = "v1.8"

FACE_BORDER_INFO = "border-radius : 17px; border : 1px outset rgb(37, 54, 68);"
FACE_DEFAULT_STYLE_SHEET = FACE_BORDER_INFO + "color : rgba(74, 135, 185, 200); background-color : rgba(179, 255, 201, 255);"
RESULT_FIELD_DEFAULT = "color : rgba(71, 128, 177, 235); background-color: rgba(179, 255, 201, 230); border-bottom : 3px solid rgba(0, 0, 0, 0); border-bottom-color : rgb(95, 136, 107); padding-bottom : 7px;"


class MainWindow(qtw.QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        uic.loadUi('basic_calculator.ui', self)
        
        self.setWindowTitle(f'Calculadora - {CALCULATOR_VERSION}')

        # Logic of the calculator
        self.temp_nums = []
        self.fin_nums = []
        self.ANS = ''
        self.expression = ''.join(self.fin_nums) + ''.join(self.temp_nums)

        self.central_widgets = self.findChild(qtw.QWidget, "centralwidget")

        self.header = self.findChild(qtw.QFrame, "header_frame")
        self.btn_frame = self.findChild(qtw.QFrame, "frame")
        self.close_btn = self.findChild(qtw.QPushButton, "close_window_button")
        self.minimize_btn = self.findChild(qtw.QPushButton, "minimize_window_button")
        self.label = self.findChild(qtw.QLabel, "Name")

        self.label.setText(f'Calculadora - {CALCULATOR_VERSION}')
        self.header.mouseMoveEvent = self.MoveWindow
        self.close_btn.clicked.connect(lambda: app.exit())
        self.minimize_btn.clicked.connect(self.hideWindow)

        self.result_field = self.findChild(qtw.QLineEdit, "result_field")

        self.face = self.findChild(qtw.QLabel, "face")

        # Define Buttons
        self.btn_result = self.findChild(qtw.QPushButton,'EQUAL')
        self.btn_clear_all = self.findChild(qtw.QPushButton,'AC')
        self.btn_del_num = self.findChild(qtw.QPushButton,'DEL')
        self.btn_reset = self.findChild(qtw.QPushButton,'C')
        self.btn_answer = self.findChild(qtw.QPushButton,'ANS')
        self.btn_pow = self.findChild(qtw.QPushButton,'POW')
        self.btn_percentage = self.findChild(qtw.QPushButton,'PERCENTAGE') # implement
        self.btn_sqrt = self.findChild(qtw.QPushButton,'SQRT')
        self.btn_times =self.findChild(qtw.QPushButton,'TIMES')
        self.btn_divide = self.findChild(qtw.QPushButton,'DIV')
        self.btn_plus = self.findChild(qtw.QPushButton,'PLUS')
        self.btn_minus = self.findChild(qtw.QPushButton,'MINUS')
        self.btn_decimal_point = self.findChild(qtw.QPushButton,'DECIMAL')
        self.btn_switch_signal = self.findChild(qtw.QPushButton,'SIGNAL')
        self.btn_9 = self.findChild(qtw.QPushButton,'N9')
        self.btn_8 = self.findChild(qtw.QPushButton,'N8')
        self.btn_7 = self.findChild(qtw.QPushButton,'N7')
        self.btn_6 = self.findChild(qtw.QPushButton,'N6')
        self.btn_5 = self.findChild(qtw.QPushButton,'N5')
        self.btn_4 = self.findChild(qtw.QPushButton,'N4')
        self.btn_3 = self.findChild(qtw.QPushButton,'N3')
        self.btn_2 = self.findChild(qtw.QPushButton,'N2')
        self.btn_1 = self.findChild(qtw.QPushButton,'N1')
        self.btn_0 = self.findChild(qtw.QPushButton,'N0')

        # Add functionality to the buttons
        self.btn_result.clicked.connect(self.func_result)
        self.btn_clear_all.clicked.connect(self.clear_calc)
        self.btn_del_num.clicked.connect(self.del_digit)
        self.btn_reset.clicked.connect(self.reset_nums)
        self.btn_answer.clicked.connect(self.answer)
        self.btn_pow.clicked.connect(self.power)
        self.btn_percentage.clicked.connect(self.percentage)
        self.btn_sqrt.clicked.connect(self.sqrt)
        self.btn_times.clicked.connect(self.times)
        self.btn_divide.clicked.connect(self.divide)
        self.btn_plus.clicked.connect(self.plus)
        self.btn_minus.clicked.connect(self.minus)
        self.btn_decimal_point.clicked.connect(self.point_press)
        self.btn_switch_signal.clicked.connect(self.switch_signal)
        self.btn_0.clicked.connect(self.num_press_0)
        self.btn_1.clicked.connect(self.num_press_1)
        self.btn_2.clicked.connect(self.num_press_2)
        self.btn_3.clicked.connect(self.num_press_3)
        self.btn_4.clicked.connect(self.num_press_4)
        self.btn_5.clicked.connect(self.num_press_5)
        self.btn_6.clicked.connect(self.num_press_6)
        self.btn_7.clicked.connect(self.num_press_7)
        self.btn_8.clicked.connect(self.num_press_8)
        self.btn_9.clicked.connect(self.num_press_9)

        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowFlags(flags)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.central_widgets.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=35, xOffset=0, yOffset=0))

        self.is_Line_empty()

        self.show()


    # Window Bar
    def MoveWindow(self, event):
        if self.isMaximized() == False:
            self.move(self.pos() + event.globalPos() - self.clickPosition)
            self.clickPosition = event.globalPos()
            event.accept()
            pass

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
        pass

    def hideWindow(self):
        self.showMinimized()


    # Face Assets
    def default_face(self):
        self.face.setText("• ◡ •")
        self.face.setStyleSheet(FACE_DEFAULT_STYLE_SHEET)

    def face_del(self):
        self.face.setText("\_(´• ⌓ •`)_/")
        self.face.setStyleSheet(FACE_BORDER_INFO + "color : #06908F; background-color : #D7F2BA")

    def face_result(self):
        self.face.setText("˶• ◡ •˶")
        self.face.setStyleSheet(FACE_BORDER_INFO + "color : #F2F5EA; background-color : #F44174")

    def face_num(self):
        self.face.setText("• ◡ •")
        self.face.setStyleSheet(FACE_DEFAULT_STYLE_SHEET)

    def face_op(self, op:str):
        self.face.setText(op + "⸜(• ◡ •)⸝" + op)
        self.face.setStyleSheet(FACE_BORDER_INFO + "color : #F2F5EA; background-color : #3A7CA5")

    def face_error(self):
        self.face.setText("¯\_(•`_ •´)_/¯")
        self.face.setStyleSheet(FACE_BORDER_INFO + "color : #FFFFFF; background-color : #FF1B1C")

    def field_default(self):
        self.result_field.setText('•  ◡  •')
        self.face.setText('')
        self.face.setStyleSheet("background-color: rgb(164, 234, 186);")
        self.result_field.setStyleSheet(RESULT_FIELD_DEFAULT)

    def field_error(self):
        self.result_field.setText('¯\_(•`_ •´)_/¯')
        self.result_field.setStyleSheet("background-color: #FF1B1C; border-bottom : 3px solid rgba(0, 0, 0, 0); border-bottom-color : rgb(102, 1, 14); padding-bottom : 7px; color : #FFFFFF;")
        self.face.setText('')
        self.face.setStyleSheet("background-color: #FF1B1C;")

    # Calculator Operations
    def num_press(self, key: str) -> None:
        self.result_field.setStyleSheet(RESULT_FIELD_DEFAULT)

        if not self.temp_nums and key == '.':
            self.temp_nums.append('0')
            self.temp_nums.append('.')
            self.result_field.setText(''.join(self.temp_nums))

        else:
            self.temp_nums.append(key)
            if len(self.temp_nums) > 1 and self.temp_nums[0] == '0' and self.temp_nums[1] != '.':
                self.temp_nums.remove('0')

            temp_string = ''.join(self.temp_nums)
            if self.fin_nums:
                self.result_field.setText(''.join(self.fin_nums) + temp_string)
            else:
                self.result_field.setText(temp_string)

    def num_press_0(self):
        self.num_press('0')
        self.face_num()

    def num_press_1(self):
        self.num_press('1')
        self.face_num()

    def num_press_2(self):
        self.num_press('2')
        self.face_num()
    
    def num_press_3(self):
        self.num_press('3')
        self.face_num()
    
    def num_press_4(self):
        self.num_press('4')
        self.face_num()

    def num_press_5(self):
        self.num_press('5')
        self.face_num()

    def num_press_6(self):
        self.num_press('6')
        self.face_num()

    def num_press_7(self):
        self.num_press('7')
        self.face_num()

    def num_press_8(self):
        self.num_press('8')
        self.face_num()

    def num_press_9(self):
        self.num_press('9')
        self.face_num()

    def point_press(self):
        self.num_press('.')
        self.face_num()

    def switch_signal(self):
        self.result_field.setStyleSheet(RESULT_FIELD_DEFAULT)

        if self.temp_nums:
            if self.temp_nums[0] == '-':
                self.temp_nums.remove('-')
            else:
                self.temp_nums.insert(0, '-')    
            self.result_field.setText(''.join(self.temp_nums))

        elif self.ANS == self.result_field.text():
            temp = [digit for digit in self.ANS]
            if temp[0] == '-':
                self.ANS = self.ANS[1:]
                self.temp_nums = temp[1:]
            else:
                temp.insert(0, '-')
                self.ANS = ''.join(temp)
                self.temp_nums = temp
            self.result_field.setText(self.ANS)

    def func_press(self, operator: str):
        self.result_field.setStyleSheet(RESULT_FIELD_DEFAULT)

        temp_string = ''.join(self.temp_nums)
        self.fin_nums.append(temp_string)
        self.fin_nums.append(operator)
        self.temp_nums = []
        self.result_field.setText(''.join(self.fin_nums))

    def error_operator(self, op):
        text = self.result_field.text()
        if text == '*' or text == '/':
            self.fin_nums.remove(op)
            self.face_error()

        else:
            self.face_op(op)

    def times(self):
        self.func_press('*')
        self.error_operator('*')

    def divide(self):
        self.func_press('/')
        self.error_operator('/')

    def plus(self):
        self.func_press('+')
        self.face_op('+')
    
    def minus(self):
        self.func_press('-')
        self.face_op('-')

    def power(self):
        self.result_field.setStyleSheet(RESULT_FIELD_DEFAULT)

        if self.temp_nums:
            if '.' in self.temp_nums:
                pow = float(''.join(self.temp_nums)) * float(''.join(self.temp_nums))
            else:
                pow = int(''.join(self.temp_nums)) * int(''.join(self.temp_nums))

            string = str(pow)
            if isinstance(pow, float):
                    if str(pow)[-2:] == '.0':
                        string = str(pow)[0:-2]

            self.ANS = string
            self.result_field.setText(self.ANS)
            self.temp_nums = [x for x in self.ANS]
            self.fin_nums = []
            self.face_result()

        elif self.ANS:
            if '.' in self.temp_nums:
                pow = float(self.ANS) * float(self.ANS)
            else:
                pow = int(self.ANS) * int(self.ANS)

            string = str(pow)
            if isinstance(pow, float):
                    if str(pow)[-2:] == '.0':
                        string = str(pow)[0:-2]

            self.ANS = string
            self.result_field.setText(self.ANS)
            self.temp_nums = [x for x in self.ANS]
            self.fin_nums = []
            self.face_result()

        else:
            self.result_field.setText("┐(•᷅ _ •᷅ )┌")
            self.face.setText('')
            self.face.setStyleSheet("background-color: rgb(164, 234, 186);")

    def sqrt(self):
        self.result_field.setStyleSheet(RESULT_FIELD_DEFAULT)

        if self.temp_nums:
            if '-' in self.fin_nums:
                self.result_field.setText("Invalid Input")
                self.face_error()
                self.fin_nums = []
                self.temp_nums = []
            
            else:
                if '.' in self.temp_nums:
                    num = float(''.join(self.temp_nums))
                else:
                    num = int(''.join(self.temp_nums))

                res = sqrt(num)
                string = f"{res:.8f}"

                if isinstance(res, float):
                    if str(res)[-2:] == '.0':
                        string = str(res)[:-2]

                self.ANS = string
                self.result_field.setText(self.ANS)
                self.temp_nums = [digit for digit in self.ANS]
                self.fin_nums = []

        elif self.ANS:
            if '-' in self.ANS:
                self.result_field.setText("Invalid Input")
                self.face_error()
                self.fin_nums = []
                self.temp_nums = []
            
            else:
                if '.' in self.ANS:
                    num = float(self.ANS)
                else:
                    num = int(self.ANS)

                res = sqrt(num)
                string = f"{res:.8f}"

                if isinstance(res, float):
                    if str(res)[-2:] == '.0':
                        string = str(res)[:-2]

                self.ANS = string
                self.result_field.setText(self.ANS)
                self.temp_nums = [digit for digit in self.ANS]
                self.fin_nums = []

        else:
            self.result_field.setText("┐(•᷅ _ •᷅ )┌")
            self.face.setText('')
            self.face.setStyleSheet("background-color: rgb(164, 234, 186);")

    def percentage(self):
        self.result_field.setStyleSheet(RESULT_FIELD_DEFAULT)
        
        if self.temp_nums:
            if '.' in self.temp_nums:
                num = float(''.join(self.temp_nums))
            else:
                num = int(''.join(self.temp_nums))

            res = num / 100
            string = f'{res}'
            self.ANS = string
            self.result_field.setText(self.ANS)
            self.temp_nums = [digit for digit in self.ANS]
            self.fin_nums = []

        elif self.ANS:
            if '.' in self.ANS:
                num = float(self.ANS)
            else:
                num = int(self.ANS)

            res = num / 100
            string = f'{res}'
            self.ANS = string
            self.result_field.setText(self.ANS)
            self.temp_nums = [digit for digit in self.ANS]
            self.fin_nums = []

        else:
            self.result_field.setText("┐(•᷅ _ •᷅ )┌")
            self.face.setText('')
            self.face.setStyleSheet("background-color: rgb(164, 234, 186);")

    def func_result(self):
        if self.fin_nums and self.temp_nums:
            self.result_field.setStyleSheet(RESULT_FIELD_DEFAULT)

            self.face_result()

            if self.temp_nums:
                fin_string = ''.join(self.fin_nums) + ''.join(self.temp_nums)
            else:    
                fin_string = ''.join(self.fin_nums) + self.fin_nums[0]

            if fin_string:
                result_string = eval(fin_string)
                string = str(result_string)
                if isinstance(result_string, float):
                    if str(result_string)[-2:] == '.0':
                        string = str(result_string)[0:-2]

                self.ANS = string

            self.result_field.setText(self.ANS)
            self.temp_nums = []
            self.fin_nums = []
        
        else:
            self.field_error()

    
    """
    def calculate(self, exp:str) -> int:
        if '+-' not in exp and '-+' not in exp:
            if '-' in exp:
                index = exp.index('-')
                if exp[index + 1] == '-':
                    exp = exp[:index+1] + exp[index + 2:]
                result = int(exp[:index]) - int(exp[index + 1:])

            elif '+' in exp:
                index = exp.index('+')
                if exp[index + 1] == '+':
                    exp = exp[:index+1] + exp[index + 2:]
                result = int(exp[:index]) + int(exp[index + 1:])
            
            elif '/' in exp:
                index = exp.index('/')
                result = int(exp[:index]) / int(exp[index + 1:])

            elif '*' in exp:
                index = exp.index('*')
                result = int(exp[:index]) * int(exp[index + 1:])

        # Special cases
        if '-+' in exp:
            index = exp.index('-')
            result = int(exp[:index]) - int(exp[index + 2:])

        elif '+-' in exp:
            index = exp.index('+')
            result = int(exp[:index]) + (-1 * (int(exp[index + 2:])))
            
        return result
    """


    # Result Field Matters
    def is_Line_empty(self):
        text = self.result_field.text()
        if text == '':
            self.field_default()

    def clear_calc(self):
        self.result_field.setStyleSheet(RESULT_FIELD_DEFAULT)
        self.result_field.clear()
        self.temp_nums = []
        self.fin_nums = []
        self.ANS = ''
        self.is_Line_empty()

    def reset_nums(self):
        self.result_field.setStyleSheet(RESULT_FIELD_DEFAULT)
        self.result_field.clear()
        self.temp_nums = []
        self.fin_nums = []
        self.is_Line_empty()

    def del_digit(self):
        self.result_field.setStyleSheet(RESULT_FIELD_DEFAULT)

        self.result_field.backspace()

        if self.ANS[:-1] == self.result_field.text():
            self.result_field.setText('0')
            self.fin_nums = []
            self.temp_nums = ['0']
            self.face_num()

        elif ''.join(self.fin_nums)[:-1] == self.result_field.text():
            if len(self.fin_nums) > 1:
                temp = [digit for digit in self.fin_nums]
                temp.pop()
                self.fin_nums = temp
                
            elif len(self.fin_nums) == 1:
                temp = [digit for digit in self.fin_nums[0]]
                temp.pop()
                self.fin_nums = [''.join(temp)]

            self.face_del()

        elif not self.temp_nums or not self.fin_nums:
            self.temp_nums = ['0']
            self.result_field.setText('0')
            self.default_face()

        else:
            self.temp_nums.pop()
            self.face_del()
        
        self.is_Line_empty()
        
    def answer(self):
        self.temp_nums = [x for x in self.ANS]
        self.result_field.setText(''.join(self.fin_nums) + self.ANS)
        self.default_face()


if __name__==  "__main__":
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())
