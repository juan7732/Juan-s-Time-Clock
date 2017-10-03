import time

try:
    open('TimeSheets\isClock.txt')
except FileNotFoundError:
    with open('TimeSheets\isClock.txt', 'w') as tm:
        tm.write('0')

with open("TimeSheets\isClock.txt", 'r+') as f:
    isClocked = f.read()
    clockIn = time.time()
    if isClocked == '1':
        print("Already Clocked In\n")
    else:
        with open("TimeSheets\\temp.txt", 'w') as ftmp:
            ftmp.write(str(clockIn))
        f.seek(0)
        f.write('1')
        print("Clocked in Successfully")
input("Press any button to continue...")
