import Date

class Task:
    cdate = Date.Date(00,00,00)
    title = ""
    subtitle = ""
    def __init__(self, cdate, title, subtitle=""):
        self.cdate = cdate
        self.title = title
        self.subtitle = subtitle
    def getTaskInf(self):
        date = self.cdate.getDate()
        strTaskInf = self.title + ":" + date + ":" + self.subtitle
        return strTaskInf
    def getTask(self):
        strTask = self.title + "," + self.cdate.month + self.cdate.day + self.cdate.hour + "," + self.subtitle
        return strTask



    

