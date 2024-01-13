from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': [], 'excludes': [], 'include_files' : ['basic_calculator.ui', 'cross.svg', 'minus.svg']}

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('basic_calculator.py', base=base, target_name = 'calculadora')
]

setup(name='Calculadora',
      version = '2.1',
      description = 'Basic_calculator',
      options = {'build_exe': build_options},
      executables = executables)
