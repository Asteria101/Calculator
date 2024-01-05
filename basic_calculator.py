import PyQt5.QtWidgets as qtw
from PyQt5 import uic
import sys

CALCULATOR_VERSION = "v1.5"


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
            self.ANS = str(result_string)

        self.result_field.setText(self.ANS)
        self.temp_nums = [self.ANS]
        self.fin_nums = []

    def clear_calc(self):
        self.result_field.clear()
        self.temp_nums = []
        self.fin_nums = []
        self.ANS = ''

    # Fix issue
    def del_digit(self):
        self.result_field.backspace()
        self.temp_nums = []

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



"""
def keypad(self):
    container = qtw.QWidget()
    container.setLayout(qtw.QGridLayout())

    # Create buttons
    self.result_field = qtw.QLineEdit()
    btn_result = qtw.QPushButton('=', clicked = self.func_result)
    btn_clear_all = qtw.QPushButton('AC', clicked = self.clear_calc)
    btn_del_num = qtw.QPushButton('DEL', clicked = self.del_digit)
    btn_reset = qtw.QPushButton('C', clicked = self.reset_nums)
    btn_answer = qtw.QPushButton('ANS', clicked = self.answer)
    btn_pow = qtw.QPushButton('POW', clicked = self.power)

    btn_percentage = qtw.QPushButton('%', clicked = lambda:self.percentage('%')) # implement
    btn_sqrt = qtw.QPushButton('SQRT') #implement
    
    btn_times = qtw.QPushButton('*', clicked = lambda:self.func_press('*'))
    btn_minus = qtw.QPushButton('-', clicked = lambda:self.func_press('-'))
    btn_plus = qtw.QPushButton('+', clicked = lambda:self.func_press('+'))
    btn_divide = qtw.QPushButton('/', clicked = lambda:self.func_press('/'))

    btn_decimal_point = qtw.QPushButton('.') # insert clicked method
    btn_switch_signal = qtw.QPushButton('+/-') # insert clicked method

    btn_9 = qtw.QPushButton('9', clicked = lambda:self.num_press('9'))
    btn_8 = qtw.QPushButton('8', clicked = lambda:self.num_press('8'))
    btn_7 = qtw.QPushButton('7', clicked = lambda:self.num_press('7'))
    btn_6 = qtw.QPushButton('6', clicked = lambda:self.num_press('6'))
    btn_5 = qtw.QPushButton('5', clicked = lambda:self.num_press('5'))
    btn_4 = qtw.QPushButton('4', clicked = lambda:self.num_press('4'))
    btn_3 = qtw.QPushButton('3', clicked = lambda:self.num_press('3'))
    btn_2 = qtw.QPushButton('2', clicked = lambda:self.num_press('2'))
    btn_1 = qtw.QPushButton('1', clicked = lambda:self.num_press('1'))
    btn_0 = qtw.QPushButton('0', clicked = lambda:self.num_press('0'))

    # Adds to the layout
    container.layout().addWidget(self.result_field, 0, 0, 1, 4)
    container.layout().addWidget(btn_answer, 1, 0, 1, 1)
    container.layout().addWidget(btn_clear_all, 1, 1, 1, 1)
    container.layout().addWidget(btn_reset, 1, 2, 1, 1)
    container.layout().addWidget(btn_del_num, 1, 3, 1, 1)

    container.layout().addWidget(btn_pow, 2, 0)
    container.layout().addWidget(btn_percentage, 2, 1)
    container.layout().addWidget(btn_sqrt, 2, 2)
    container.layout().addWidget(btn_plus, 2, 3)

    container.layout().addWidget(btn_9, 3, 0)
    container.layout().addWidget(btn_8, 3, 1)
    container.layout().addWidget(btn_7, 3, 2)
    container.layout().addWidget(btn_minus, 3, 3)
    container.layout().addWidget(btn_6, 4, 0)
    container.layout().addWidget(btn_5, 4, 1)
    container.layout().addWidget(btn_4, 4, 2)
    container.layout().addWidget(btn_times, 4, 3)
    container.layout().addWidget(btn_3, 5, 0)
    container.layout().addWidget(btn_2, 5, 1)
    container.layout().addWidget(btn_1, 5, 2)
    container.layout().addWidget(btn_divide, 5, 3)
    container.layout().addWidget(btn_switch_signal, 6, 0, 1, 1)
    container.layout().addWidget(btn_0, 6, 1, 1, 1)
    container.layout().addWidget(btn_decimal_point, 6, 2, 1, 1)
    container.layout().addWidget(btn_result, 6, 3)

    self.layout().addWidget(container)
"""