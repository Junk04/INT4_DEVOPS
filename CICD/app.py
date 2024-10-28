from flask import Flask, render_template_string

app = Flask(__name__)

index_html = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask Health Check</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f4f4f9;
        }
        .container {
            text-align: center;
            padding: 2em;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            background-color: #fff;
            max-width: 400px;
        }
        h1 {
            color: #333;
            font-size: 24px;
            margin-bottom: 0.5em;
        }
        p {
            font-size: 16px;
            color: #666;
        }
        a {
            color: #007bff;
            text-decoration: none;
            font-weight: bold;
        }
        a:hover {
            color: #0056b3;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Welcome to the Flask App!</h1>
        <p>Перейдите на <a href="/healthz">/healthz</a> для проверки состояния.</p>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(index_html)

@app.route('/healthz', methods=['GET'])
def health():
    return '', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
