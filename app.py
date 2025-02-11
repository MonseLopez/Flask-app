from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        birthdate = request.form.get('birthdate')
        gender = request.form.get('gender')

        # Validación: Si falta algún campo, muestra error 400
        if not name or not email or not birthdate or not gender:
            return render_template("400.html"), 400  # Error 400 - Bad Request

        return render_template("success.html", name=name)

    return render_template("form.html")

# Manejo de errores personalizados
@app.errorhandler(400)
def bad_request_error(error):
    return render_template("400.html"), 400

@app.errorhandler(404)
def not_found_error(error):
    return render_template("404.html"), 404

@app.errorhandler(500)
def internal_server_error(error):
    return render_template("500.html"), 500

if __name__ == '__main__':
    app.run(debug=True)
