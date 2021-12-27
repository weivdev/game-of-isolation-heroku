import sys
import os
from io import StringIO
from copy import deepcopy
import time
import platform
import ipywidgets as widgets
from ipywidgets import interact, interactive, fixed, interact_manual
from ipywidgets import VBox, HBox, Label, Button, GridspecLayout
from ipywidgets import Button, GridBox, Layout, ButtonStyle
from IPython.display import display, clear_output