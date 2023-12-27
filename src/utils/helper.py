import os
import scheduler

def is_file_exists(file_path):
    return os.path.isfile(file_path)


def is_dir_exists(dir_path):
    return os.path.isdir(dir_path)
