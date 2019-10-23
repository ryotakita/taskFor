import main_func
import datetime
import os
import statistics
import pickle

if __name__ == '__main__':
    lstTask = main_func.startTaskFor()
    lstTagProject = main_func.startTagProjectFor()
    lstTagKind = main_func.startTagKindFor()
    i = 0
    os.system("cls")
    main_func.printStartTime()
    while i == 0:
        userinput = input("input...")
        if (userinput == "set"):
            main_func.setTask(lstTask)
            os.system("cls")
            main_func.saveTask(lstTask)
        if (userinput == "get"):
            main_func.getTaskInf(lstTask)
        if (userinput == "delete"):
            os.system("cls")
            main_func.getTaskInf(lstTask)
            main_func.deleteTask(lstTask)
            main_func.saveTask(lstTask)
        if (userinput == "start"):
            main_func.setLogStartTime()
        if (userinput == "end"):
            main_func.setTaskLog(lstTagProject, lstTagKind)
        if (userinput == "getlog"):
            print("現在調整中")
            os.system("cls")
        if (userinput == "stat"):
            csv = statistics.CSV()
            main_func.startStat(csv)
        if (userinput == "deletetag"):
            main_func.deleteTag(lstTagKind,lstTagProject)
        if (userinput == "0"):
            i = 1
    


