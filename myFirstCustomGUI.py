from tkinter import *
import Files_and_Exceptions

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
# dropdown menu from main menu
file_menu = Menu(main_menu, tearoff=0)
# makes a drop down File menu option
main_menu.add_cascade(label='File', menu=file_menu)
# Open File menu option in the File menu. Saves file path for manipulation later.
file_path = file_menu.add_command(label='Open File', command='')
# adds a seperator between menu options
file_menu.add_separator()
# close program
file_menu.add_command(label='Exit', command=root.quit)
# not too sure about this line, but menus dont work without it.
root.config(menu=main_menu)


'''Status bar'''
cur_status = 'Ready'
status = Label(root, text=cur_status, bd='1', relief='sunken', anchor='w')
status.pack(side='bottom', fill='x')


'''Buttons'''



'''Main loop for the program'''
# main program loop
root.mainloop()
