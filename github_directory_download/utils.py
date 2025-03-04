import os
import platform
import re

def extract_repo_info(url):
    """
    Extracts repository owner, name, branch, and directory path from a GitHub URL.

    :param url: GitHub directory URL
    :return: Tuple (owner, repo, branch, directory)
    """
    match = re.match(r"https://github\.com/([^/]+)/([^/]+)/tree/([^/]+)/(.*)", url)
    if not match:
        raise ValueError("Invalid GitHub directory URL format.")

    owner, repo, branch, directory = match.groups()
    return owner, repo, branch, directory

def get_default_download_path():
    """
    Returns the user's default Downloads folder based on the operating system.

    :return: Path to Downloads folder
    """
    home = os.path.expanduser("~")

    if platform.system() == "Windows":
        return os.path.join(home, "Downloads")
    elif platform.system() == "Darwin":  # macOS
        return os.path.join(home, "Downloads")
    else:  # Linux
        return os.path.join(home, "Downloads")
