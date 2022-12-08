import datetime
import json
import pandas as pd
import os
import atexit

from flask import Flask, request, jsonify, make_response, send_file
from flask_restx import Resource, Api, fields, apidoc
from flask_cors import CORS
from flask_login import LoginManager

app = Flask(__name__)
CORS(app)
api = Api(app, version="1.0", title="API teste")

us = api.namespace("user", description="teste")


@us.route('/teste', doc={"description":"testee"})
class Index(Resource):
    @us.doc(responses={200: "bora bil"})
    def get(self):
        resp = make_response(jsonify({"message":"funcionou"}), 200)
        resp.headers["Access-Control-Allow-Origin"] = "*"

        return resp

    