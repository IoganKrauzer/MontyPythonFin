from noteBook import *
from note import Note
from generateID import GenerateID
import os
os.system('cls')


notebook = Notebook()
RUN = True


def create_note():
    print("Создание заметки...")
    note = Note(input("Заголовок: "), input("Содеражание: "), GenerateID.generate_id())
    notebook.add_note(note)
    print("Заметки успешно создана")
    save_notebook()


def show_all():
    for x in notebook.list:
        print(x)


def edit_note():
    print("Режим правки...")
    try:
        note_edit_id = int(input("\nВведите ID заметки для правки: "))
        notebook.show_note(note_edit_id)
        notebook.edit_note(note_edit_id)
        save_notebook()
    except ValueError:
        print("Такого ID нет...")


def delete_note():
    print("Удаление заметки...")
    try:
        note_delete_id = int(input("\nВведите ID заметки на удаление: "))
        notebook.remove_note(note_delete_id)
    except ValueError:
        print("Такого ID нет...")


def save_notebook():
    notebook.save_notebook()


def load_notebook():
    notebook.load_notebook()


while RUN:
    print("\n\tМеню записной книжки:"
    "\n\t1 - create note"
    "\n\t2 - edit note"
    "\n\t3 - delete note"
    "\n\t4 - show all"
    "\n\t5 - load notes"
    "\n\t0 - exit program")

    command = input()

    match command:
        case "1":
            create_note()
        case "2":
            edit_note()
        case "3":
            delete_note()
        case "4":
            show_all()
        case "5":
            load_notebook()
        case "0":
            print("Закрытие...")
            RUN = False
        case _:
            print("Неверная команда")