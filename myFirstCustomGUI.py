from tkinter import *
from tkinter import filedialog


# main gui window(visible) sits on gui controller(not visible)
root = Tk()
# top menu bare(ie. File Edit View Options etc.) menu sits on main window
main_menu = Menu(root)
# dropdown menu from main menu
file_menu = Menu(main_menu, tearoff=0)
# makes a drop down File menu option
main_menu.add_cascade(label='File', menu=file_menu)
# Open File menu option in the File menu. Saves file path for manipulation later.
file_path = file_menu.add_command(label='Open File', command=filedialog.askopenfilename)
# adds a seperator between menu options
file_menu.add_separator()
# close program
file_menu.add_command(label='Exit', command=root.quit)

# not too sure about this line, but menus dont work without it.
root.config(menu=main_menu)
# main program loop
root.mainloop()
