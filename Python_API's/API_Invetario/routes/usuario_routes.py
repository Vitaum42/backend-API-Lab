from fastapi import APIRouter, HTTPException
from models.usuario import Usuario
from services.usuario_service import *

router = APIRouter()

@router.post("/usuarios")
def criar(dados: Usuario):
    usuario = criar_usuario(dados)
    return {
        "mensagem": "Usuario criado com sucesso",
        "usuario": usuario
    }

@router.get("/usuarios")
def listar():
    return listar_usuarios()

@router.get("/usuarios/{usuario_id}")
def obter(usuario_id: int):
    usuario = obter_usuario(usuario_id)

    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario não encontrado")

    return usuario

@router.delete("/usuarios/{usuario_id}")
def deletar(usuario_id: int):
    deletado = deletar_usuario(usuario_id)

    if not deletado:
        raise HTTPException(status_code=404, detail="Usuario não encontrado")

    return {"mensagem": "Usuario deletado com sucesso"}

@router.put("/usuarios/{usuario_id}")
def atualizar(usuario_id: int, dados: Usuario):
    usuario = atualizar_usuario(usuario_id, dados)

    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario não encontrado")

    return {
        "mensagem": "Usuario atualizado com sucesso!",
        "usuario": usuario
    }