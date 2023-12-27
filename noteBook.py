import json
from customEncoder import CustomEncoder
from note import Note
from datetime import datetime
from pathlib import Path
import os


                
                
class Notebook:

    def __init__(self):
        self.list = list()
        self.is_first_start()


    def add_note(self, note):
        self.list.append(note)


    def remove_note(self, note_id):
        for note in self.list:
            if note.__getattribute__("note_id") == note_id:
                if len(self.list) == 1:
                    self.init_database()
                self.list.remove(note)
        self.save_notebook()


    def edit_note(self, note_id):
        for note in self.list:
            if note.__getattribute__("note_id") == note_id:
                command = input("\n\t1 - edit header"
                                "\n\t2 - edit body")
                
                if command != "1" and command != "2":
                    print("Неверная команда")
                match command:
                    case "1":
                        new_header = input("\nВведите новый заголовок: ")
                        note.__setattr__("header", new_header)
                        note.__setattr__("datetime", str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
                    case "2":
                        new_body = input("\nВведите новое содержание: ")
                        note.__setattr__("body", new_body)
                        note.__setattr__("datetime", str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))


    def show_note(self, note_id):
        for note in self.list:
            if note.__getattribute__("note_id") == note_id:
                print(note)


    def save_notebook(self):
        with open("data.json", "w") as file:
            json.dump(self.list, file, cls=CustomEncoder)


    def load_notebook(self):
        db_path = Path("data.json")
        is_blank = db_path.stat().st_size == 0
        if is_blank:
            print("Записная книжка пуста.")
        else:
            with open(db_path, "r") as file:
                json_input = json.load(file)
                if json_input == '0' or len(json_input) == 0:
                    print("Записная книжка пуста.")
                else:
                    dict_keys = json_input[0].keys()
                    temp_list = list()
                    for x in range(len(json_input)):
                        temp_note = Note(None, None, 0)
                        for y in dict_keys:
                            temp_note.__setattr__(y, json_input[x][y])
                        temp_list.append(temp_note)
                        self.list = temp_list
                    print("Заметка загружена.")


    def init_database(self):
        default_db_value = "0"
        with open("data.json", "w") as db:
            db.seek(0)
            json.dump(default_db_value, db)
        with open("ids.json", "w") as id_db:
            id_db.seek(0)
            json.dump(default_db_value, id_db)


    def is_first_start(self):
        is_data_base_exists = os.path.exists("data.json")
        is_id_data_base_exists = os.path.exists("ids.json")
        if not is_id_data_base_exists and not is_data_base_exists:
            self.init_database()


