# Importa a classe SQLAlchemy, que será usada como ORM na aplicação
from flask_sqlalchemy import SQLAlchemy

# Cria uma instância global do SQLAlchemy
# Isso permite que a mesma instância seja usada em vários arquivos (como app.py, models.py, etc.)
db = SQLAlchemy()
