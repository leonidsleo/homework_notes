import Addnote as add
import ShowAllNote as shl
import ToEditNote as e
import DeleteNotes as d
import DataFilter as dd
import SearchNoteHeading as s

def main():
    while True:
        print("\n")
        print("ВВЕДИТЕ:\n 1 - для создани новой заметки\n 2 - для вывода на экран всех заметок\n 3 - для изменения заметки\n 4 - для удаления заметки\n 5 - для вывода всех заметок по дате\n 6 - для поиска заметки по заголовку\n 7 - для выхода")
        print("\n")
        team = int(input("Введите команду, что необходимо сделать: "))
        
        if team == 1:
            add.new_note_fail()
        elif team == 2:
            shl.show_all_note()
        elif team == 3:
            e.to_edit_note()
        elif team == 4:
            d.delete_note()  
        elif team == 5:
            dd.data_filter_notes()
        elif team == 6:
            s.search_note_heading()
        elif team == 7:
            break   
        else:
            print(f"Неизвестная команда: {team}")

main()