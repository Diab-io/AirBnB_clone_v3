#!/usr/bin/python3
"""
an endpoint that retrieves the number of each objects by type
"""

from . import app_views
from models import storage
from flask.json import jsonify


@app_views.route("/status")
def status():
    return jsonify(status="OK")
