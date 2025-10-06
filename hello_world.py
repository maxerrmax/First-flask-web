from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Hello Page</title>
        </head>
        <body style="display: flex; justify-content: center; align-items: center; height: 100vh;">
            <button style="
                padding: 15px 30px;
                font-size: 1.5em;
                background-color: #007BFF;
                color: white;
                border: none;
                border-radius: 10px;
                cursor: pointer;
                transition: background-color 0.3s;">
                Hello World!
            </button>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
