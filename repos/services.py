from git import Repo


def clone_repository(url, destination):
    Repo.clone_from(url, destination)