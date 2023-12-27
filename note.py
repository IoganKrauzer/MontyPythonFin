from datetime import datetime


class Note:
    
    def __init__(self, header, body, note_id):

        self.header = header
        self.body = body
        self.date_time = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        self.note_id = note_id

        
    def __setattr__(self, __name, __value):
        super().__setattr__(__name, __value)
   
        
    def __str__(self):
        return (f"\n\t---------------------------------"
                f"\n\tID: {self.note_id};"
                f"\n\tCreate date: {self.date_time};"
                f"\n\tHeader: {self.header};"
                f"\n\tBody: {self.body}"
                f"\n\t---------------------------------")
