#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK

'''Echo cancellation (template).'''

import numpy as np
import struct
import math
import logging

#import pygame_widgets
import pygame
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox

import minimal
import buffer
#import queue

import threading

from scipy import signal
import tkinter as tk
#from tkinter import ttk
        
class Echo_Cancellation(buffer.Buffering):
    def __init__(self):
        super().__init__()
        logging.info(__doc__)
        
class Echo_Cancellation__verbose(Echo_Cancellation, buffer.Buffering__verbose):
    def __init__(self):
        super().__init__()

try:
    import argcomplete  # <tab> completion for argparse.
except ImportError:
    logging.warning("Unable to import argcomplete (optional)")

if __name__ == "__main__":
    minimal.parser.description = __doc__
    try:
        argcomplete.autocomplete(minimal.parser)
    except Exception:
        logging.warning("argcomplete not working :-/")
    minimal.args = minimal.parser.parse_known_args()[0]

    if minimal.args.show_stats or minimal.args.show_samples:
        intercom = Echo_Cancellation__verbose()
    else:
        intercom = Echo_Cancellation()
    try:
        intercom.run()
    except KeyboardInterrupt:
        minimal.parser.exit("\nSIGINT received")
    finally:
       intercom.print_final_averages()
