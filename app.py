GNU nano 7.2
from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
import psycopg2
import psutil # For systemstatistikk
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://monitor_admin:nftn47@>db = SQLAlchemy(app)

class Metrics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime)
    cpu_usage = db.Column(db.Float)
    memory_usage = db.Column(db.Float)
    disk_usage = db.Column(db.Float)
    network_traffic = db.Column(db.BigInteger)

@app.route('/')
def index():
    metrics = Metrics.query.order_by(Metrics.timestamp.desc()).limit(10).al>    return render_template('index.html', metrics=metrics)

# Ny API rute for systemstatistikk i "real-time"!
@app.route('/system-stats')
def system_stats():
        stats = {
            "cpu_usage": psutil.cpu_percent(interval=1),
            "ram_usage": psutil.virtual_memory().percent,
            "disk_usage": psutil.disk_usage('/').percent,
        }
        return stats

# Ny API rute for systemstatistikk i "real-time"!
@app.route('/system-stats')
def system_stats():
	stats = {
	    "cpu_usage": psutil.cpu_percent(interval=1),
	    "ram_usage": psutil.virtual_memory().percent,
	    "disk_usage": psutil.disk_usage('/').percent,
        }
	return jsonify(stats)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
