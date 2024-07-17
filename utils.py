import os
import shutil
import subprocess

def get_python_environments():
    environments = []

    # Global Python installations
    for path in ["/usr/bin/python3", "/bin/python3"]:
        if os.path.exists(path):
            version = get_python_version(path)
            environments.append({
                'name': f"Python {version} (Global) - {path}",
                'path': path
            })

    # pyenv installations
    pyenv_root = os.path.expanduser("~/.pyenv/versions")
    if os.path.exists(pyenv_root):
        for version in os.listdir(pyenv_root):
            path = os.path.join(pyenv_root, version, "bin", "python")
            if os.path.exists(path):
                environments.append({
                    'name': f"Python {version} (pyenv) - {path}",
                    'path': path
                })

    # Virtual environments
    venv_dirs = [os.path.expanduser("~/.virtualenvs"), os.path.expanduser("~/.local/share/virtualenvs")]
    for venv_dir in venv_dirs:
        if os.path.exists(venv_dir):
            for venv in os.listdir(venv_dir):
                path = os.path.join(venv_dir, venv, "bin", "python")
                if os.path.exists(path):
                    version = get_python_version(path)
                    environments.append({
                        'name': f"Python {version} ({venv}) - {path}",
                        'path': path
                    })

    return environments

def get_python_version(path):
    try:
        output = subprocess.check_output([path, "--version"]).decode().strip()
        return output.split()[1]
    except:
        return "Unknown"

def get_environment_info(path):
    info = f"Path: {path}\n"
    info += f"Version: {get_python_version(path)}\n"
    
    # Get environment size
    env_dir = os.path.dirname(os.path.dirname(path))
    try:
        size = get_dir_size(env_dir)
        info += f"Size: {size:.2f} MB\n"
    except Exception as e:
        info += f"Size: Unable to calculate\n"

    return info

def get_dir_size(path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size / (1024 * 1024)  # Convert to MB

def create_environment(version, name):
    try:
        subprocess.run(["pyenv", "install", "-s", version], check=True)
        venv_path = os.path.expanduser(f"~/.virtualenvs/{name}")
        subprocess.run(["pyenv", "virtualenv", version, name], check=True)
        return {'success': True, 'message': f"Virtual environment '{name}' created with Python {version}"}
    except subprocess.CalledProcessError as e:
        return {'success': False, 'message': f"Failed to create environment: {str(e)}"}

def delete_environment(path):
    try:
        env_dir = os.path.dirname(os.path.dirname(path))
        shutil.rmtree(env_dir)
        return {'success': True, 'message': "Environment deleted successfully"}
    except Exception as e:
        return {'success': False, 'message': f"Failed to delete environment: {str(e)}"}

def get_package_list(python_path):
    try:
        output = subprocess.check_output([python_path, "-m", "pip", "list", "--format=freeze"]).decode()
        return output.splitlines()
    except subprocess.CalledProcessError:
        return ["Unable to retrieve package list"]

def delete_packages(python_path, packages):
    try:
        for package in packages:
            subprocess.run([python_path, "-m", "pip", "uninstall", "-y", package], check=True)
        return {'success': True, 'message': "Selected packages deleted successfully"}
    except subprocess.CalledProcessError as e:
        return {'success': False, 'message': f"Failed to delete packages: {str(e)}"}