import json
class MyNote:
    def __init__(self, id, title, note, date, time):
        self.id = id
        self.title = title
        self.note = note
        self.date = date
        self.time = time
class MyNoteEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, MyNote):
            return {"id": obj.id, "title": obj.title, "note": obj.note, "date": obj.date, "time": obj.time}
        return json.JSONEncoder.default(self, obj)