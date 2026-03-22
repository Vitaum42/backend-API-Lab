🚀 Backend API Lab

Coleção de projetos de APIs back-end desenvolvidos com Java e Python, com foco em aprendizado e prática.

📌 Sobre

Este repositório contém projetos práticos voltados para a construção de APIs REST, com o objetivo de fortalecer habilidades em desenvolvimento back-end e entender conceitos utilizados no mercado.

🛠️ Tecnologias
Java (Spring Boot)
Python (FastAPI / Flask)
APIs REST
Git e GitHub
📚 O que você encontrará aqui
Implementações de CRUD
Estrutura de back-end (Controller, Service, Repository)
Integração com banco de dados (em projetos futuros)
Boas práticas e organização de código
🎯 Objetivo

Evoluir as habilidades em desenvolvimento back-end e construir uma base sólida para aplicações reais.

📈 Status

🚧 Em desenvolvimento — novos projetos serão adicionados continuamente.
---
🚀 Guia Completo

Este documento reúne **todos os comandos de terminal (Bash)** utilizados durante a criação da API com FastAPI, além de explicar os principais **métodos HTTP (GET, POST, etc.)** de forma clara e prática.

---

# 📦 1. Configuração do Ambiente

## 🔹 Criar pasta do projeto

```bash
mkdir nome-do-projeto
cd nome-do-projeto
```

## 🔹 Criar ambiente virtual (venv)

```bash
python -m venv venv
```

## 🔹 Ativar ambiente virtual

### Windows:

```bash
venv\Scripts\activate
```

### Linux/Mac:

```bash
source venv/bin/activate
```

## 🔹 Atualizar o pip

```bash
pip install --upgrade pip
```

## 🔹 Instalar FastAPI e Uvicorn

```bash
pip install fastapi uvicorn
```

---

# ▶️ 2. Rodando a API

## 🔹 Executar o servidor

```bash
uvicorn main:app --reload
```

### Explicação:

* `main`: nome do arquivo (main.py)
* `app`: nome da instância do FastAPI
* `--reload`: reinicia automaticamente ao salvar alterações

---

# 🧪 3. Testando a API

## 🔹 Acessar no navegador:

```
http://127.0.0.1:8000
```

## 🔹 Documentação automática:

* Swagger UI:

```
http://127.0.0.1:8000/docs
```

* Redoc:

```
http://127.0.0.1:8000/redoc
```

---

# 📁 4. Estrutura básica

```bash
.
├── venv/
├── main.py
└── README.md
```

---

# 🔄 5. Métodos HTTP (ESSENCIAL)

Esses são os “tipos de operação” que sua API pode fazer.

---

## 🟢 GET → Buscar dados

Usado para **ler informações**.

### Exemplo:

```python
@app.get("/")
def home():
    return {"mensagem": "Olá mundo"}
```

📌 Características:

* Não altera dados
* Pode ser chamado várias vezes sem problema
* Usado para consultas

---

## 🔵 POST → Criar dados

Usado para **enviar dados e criar algo novo**.

### Exemplo:

```python
@app.post("/usuarios")
def criar_usuario(usuario: dict):
    usuarios.append(usuario)
    return usuario
```

📌 Características:

* Cria novos registros
* Envia dados no corpo (body)
* Pode duplicar dados se não houver controle

---

## 🟡 PUT → Atualizar (substituir tudo)

Usado para **atualizar um recurso inteiro**.

### Exemplo:

```python
@app.put("/usuarios/{id}")
def atualizar_usuario(id: int, usuario: dict):
    usuarios[id] = usuario
    return usuario
```

📌 Características:

* Substitui todos os dados
* Precisa enviar o objeto completo

---

## 🟠 PATCH → Atualizar parcialmente

Usado para **alterar apenas alguns campos**.

### Exemplo:

```python
@app.patch("/usuarios/{id}")
def atualizar_parcial(id: int, dados: dict):
    usuarios[id].update(dados)
    return usuarios[id]
```

📌 Características:

* Atualiza só o necessário
* Mais eficiente que PUT em muitos casos

---

## 🔴 DELETE → Remover dados

Usado para **deletar um recurso**.

### Exemplo:

```python
@app.delete("/usuarios/{id}")
def deletar_usuario(id: int):
    usuarios.pop(id)
    return {"msg": "Usuário removido"}
```

📌 Características:

* Remove dados permanentemente
* Deve ser usado com cuidado

---

# 🧠 6. Conceitos importantes que você usou

## 🔹 Rota (Endpoint)

É o “caminho” da API.

Exemplo:

```
/usuarios
/usuarios/{id}
```

---

## 🔹 Path Parameter

Valor dinâmico na URL.

```python
@app.get("/usuarios/{id}")
```

---

## 🔹 Body (corpo da requisição)

Dados enviados no POST/PUT/PATCH.

---

## 🔹 JSON

Formato padrão de comunicação da API.

Exemplo:

```json
{
  "nome": "João",
  "idade": 20
}
```

---

# ⚠️ 7. Observações importantes

* Não pode ter duas rotas iguais com o mesmo método:

```python
@app.get("/") ❌ duplicado dá erro
```

* Use listas ou banco de dados para armazenar múltiplos usuários:

```python
usuarios = []
```

* Sempre que adicionar algo:

```python
usuarios.append(novo_usuario)
```

---

# 🏁 Conclusão

Você já construiu uma API com:

* CRUD completo (Create, Read, Update, Delete)
* Estrutura funcional
* Testes via navegador
* Documentação automática

---

Se quiser evoluir agora, próximos passos naturais:

* Validação com Pydantic
* Separar rotas em arquivos
* Conectar com banco de dados (SQLite/PostgreSQL)
* Dockerizar a aplicação

---

Se quiser, posso montar o próximo nível contigo passo a passo.

