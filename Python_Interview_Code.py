from typing import List,Dict,Optional
from enum import Enum
from datetime import datetime

class Status(Enum):
    New=1
    Progress=2
    Done=3

class Ticket:
    ticket_id = 0
    def get_Next_Id():
        Ticket.ticket_id+=1
        return Ticket.ticket_id
    
    def __init__(self,type:Status, 
                 Assignee:Optional[str]="System",
                 requestTime:Optional[datetime]=None,
                 id:Optional[int]=None,
                 comments:List[str]=[]):
        self.id = id or Ticket.get_Next_Id()
        self.requestTime = requestTime or datetime.now()
        self.assignee = Assignee
        self.type = type
        self.request_time = requestTime
        self.comments = comments
    
    def add_comments(self,comments:List[str]=None): # DO NOT USE []as default as this is mutable and share among instances
    # def add_comments(self,comments:List[str]=[]]): # BAD PROGRAMMING AS [] is a mutable data type     
        if comments:
            self.comments.extend(comments)
        
    def __str__(self):
        return "Ticket Id={},Type={},Assignee={},requestTime={}".format(self.id,self.type,self.assignee,self.request_time)

t = Ticket(type=Status.New,requestTime=datetime.now())
print(t)
t = Ticket(type=Status.Progress)
print(t)
t = Ticket(type=Status.New,requestTime=datetime.now())
print(t)
