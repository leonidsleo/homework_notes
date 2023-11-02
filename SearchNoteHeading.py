import json
import Addnote as a

def search_note_heading():
    search_note = input("Введите заголовок для поиска: ")
    print("\n")
    print("Заметки с заголовком: ")
    try:
        with open(a.file_note, 'r', encoding="utf-8") as file:
            for f in file:
                n = json.loads(f.strip())
                if n['заголовок'] == search_note:
                    print(f"ЗАГОЛОВОК: {n['заголовок']}\nID: {n['id']}\nЗАМЕТКА: {n['заметка']}\nДАТА: {n['дата_заметки']}")
                    break
            else:
                print("Заметки с таким заголовком нет!")
    except FileExistsError:
        print("упс. Заметок еще нет!")