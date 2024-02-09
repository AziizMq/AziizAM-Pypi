import os 

from dotenv import load_dotenv
load_dotenv()

Username_ID = os.getenv('Username_ID')
Password = os.getenv('Password')

commands = [
    'python3 increment.py',
    'move dist\*.whl History',
    'move dist\*.gz History',
    'python3 -m build'
]

commands.append(f'python3 -m twine upload -u {Username_ID} -p {Password} --repository-url https://upload.pypi.org/legacy/ dist/*')
commands.append('pip install -U aziizam')

for i in range(len(commands)):
    # print(commands[i])
    os.system(commands[i])
