from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import os


# configurações
app = Flask(__name__)
# caminho do arquivo de banco de dados
caminho = os.path.dirname(os.path.abspath(__file__))
arquivobd = os.path.join(caminho, "spells.db")
# sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+arquivobd
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # remover warnings
db = SQLAlchemy(app)
