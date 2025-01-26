from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Necesario para usar `flash` mensajes

# Página principal
@app.route("/")
def index():
    return render_template("index.html")

# Página con formulario avanzado
@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        # Validación de datos
        name = request.form.get("name")
        email = request.form.get("email")
        age = request.form.get("age")
        password = request.form.get("password")
        gender = request.form.get("gender")
        terms = request.form.get("terms")

        # Validaciones básicas en el servidor
        if not name or not email or not age or not password or not gender or terms != "on":
            flash("Por favor, llena todos los campos correctamente.")
            return redirect(url_for("form"))
        
        if not email.endswith("@example.com"):
            flash("El correo electrónico debe pertenecer al dominio @example.com.")
            return redirect(url_for("form"))
        
        # Si todo es válido, redirigir a la página de inicio
        flash("¡Formulario enviado correctamente!")
        return redirect(url_for("index"))
    return render_template("form.html")

# Página de error personalizada
@app.errorhandler(404)
def page_not_found(e):
    return render_template("error.html", error="Página no encontrada"), 404

if __name__ == "__main__":
    app.run(debug=True)