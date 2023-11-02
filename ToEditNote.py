import json
import ShowAllNote as shl
import Addnote as a
import datetime

def to_edit_note():
    shl.show_all_note()
    id_note_edit = int(input("Введите id заметки которую хотите изменить: "))
    edit_note = []
    edits = False
    with open (a.file_note, "r", encoding="utf-8") as file:
        for f in file:
            note = json.loads(f.strip())
            if note['id'] == id_note_edit:
                # id = a.counter_note()
                heading = input("Введите новый заголовок или оставьте пустым, что бы не менять: ")
                msg = input("Введите новый текст заметки или оставьте пустым, что бы не менять: ")
                note['id'] = id_note_edit
                note['заголовок'] = heading if heading else note['заголовок']
                note['заметка'] = msg if msg else note['заметка']
                note['дата_заметки'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                edits = True
            edit_note.append(note)
                
    with open(a.file_note, 'w', encoding="utf-8") as file:
        for notes in edit_note:
            json.dump(notes, file, ensure_ascii=False)
            file.write("\n")
    if edits:
        print("Заметка успешно отредактирована!")
    else:
        print("Заметки с таким id нет!")
