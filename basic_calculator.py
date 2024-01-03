import PyQt5.QtWidgets as qtw

CALCULATOR_VERSION = "0.0.1"

OPERATORS = ['+', '-', '*', '/']

class MainWindow(qtw.QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle(f'Calculadora - {CALCULATOR_VERSION}')

        self.setLayout(qtw.QVBoxLayout())
        self.keypad()

        self.temp_nums = []
        self.fin_nums = []
        self.ANS = ''

        self.show()

    def keypad(self):
        container = qtw.QWidget()
        container.setLayout(qtw.QGridLayout())

        # Create buttons
        self.result_field = qtw.QLineEdit()
        btn_result = qtw.QPushButton('=', clicked = self.func_result)
        btn_clear_all = qtw.QPushButton('AC', clicked = self.clear_calc)
        btn_del_num = qtw.QPushButton('DEL', clicked = self.del_digit)
        btn_times = qtw.QPushButton('*', clicked = lambda:self.func_press('*'))
        btn_minus = qtw.QPushButton('-', clicked = lambda:self.func_press('-'))
        btn_plus = qtw.QPushButton('+', clicked = lambda:self.func_press('+'))
        btn_divide = qtw.QPushButton('/', clicked = lambda:self.func_press('/'))
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
        container.layout().addWidget(btn_result, 1, 1, 1, 1)
        container.layout().addWidget(btn_clear_all, 1, 2, 1, 1)
        container.layout().addWidget(btn_del_num, 1, 3, 1, 1)
        container.layout().addWidget(btn_9, 2, 0)
        container.layout().addWidget(btn_8, 2, 1)
        container.layout().addWidget(btn_7, 2, 2)
        container.layout().addWidget(btn_plus, 2, 3)
        container.layout().addWidget(btn_6, 3, 0)
        container.layout().addWidget(btn_5, 3, 1)
        container.layout().addWidget(btn_4, 3, 2)
        container.layout().addWidget(btn_minus, 3, 3)
        container.layout().addWidget(btn_3, 4, 0)
        container.layout().addWidget(btn_2, 4, 1)
        container.layout().addWidget(btn_1, 4, 2)
        container.layout().addWidget(btn_times, 4, 3)
        container.layout().addWidget(btn_0, 5, 0, 1, 3)
        container.layout().addWidget(btn_divide, 5, 3)

        self.layout().addWidget(container)

    def num_press(self, key_number):
        self.temp_nums.append(key_number)
        temp_string = ''.join(self.temp_nums)
        if self.fin_nums:
            self.result_field.setText(''.join(self.fin_nums) + temp_string)
        else:
            self.result_field.setText(temp_string)

    def func_press(self, operator):
        temp_string = ''.join(self.temp_nums)
        self.fin_nums.append(temp_string)
        self.fin_nums.append(operator)
        self.temp_nums = []
        self.result_field.setText(''.join(self.fin_nums))

    def func_result(self):
        if self.temp_nums:
            fin_string = ''.join(self.fin_nums) + ''.join(self.temp_nums)
        else:    
            fin_string = ''.join(self.fin_nums) + self.fin_nums[0]

        if fin_string:
            result_string = eval(fin_string)
            self.ANS = str(result_string)

        self.result_field.setText(self.ANS)
        self.temp_nums = self.ANS
        self.fin_nums = []

    def clear_calc(self):
        self.result_field.clear()
        self.temp_nums = []
        self.fin_nums = []

    def del_digit(self):
        self.result_field.backspace()
        self.temp_nums = []

        


app = qtw.QApplication([])
mw = MainWindow()
app.setStyle(qtw.QStyleFactory.create('Fusion'))
app.exec_()