from flask import Flask, render_template_string

app = Flask(__name__)

index_html = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask Health Check</title>
</head>
<body>
    <h1>Welcome to the Flask App!</h1>
    <p>Перейдите на <a href="/healthz">/healthz</a> для проверки состояния.</p>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(index_html)

@app.route('/healthz', methods=['GET'])
def health_check():
    return '', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
