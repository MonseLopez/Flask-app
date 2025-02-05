from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/form', methods=['POST'])
def form():
    name = request.form.get('name')
    email = request.form.get('email')
    birthdate = request.form.get('birthdate')
    gender = request.form.get('gender')

    # Validación: Si falta algún campo, redirige a error 400
    if not name or not email or not birthdate or not gender:
        return render_template("400.html"), 400  # Retorna código de error 400 (Bad Request)

    return render_template("success.html", name=name)

@app.errorhandler(400)
def bad_request_error(error):
    return render_template("400.html"), 400

if __name__ == '__main__':
    app.run(debug=True)
