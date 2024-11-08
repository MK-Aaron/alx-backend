#!/usr/bin/env python3
""""
Simple flask app
"""

from flask import Flask, render_template
from flask_babel import Babel


class config(object):
    """Class config"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(config)
app.url_map.strict_slashes = False

babel = Babel(app)


@app.route('/')
def home():
    """Home page"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=TRue)