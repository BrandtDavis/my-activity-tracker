from flask import Flask
from config import Config
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# This must be here to avoid a circular structure
from app import routes