import os


def get_dir_size(path):
    size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            size += os.path.getsize(fp)
    return size


def print_directory_tree(path, prefix=""):
    print(f"{prefix[:-1]} ({get_dir_size(path)} bytes)")
    prefix += "|__ "
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            print(f"{prefix}{item}/")
            print_directory_tree(item_path, prefix)


root_path = 'E:\\code\\script'
print_directory_tree(root_path)
