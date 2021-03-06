# -*- coding: utf-8 -*-
"""Examples for halo.
"""
from __future__ import unicode_literals, absolute_import, print_function
import os
import time
import random

os.sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from halo import Halo

spinner = Halo(text='Downloading dataset.zip', spinner='dots')

try:
    spinner.start()
    for i in xrange(100):
        spinner.text = '{0}% Downloaded dataset.zip'.format(i)
        time.sleep(random.random())
    spinner.succeed('Downloaded dataset.zip')
except (KeyboardInterrupt, SystemExit):
    spinner.stop()
