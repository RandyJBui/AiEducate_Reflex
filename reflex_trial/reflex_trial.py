"""Welcome to Reflex!."""

from reflex_trial import styles

# Import all the pages.
from reflex_trial.pages import *
import os

import reflex as rx
from credentials import *

# Create the app and compile it.
app = rx.App(style=styles.base_style)
app.compile()
