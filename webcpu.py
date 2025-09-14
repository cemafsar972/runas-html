from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import os

app = Flask(__name__)
CORS(app)  # Webden erişim için şart

@app.route("/run", methods=["POST"])
def run_command():
    data = request.json
    cmd = data.get("cmd")

    if not cmd:
        return jsonify({"error": "Komut eksik"}), 400

    try:
        result = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        return jsonify({"output": result})
    except subprocess.CalledProcessError as e:
        return jsonify({"error": e.output}), 500
@app.route("/cwd", methods=["GET"])
def get_cwd():
    import os
    return jsonify({"cwd": os.getcwd()})
if __name__ == "__main__":
    app.run(port=5000)