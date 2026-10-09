from flask import Flask

app = Flask(_name_)


@app.route("/")
def home():
    return "Hello from Jenkins AWS DevOps Lab!"


@app.route("/health")
def health():
    return "OK"


if _name_ == "_main_":
    app.run(host="0.0.0.0", port=5000)
