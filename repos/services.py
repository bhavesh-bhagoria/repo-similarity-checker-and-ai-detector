from git import Repo
import tokenize
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

def read_file(file_path):
    with open(file_path, "r") as file:
        content = file.read()

    return content

def read_all_files(files):

    file_contents = []
    for file_path in files:
        content = read_file(file_path)
        file_contents.append(content)

    return file_contents



def tokenize_file(file_path):
    tokens = []
    with open(file_path, "rb") as file:
        for token in tokenize.tokenize(file.readline):
            if token.type == tokenize.ENCODING:
                continue
            tokens.append(token.string)

    return tokens

def normalize_tokens(tokens):
    normalized = []

    for token in tokens:
        if token.isidentifier():
            normalized.append("NAME")
        else:
            normalized.append(token)

    return normalized