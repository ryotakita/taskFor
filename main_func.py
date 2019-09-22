import re
import os
import time
import pickle
import datetime

import Date
import Task
import main_func
import TaskLog

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

def getLogInf(lstLog):
    when = input("when?>>>")
    if (when == "today"):
        today = datetime.datetime.now()
        day = today.day
        os.system("clear")
        print("start" + "\t" + "end" + "\t" +
                "time" +"\t"+"project"+"\t"+"kind")
        for log in lstLog:
            logDay = log.startTime.day
            if (logDay == day):
                logInf = log.getLogInfForDay()
                print(logInf)
    else:
        for log in lstLog:
            logDay = log.startTime.day
            os.system("clear")
            print("start" + "\t" + "end" + "\t" +
                    "time" +"\t"+"project"+"\t"+"kind")
            if (logDay == int(when)):
                logInf = log.getLogInfForDay()
                print(logInf)

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

def saveLog(lstLog):
    with open("log.pickle", mode="wb") as f:
        pickle.dump(lstLog, f)

def startTaskFor():
    try:
        with open("task.pickle", mode="rb") as f:
            lstTask = pickle.load(f)
            return lstTask
    except FileNotFoundError:
        lstTask = []
        return lstTask

def startLogFor():
    try:
        with open("log.pickle", mode="rb") as f:
            lstLog = pickle.load(f)
            return lstLog
    except FileNotFoundError:
        lstLog = []
        return lstLog

def startTagProjectFor():
    try:
        with open("tagProject.pickle", mode="rb") as f:
            lstTagProject = pickle.load(f)
            return lstTagProject
    except FileNotFoundError:
        lstTagProject = []
        return lstTagProject

def startTagKindFor():
    try:
        with open("tagKind.pickle", mode="rb") as f:
            lstTagKind = pickle.load(f)
            return lstTagKind
    except FileNotFoundError:
        lstTagKind = []
        return lstTagKind

def setLogStartTime():
    startTime = datetime.datetime.now()
    with open("startTime.pickle", mode="wb") as f:
        pickle.dump(startTime, f)

def setTaskLog(lstTagProject, lstTagKind, lstLog):
    try:
        with open("startTime.pickle", mode="rb") as f:
            startTime = pickle.load(f)
    except FileNotFoundError:
        print("Not Found StartTime")
        return
    endTime = datetime.datetime.now()
    title = input("title>>>")
    os.system("clear")
    for tagProject in lstTagProject:
        print(str(lstTagProject.index(tagProject) + 1) + ":" + tagProject)
    print("0:addTaskProject")
    userinput = input("setTaskProject>>>")
    if (userinput == "0"):
        ProjectName = input("projectName>>>")
        lstTagProject.append(ProjectName)
        with open("tagProject.pickle", mode="wb") as f:
            pickle.dump(lstTagProject, f)
        tagProjectForSet = ProjectName
    else:
        tagProjectForSet = lstTagProject[int(userinput) - 1]

    os.system("clear")
    for tagKind in lstTagKind:
        print(str(lstTagKind.index(tagKind) + 1) + ":" + tagKind)
    print("0:addTaskKind")
    userinput = input("setTaskKind>>>")
    if (userinput == "0"):
        KindName = input("kindName>>>")
        lstTagKind.append(KindName)
        with open("tagKind.pickle", mode="wb") as f:
            pickle.dump(lstTagKind, f)
        tagKindForSet = KindName
    else:
        tagKindForSet = lstTagKind[int(userinput) - 1]

    doTime = endTime - startTime

    taskLog = TaskLog.Log(startTime, endTime, title, tagProjectForSet, tagKindForSet, doTime)
    lstLog.append(taskLog)
    

    

