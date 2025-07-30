# Importa os módulos necessários do Flask
from flask import Blueprint, request, jsonify

# Importa a instância do banco de dados (SQLAlchemy)
from extensions import db

# Importa o modelo de dados Task
from models import Task

# Cria um "Blueprint" para agrupar as rotas relacionadas às tarefas
# Isso permite organizar o código em módulos
task_bp = Blueprint('task_bp', __name__)

# Rota para listar todas as tarefas (GET /tasks)
@task_bp.route('/tasks', methods=['GET'])
def get_tasks():
    # Busca todas as tarefas no banco de dados
    tasks = Task.query.all()
    # Converte cada tarefa para dicionário e retorna em formato JSON
    return jsonify([task.to_dict() for task in tasks])

# Rota para adicionar uma nova tarefa (POST /tasks)
@task_bp.route('/tasks', methods=['POST'])
def add_task():
    # Pega os dados enviados no corpo da requisição (espera JSON)
    data = request.json

    # Cria uma nova tarefa com o título recebido
    new_task = Task(title=data['title'])

    # Adiciona a nova tarefa ao banco de dados
    db.session.add(new_task)
    db.session.commit()

    # Retorna a nova tarefa criada em formato JSON e status 201 (Created)
    return jsonify(new_task.to_dict()), 201

# Rota para marcar uma tarefa como concluída (PUT /tasks/<id>)
@task_bp.route('/tasks/<int:task_id>', methods=['PUT'])
def complete_task(task_id):
    # Busca a tarefa pelo ID ou retorna erro 404 se não existir
    task = Task.query.get_or_404(task_id)

    # Marca a tarefa como concluída
    task.completed = True
    db.session.commit()

    # Retorna a tarefa atualizada em JSON
    return jsonify(task.to_dict())

# Rota para deletar uma tarefa (DELETE /tasks/<id>)
@task_bp.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    # Busca a tarefa pelo ID ou retorna erro 404 se não existir
    task = Task.query.get_or_404(task_id)

    # Remove a tarefa do banco
    db.session.delete(task)
    db.session.commit()

    # Retorna uma resposta vazia com status 204 (No Content)
    return '', 204
