from tkinter import filedialog

# Opens file to be manipulated
def openfile():
    try:
        data = open('nums.txt', 'r')
    except FileNotFoundError:
        new = input('There was an issue locating the specified file.\n Would you like to create this file now? \n'
                    'Please enter "y" to create or any other key to exit.')
        if new == 'y' or new == 'Y':
            data = createfile()
        else:
            exit(print('Good bye'))
    return data


def adddata(num, file, option):
        try:
            file = open(file, option)
            file.write(str(int(input('Enter an integer value'))) + '\n')
        except ValueError:
            print('Invalid entry. Please try again.')


# Reads file and calculates total of all numbers
def gettotal():
    file = openfile()
    total = 0
    for num in file:
        total += int(num)
    file.close()
    return total


# Reads file and counts the number of lines
def getcount():
    file = openfile()
    count = 0
    test = file.readline()
    while test != '':
        count = count + 1
        test = file.readline()
    file.close()
    return count


# Divides the total by the count
def getaverage():
    total = gettotal()
    count = getcount()
    try:
        average = total / count
    except ZeroDivisionError:
        print('There is insufficient data in the file provided. Please check the file and run the program again.')
        exit(input('Press ENTER to EXIT'))
    return average


# Prints total
def printtotal():
    print('total of all numbers is ' + str(gettotal()))


# Prints count
def printcount():
    print('the total count is ' + str(getcount()) + ' numbers in the list')


# Prints average
def printaverage():
    print('the average of all numbers combined is ' + str(getaverage()))


datatest()
printtotal()
printcount()
printaverage()

leave = input('PRESS ENTER TO EXIT PROGRAM')
exit()

