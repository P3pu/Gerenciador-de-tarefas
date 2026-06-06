import json
import datetime
db_file = "./tasks.json"
x = datetime.datetime.now()
date = x.strftime("%Y/%m/%d")

def menu():
        try:
                     print(" ======== Gerenciador de Tarefas ======== \n")
                     print(
                     "1 - Adicionar tarefa\n" 
                     "2 - Listar tarefas\n"
                     "3 - Marcar tarefa como concluída\n"
                     "4 - Remover tarefa\n"
                     "5 - Buscar tarefa\n"
                     "6 - Sair\n"
        )
                     return
        except:
               print("Error ao mostrar menu")
              

# CREATE
def add_task():
       try:
                      titulo = input("\nTitulo da tarefa:\n")
                      tarefas = read_task()

                      tarefa = {
                      "id": len(tarefas)+1,
                      "titulo": titulo,
                      "progresso":"pendente",
                      "created_at": date
                      }

                      tarefas.append(tarefa)
                      save_task(tarefas)
                      print("Tarefa salva com sucesso!")
                      return

       except:
              print("Error ao salvar tarefa!")
              return 

#READ
def read_task():
    try:
        with open(db_file, "r", encoding='utf-8') as file:
            return json.load(file)  
    except (FileNotFoundError, json.JSONDecodeError):
        return []
        
def list_task():
       try:
              with open(db_file,"r",encoding='utf-8') as file:
               formato_list = json.load(file)
               for x in formato_list:
                     print(f"[{x["id"]}] {x["titulo"].upper()} - {x["progresso"]} | {x['created_at']} ")
              return
       except:
              print("Não há nenhuma tarefa")
              return

def save_task(dados):
       try:
                     with open(db_file,"w",encoding='utf-8') as file:
                            json.dump(dados,file,indent=4)
                     return
       except:
              print("Error ao salvar tarefa")
              return
       
def search_id_task(tarefas,id_buscado):
       try:
                     for tarefa in tarefas:
                            if tarefa["id"] == id_buscado:
                             return tarefa
       except:
              print("Id não encontrado")
              return None


def search_text_task(tarefas,text):
       try:
               new_tarefas = []
               for tarefa in tarefas:
                     if text.lower() in tarefa['titulo'].lower():
                            new_tarefas.append(tarefa)
        
               if len(new_tarefas) > 0:
                     return new_tarefas
       except:
              print("nenhuma tarefa encontrada!")
              return None
       
#DELETE
def delete_task():
       try:
              id = int(input("Digite o id da terefa:\n"))
              tarefas = read_task()
              id_task = search_id_task(tarefas,id)
              nova_tarefas = []
              if id_task:
                     for x in tarefas:
                            if x["id"] != id_task["id"]:
                                   nova_tarefas.append(x)
        
              print(f"Tarefa removida: {id_task}")
              save_task(nova_tarefas)
              return

       except:
              print("tarefa não encontrada")
              return 

def mark_task():
       try:
                     id = int(input("Digite o id da tarefa:\n"))
                     progresso = input("(Pendente | Andamento | Finalizado) - Qual progresso Deseja atribuir?\n")
                     tarefas = read_task()
                     id_task = search_id_task(tarefas,id)
                     if id_task:
                            id_task["progresso"] = progresso
                     save_task(tarefas)
                     return
       except: 
              print("tarefa não encontrada")

def search_task():
       try:
              termo = input("Digite o termo:")
              tarefas = read_task()
              search = search_text_task(tarefas,termo)
              for x in search:
                     print(f"[{x["id"]}] {x["titulo"].upper()} - {x["progresso"]} ")
              return
       except:
              print("termo não encontrado!")



                
        
        
                

              
       
       
       
        
            


