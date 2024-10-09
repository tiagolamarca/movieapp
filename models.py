from db_setup import db

# Classe User para representar os usuários registrados
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    movies = db.relationship('Movie', backref='owner', lazy=True)

# Classe Movie para representar os filmes e o status (assistido, favoritos, etc.)
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    status = db.Column(db.String(50))  # 'watched', 'favorite', 'watchlist'
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
