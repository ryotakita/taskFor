
# -*- coding: utf-8 -*-
import main_func
import datetime
import os
import statistics
import pickle

if __name__ == '__main__':
    lstTask = main_func.startTaskFor()
    lstTagProject = main_func.startTagProjectFor()
    lstTagKind = main_func.startTagKindFor()
    lstLog = main_func.startLogFor()
    i = 0
    os.system("clear")
    main_func.printStartTime()
    while i == 0:
        userinput = input("input...")
        if (userinput == "set"):
            main_func.setTask(lstTask)
            os.system("clear")
            main_func.saveTask(lstTask)
        if (userinput == "get"):
            main_func.getTaskInf(lstTask)
        if (userinput == "delete"):
            os.system("clear")
            main_func.getTaskInf(lstTask)
            main_func.deleteTask(lstTask)
            main_func.saveTask(lstTask)
        if (userinput == "start"):
            main_func.setLogStartTime()
        if (userinput == "end"):
            main_func.setTaskLog(lstTagProject, lstTagKind, lstLog)
            main_func.saveLog(lstLog)
        if (userinput == "getlog"):
            main_func.getLogInf(lstLog)
            main_func.saveLog(lstLog)
        if (userinput == "stat"):
            main_func.getCSV(lstLog)
            csv = statistics.CSV()
            main_func.startStat(csv)
        if (userinput == "deletetag"):
            main_func.deleteTag(lstTagKind,lstTagProject)
        if (userinput == "0"):
            i = 1
    


