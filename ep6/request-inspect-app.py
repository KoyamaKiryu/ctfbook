from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

METHODS = ['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE']

@app.route