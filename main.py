import main_func
import os

if __name__ == '__main__':
    lstTask = main_func.startTaskFor()
    lstTagProject = main_func.startTagProjectFor()
    lstTagKind = main_func.startTagKindFor()
    lstLog = main_func.startLogFor()
    i = 0
    while i == 0:
        userinput = input("input...")
        if (userinput == "set"):
            main_func.setTask(lstTask)
            os.system("clear")
            main_func.saveTask(lstTask)
        if (userinput == "get"):
            os.system("clear")
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
        if (userinput == "0"):
            i = 1
    

