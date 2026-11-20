
from flask import Flask, render_template

app = Flask(__name__)

# Página principal de BioByte Systems
@app.route("/")
def inicio():
    return """
    <h1>BioByte Systems</h1>
    <p>Bienvenidos a BioByte Systems.</p>
    <p>Próximamente incorporaremos nuestros proyectos.</p>
    <a href="/degustaciones-en-monte">
        Visitar Degustaciones en Monte
    </a>
    """

# Sitio Degustaciones en Monte
@app.route("/degustaciones-en-monte")
def degustaciones():
    return render_template("inicio.html")


if __name__ == "__main__":
    app.run(debug=True)


