from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
  return jsonify(message="Hello DevOps World!!")

@app.route("/health")
def health():
  return jsonify(status="Healthy")

if __name__ == "main":
  app.run(host="0.0.0.0", port=5000)
