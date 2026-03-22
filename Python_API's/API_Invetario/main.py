from fastapi import FastAPI
from pydantic import BaseModel

#Para iniciar a API, use no bash o comando abaixo:
#uvicorn main:app --reload
app = FastAPI()

#Criando uma classe de Usuario (oque sera solicitado ao cliente para preenchimento)
class usuario(BaseModel):
    nome: str
    idade: int

#criar uma lista para armazenar os usuarios
usuarios = []
contador_id = 1

@app.get("/")
def home():
    return {"message": "API em funcionamento!"}

#Criar um endpoint para criar um usuario
@app.post("/usuarios")
def criar_usuario(usuario: usuario):
    global contador_id

    #Oque sera armazenado para cada usuario criado, o id é gerado automaticamente
    novo_usuario = {
        "id": contador_id,
        "nome": usuario.nome,
        "idade": usuario.idade
    }

    usuarios.append(novo_usuario) #armazena o usuario na lista de usuarios
    contador_id += 1 #Adiciona automaticamente um id para cada usuario criado

    return {
        "mensagem": "Usuario criado com sucesso!",
            "usuario": novo_usuario
            }

#Lista os Usuarios na lista Usuarios
@app.get("/usuarios")
def listar_usuarios():
    return usuarios