from collections import deque

events_inmoment = deque()
UserEventsInMoment = deque()

class event:
    def __init__(self, type, data):
        import pyga_me
        self.type = type

        if self.type == pyga_me.NOTEPLAYED:
            self.note =  data
        
        elif self.type == pyga_me.NOTESTOP:
            self.note = data
        
        elif self.type == pyga_me.LAGANIMATION:
            self.delay = data

        elif self.type == pyga_me.SAFEANIMATION:
            self.delay = data

        elif self.type == pyga_me.NEGATIVEROLL:
            self.object = data[0]
            self.value = data[1]

        elif self.type == pyga_me.POSITIVEROLL:
            self.object = data[0]
            self.value = data[1]

        elif self.type == pyga_me.GIFEXECUTED:
            self.number_of_executions = data
        
        elif self.type == pyga_me.NOTESTOP_INACCURATE:
            self.note = data
        
        elif self.type == pyga_me.SELECTUP:
            self.selected = data

        elif self.type == pyga_me.SELECTDOWN:
            self.selected = data

        elif self.type == pyga_me.SELECTCONFIRM:
            self.selected = data

        elif self.type == pyga_me.NULLNOTEPLAYED:
            self.note = data
        
        elif self.type == pyga_me.NULLNOTESTOP:
            self.note = data
        
        elif self.type == pyga_me.NULLNOTESTOP_INACCURATE:
            self.note = data
        
        elif self.type == pyga_me.LAGDOWNLOAD:
            self.delay = data
        
        elif self.type == pyga_me.SAFEDOWNLOAD:
            self.delay = data
        
        elif self.type == pyga_me.EXCEPTDOWNLOAD:
            self.url = data[0]
            self.exception = data[1]
        
        elif self.type == pyga_me.P2DCREATED:
            self.player = data

        elif self.type == pyga_me.P2DUPDATE:
            self.player = data
        
        elif self.type == pyga_me.P2DRMOVE:
            self.player = data[0]
            self.posX = data[1]
        
        elif self.type == pyga_me.P2DLMOVE:
            self.player = data[0]
            self.posX = data[1]
        
        elif self.type == pyga_me.P2DJUMP:
            self.player = data[0]
            self.posY = data[1]

        elif self.type == pyga_me.P2DLANDED:
            self.player = data[0]
            self.posY = data [1]
        
        elif self.type == pyga_me.P2DSPECIALKEYPRESSED:
            self.player = data[0]
            self.key = data[1]
            self.consequence = data[2]
        
        elif self.type == pyga_me.P2DDEAD:
            self.player = data
        
        else:
            self.data = data

def get_events():
    import pyga_me
    validated: list[event] = []
    while events_inmoment: 
        ev = events_inmoment.popleft()
        if ev.type in range(pyga_me.V_NONE, pyga_me.USEREVENT + 1): 
            validated.append(ev)
    while UserEventsInMoment:
        ev = UserEventsInMoment.popleft()
        validated.append(ev)
    return validated