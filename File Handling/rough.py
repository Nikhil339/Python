import os 

source_path = os.path.join(os.getcwd(), 'prime.py')
os.chdir("Practice_Programs")
destination_path = os.path.join(os.getcwd(), 'prime.py')

os.rename(source_path, destination_path)