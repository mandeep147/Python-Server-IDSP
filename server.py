#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
import argparse
import os

from PredictionEngine.app import app

parser = argparse.ArgumentParser(description="PredictionEngine")
parser.add_argument(
    "--port", "-p",
    type=int,
    help="Port to listen on",
    default=5000,
)
args = parser.parse_args()

if __name__ == '__main__':
    
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', 
    		port=port,
    		debug=True,
    		threaded=True,
    )        
   
