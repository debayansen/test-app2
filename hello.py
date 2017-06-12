import os
import logging
from flask import Flask

app = Flask(__name__)
log = logging.getLogger()

@app.route('/')
def hello():
    return "Hello Dream Force"


# from flask import Flask
# app = Flask(__name__)
#
# @app.route("/")
# def hello():
#     return "Hello World!"
#
# if __name__ == "__main__":
#     app.run()
