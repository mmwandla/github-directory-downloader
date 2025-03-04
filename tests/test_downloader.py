import unittest
from github_directory_download.utils import extract_repo_info

class TestUtils(unittest.TestCase):
    def test_extract_repo_info(self):
        url = "https://github.com/user/repo/tree/main/folder/subfolder"
        owner, repo, branch, directory = extract_repo_info(url)
        self.assertEqual(owner, "user")
        self.assertEqual(repo, "repo")
        self.assertEqual(branch, "main")
        self.assertEqual(directory, "folder/subfolder")

if __name__ == "__main__":
    unittest.main()
