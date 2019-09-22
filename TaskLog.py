import datetime

def get_h_m_s(doTime):
    m, s = divmod(doTime.seconds, 60)
    h, m = divmod(m, 60)
    return h, m

class Log:
    tagProject = ""
    tagKind = ""
    startTime = datetime.datetime.now()
    endTime = datetime.datetime.now()
    LogTitle = ""
    doTime = datetime.timedelta(weeks=1, days=1, hours=1, minutes=1,
                                 seconds=1, milliseconds=1, microseconds=1)
    def __init__(self, startTime, endTime, LogTitle, tagProject, tagKind, doTime):
        self.startTime = startTime
        self.endTime = endTime
        self.LogTitle = LogTitle
        self.tagProject = tagProject
        self.tagKind = tagKind
        self.doTime = doTime
    def getLogInfForDay(self):
        startTimeInf = str(self.startTime.hour) + ":" + str(self.startTime.minute)
        endTimeInf = str(self.endTime.hour) + ":" + str(self.endTime.minute)
        doTimeInf_h, doTimeInf_m = get_h_m_s(self.doTime)
        doTimeInf = str(doTimeInf_h) + "時間" + str(doTimeInf_m) + "分"
        logInfForDay = "*"+self.LogTitle +"\n"+startTimeInf+"\t"+endTimeInf+"\t"+doTimeInf+"\t"+self.tagProject+"\t"+self.tagKind

        return logInfForDay

    


