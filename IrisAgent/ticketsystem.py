from enum import Enum
from typing import Optional

class TicketType(Enum):
    Created=1
    InProgress=2
    Closed=3

class Ticket:
    TicketId = 0

    @classmethod
    def get_next_Id(cls):
        cls.TicketId+=1
        return cls.TicketId
    
    def __init__(self, ticketSubject:str, id:Optional[int]=None, ticketType:Optional[TicketType]=TicketType.Created):
        self.Id = id or Ticket.get_next_Id()
        self.Subject = ticketSubject
        self.ticketType = ticketType    
    
    def __str__(self):
        return "Ticket No:{}, Subject={}, Type={}".format(self.TicketId,self.Subject,self.ticketType)
    

if __name__=="__main__":
    ticket = []
    ticket.append(Ticket(ticketSubject="First"))
    ticket.append(Ticket("Second",100))
    ticket.append(Ticket("Third",ticketType=TicketType.Closed))

    for t in ticket:
        print(t)
    


