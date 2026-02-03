from flask import Flask, request, jsonify, render_template

app = Flask(__name__) # this constructs a web app, which Flask references

@app.get("/")
def home():
    return render_template("index.html")

@app.post("/api/ping")
def ping():
    return jsonify({"ok": True, "message": "pong", "your_ip": request.remote_addr})

if __name__ == "__main__":
    # host = 127.0.0.1 => local only
    app.run(host="127.0.0.1", port=8000, debug=True)

#8000/8080 are common developer ports
#80 is HTTP
