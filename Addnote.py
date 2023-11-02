import json
import datetime

id = 1
def counter_note():
    global id
    id += 1
    return id

def save_note_file(heading, msg):
    date_note = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    id = counter_note()
    note = {
        'id' : id,
        'заголовок': heading,
        'заметка': msg,
        'дата_заметки': date_note
    }
    with open(file_note, 'a', encoding="utf-8") as file:
        json.dump(note, file, ensure_ascii=False)
        file.write("\n")

def new_note_fail():
    heading = input("Введите заголовок заметки: ")
    msg = input("Введите текст заметки: ")
    save_note_file(heading, msg)
    print("Заметка успешно сохранена")

file_note = "notes.json" 