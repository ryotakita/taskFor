# -*- coding: utf-8 -*-
import re
import os
import time
import pickle
import datetime
import csv

import Date
import Task
import main_func
import TaskLog
import statistics

#TODO: タグとタスクログの削除対応


def setTask(lstTask):
    taskInf = input("title,date,subtitle>>>")
    lstTaskInf = re.split('\s', taskInf)
    title = ""
    subtitle = ""
    month = "00"
    day = "00.datetime"
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
    os.system("clear")
    printStartTime()
    count = 1
    for task in lstTask:
        taskInf = task.getTaskInf()
        print(str(count) + ":" + taskInf)
        count += 1

def getLogInf(lstLog):
    when = input("when?>>>")
    if (when == "today" or when == ""):
        today = datetime.datetime.now()
        day = today.day
        os.system("clear")
        printStartTime()
        for log in lstLog:
            logDay = log.startTime.day
            if (logDay == day):
                logInf = log.getLogInfForDay()
                print(str(lstLog.index(log)) + logInf)
    else:
        os.system("clear")
        printStartTime()
        for log in lstLog:
            logDay = log.startTime.day
            if (logDay == int(when)):
                logInf = log.getLogInfForDay()
                print(str(lstLog.index(log)) + logInf)
    userinput = input("deleteAnyLog?")
    if (userinput == "1"):
        deleteindex = input("deleteIndex?")
        del lstLog[int(deleteindex)]

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
    global startTime
    startTime = datetime.datetime.now()
    with open("startTime.pickle", mode="wb") as f:
        pickle.dump(startTime, f)
    print("startYourTask->" + str(startTime))

def setTaskLog(lstTagProject, lstTagKind, lstLog):
    try:
        with open("startTime.pickle", mode="rb") as f:
            startTime = pickle.load(f)
            print(str(startTime))
    except FileNotFoundError:
        print("Not Found StartTime")
        return
    endTime = datetime.datetime.now()
    userinput = input("customStart?")
    if (userinput == "1"):
        startTimeTmp = input("insertStartTime>>>")
        if (len(startTimeTmp) == 4):
            hour = startTimeTmp[:2]
            minutes = startTimeTmp[2:4]
            now = datetime.datetime.now()
            startTime = datetime.datetime(now.year, now.month, now.day, int(hour), int(minutes))
        else:
            print("InvalidData")
            return
    userinput = input("customEnd?")
    if (userinput == "1"):
        endTimeTmp = input("insertEndTime>>>")
        if (len(endTimeTmp) == 4):
            hour = endTimeTmp[:2]
            minutes = endTimeTmp[2:4]
            now = datetime.datetime.now()
            endTime = datetime.datetime(now.year, now.month, now.day, int(hour), int(minutes))
        else:
            print("InvalidData")
            return
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
    os.remove("startTime.pickle")


def getCSV(lstLog):
    with open("log.csv", "w") as f:
        writer = csv.writer(f)
        for log in lstLog:
            lstLogParameta = log.getLogParametaList()
            writer.writerow(lstLogParameta)
    return

def startStat(csv):
    os.system("clear")
    printStartTime()
    sortDate = input("day or month or year>>>")
    year = 0
    month = 0
    day = 0
    if (sortDate == "day"):
        year = input("input year>>>")
        month = input("input month>>>")
        day = input("input day>>>")
        data = csv.getDataOfDay(year, month, day)
    elif (sortDate == "month"):
        year = input("inpur year>>>")
        month = input("input month>>>")
        data = csv.getDataOfMonth(year, month)
    elif (sortDate == "year"):
        year = input("input year>>>")
        data = csv.getDataOfYear(year)
    else:
        print("Error")
        return
    
    sortTag = input("1:Project\n2:Kind>>>\n")
    if (sortTag == "1" or sortTag == ""):
        os.system("clear")
        printStartTime()
        csv.getSumOfProject(data)
    elif (sortTag == "2"):
        os.system("clear")
        printStartTime()
        csv.getSumOfKind(data)
    else:
        print("Error")
    return
    
def deleteTag(lstTagKind,lstTagProject):
    os.system("clear")
    print("0:Project")
    userinput = input("1:Kind")
    if (userinput == "0"):
        for tag in lstTagProject:
            print(str(lstTagProject.index(tag)) + ":" + tag)
        deleteIndex = input("deleteNumber?>>>")
        print("deleteThisTag-> " + lstTagProject[int(deleteIndex)])
        del lstTagProject[int(deleteIndex)]
        with open("tagProject.pickle", mode="wb") as f:
            pickle.dump(lstTagProject, f)
    if (userinput == "1"):
        for tag in lstTagKind:
            print(str(lstTagKind.index(tag)) + ":" + tag)
        deleteIndex = input("deleteNumber?")
        print("deleteThisTag-> " + lstTagKind[int(deleteIndex)])
        del lstTagKind[int(deleteIndex)]
        with open("tagKind.pickle", mode="wb") as f:
            pickle.dump(lstTagKind, f)

def printStartTime():
    try:
        with open("startTime.pickle", mode="rb") as f:
            startTime = pickle.load(f)
            print(str(startTime))
    except FileNotFoundError:
        print("Not Found StartTime")

        

    
