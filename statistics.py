import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime

class CSV:
    def __init__(self):
        self.data = pd.read_csv("log.csv", names=("starTIme","endTime","Title","project","kind","time"))
        self.data.head(2)
        self.data = pd.read_csv("log.csv", names=(
            "startTime", "endTime", "Title", "project", "kind", "time"))
        self.data.head(2)
        self.data.set_index("startTime", inplace=True)
        self.data.index = pd.to_datetime(self.data.index)
        self.data["year"] = list(pd.Series(self.data.index).apply(lambda x: x.year))
        self.data["month"] = list(pd.Series(self.data.index).apply(lambda x: x.month))
        self.data["day"] = list(pd.Series(self.data.index).apply(lambda x: x.day))
        self.data.set_index("time", inplace = True)
        self.data.index = pd.to_timedelta(self.data.index)
        self.data["seconds"] = list(pd.Series(self.data.index).apply(lambda x: x.seconds))
    def getSumOfProject(self, dataSource):
        self.test = dataSource.groupby(["project"])["seconds"].sum()
        self.m, self.s = divmod(self.test  ,60)
        self.h, self.m = divmod(self.m,60)
        data = pd.concat([self.test,self.h,self.m], axis =1,sort=True, keys = ["seconds", "hour", "minutes"])
        print(data)
    def getSumOfKind(self, dataSource):
        self.test = dataSource.groupby(["kind"])["seconds"].sum()
        self.m, self.s = divmod(self.test  ,60)
        self.h, self.m = divmod(self.m,60)
        data = pd.concat([self.test,self.h,self.m], axis =1,sort=True, keys = ["seconds", "hour", "minutes"])
        print(data)
    def getDataOfDay(self, year, month, day):
        now = datetime.datetime.now()
        yearNow = now.year
        monthNow = now.month
        dayNow = now.day
        if (year == ""):
            year = yearNow
        if (month == ""):
            month = monthNow
        if (day == ""):
            day = dayNow
        DataDay = self.data[(self.data["day"] == int(day)) & (self.data["year"] == int(year)) & (self.data["month"] == int(month))]
        return DataDay
    def getDataOfMonth(self, year, month):
        now = datetime.datetime.now()
        yearNow = now.year
        monthNow = now.month
        if (year == ""):
            year = yearNow
        if (month == ""):
            month = monthNow
        DataDay = self.data[(self.data["year"] == int(year)) & (self.data["month"] == int(month))]
        return DataDay
    def getDataOfYear(self, year):
        now = datetime.datetime.now()
        yearNow = now.year
        if (year == ""):
            year = yearNow
        DataDay = self.data[(self.data["year"] == int(year))]
        return DataDay

        

