'''
pip install mysql-connector
pip install flask
python \.app.py
'''

from flask import Flask, render_template, request, redirect, url_for, session
from db_connection import get_db_connection
import pymysql
import hashlib

app = Flask(__name__)
app.secret_key = 'mi_secreto'  # Cambia esto por un valor seguro


@app.route('/')
def home():
    return redirect(url_for('dashboard'))


# Ruta para el dashboard


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/suscribirse')
def suscribirse():
    return render_template('suscribirse.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        correo = request.form['email']
        cel = request.form['Cel']
        horario = request.form['Horario']

        conn = get_db_connection()
        cursor = conn.cursor()

        # Insertar usuario en la base de datos
        query = "INSERT INTO users (nombre, apellido, correo, cel, horario) VALUES (%s, %s, %s, %s, %s)"
        try:
            cursor.execute(query, (nombre, apellido, correo, cel, horario))
            conn.commit()
            cursor.close()
            conn.close()
        except pymysql.connect.Error as err:
            return f"Error: {err}"

    return render_template('suscribirse.html')


if __name__ == '__main__':
    app.run(debug=True)
