# 📝 Lista de Tarefas - Aplicação Flask

Uma aplicação web interativa e responsiva para gerenciamento de tarefas, desenvolvida com **Python (Flask)** e **SQLite**, utilizando uma **API RESTful completa** com frontend em **HTML, CSS e JavaScript puro**.

---

## 📌 Funcionalidades

✅ Adicionar uma nova tarefa
✅ Listar todas as tarefas
✅ Marcar tarefa como **concluída**
✅ Marcar tarefa como **não concluída**
✅ Remover tarefa
✅ Interface web moderna e responsiva
✅ Botão para atualizar lista manualmente
✅ Notificações e feedbacks visuais

---

## 🚀 Tecnologias Utilizadas

- **Python 3.10+**
- **Flask**
- **Flask-SQLAlchemy**
- **SQLite** (banco local e persistente)
- HTML5, CSS3, JavaScript
- Estrutura modular (rotas, modelos, configuração separados)

---

## 📁 Estrutura do Projeto

```
todo-api-flask/
├── app.py               # Inicialização da aplicação Flask
├── models.py            # Modelo de dados (ORM com SQLAlchemy)
├── routes.py            # API RESTful com todos os endpoints
├── extensions.py        # Extensões compartilhadas (SQLAlchemy)
├── templates/
│   └── index.html       # Interface HTML
├── static/
│   └── style.css        # Estilo da interface
├── requirements.txt     # Dependências da aplicação
├── .gitignore           # Arquivos ignorados pelo Git
└── README.md            # Este arquivo
```

---

## 🛠️ Como rodar a aplicação localmente

### 1. Clone o repositório

```bash
git clone https://github.com/RochiM087/todo-api-flask.git
cd todo-api-flask
```

### 2. Crie e ative o ambiente virtual (opcional, mas recomendado)

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate    # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute a aplicação

```bash
python app.py
```

Acesse no navegador: [http://localhost:5000](http://localhost:5000)

---

## 📡 Endpoints da API (REST)

| Método | Rota            | Ação                              |
| ------- | --------------- | ----------------------------------- |
| GET     | `/tasks`      | Lista todas as tarefas              |
| POST    | `/tasks`      | Adiciona nova tarefa                |
| PUT     | `/tasks/<id>` | Alterna o status (feito/não feito) |
| DELETE  | `/tasks/<id>` | Remove a tarefa                     |

---

## 🧠 Critérios Atendidos

### ✅ Funcionalidade

Todos os requisitos foram implementados:

- [X] CRUD completo (criar, listar, atualizar, remover tarefas)
- [X] Persistência em banco de dados local
- [X] API RESTful
- [X] Interface completa, responsiva e funcional

### ✅ Qualidade do Código

- Código modular e organizado (`app.py`, `routes.py`, `models.py`)
- Separação entre responsabilidades
- Comentários e nomes claros

### ✅ Persistência de Dados

- Todas as tarefas são armazenadas de forma persistente no banco `SQLite` (`database.db`);
- Uso do ORM SQLAlchemy para abstração e segurança.

### ✅ Documentação

- Código comentado quando necessário
- README completo com instruções, funcionalidades e estrutura
- `.gitignore` configurado corretamente

---

## 📦 Observações

- O banco de dados utilizado é **SQLite**, ideal para desenvolvimento local;
- Caso deseje usar PostgreSQL, o projeto pode ser facilmente adaptado trocando a string de conexão;
- Ambiente testado em **Ubuntu 22.04** com **Python 3.10**.

---

## 👨‍💻 Desenvolvedor

**Bruno Rodrigues**
🔗 [GitHub - @RochiM087](https://github.com/RochiM087)
🔗 [LinkedIn - Bruno Rodrigues](https://linkedin.com/in/bruno-rodrigues-858018209)
