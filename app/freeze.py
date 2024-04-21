#!/usr/bin/env python

import warnings
from app import app, pages
from flask import url_for
from flask_frozen import Freezer, MissingURLGeneratorWarning

# suppress `index_extend` route warning
warnings.simplefilter("ignore", category=MissingURLGeneratorWarning)

app.config['FREEZER_DESTINATION_IGNORE'] = ['.git*', 'CNAME']
freezer = Freezer(app)


@freezer.register_generator
def pagelist():
    for page in pages:
        print(f"making page for {page.path}")
        yield url_for('page', path=page.path)


if __name__ == "__main__":
    freezer.freeze()
