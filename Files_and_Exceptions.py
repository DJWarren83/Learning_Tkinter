from tkinter import filedialog


def get_file_path():
    global cur_path
    path = filedialog.askopenfilename()
    cur_path = path
    print(path)
    return path


def open_file(path):
    file = open(path, 'r')
    return file


def add_new_num(num, path):
    file = open(path, 'a')
    file.write(str(int(input(num))) + '\n')


def read_file_line(origin):
    file = origin
    line = file.readline()
    line = line.rstrip('\n')

    return line


def get_count(path):
    print(path)
    count = 0

    file = open_file(path)
    cur_line = read_file_line(file)
    while cur_line != '':
        count += 1

    return str(count)


