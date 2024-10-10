from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configurações do banco de dados
DATABASE_URI = 'mysql+mysqlconnector://tiago:Jimi2022@localhost/movie'

# Cria a engine
engine = create_engine(DATABASE_URI)

# Cria a base declarativa
Base = declarative_base()

# Define o modelo de User
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String, nullable=False)

# Define o modelo de Movie
class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    poster_path = Column(String, nullable=False)

# Define o modelo de UserMovie
class UserMovie(Base):
    __tablename__ = 'user_movies'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    movie_id = Column(Integer, ForeignKey('movies.id'), nullable=False)
    status = Column(String(50), nullable=False)

# Cria as tabelas no banco de dados
def setup_database():
    Base.metadata.create_all(engine)
    print("Banco de dados e tabelas criados com sucesso!")

if __name__ == '__main__':
    setup_database()

