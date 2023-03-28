"""Get clone dir from pre file."""

import os


def get_clone_dir(pre_file: str) -> tuple[str, str]:
    """
    Create pre_clone_files, take pre_file add titles, compare.
    Returns clone_dir.
    """
    pre_clone_files = []
    with open(pre_file, 'r') as titles:
        for line in titles:
            pre_clone_files.append(line.replace('\n', ''))

    clone_dir = [some_dir for some_dir in os.listdir(path=".")
        if some_dir not in pre_clone_files]
    clone_dir_git = clone_dir[0] + "/.git/"

    return clone_dir[0], clone_dir_git
