from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import psycopg2

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://monitor_admin:nftn47@localhost/server_monitor'
db = SQLAlchemy(app)

class Metrics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime)
    cpu_usage = db.Column(db.Float)
    memory_usage = db.Column(db.Float)
    disk_usage = db.Column(db.Float)
    network_traffic = db.Column(db.BigInteger)

@app.route('/')
def index():
    metrics = Metrics.query.order_by(Metrics.timestamp.desc()).limit(10).all()  # Last 10 records
    return render_template('index.html', metrics=metrics)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
