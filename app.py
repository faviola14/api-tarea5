from flask import Flask, jsonify, request

app = Flask(__name__)

tareas = [
    {"id": 1, "titulo": "Crear instancia EC2", "hecha": True},
    {"id": 2, "titulo": "Conectar por SSH", "hecha": False},
]

@app.route("/")
def inicio():
    return jsonify({"mensaje": "API funcionando en EC2"})

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/tareas", methods=["GET"])
def listar():
    return jsonify(tareas)

@app.route("/tareas", methods=["POST"])
def crear():
    datos = request.get_json()
    nueva = {
        "id": len(tareas) + 1,
        "titulo": datos.get("titulo", "sin título"),
        "hecha": False,
    }
    tareas.append(nueva)
    return jsonify(nueva), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)