import PyQt5.QtWidgets as qtw
from PyQt5 import uic, QtCore, QtWidgets

CALCULATOR_VERSION = "v1.6"


class MainWindow(qtw.QMainWindow, qtw.QWidget):
    def __init__(self) -> None:
        super().__init__()

        uic.loadUi('basic_calculator.ui', self)
        
        self.setWindowTitle(f'Calculadora - {CALCULATOR_VERSION}')

        # Logic of the calculator
        self.temp_nums = []
        self.fin_nums = []
        self.ANS = ''

        self.central_widgets = self.findChild(qtw.QWidget, "centralwidget")

        self.header = self.findChild(qtw.QFrame, "header_frame")
        self.btn_frame = self.findChild(qtw.QFrame, "frame")
        self.close_btn = self.findChild(qtw.QPushButton, "close_window_button")
        self.minimize_btn = self.findChild(qtw.QPushButton, "minimize_window_button")
        self.label = self.findChild(qtw.QLabel, "Name")

        self.label.setText(f'Calculadora - {CALCULATOR_VERSION}')

        self.result_field = self.findChild(qtw.QLineEdit, "result_field")

        # Define Buttons
        self.btn_result = self.findChild(qtw.QPushButton,'EQUAL')
        self.btn_clear_all = self.findChild(qtw.QPushButton,'AC')
        self.btn_del_num = self.findChild(qtw.QPushButton,'DEL')
        self.btn_reset = self.findChild(qtw.QPushButton,'C')
        self.btn_answer = self.findChild(qtw.QPushButton,'ANS')
        self.btn_pow = self.findChild(qtw.QPushButton,'POW')
        self.btn_percentage = self.findChild(qtw.QPushButton,'PERCENTAGE') # implement
        self.btn_sqrt = self.findChild(qtw.QPushButton,'SQRT') #implement
        self.btn_times =self.findChild(qtw.QPushButton,'TIMES')
        self.btn_divide = self.findChild(qtw.QPushButton,'DIV')
        self.btn_plus = self.findChild(qtw.QPushButton,'PLUS')
        self.btn_minus = self.findChild(qtw.QPushButton,'MINUS')
        self.btn_decimal_point = self.findChild(qtw.QPushButton,'DECIMAL') # implement
        self.btn_switch_signal = self.findChild(qtw.QPushButton,'SIGNAL') #implement
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
        # self.btn_percentage
        # self.btn_sqrt
        self.btn_times.clicked.connect(self.times)
        self.btn_divide.clicked.connect(self.divide)
        self.btn_plus.clicked.connect(self.plus)
        self.btn_minus.clicked.connect(self.minus)
        # self.btn_decimal_point
        # self.btn_switch_signal
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

        self.show()

    def num_press(self, key_number: str) -> None:
        self.temp_nums.append(key_number)
        if len(self.temp_nums) > 1 and self.temp_nums[0] == '0' and self.temp_nums[1] != '.':
            self.temp_nums.remove('0')

        temp_string = ''.join(self.temp_nums)
        if self.fin_nums:
            self.result_field.setText(''.join(self.fin_nums) + temp_string)
        else:
            self.result_field.setText(temp_string)

    def num_press_0(self):
        self.num_press('0')

    def num_press_1(self):
        self.num_press('1')

    def num_press_2(self):
        self.num_press('2')
    
    def num_press_3(self):
        self.num_press('3')
    
    def num_press_4(self):
        self.num_press('4')

    def num_press_5(self):
        self.num_press('5')

    def num_press_6(self):
        self.num_press('6')

    def num_press_7(self):
        self.num_press('7')

    def num_press_8(self):
        self.num_press('8')

    def num_press_9(self):
        self.num_press('9')

    def func_press(self, operator):
        temp_string = ''.join(self.temp_nums)
        self.fin_nums.append(temp_string)
        self.fin_nums.append(operator)
        self.temp_nums = []
        self.result_field.setText(''.join(self.fin_nums))

    def times(self):
        self.func_press('*')

    def divide(self):
        self.func_press('/')

    def plus(self):
        self.func_press('+')
    
    def minus(self):
        self.func_press('-')

    def func_result(self):
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
        self.temp_nums = [self.ANS]
        self.fin_nums = []

    def clear_calc(self):
        self.result_field.clear()
        self.temp_nums = []
        self.fin_nums = []
        self.ANS = ''

    # Fix issue for floats
    def del_digit(self):
        self.result_field.backspace()
        if self.ANS == self.temp_nums[0]:
            temp = [digit for digit in self.temp_nums[0]]
            temp.pop()
            self.temp_nums = [''.join(temp)]
        else:
            self.temp_nums.pop()
        

    def power(self):
        pow = ''.join(self.temp_nums) + '*' + ''.join(self.temp_nums)
        result_string = eval(pow)
        self.ANS = str(result_string)
        self.result_field.setText(self.ANS)
        self.temp_nums = self.ANS
        self.fin_nums = []

    def answer(self):
        self.temp_nums = [self.ANS]
        self.result_field.setText(''.join(self.fin_nums) + self.ANS)

    def reset_nums(self):
        self.result_field.clear()
        self.temp_nums = []
        self.fin_nums = []


app = qtw.QApplication([])
mw = MainWindow()
app.setStyle(qtw.QStyleFactory.create('Fusion'))
app.exec_()
