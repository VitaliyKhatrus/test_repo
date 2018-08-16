#!/usr/bin/env python

import sys
import os


path = sys.path

for c, value in enumerate(path, 1):
    print c, value
