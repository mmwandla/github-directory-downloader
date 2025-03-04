import argparse
import sys
from github_directory_download.downloader import download_github_directory
from github_directory_download.utils import get_default_download_path


def main():
    parser = argparse.ArgumentParser(description="Download a GitHub repository directory as a ZIP file.")
    parser.add_argument("url", type=str, help="URL of the GitHub directory to download")

    args = parser.parse_args()

    # Get user's default Downloads folder
    save_path = get_default_download_path()

    try:
        zip_file_path = download_github_directory(args.url, save_path)
        print(f"✅ Download complete! File saved at: {zip_file_path}")
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
