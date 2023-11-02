# from Addnote import file_note
import Addnote as a
import json

def show_all_note():
    try:
        print("\n")
        print("Ваши заметки: ")
        with open(a.file_note, 'r', encoding="utf-8") as file:
            for f in file:
                note = json.loads(f.strip())
                print(note)
    except FileExistsError:
        print("Заметок нет!")
