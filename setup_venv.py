import subprocess
import os
import sys

def run_command(command):
    """Helper function to run a command in the shell"""
    print(f"Running command: {command}")
    subprocess.check_call(command, shell=True)

def create_virtualenv():
    """Create a virtual environment"""
    print("Creating virtual environment...")
    run_command("python -m venv venv")

def install_requirements():
    """Install dependencies from requirements.txt"""
    print("Installing dependencies from requirements.txt...")
    if not os.path.exists("requirements.txt"):
        print("requirements.txt file not found!")
        return
    run_command("venv\\Scripts\\pip install -r requirements.txt" if sys.platform == "win32" else "venv/bin/pip install -r requirements.txt")

def main():
    """Main function to orchestrate the setup steps"""
    try:
        # 1. Create virtual environment
        create_virtualenv()

        # 2. Install dependencies from requirements.txt
        install_requirements()

    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
