from flask import Flask
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP Requests')

@app.route('/')
def home():
    REQUEST_COUNT.inc()
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>KMC Systems Team</title>
        <style>
            body {
                background: linear-gradient(135deg, #6dd5ed, #2193b0);
                color: #fff;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
                margin: 0;
            }
            .navbar {
                width: 100vw;
                background: rgba(0,0,0,0.6);
                padding: 1rem 0;
                position: absolute;
                top: 0;
                left: 0;
                display: flex;
                justify-content: center;
                box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            }
            .nav-menu {
                display: flex;
                gap: 2rem;
                list-style: none;
                margin: 0;
                padding: 0;
            }
            .nav-menu li a {
                color: #fff;
                text-decoration: none;
                font-weight: 500;
                font-size: 1.1rem;
                transition: color 0.2s;
            }
            .nav-menu li a:hover {
                color: #6dd5ed;
            }
            .container {
                background: rgba(0,0,0,0.4);
                padding: 2rem 3rem;
                border-radius: 1rem;
                box-shadow: 0 4px 24px rgba(0,0,0,0.2);
                text-align: center;
                margin-top: 5rem;
            }
            h1 {
                margin-bottom: 1rem;
                font-size: 2.5rem;
            }
            p {
                font-size: 1.2rem;
            }
            .footer {
                margin-top: 2rem;
                font-size: 0.9rem;
                color: #e0e0e0;
            }
        </style>
    </head>
    <body>
        <nav class="navbar">
            <ul class="nav-menu">
                <li><a href="#">Home</a></li>
                <li><a href="#">Products</a></li>
                <li><a href="#">Cart</a></li>
                <li><a href="#">Contact</a></li>
            </ul>
        </nav>
        <div class="container">
            <h1>Welcome to KMC Systems Team!</h1>
            <p>Designed Flask app with Prometheus monitoring.</p>
            <div class="footer">&copy; 2024 KMC Systems Team</div>
        </div>
    </body>
    </html>
    '''

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
