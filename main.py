from functions import menu,add_task,list_task,delete_task,mark_task,search_task

game = True
menu()


while game:
    opt = int(input("\nEscolha uma opção:\n"))
    
    match opt:
        case 1:
            add_task()
            menu()
        case 2:
            list_task()
            menu()
        case 3:
            mark_task()
            menu()
        case 4:
            delete_task()
            menu()
        case 5:
            search_task()
            menu()
        case 6: 
            print("Saindo...")
            game = False
        case _:
             print("=== Numero errado ===\n")
             menu()


