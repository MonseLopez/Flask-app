from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Página principal
@app.route("/")
def index():
    return render_template("index.html")

# Página con formulario
@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        # Validación de datos (servidor)
        name = request.form.get("name")
        age = request.form.get("age")
        if not name or not age.isdigit():
            error = "Por favor, ingresa un nombre y una edad válidos."
            return render_template("form.html", error=error)
        return redirect(url_for("index"))
    return render_template("form.html")

# Página de error personalizada
@app.errorhandler(404)
def page_not_found(e):
    return render_template("error.html", error="Página no encontrada"), 404

# Ejecutar la aplicación
if __name__ == "__main__":
    app.run(debug=True)

