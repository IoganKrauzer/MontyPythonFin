import json
from customEncoder import CustomEncoder
from note import Note
from datetime import datetime
from pathlib import Path
import os

class GenerateID:
    
    def generate_id() -> int:
        id_db_path = Path("ids.json")
        db_path = Path("data.json")
        with open(db_path, "r+") as db:
            json_read = json.load(db)
            if len(json_read) > 0 and json_read != '0':
                identifiers_list = list()
                for i in range(len(json_read)):
                    identifiers_list.append(json_read[i]["note_id"])
                available_id = int(max(identifiers_list) + 1)
                with open(id_db_path, "w") as id_db:
                    json.dump(available_id, id_db)
                return int(available_id)

            else:
                with open(id_db_path, "r+") as file:
                    id_db = json.load(file)
                    if id_db == "0":
                        file.seek(0)
                        json.dump("1", file)
                        return 1
                    else:
                        available_id = int(id_db) + 1
                        file.seek(0)
                        json.dump(str(available_id), file)
                        return available_id