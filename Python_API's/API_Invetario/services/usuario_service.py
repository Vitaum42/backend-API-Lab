def home():
    return {"message": "API em funcionamento!"}

usuarios = []
contador_id = 1

def criar_usuario(Dados_Usuario: usuarios): # type: ignore
    global contador_id

    #Oque sera armazenado para cada usuario criado, o id é gerado automaticamente
    Novo_Usuario = {
        "id": contador_id,
        "nome": Dados_Usuario.nome,
        "idade": Dados_Usuario.idade
    }

    usuarios.append(Novo_Usuario) #armazena o usuario na lista de usuarios
    contador_id += 1 #Adiciona automaticamente um id para cada usuario criado

    return Novo_Usuario

def listar_usuarios():
    return usuarios

def obter_usuario(usuario_id: int):
    for Usuario in usuarios:
        if Usuario["id"] == usuario_id:
            return Usuario
        
    return None

def deletar_usuario(usuario_id: int):
    for i in range(len(usuarios)):
        if usuarios[i]["id"] == usuario_id:
            usuarios.pop(i)
            return True
        
    return False

def atualizar_usuario(usuario_id: int, usuario_atualizado: usuarios): # type: ignore
    for i in range(len(usuarios)):
        if usuarios[i]["id"] == usuario_id:
            usuarios[i]["nome"] = usuario_atualizado.nome
            usuarios[i]["idade"] = usuario_atualizado.idade
            return usuarios[i]
    return None