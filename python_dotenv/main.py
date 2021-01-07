import os
from dotenv import load_dotenv

load = load_dotenv(dotenv_path='./envs/python_tips.env')

STRING = os.getenv('STRING')
INTEGER = int(os.getenv('INTEGER'))
FLOAT = float(os.getenv('FLOAT'))
BOOLEAN = os.getenv('BOOLEAN') == 'True'

print(STRING, type(STRING))
print(INTEGER, type(INTEGER))
print(FLOAT, type(FLOAT))
print(BOOLEAN, type(BOOLEAN))