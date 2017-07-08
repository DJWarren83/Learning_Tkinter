from tkinter import filedialog


class App(object):

    cur_count = 0

    def add_new_num(self, num, path):
        file = open(path, 'a')
        file.write(str(int(input(num))) + '\n')

    def open_file(self, path, option):
        file = open(path, option)
        return file

    def set_file_path(self):
        path = filedialog.askopenfilename()
        self.open_file(path, 'r')
        return path

    def get_file_path(self):
        return self.cur_file_path

    def read_file_line(self, origin):
        file = origin
        line = file.readline()
        line = line.rstrip('\n')

        return line

    def set_count(self, path):
        App.cur_count = 0

        file = App.open_file(None, path, 'r')
        cur_line = App.read_file_line(None, file)
        while cur_line != '':
            App.cur_count += 1

    set_cur_file_path = set_file_path()
