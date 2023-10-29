"""Welcome to Reflex!."""

from reflex_trial import styles
# Import all the pages.
import os
from .pages import *
import reflex as rx
from credentials import *
# Create the app and compile it.

app = rx.App(style=styles.base_style)
app.compile()
