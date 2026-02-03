from flask import Flask, request, jsonify

app = Flask(__name__) # this constructs a web app, which Flask references

@app.get("/")
def home():
    return """
    <!doctype html>
    <html>
        <head>
            <meta charset="utf-8" />
        </head>
        <body>
            <h1>Traffic Simulation</title>
            <p>If you see this, I did the right thing.</p>

            <button id="btn">Test API call</button>
            <pre id="out"></pre>

            <script>
                const out =document.getElementById("out");
                document.getElementById("btn").addEventListener("click", async () => {
                    const res = await fetch("/api/ping", {method: "POST" });
                    const data = await res.json();
                    out.textContent = JSON.stringify(data, null, 2);
                });
            </script>
        </body>
    </html>
    """

@app.post("/api/ping")
def ping():
    return jsonify({"ok": True, "message": "pong", "your_ip": request.remote_addr})

if __name__ == "__main__":
    # host = 127.0.0.1 => local only
    app.run(host="127.0.0.1", port=8000, debug=True)

#8000/8080 are common developer ports
#80 is HTTP
