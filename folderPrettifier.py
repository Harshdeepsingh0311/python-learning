import os


def soldier(path, file, format):
    os.chdir(path)
    i = 1
    files = os.listdir(path)
    with open(file) as f:
        fileLists = f.read().split('\n')

    for file in files:
        if file not in fileLists:
            os.rename(file, file.capitalize())

        if os.path.splitext(file)[1] == format:
            os.rename(file, f'{i}.{format}')
            i += 1


soldier(r'YOUR FOLDER',r'YOUR FILE WHICH CONTAINS THE NON NAMES NOT TO BE CHANGED', 'FILE FORMAT')