#!/usr/bin/env python

import os
import json

from itertools import groupby

from rest_framework_ccbv.config import VERSION
from rest_framework_ccbv.inspector import drfviews


def main():
    d = {}
    d_version = {}
    views = sorted(drfviews.values(),
                   key=lambda x: (x.__module__, x.__name__))

    for key, value in groupby(views, lambda x:x.__module__):
        d_version[key] = map(lambda x: x.__name__, list(value))

    if os.path.isfile('views.txt'):
        with open('views.txt', 'r') as f:
            d = json.loads(f.read())
    
    d[VERSION] = d_version
    with open('views.txt', 'w') as f:
        json.dump(d, f)
        

if __name__ == '__main__':
    main()
