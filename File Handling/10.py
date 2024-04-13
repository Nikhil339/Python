import os

source_path = os.path.join(os.getcwd(), '9.py')

os.chdir('File Handling')
desination_path = os.path.join(os.getcwd(), '9.py')

os.rename(source_path, desination_path)