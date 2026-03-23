from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel

#Para iniciar a API, use no bash o comando abaixo:
#uvicorn main:app --reload
app = FastAPI()

#Criando uma classe de Usuario (oque sera solicitado ao cliente para preenchimento)
class Usuario(BaseModel):
    nome: str
    idade: int

#criar uma lista para armazenar os usuarios
Usuarios = []
contador_id = 1

@app.get("/")
def home():
    return {"message": "API em funcionamento!"}

#Criar um endpoint para criar um usuario
@app.post("/Usuarios")
def criar_usuario(Dados_Usuario: Usuario):
    global contador_id

    #Oque sera armazenado para cada usuario criado, o id é gerado automaticamente
    Novo_Usuario = {
        "id": contador_id,
        "nome": usuario.nome,
        "idade": usuario.idade
    }

    Usuarios.append(Novo_Usuario) #armazena o usuario na lista de usuarios
    contador_id += 1 #Adiciona automaticamente um id para cada usuario criado

    return {
        "mensagem": "Usuario criado com sucesso!",
            "usuario": Novo_Usuario
            }

#Lista os Usuarios na lista Usuarios
@app.get("/usuarios")
def listar_usuarios():
    return Usuarios


@app.get("/usuarios/{usuario_id}")
def obter_usuario(usuario_id: int):
    for Usuario in Usuarios:
        if Usuario["id"] == usuario_id:
            return Usuario
        
    raise HTTPException(status_code=404, detail="Usuario não encontrado")

@app.delete("/usuarios/{usuario_id}")
def deletar_usuario(usuario_id: int):
    for i in range(len(Usuarios)):
        if Usuarios[i]["id"] == usuario_id:
            Usuarios.pop(i)
            return {"mensagem": "Usuario deletado com sucesso!"}
        
    raise HTTPException(status_code=404, detail="Usuario não encontrado")

@app.put("/usuarios/{usuario_id}")
def atualizar_usuario(usuario_id: int, usuario_atualizado: Usuario):
    for i in range(len(Usuarios)):
        if Usuarios[i]["id"] == usuario_id:
            Usuarios[i]["nome"] = usuario_atualizado.nome
            Usuarios[i]["idade"] = usuario_atualizado.idade
            return {"mensagem": "Usuario atualizado com sucesso!", "usuario": Usuarios[i]}
        
    raise HTTPException(status_code=404, detail="Usuario não encontrado")