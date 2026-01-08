import os
import psycopg2
from flask import Flask

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host="db",
        database=os.environ['POSTGRES_DB'],
        user=os.environ['POSTGRES_USER'],
        password=os.environ['POSTGRES_PASSWORD']
    )
    return conn

@app.route('/')
def index():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT version();')
        db_version = cur.fetchone()
        cur.close()
        conn.close()
        return f"<h1>Успех! 🚀</h1><p>Python подключился к базе данных:</p><p>{db_version}</p>"
    except Exception as e:
        return f"<h1>Ошибка :(</h1><p>{e}</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
