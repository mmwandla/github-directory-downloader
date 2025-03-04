import os
import requests
import zipfile
import shutil
from tqdm import tqdm
from github_directory_download.utils import extract_repo_info

GITHUB_API_BASE = "https://api.github.com/repos"


def download_github_directory(url, save_path):
    """
    Downloads a directory from a GitHub repository and saves it as a ZIP file.

    :param url: GitHub directory URL
    :param save_path: Path to save the ZIP file
    :return: Path to the saved ZIP file
    """
    owner, repo, branch, directory = extract_repo_info(url)

    # GitHub API URL to fetch repository contents
    api_url = f"{GITHUB_API_BASE}/{owner}/{repo}/contents/{directory}?ref={branch}"
    response = requests.get(api_url, headers={"Accept": "application/vnd.github.v3+json"})

    if response.status_code != 200:
        raise ValueError("Failed to fetch directory. Check if the URL is correct.")

    files = response.json()
    temp_dir = os.path.join(save_path, f"{repo}-{directory}")

    os.makedirs(temp_dir, exist_ok=True)

    # Download files
    for file in tqdm(files, desc="Downloading files", unit="file"):
        if file["type"] == "file":
            download_file(file["download_url"], os.path.join(temp_dir, file["name"]))

    # Create ZIP archive
    zip_file_path = shutil.make_archive(temp_dir, 'zip', temp_dir)

    # Cleanup temporary directory
    shutil.rmtree(temp_dir)

    return zip_file_path


def download_file(url, file_path):
    """
    Downloads a file from a given URL.

    :param url: File URL
    :param file_path: Destination path
    """
    response = requests.get(url, stream=True)
    response.raise_for_status()

    with open(file_path, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
