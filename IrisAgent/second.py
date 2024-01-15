from typing import Optional

class Second:
    TicketId = 0
    @classmethod
    def get_next_Id(cls):
        cls.TicketId+=1
        return cls.TicketId
    
    def __init__(self, id:Optional[int])->None:
        self.id = id or Second.get_next_Id()
        print(self.id)
    

if __name__=="__main__":
    s = Second()
    
        