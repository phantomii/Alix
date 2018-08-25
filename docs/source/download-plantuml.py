#!/bin/env python

from os import path
import logging

import wget

URL = 'https://netix.dl.sourceforge.net/project/plantuml/plantuml.jar'
OUTPUT_PATH = '/tmp/plantuml.jar'

logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    logging.info("Checking PlantUML files...")
    if not path.exists(OUTPUT_PATH):
        logging.info("Downloading plantuml.jar from %s", URL)
        wget.download(url=URL, out=OUTPUT_PATH)
        logging.info("Downloaded and saved to %s", OUTPUT_PATH)
    logging.info("Done!")
