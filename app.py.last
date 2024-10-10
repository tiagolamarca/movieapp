from flask import Flask, request, jsonify, render_template, redirect, url_for, flash, session
import requests
from database import get_connection

app = Flask(__name__)
app.secret_key = 'p@c3nT0s!Xyz89#R!fD2y@xC5h&7vQ1nA'

# Chave de API do The Movie DB
TMDB_API_KEY = 'd2b99c782375e6400be06c7a3f0650d6'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    data = request.form
    username = data['username']
    password = data['password']

    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
            cursor.execute(sql, (username, password))
        connection.commit()
        flash("Usuário registrado com sucesso!", "success")
    except Exception as e:
        print(e)
        flash("Falha no registro!", "error")
    finally:
        connection.close()

    return redirect(url_for('index'))

@app.route('/login', methods=['POST'])
def login():
    data = request.form
    username = data['username']
    password = data['password']

    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM users WHERE username = %s AND password = %s"
            cursor.execute(sql, (username, password))
            user = cursor.fetchone()

            if user:
                session['user_id'] = user[0]  # Armazena o ID do usuário na sessão
                return redirect(url_for('user_movies'))  # Redirecionar para a lista de filmes
            else:
                flash("Usuário ou senha inválidos!", "error")
    except Exception as e:
        print(e)
        flash("Falha ao realizar login!", "error")
    finally:
        connection.close()

    return redirect(url_for('index'))

@app.route('/movies', methods=['GET', 'POST'])
def movies():
    if 'user_id' not in session:
        return redirect(url_for('index'))

    if request.method == 'POST':
        search_query = request.form.get('search_query')
        response = requests.get(f'https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={search_query}')
        results = response.json().get('results', [])

        # Adiciona filmes à tabela 'movies' se não existirem
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                for movie in results:
                    movie_id = movie['id']
                    title = movie['title']
                    poster_path = movie['poster_path']

                    # Verifica se o filme já existe
                    cursor.execute("SELECT * FROM movies WHERE id = %s", (movie_id,))
                    if cursor.fetchone() is None:  # Se não existe, insere
                        cursor.execute("INSERT INTO movies (id, title, poster_path) VALUES (%s, %s, %s)", (movie_id, title, poster_path))
            connection.commit()
        except Exception as e:
            print("Erro ao inserir filmes na tabela:", e)
        finally:
            connection.close()

        return render_template('movies.html', movies=results)

    return render_template('movies.html')

@app.route('/movie/<int:movie_id>', methods=['GET'])
def movie_details(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}')
    if response.status_code != 200:
        return "Filme não encontrado", 404
    movie = response.json()
    return render_template('movie_details.html', movie=movie)

@app.route('/mark_movie', methods=['POST'])
def mark_movie():
    if 'user_id' not in session:
        return redirect(url_for('index'))

    user_id = session['user_id']
    movie_id = request.form.get('movie_id')
    status = request.form.get('status')

    print(f"User ID: {user_id}, Movie ID: {movie_id}, Status: {status}")  # Depuração

    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            # Verifica se o filme existe na tabela 'movies'
            cursor.execute("SELECT * FROM movies WHERE id = %s", (movie_id,))
            movie_exists = cursor.fetchone()

            if not movie_exists:
                flash("Filme não encontrado na lista!", "error")
                return redirect(url_for('user_movies'))

            # Verifica se o filme já foi marcado pelo usuário com o mesmo status
            check_sql = "SELECT * FROM user_movies WHERE user_id = %s AND movie_id = %s AND status = %s"
            cursor.execute(check_sql, (user_id, movie_id, status))
            existing_entry = cursor.fetchone()

            if existing_entry:
                session['warning_message'] = f"Você já marcou este filme como {status.upper()}!"
                return redirect(url_for('user_movies'))

            # Se o filme não foi marcado, insere a nova entrada
            sql = "INSERT INTO user_movies (user_id, movie_id, status) VALUES (%s, %s, %s)"
            cursor.execute(sql, (user_id, movie_id, status))
        connection.commit()
        flash("Filme marcado como " + status + " com sucesso!", "success")
    except Exception as e:
        print("Erro ao marcar o filme:", e)
        flash("Falha ao marcar o filme!", "error")
    finally:
        connection.close()

    return redirect(url_for('user_movies'))

@app.route('/user_movies', methods=['GET'])
def user_movies():
    if 'user_id' not in session:
        return redirect(url_for('index'))

    user_id = session['user_id']
    connection = get_connection()
    movies = []
    messages = []

    # Captura as mensagens de sucesso e aviso
    if 'success_message' in session:
        messages.append(session.pop('success_message'))  # Exibir e remover a mensagem de sucesso
    if 'warning_message' in session:
        messages.append(session.pop('warning_message'))  # Exibir e remover a mensagem de aviso

    try:
        with connection.cursor() as cursor:
            sql = """
                SELECT m.id, m.title, m.poster_path, um.status
                FROM user_movies um
                JOIN movies m ON um.movie_id = m.id
                WHERE um.user_id = %s
            """
            cursor.execute(sql, (user_id,))
            movies = cursor.fetchall()
    except Exception as e:
        print("Erro ao recuperar filmes:", e)

    return render_template('user_movies.html', movies=movies, messages=messages)

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash("Você saiu com sucesso!", "success")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

