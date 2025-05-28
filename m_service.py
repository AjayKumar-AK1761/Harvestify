import subprocess
import os

env_name = "chatbot"
python_version = "3.10"
script_path = os.path.join("chatbot_server", "app.py")
requirements_path = os.path.join("chatbot_server", "requirements.txt")

def env_exists(name):
    """Check if a conda environment already exists."""
    result = subprocess.run("conda env list", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    return any(line.split()[0] == name for line in result.stdout.splitlines() if line and not line.startswith("#"))


def create_env():
    """Create a new conda environment if it doesn't exist."""
    print(f"Creating Conda environment '{env_name}' (if it doesn't exist)...")
    subprocess.run(f"conda create -n {env_name} python={python_version} -y", shell=True, check=True)
    print(f"✅ Environment '{env_name}' created.")

def install_packages():
    """Install packages from requirements.txt."""
    if os.path.exists(requirements_path):
        print(f"Installing dependencies from {requirements_path} into '{env_name}'...")
        subprocess.run(f"conda run -n {env_name} pip install -r {requirements_path}", shell=True, check=True)
    else:
        print(f"❌ requirements.txt not found at {requirements_path}")

def run_microservice():
    print(f"Running microservice in environment '{env_name}'...")
    subprocess.Popen(
        f"conda run -n {env_name} python {script_path}",
        shell=True
    )
    print("✅ Microservice launched.")



def launch():
    """Programmatic entry point to launch the microservice."""
    print("Launching microservice...")
    if not env_exists(env_name):
        create_env()
        install_packages()
    else:
        print(f"✅ Environment '{env_name}' already exists.")
    run_microservice()

