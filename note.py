import json
class MyNote:
    def __init__(self, id, title, note, date, time):
        self.id = id
        self.title = title
        self.note = note
        self.date = date
        self.time = time
    def from_json(self, jsonnote):
        self.id = jsonnote['id']
        self.title = jsonnote['title']
        self.note = jsonnote['note']
        self.date = jsonnote['date']
        self.time = jsonnote['time']
    def to_json(self):
        return json.dump(self)
