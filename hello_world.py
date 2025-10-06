from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Hello Page</title>
            <style>
                body {
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    transition: background-color 1s;
                    background-color: white;
                }
                button {
                    padding: 15px 30px;
                    font-size: 1.5em;
                    background-color: #007BFF;
                    color: white;
                    border: none;
                    border-radius: 10px;
                    cursor: pointer;
                    transition: background-color 0.3s, transform 0.1s;
                }
                button:hover {
                    background-color: #0056b3;
                }
                button:active {
                    transform: scale(0.95);
                }
            </style>
        </head>
        <body id="body">
            <button onclick="changeBackground()">Hello World!</button>

            <script>
                function changeBackground() {
                    const colors = ['#FFADAD', '#FFD6A5', '#FDFFB6', '#CAFFBF', '#9BF6FF', '#A0C4FF', '#BDB2FF', '#FFC6FF'];
                    const randomColor = colors[Math.floor(Math.random() * colors.length)];
                    document.getElementById('body').style.backgroundColor = randomColor;
                }
            </script>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
