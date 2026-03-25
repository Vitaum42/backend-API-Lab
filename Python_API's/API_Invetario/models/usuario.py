from pydantic import BaseModel

#Criando uma classe de Usuario (oque sera solicitado ao cliente para preenchimento)
class Usuario(BaseModel):
    nome: str
    idade: int