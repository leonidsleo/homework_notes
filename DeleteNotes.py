import json
import ShowAllNote as shl
import Addnote as a

def delete_note():
    shl.show_all_note()
    id_note_delete = int(input("Введите id заметки которую хотите удалить: "))
    del_note = []
    deletes = False
    with open(a.file_note, "r", encoding="utf-8") as file:
        for f in file:
            note = json.loads(f.strip())
            if note['id'] != id_note_delete:
                del_note.append(note)
            else:
                deletes = True

    with open(a.file_note, 'w', encoding="utf-8") as file:
        for n in del_note:
            json.dump(n,file, ensure_ascii=False)
            file.write("\n")
    
    if deletes:
        print("Заметка удалена!")
    else:
        print("Заметки с таким id нет!")