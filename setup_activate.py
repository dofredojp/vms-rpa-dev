import os
import subprocess

venv_path = os.path.join("venv", "Scripts", "activate.bat")
subprocess.call(f'cmd.exe /k {venv_path}', shell=True)
