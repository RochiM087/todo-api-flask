from flask import Flask, render_template
from extensions import db
from routes import task_bp
import models  # importa o modelo para garantir que a tabela Task seja registrada

# Inicializa a aplicação Flask
app = Flask(__name__)

# Configuração do banco de dados SQLite, que será salvo no arquivo 'database.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

# Desativa o warning do SQLAlchemy relacionado a mudanças de rastreamento — boa prática
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa a extensão do SQLAlchemy com a app Flask
db.init_app(app)

# Registra o blueprint com as rotas da API (GET, POST, PUT, DELETE de tarefas)
app.register_blueprint(task_bp)

# Rota principal que renderiza a interface HTML com a lista de tarefas
@app.route('/')
def index():
    return render_template('index.html')

# Bloco principal da aplicação — executa se o arquivo for rodado diretamente
if __name__ == '__main__':
    # Garante que o contexto da app está ativo ao criar o banco/tabela se ainda não existir
    with app.app_context():
        db.create_all()  # Cria a tabela 'Task' no banco de dados se ela não existir ainda
    # Roda o servidor Flask em modo de desenvolvimento
    app.run(debug=True)
