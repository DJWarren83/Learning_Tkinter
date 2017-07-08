from tkinter import *
from Files_and_Exceptions import *

# main gui window(visible) sits on gui controller(not visible)
root = Tk()


"""
The following section deals exclusively with the main menu. 
These areas are where the File Edit View Help etc, menu sections will be
created and handled, as well as the Status bar along the bottom of the main program window.
"""
# top menu bar(ie. File Edit View Options etc.) menu sits on main window
main_menu = Menu(root)

'''File Menu'''
# drop down menu from main menu
file_menu = Menu(main_menu, tearoff=0)
# makes a drop down File menu option
main_menu.add_cascade(label='File', menu=file_menu)
# Open File menu option in the File menu. Saves file path for manipulation later.
cur_path = file_menu.add_command(label='Select File', command=App.set_cur_file_path)
# adds a separator between menu options
file_menu.add_separator()
# close program
file_menu.add_command(label='Exit', command=root.quit)
# not too sure about this line, but menus dont work without it.
root.config(menu=main_menu)


'''Status bar'''
cur_status = 'Ready'
status = Label(root, text=cur_status, bd='1', relief='sunken', anchor='w')
status.pack(side='bottom', fill='x')


'''
This section builds the main area of the gui where
the user spends most of their time.
'''
# creates and places a new frame for the main area to built on.
main = Frame(root)
main.pack()


# title line at top of main area
title = Label(main, text='Functions and Exceptions')
title.pack()

# add_new_entry label
add_label = Label(main, text='Add a new number to the file')
add_label.pack()
# add_new_entry entry field
add_entry = Entry(main, textvariable='test')
add_entry.pack()
# add_new_entry button
add_button = Button(main, text='Submit', command='')
add_button.pack()

# count_label displays the number of entries in the file
cur_count = App.cur_count
count_label = Label(main, text=str(cur_count))
count_label.pack()


'''Main loop for the program'''
# main program loop
root.mainloop()
