from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Demo Day DevOps: Aplicação rodando de forma independente em container.\n"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
