from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 🚨 ATENÇÃO: Substitua pelos dados do seu MySQL local!
# Formato: mysql+pymysql://USUARIO:SENHA@localhost:3306/NOME_DO_BANCO
URL_DO_BANCO = "mysql+pymysql://root:""@localhost:3306/reservas_ambientes"

# Cria o "motor" que vai gerenciar a comunicação com o banco
engine = create_engine(URL_DO_BANCO)

# Cria a fábrica de sessões (cada vez que alguém acessa a API, abrimos uma sessão)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# A classe base que nossas tabelas (models) vão herdar
Base = declarative_base()

# Função para entregar a conexão para as rotas da API e fechar depois do uso
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()