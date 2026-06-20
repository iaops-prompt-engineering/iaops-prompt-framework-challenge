from flask import Flask, jsonify

from lib.auth import runtime_configured

app = Flask(__name__)


@app.get("/healthz")
def healthz():
    return jsonify(status="ok")


@app.get("/readyz")
def readyz():
    if not runtime_configured():
        return jsonify(status="not_ready", reason="missing runtime configuration"), 503
    return jsonify(status="ready")


@app.get("/")
def index():
    return jsonify(service="lift", status="running")
