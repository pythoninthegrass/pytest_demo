#!/usr/bin/env python

from flask_frozen import Freezer
from app import app


if __name__ == '__main__':
    app.run(debug=True)
