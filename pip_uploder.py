import os 

commands = [
    'python3 increment.py',
    'move dist\*.whl History',
    'move dist\*.gz History',
    'python3 -m build',
    'python3 -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*'
    'pip install -U aziizam'
]

for i in range(len(commands)):
    # print(commands[i])
    os.system(commands[i])
