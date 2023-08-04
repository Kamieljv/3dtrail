import os
from flask import Flask, request, jsonify, render_template
from sqlalchemy import create_engine
from config import Config

# Initialize app and load config
app = Flask(__name__)

app.config.from_object(Config)

print(app.config)

# Connect to database
engine = create_engine(app.config['DATABASE_URI'])

@app.route('/')
def hello():
	return render_template('index.html')

@app.route('/cache-me')
def cache():
	return "nginx will cache this response"

@app.route('/info')
def info():

	resp = {
		'connecting_ip': request.headers['X-Real-IP'],
		'proxy_ip': request.headers['X-Forwarded-For'],
		'host': request.headers['Host'],
		'user-agent': request.headers['User-Agent']
	}

	return jsonify(resp)

@app.route('/flask-health-check')
def flask_health_check():
	return "success"
