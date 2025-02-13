from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuarios.db'  # Base de datos local
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '12345678'

db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    fecha_nacimiento = db.Column(db.String(10), nullable=False)
    genero = db.Column(db.String(10), nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        nombre = request.form['name']
        email = request.form['email']
        fecha_nacimiento = request.form['birthdate']
        genero = request.form['gender']
        
        nuevo_usuario = Usuario(nombre=nombre, email=email, fecha_nacimiento=fecha_nacimiento, genero=genero)
        db.session.add(nuevo_usuario)
        db.session.commit()
        flash('Usuario registrado con éxito', 'success')
        return redirect(url_for('usuarios'))
    return render_template('form.html')

@app.route('/usuarios')
def usuarios():
    usuarios = Usuario.query.all()
    return render_template("usuarios.html", usuarios=usuarios)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Crea la base de datos si no existe
    app.run(debug=True)