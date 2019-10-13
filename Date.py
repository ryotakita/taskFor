# -*- coding: utf-8 -*-
class Date:
    def __init__(self, month, day, hour = "00"):
        self.year = "2019"
        self.month = month
        self.day = day
        self.hour = hour
    def getDate(self):
        date = self.month + "月" + self.day + "日" + self.hour + "時"
        return date
        

        
        
        