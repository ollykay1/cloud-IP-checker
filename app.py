from flask import Flask, render_template, request
from utils.ip_lookup import lookup_ip

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/lookup", methods=["POST"])
def lookup():
    ip = request.form.get("ip")
    result = lookup_ip(ip)
    return render_template("result.html", result=result, ip=ip)

if __name__ == "__main__":
    app.run(debug=True)