from flask import Flask

app = Flask(__name__)

# This must be here to avoid a circular structure
from app import routes