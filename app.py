from flask import Flask

app = Flask(__name__)

HTML_PAGE = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>App Docker - ABBA</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', sans-serif;
            background: linear-gradient(135deg, #1B5E20 0%, #2E7D32 50%, #388E3C 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .card {
            background: white;
            border-radius: 20px;
            padding: 50px 60px;
            text-align: center;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            max-width: 600px;
            width: 90%;
        }
        .docker-icon { font-size: 60px; margin-bottom: 20px; }
        h1 { color: #1B5E20; font-size: 2rem; margin-bottom: 10px; }
        .subtitle { color: #666; font-size: 1.1rem; margin-bottom: 30px; }
        .badge {
            background: #1B5E20;
            color: white;
            padding: 10px 25px;
            border-radius: 50px;
            display: inline-block;
            font-weight: bold;
            margin-bottom: 25px;
        }
        .info-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 15px;
            margin-top: 25px;
        }
        .info-item {
            background: #f1f8e9;
            border: 1px solid #c8e6c9;
            border-radius: 10px;
            padding: 15px;
        }
        .info-item .label { color: #888; font-size: 0.8rem; }
        .info-item .value { color: #1B5E20; font-weight: bold; font-size: 1rem; }
        footer { margin-top: 30px; color: #aaa; font-size: 0.85rem; }
    </style>
</head>
<body>
    <div class="card">
        <div class="docker-icon">&#x1F433;</div>
        <h1>Application Conteneurisee</h1>
        <p class="subtitle">Deploye avec Docker par</p>
        <div class="badge">ABBA - CC1 DevOps 2026</div>
        <p>Bonjour a tous ! Ceci est une application Flask conteneurisee avec Docker.</p>
        <div class="info-grid">
            <div class="info-item">
                <div class="label">Framework</div>
                <div class="value">Flask (Python)</div>
            </div>
            <div class="info-item">
                <div class="label">Plateforme</div>
                <div class="value">Docker</div>
            </div>
            <div class="info-item">
                <div class="label">Port</div>
                <div class="value">5000</div>
            </div>
            <div class="info-item">
                <div class="label">Ecole</div>
                <div class="value">KEYCE</div>
            </div>
        </div>
        <footer>TP1 - Conduite de Projet Agile DevOps Kanban</footer>
    </div>
</body>
</html>"""


@app.route("/")
def home():
    return HTML_PAGE


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)