import json
import Addnote as a

def data_filter_notes():
    filter_data = input("Введите дату за которую интересуют заметки (формат ввода: ГГГГ-ММ-ДД): ")
    try:
        with open(a.file_note, 'r', encoding="utf-8") as file:
            for f in file:
                n = json.loads(f.strip())
                if n['дата_заметки'].startswith(filter_data):
                    print(n['дата_заметки'], n['id'])
    except FileExistsError:
        print("Заметок на эту дату нет!")