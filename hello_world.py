from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Hello Page</title>
        </head>
        <body style="display: flex; justify-content: center; align-items: center; height: 100vh; font-size: 2em;">
            Hello World!
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
