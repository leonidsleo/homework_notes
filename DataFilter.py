import json
import Addnote as a

def data_filter_notes():
    
    filter_data = input("Введите дату за которую интересуют заметки (формат ввода: ГГГГ-ММ-ДД): ")
    print("\n")
    print("Заметки на запрашиваюмую дату:")
    try:
        with open(a.file_note, 'r', encoding="utf-8") as file:
            for f in file:
                n = json.loads(f.strip())
                if n['дата_заметки'].startswith(filter_data):
                    print(f"Дата: {n['дата_заметки']}, ID: {n['id']}, Заголовок: {n['заголовок']}, Заметка: {n['заметка']}, Дата: {n['дата_заметки']}")
                else:
                    print("Заметок на эту дату нет!")
                    break
    except FileExistsError:
        print("Заметок нет!")