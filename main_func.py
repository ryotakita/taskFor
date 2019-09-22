import re
import os
import time
import pickle
import datetime

import Date
import Task
import main_func

def setTask(lstTask):
    taskInf = input("title,date,subtitle>>>")
    lstTaskInf = re.split('\s', taskInf)
    title = ""
    subtitle = ""
    month = "00"
    day = "00"
    hour = "00"
    if (len(lstTaskInf) == 2):
        title = lstTaskInf[0]
        date = lstTaskInf[1]
        if (date == "today"):
            now = datetime.datetime.now()
            month = str(now.month)
            day = str(now.day)
        elif(len(date) == 4):
            month = date[:2]
            day = date[2:4]
        elif (len(date) == 6):
            month = date[:2]
            day = date[2:4]
            hour = date[4:6]
        else:
            print("日にちの形式が不正です")
            time.sleep(1)
            return
    elif (len(lstTaskInf) == 3):
        title = lstTaskInf[0]
        date = lstTaskInf[1]
        subtitle = lstTaskInf[2]
        if (date == "today"):
            now = datetime.datetime.now()
            month = str(now.month)
            day = str(now.day)
        elif(len(date) == 4):
            month = date[:2]
            day = date[2:4]
        elif (len(date) == 6):
            month = date[:2]
            day = date[2:4]
            hour = date[4:6]
        else:
            print("日にちの形式が不正です")
            time.sleep(1)
            return
    else:
        print("不正な入力です")
        time.sleep(1)
        return
    
    cdate = Date.Date(month, day, hour)
    task = Task.Task(cdate, title, subtitle)
    lstTask.append(task)


def getTaskInf(lstTask):
    count = 1
    for task in lstTask:
        taskInf = task.getTaskInf()
        print(str(count) + ":" + taskInf)
        count += 1

def deleteTask(lstTask):
    deleteNum = input("deleteNumber?>>>")
    try:
        deleteTask = lstTask.pop(int(deleteNum) - 1)
        print("deleted this task -> " + deleteTask.getTaskInf())
    except IndexError:
        print("Not Found Such Index")

def saveTask(lstTask):
    with open("task.pickle", mode="wb") as f:
        pickle.dump(lstTask, f)

def startTaskFor():
    try:
        with open("task.pickle", mode="rb") as f:
            lstTask = pickle.load(f)
            return lstTask
    except FileNotFoundError:
        lstTask = []
        return lstTask