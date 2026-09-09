from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>AI Smart CI/CD</title>
        </head>

        <body>
            <h1>AI Smart CI/CD Pipeline</h1>
            <h2>Flask Application</h2>
            <p>Application is running successfully!</p>
        </body>
    </html>
    """


@app.route("/health")
def health():
    return "Application is healthy!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)