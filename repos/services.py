from git import Repo
import os


def clone_repository(url, destination):
    Repo.clone_from(url, destination)

def get_source_files(directory):
    supported_extensions = (
        ".py", ".js", ".java", ".cpp", ".c",
        ".html", ".css", ".txt", ".md")
    files_found = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(supported_extensions):
                files_found.append(os.path.join(root, file))

    return files_found