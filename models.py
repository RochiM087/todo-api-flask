from extensions import db  # Importa a instância global do SQLAlchemy

# Define a classe 'Task' como modelo de dados (tabela do banco de dados)
class Task(db.Model):
    # Coluna 'id' — chave primária, valor inteiro autoincrementável
    id = db.Column(db.Integer, primary_key=True)

    # Coluna 'title' — armazena o título da tarefa, obrigatório (nullable=False)
    title = db.Column(db.String(100), nullable=False)

    # Coluna 'completed' — indica se a tarefa foi concluída ou não (bool), começa como False
    completed = db.Column(db.Boolean, default=False)

    # Método utilitário para transformar o objeto em um dicionário (usado para retornar JSON)
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'completed': self.completed
        }
