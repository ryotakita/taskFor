import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime

class CSV:
    def __init__(self):
        self.data = pd.read_csv("log.csv", names=("starTIme","endTime","Title","project","kind","time"))
        self.data.head(2)
        #print(data)
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
    def get(self):
        self.test = self.data.groupby(["project"])["seconds"].sum()
        #print(test)
        self.m, self.s = divmod(self.test  ,60)
        self.h, self.m = divmod(self.m,60)
        #print(s)
        #print(m)
        # test["time_hour"] = list(h)
        # test["time_minutes"] = list(m)
        #print(test)
        self.test_new = pd.concat([self.test,self.h,self.m], axis =1,sort=True)
        print(self.test_new)
        #test["workingtime"] = list(test.apply(lambda x: str(x['time_hour']) +":"+ str(x['time_minutes'])))
        #print(test)
        #print(data)
