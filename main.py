# import Date
# import Task
import main_func

# import re
import os
# import time
# import pickle
# import datetime

if __name__ == '__main__':
    lstTask = main_func.startTaskFor()
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
        if (userinput == "0"):
            i = 1
    

