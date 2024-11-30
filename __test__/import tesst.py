import os
import sys
parent_dir = os.path.dirname(os.path.abspath(__file__))
grandparent_dir = os.path.dirname(parent_dir)
sys.path.append(grandparent_dir)

import pygame
import __init__ as faste

faste.element.TextBox