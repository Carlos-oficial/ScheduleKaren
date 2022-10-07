from datetime import datetime

class event:
    def __init__(self,id,name,date,time,channel,role,creator):
        self.id = id
        self.name = name
        self.date = datetime.strptime(date, '%d %b %Y') #dia mes ano 
        self.time = datetime.strptime(time, '%H:%M') #hora:minuto
        self.channel = str(channel)
        self.role = str(role)
        self.creator = str(creator)