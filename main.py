import Date
import Task

import re
import os
import time


def setTask(lstTask):
    taskInf = input("title,date,subtitle>>>")
    lstTaskInf = re.split('\s',taskInf)
    if (len(lstTaskInf) == 2):
        title = lstTaskInf[0]
        date = lstTaskInf[1]
        if(len(date) == 4):
            month = date[:2]
            day = date[2:4]
            cdate = Date.Date(month, day)
            task = Task.Task(cdate, title)
        elif (len(date) == 6):
            month = date[:2]
            day = date[2:4]
            hour = date[4:6]
            cdate = Date.Date(month, day, hour)
            task = Task.Task(cdate, title)
        else:
            print("日にちの形式が不正です")
            time.sleep(1)
            return
    elif (len(lstTaskInf) == 3):
        title = lstTaskInf[0]
        date = lstTaskInf[1]
        subtitle = lstTaskInf[2]
        if(len(date) == 4):
            month = date[:2]
            day = date[2:4]
            cdate = Date.Date(month, day)
            task = Task.Task(cdate, title, subtitle)
        elif (len(date) == 6):
            month = date[:2]
            day = date[2:4]
            hour = date[4:6]
            cdate = Date.Date(month, day, hour)
            task = Task.Task(cdate, title, subtitle)
        else:
            print("日にちの形式が不正です")
            time.sleep(1)
            return
    else:
        print("不正な入力です")
        time.sleep(1)
        return
    
    lstTask.append(task)


def getTaskInf(lstTask):
    count = 1
    for task in lstTask:
        taskInf = task.getTaskInf()
        print(str(count) + ":" + taskInf)
        count += 1

def saveTask(lstTask):
    lstTaskSave = []
    for task in lstTask:
        task = task.getTask()
        lstTaskSave.append(task)
    file = open("task.txt", "w")
    file.write('\n'.join(lstTaskSave))
    file.close()

def startSetTask(lstTask):
    file = open("Task.txt", "r")
    for task in file:
        lstTaskInf = task.split(',')
        if (len(lstTaskInf) == 2):
            title = lstTaskInf[0]
            date = lstTaskInf[1]
            if(len(date) == 4):
                month = date[:2]
                day = date[2:4]
                cdate = Date.Date(month, day)
                task = Task.Task(cdate, title)
            elif (len(date) == 6):
                month = date[:2]
                day = date[2:4]
                hour = date[4:6]
                cdate = Date.Date(month, day, hour)
                task = Task.Task(cdate, title)
        elif (len(lstTaskInf) == 3):
            title = lstTaskInf[0]
            date = lstTaskInf[1]
            subtitle = lstTaskInf[2].rstrip('\n')
            if(len(date) == 4):
                month = date[:2]
                day = date[2:4]
                cdate = Date.Date(month, day)
                task = Task.Task(cdate, title, subtitle)
            elif (len(date) == 6):
                month = date[:2]
                day = date[2:4]
                hour = date[4:6]
                cdate = Date.Date(month, day, hour)
                task = Task.Task(cdate, title, subtitle)
        
        lstTask.append(task)

def deleteTask(lstTask):
    deleteNum = input("deleteNumber?>>>")
    deleteTask = lstTask.pop(int(deleteNum) - 1)
    print("deleted this task -> " + deleteTask.getTaskInf())



        
    
    
        



if __name__ == '__main__':
    lstTask = []
    startSetTask(lstTask) 
    i = 0
    while i == 0:
        userinput = input("input...")
        if (userinput == "set"):
            setTask(lstTask)
            os.system("clear")
            saveTask(lstTask)
        if (userinput == "get"):
            os.system("clear")
            getTaskInf(lstTask)
        if (userinput == "delete"):
            os.system("clear")
            getTaskInf(lstTask)
            deleteTask(lstTask)
            saveTask(lstTask)
        if (userinput == "0"):
            i = 1
    

