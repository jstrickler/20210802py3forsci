#!/usr/bin/env python

import logging

logging.basicConfig(
    format='%(levelname)s %(name)s %(asctime)s %(message)s %(process)d', # <1>
    filename='../TEMP/simple.log',
    level=logging.INFO,
)

logging.info("this is information")
logging.warning("this is a warning")
logging.info("this is information")
logging.critical("this is critical")
