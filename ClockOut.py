import time
import math
import datetime
import os


def time_format(timeTotal):
    timeTotal = int(math.floor(timeTotal))
    hours = timeTotal / 3600
    timeTotal = timeTotal % 3600
    minutes = timeTotal / 60
    timeTotal = timeTotal % 60
    seconds = timeTotal
    return [math.floor(hours), math.floor(minutes), seconds]


def mktimedir(today):
    defpath = 'TimeSheets\\'
    if os.path.exists(defpath + time.strftime('%Y', today)):
        if os.path.exists(defpath + time.strftime('%Y\\%b', today)):
            if os.path.exists(defpath + time.strftime('%Y\\%b\\%d', today)):
                pass
            else:
                os.mkdir(defpath + time.strftime('%Y\\%b\\%d', today))
        else:
            os.mkdir(defpath + time.strftime('%Y\\%b', today))
            os.mkdir(defpath + time.strftime('%Y\\%b\\%d', today))
    else:
        os.mkdir(defpath + time.strftime('%Y', today))
        os.mkdir(defpath + time.strftime('%Y\\%b', today))
        os.mkdir(defpath + time.strftime('%Y\\%b\\%d', today))
    return time.strftime(defpath + time.strftime('%Y\\%b\\%d', today))


with open("TimeSheets\isClock.txt", 'r+') as f:
    isClocked = f.read()
    clockOut = time.time()
    today = time.localtime(clockOut)
    todayPath = mktimedir(today)
    clockIn = 0
    if isClocked == '0':
        print("Already Clocked Out\n")
    else:
        with open("TimeSheets\\temp.txt", 'r') as ftmp:
            clockIn = float(ftmp.read())
        f.seek(0)
        f.write('0')
        timeTotal = clockOut - clockIn
        timeTotal = time_format(timeTotal)
        with open(todayPath + '\TimeSheet.txt','a') as ts:
            ts.write(str(datetime.time(timeTotal[0], timeTotal[1], timeTotal[2])) + time.strftime(' %b %d, %Y %a [%H:%M:%S]', time.localtime(clockIn)) + time.strftime(' - %b %d, %Y %a [%H:%M:%S]\n', time.localtime(clockOut)) )
        print("Clocked out Successfully")
        print("Time Worked: \t" + str(datetime.time(timeTotal[0], timeTotal[1], timeTotal[2])))
        os.remove("TimeSheets\\temp.txt")
input("Press any button to continue...")
